#!/usr/bin/env python3

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_docs import (
    Severity,
    check_links,
    dedupe_slugs,
    extract_headings,
    extract_link_refs,
    github_slug,
    resolve_image_target,
    resolve_path_part,
    run,
    split_fragment,
    unfenced_lines,
)


class SlugTest(unittest.TestCase):
    def test_plain_heading(self) -> None:
        self.assertEqual(github_slug("How to contribute"), "how-to-contribute")

    def test_strips_punctuation_without_replacing_with_hyphen(self) -> None:
        # Matches the real heading "### How archbee.json works" on
        # docs/resources/docs/About-Docs.md, linked as #how-archbeejson-works.
        self.assertEqual(github_slug("How archbee.json works"), "how-archbeejson-works")

    def test_strips_emoji_and_collapses_whitespace(self) -> None:
        self.assertEqual(github_slug("✅  Tasks tracker"), "tasks-tracker")

    def test_markdown_link_in_heading_uses_link_text(self) -> None:
        self.assertEqual(github_slug("[Hardware](./hardware/About-Hardware.md)"), "hardware")

    def test_inline_code_in_heading_keeps_content(self) -> None:
        # The heading's own "-i" flag keeps its hyphen, so the space before it
        # turns into a second one -- GitHub doesn't collapse repeated hyphens.
        self.assertEqual(github_slug("`ethtool -i wlxb06b11673ade`"), "ethtool--i-wlxb06b11673ade")

    def test_archbee_directive_in_heading_is_dropped(self) -> None:
        self.assertEqual(
            github_slug(':inlineImage[]{src="/files/icons/apple-logo.png"} macOS'), "macos"
        )

    def test_bold_and_italic_markers_are_dropped(self) -> None:
        self.assertEqual(github_slug("**Bold** and _italic_ text"), "bold-and-italic-text")


class DedupeSlugsTest(unittest.TestCase):
    def test_first_occurrence_unsuffixed_rest_incrementing(self) -> None:
        self.assertEqual(
            dedupe_slugs(["setup", "usage", "setup", "setup"]),
            ["setup", "usage", "setup-1", "setup-2"],
        )

    def test_no_duplicates_unaffected(self) -> None:
        self.assertEqual(dedupe_slugs(["a", "b", "c"]), ["a", "b", "c"])


class UnfencedLinesTest(unittest.TestCase):
    def test_skips_fenced_code_block(self) -> None:
        text = (
            "Intro text\n"
            "```markdown\n"
            "![Caption text](/files/pics/your-image.png)\n"
            "```\n"
            "Real content\n"
        )
        lines = unfenced_lines(text)
        self.assertEqual([line for _, line in lines], ["Intro text", "Real content"])

    def test_heading_inside_fence_is_not_extracted(self) -> None:
        text = (
            "```markdown\n"
            ":::ExpandableHeading\n"
            "### Section title\n"
            ":::\n"
            "```\n"
            "\n"
            ":::ExpandableHeading\n"
            "### Section title\n"
            ":::\n"
        )
        lines = unfenced_lines(text)
        headings = extract_headings(lines)
        self.assertEqual(len(headings), 1)
        self.assertEqual(headings[0].slug, "section-title")

    def test_hash_lines_inside_fence_are_not_headings(self) -> None:
        # Real case from docs/dev-log/3.md: C #define macros inside a fenced
        # block look like level-1 ATX headings if fencing isn't respected.
        text = (
            "```c\n"
            "#define I2C_HAPTIC_PLAY_EFFECT_BIT (15)\n"
            "```\n"
            "## Real heading\n"
        )
        headings = extract_headings(unfenced_lines(text))
        self.assertEqual([h.text for h in headings], ["Real heading"])


class FragmentSplitTest(unittest.TestCase):
    def test_no_fragment(self) -> None:
        self.assertEqual(split_fragment("./Other-Page.md"), ("./Other-Page.md", None))

    def test_with_fragment(self) -> None:
        self.assertEqual(
            split_fragment("./Other-Page.md#some-section"), ("./Other-Page.md", "some-section")
        )

    def test_bare_fragment(self) -> None:
        self.assertEqual(split_fragment("#known-issues"), ("", "known-issues"))


class ResolvePathPartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.docs_root = Path("/repo/docs").resolve()
        self.current_file = (self.docs_root / "testing" / "About-Testing.md").resolve()

    def test_same_page_variants_resolve_to_none(self) -> None:
        for value in ("", ".", "./"):
            with self.subTest(value=value):
                self.assertIsNone(resolve_path_part(value, self.current_file, self.docs_root))

    def test_absolute_path_resolves_against_docs_root(self) -> None:
        target = resolve_path_part("/files/pics/foo.png", self.current_file, self.docs_root)
        self.assertEqual(target, self.docs_root / "files" / "pics" / "foo.png")

    def test_relative_path_resolves_against_current_file_dir(self) -> None:
        target = resolve_path_part("Style-guide.md", self.current_file, self.docs_root)
        self.assertEqual(target, self.docs_root / "testing" / "Style-guide.md")

    def test_malformed_absolute_dot_does_not_resolve_to_a_page(self) -> None:
        # The real bug on docs/testing/About-Testing.md: `/.#comment-on-an-open-task`
        # instead of `./#comment-on-an-open-task`.
        target = resolve_path_part("/.", self.current_file, self.docs_root)
        self.assertEqual(target, self.docs_root)
        self.assertNotEqual(target, self.current_file)


class ResolveImageTargetTest(unittest.TestCase):
    def test_dotdot_relative_hit_is_used_as_is(self) -> None:
        # docs/hardware/GPIO-Modules.md's real image reference: "../" only
        # makes sense relative to the referencing file's own directory, and
        # it resolves on the first try, so the docs-root fallback never
        # kicks in.
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            (docs_root / "files" / "pics").mkdir(parents=True)
            (docs_root / "files" / "pics" / "walkie-talkie-module.png").write_text("x")
            current_file = docs_root / "hardware" / "GPIO-Modules.md"
            current_file.parent.mkdir(parents=True)
            target = resolve_image_target(
                "../files/pics/walkie-talkie-module.png", current_file, docs_root
            )
            self.assertEqual(target, docs_root / "files" / "pics" / "walkie-talkie-module.png")

    def test_falls_back_to_docs_root_when_file_relative_resolution_misses(self) -> None:
        # The real false positive on docs/cpu-software/How-to-install-linux-image.md:
        # a bare relative path with no leading slash and no "../" doesn't
        # resolve next to the referencing page, but Archbee renders it fine
        # live by falling back to a docs-root-relative lookup.
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            (docs_root / "files" / "pics").mkdir(parents=True)
            (docs_root / "files" / "pics" / "rk3576_maskrom_mode.jpg").write_text("x")
            current_file = docs_root / "cpu-software" / "How-to-install-linux-image.md"
            current_file.parent.mkdir(parents=True)
            target = resolve_image_target(
                "files/pics/rk3576_maskrom_mode.jpg", current_file, docs_root
            )
            self.assertEqual(target, docs_root / "files" / "pics" / "rk3576_maskrom_mode.jpg")

    def test_missing_from_both_locations_stays_broken(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            current_file = docs_root / "cpu-software" / "How-to-install-linux-image.md"
            current_file.parent.mkdir(parents=True)
            target = resolve_image_target(
                "files/pics/does-not-exist.jpg", current_file, docs_root
            )
            assert target is not None
            self.assertFalse(target.is_file())

    def test_leading_slash_path_is_unaffected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            (docs_root / "files" / "pics").mkdir(parents=True)
            (docs_root / "files" / "pics" / "foo.png").write_text("x")
            current_file = docs_root / "testing" / "About-Testing.md"
            current_file.parent.mkdir(parents=True)
            target = resolve_image_target("/files/pics/foo.png", current_file, docs_root)
            self.assertEqual(target, docs_root / "files" / "pics" / "foo.png")


class ArchbeeImageParsingTest(unittest.TestCase):
    def test_extracts_src_from_image_directive(self) -> None:
        line = '::Image[]{src="/files/pics/foo.jpg" size="80" position="flex-start"}'
        refs = extract_link_refs(Path("docs/x.md"), [(1, line)])
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].raw_url, "/files/pics/foo.jpg")
        self.assertTrue(refs[0].is_image)

    def test_extracts_src_from_inline_image_directive(self) -> None:
        line = 'Press :inlineImage[]{src="/files/pics/ui/button.png" alt caption} to continue.'
        refs = extract_link_refs(Path("docs/x.md"), [(1, line)])
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].raw_url, "/files/pics/ui/button.png")

    def test_extracts_src_with_extra_metadata_attributes(self) -> None:
        # Real shape: Archbee adds sha/initialPath/githubPath/width/height
        # after src, and the docs corpus has 3 real instances where src is
        # missing its leading slash while githubPath still has it.
        line = (
            '::Image[]{src="files/pics/rk3576_maskrom_mode.jpg" size="80" '
            'githubPath="docs/files/pics/rk3576_maskrom_mode.jpg" width="2658"}'
        )
        refs = extract_link_refs(Path("docs/x.md"), [(1, line)])
        self.assertEqual(refs[0].raw_url, "files/pics/rk3576_maskrom_mode.jpg")

    def test_plain_markdown_image_and_archbee_directive_both_found(self) -> None:
        line = '![Alt](/files/pics/a.png) and :inlineImage[]{src="/files/pics/b.png" alt}'
        refs = extract_link_refs(Path("docs/x.md"), [(1, line)])
        urls = sorted(r.raw_url for r in refs)
        self.assertEqual(urls, ["/files/pics/a.png", "/files/pics/b.png"])


class CheckLinksIntegrationTest(unittest.TestCase):
    def _write_docs(self, tmp: Path, files: dict[str, str]) -> Path:
        docs_root = tmp / "docs"
        for rel, content in files.items():
            path = docs_root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return docs_root

    def test_flags_anchor_that_does_not_match_any_heading(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {
                    "mechanics/About-Mechanics.md": "### Contribute a third-party module\n",
                    "dev-log/4.md": (
                        "See the [contribution guide]"
                        "(../mechanics/About-Mechanics.md#contributing-a-third-party-module).\n"
                    ),
                },
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            anchor_findings = [f for f in findings if f.check == "anchor"]
            self.assertEqual(len(anchor_findings), 1)
            self.assertEqual(anchor_findings[0].severity, Severity.ERROR)
            self.assertIn("contributing-a-third-party-module", anchor_findings[0].message)

    def test_correct_anchor_produces_no_finding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {
                    "mechanics/About-Mechanics.md": "### Contribute a third-party module\n",
                    "dev-log/4.md": (
                        "See the [contribution guide]"
                        "(../mechanics/About-Mechanics.md#contribute-a-third-party-module).\n"
                    ),
                },
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            self.assertEqual(findings, [])

    def test_bare_relative_image_path_resolves_against_docs_root(self) -> None:
        # The real false positive on docs/cpu-software/How-to-install-linux-image.md:
        # an ::Image[] directive with a bare relative "src" (no leading
        # slash) that doesn't sit next to files/pics/ in the same
        # directory. Archbee still renders this fine live, resolving it
        # against the docs root, so this must not be flagged.
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {
                    "cpu-software/How-to-install-linux-image.md": (
                        '::Image[]{src="files/pics/rk3576_maskrom_mode.jpg"}\n'
                    ),
                    "files/pics/rk3576_maskrom_mode.jpg": "not-a-real-image-just-a-marker",
                },
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            self.assertEqual(findings, [])

    def test_dotdot_relative_image_still_resolves_next_to_referencing_file(self) -> None:
        # docs/hardware/GPIO-Modules.md's real, currently-correct pattern: an
        # explicit "../" that only makes sense relative to the referencing
        # file's own directory. This must keep working, not fall through to
        # the docs-root fallback.
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {
                    "hardware/GPIO-Modules.md": (
                        "![Walkie-talkie module structural diagram]"
                        "(../files/pics/walkie-talkie-module.png)\n"
                    ),
                    "files/pics/walkie-talkie-module.png": "not-a-real-image-just-a-marker",
                },
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            self.assertEqual(findings, [])

    def test_genuinely_missing_image_is_still_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {
                    "cpu-software/How-to-install-linux-image.md": (
                        "![Missing](files/pics/does-not-exist.jpg)\n"
                    ),
                },
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            path_findings = [f for f in findings if f.check == "path"]
            self.assertEqual(len(path_findings), 1)
            self.assertIn("files/pics/does-not-exist.jpg", path_findings[0].message)

    def test_placeholder_path_inside_fence_is_not_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {
                    "resources/docs/About-Docs.md": (
                        "To use an image, reference it like this:\n\n"
                        "```markdown\n"
                        "![Caption text](/files/pics/your-image.png)\n"
                        "```\n"
                    ),
                },
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            self.assertEqual(findings, [])

    def test_external_url_is_never_checked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {"Welcome.md": "![Banner](https://cdn.flipper.net/banner.jpg)\n"},
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            self.assertEqual(findings, [])

    def test_same_page_fragment_resolves_against_own_headings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {
                    "testing/About-Testing.md": (
                        "### Comment on an open task\n\n"
                        "See [comments on open task](./#comment-on-an-open-task).\n"
                    )
                },
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            self.assertEqual(findings, [])

    def test_malformed_same_page_slash_dot_link_is_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {
                    "testing/About-Testing.md": (
                        "### Comment on an open task\n\n"
                        "See [comments on open task](/.#comment-on-an-open-task).\n"
                    )
                },
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].check, "path")


class RunEndToEndTest(unittest.TestCase):
    def test_run_combines_anchor_and_path_findings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            docs_root.mkdir()
            (docs_root / "A.md").write_text(
                "[broken anchor](#nope)\n![broken path](/files/pics/nope.png)\n",
                encoding="utf-8",
            )
            findings = run(docs_root, docs_root.parent)
            checks = {f.check for f in findings}
            self.assertEqual(checks, {"anchor", "path"})


if __name__ == "__main__":
    unittest.main()
