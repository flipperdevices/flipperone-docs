#!/usr/bin/env python3

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_docs import (
    DEFAULT_PART_FAMILIES,
    Severity,
    check_links,
    check_part_families,
    dedupe_slugs,
    extract_headings,
    extract_link_refs,
    find_part_occurrences,
    github_slug,
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

    def test_flags_missing_leading_slash_image_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = self._write_docs(
                Path(tmp_str),
                {
                    "testing/Video-decoding.md": "![Decoders](files/pics/rk3576.png)\n",
                    "files/pics/rk3576.png": "not-a-real-image-just-a-marker",
                },
            )
            md_files = sorted(docs_root.rglob("*.md"))
            findings = check_links(md_files, docs_root, docs_root.parent)
            path_findings = [f for f in findings if f.check == "path"]
            self.assertEqual(len(path_findings), 1)
            self.assertIn("files/pics/rk3576.png", path_findings[0].message)

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


class PartFamilyTest(unittest.TestCase):
    def test_diverging_family_produces_one_warning_per_occurrence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            docs_root.mkdir()
            (docs_root / "Tech-Specs.md").write_text(
                "Charger IC: TI BQ25792\n", encoding="utf-8"
            )
            (docs_root / "Heatsink.md").write_text(
                "Uses a BQ25798 charger.\n", encoding="utf-8"
            )
            md_files = sorted(docs_root.rglob("*.md"))
            occurrences = find_part_occurrences(md_files, docs_root.parent, DEFAULT_PART_FAMILIES)
            findings = check_part_families(occurrences)
            self.assertEqual(len(findings), 2)
            self.assertTrue(all(f.severity is Severity.WARNING for f in findings))
            self.assertTrue(all(f.check == "part-number" for f in findings))

    def test_single_consistent_value_produces_no_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            docs_root.mkdir()
            (docs_root / "Tech-Specs.md").write_text("Fuel gauge: BQ28Z620\n", encoding="utf-8")
            (docs_root / "Power-subsystem.md").write_text(
                "Uses a BQ28Z620 gauge.\n", encoding="utf-8"
            )
            md_files = sorted(docs_root.rglob("*.md"))
            occurrences = find_part_occurrences(md_files, docs_root.parent, DEFAULT_PART_FAMILIES)
            self.assertEqual(check_part_families(occurrences), [])

    def test_family_regex_is_case_sensitive_and_skips_driver_names(self) -> None:
        # Real corpus case: the lowercase Linux driver name `mt7921u` is not
        # the same thing as the chip part number `MT7921AU` / `MT7921AUN`,
        # and shouldn't be pulled into the same family comparison.
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            docs_root.mkdir()
            (docs_root / "WiFi.md").write_text(
                "driver: mt7921u\nChipset: MediaTek MT7921AUN\n", encoding="utf-8"
            )
            md_files = sorted(docs_root.rglob("*.md"))
            occurrences = find_part_occurrences(md_files, docs_root.parent, DEFAULT_PART_FAMILIES)
            values = {occ.value for occ in occurrences}
            self.assertEqual(values, {"MT7921AUN"})

    def test_code_fence_is_skipped_for_part_number_scanning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            docs_root.mkdir()
            (docs_root / "Example.md").write_text(
                "```\nBQ25792 shown only as an example value here: BQ25798\n```\n",
                encoding="utf-8",
            )
            md_files = sorted(docs_root.rglob("*.md"))
            occurrences = find_part_occurrences(md_files, docs_root.parent, DEFAULT_PART_FAMILIES)
            self.assertEqual(occurrences, [])


class RunEndToEndTest(unittest.TestCase):
    def test_run_combines_link_and_part_number_findings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_str:
            docs_root = Path(tmp_str) / "docs"
            docs_root.mkdir()
            (docs_root / "A.md").write_text(
                "[broken](#nope)\nBQ25792 here.\n", encoding="utf-8"
            )
            (docs_root / "B.md").write_text("BQ25798 there.\n", encoding="utf-8")
            findings = run(docs_root, docs_root.parent)
            checks = {f.check for f in findings}
            self.assertIn("anchor", checks)
            self.assertIn("part-number", checks)


if __name__ == "__main__":
    unittest.main()
