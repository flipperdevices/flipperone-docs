#!/usr/bin/env python3
"""
Check the Flipper One docs for broken anchors and broken internal paths.

Archbee's own CI (`archbee validate` / `archbee broken-links`, see
.github/workflows/validate.yml) checks the sidebar structure and confirms
that link targets exist, but it doesn't resolve `#fragment` anchors against
the target page's real headings. This script covers that gap, plus a path
check that's stricter about image references than Archbee's own check:

1. Anchor check: for every internal link with a `#fragment`, resolve the
   target page and confirm the fragment matches a GitHub-style slug of one
   of its headings.
2. Path check: for every internal link and image reference -- plain
   Markdown and Archbee's `::Image[]{src="..."}` / `:inlineImage[]{src="..."}`
   directives -- confirm the target file actually exists. Image references
   are resolved the way Archbee resolves them: relative to the referencing
   page first, then falling back to a path relative to the docs root (see
   `resolve_image_target` for why both are tried).

Each check can be run on its own with `--check anchor` / `--check path`, so
CI can wire them up as separate steps and name precisely which one failed.

Fenced code blocks are skipped by both checks. The contribution-guide pages
use placeholder paths like `your-image.png` as syntax examples inside
` ```markdown ` fences, and those aren't real broken links.

Usage:
    python3 tools/validate_docs.py                  # scan docs/, human output
    python3 tools/validate_docs.py --check anchor    # anchors only
    python3 tools/validate_docs.py --check path      # paths only
    python3 tools/validate_docs.py --docs-root docs
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DOCS_ROOT = REPO_ROOT / "docs"


class Severity(str, Enum):
    ERROR = "error"
    WARNING = "warning"


_FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")

# `[text](url "title")` and `![alt](url "title")`. The URL itself is
# assumed to contain no whitespace and no unescaped `)`, which holds for
# every link in this repo (checked against the actual corpus).
_MD_LINK_OR_IMAGE_RE = re.compile(
    r"(?P<bang>!?)\[(?P<text>[^\]]*)\]\((?P<url>[^\s)]+)(?:\s+(?:\"[^\"]*\"|'[^']*'))?\)"
)
# Archbee's `::Image[]{src="..." ...}` and `:inlineImage[]{src="..." ...}`.
_ARCHBEE_IMAGE_RE = re.compile(
    r"::?(?:Image|inlineImage)\[[^\]]*\]\{[^}]*?src=\"(?P<src>[^\"]*)\"[^}]*\}"
)

# Used to strip Markdown/Archbee markup out of a heading before slugifying,
# so the anchor is computed from the *rendered* text, same as GitHub does.
_DIRECTIVE_RE = re.compile(r":{1,2}[A-Za-z][\w-]*\[[^\]]*\](?:\{[^}]*\})?")
_MD_IMAGE_ONLY_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_MD_LINK_TEXT_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_INLINE_CODE_RE = re.compile(r"`([^`]*)`")
_BOLD_STAR_RE = re.compile(r"\*\*(.+?)\*\*")
_BOLD_UNDER_RE = re.compile(r"__(.+?)__")
_ITALIC_STAR_RE = re.compile(r"(?<!\w)\*(.+?)\*(?!\w)")
_ITALIC_UNDER_RE = re.compile(r"(?<!\w)_(.+?)_(?!\w)")
_NON_SLUG_RE = re.compile(r"[^\w\s-]")

_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")


@dataclass(frozen=True)
class Finding:
    severity: Severity
    check: str
    path: Path
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.severity.value.upper():7} {self.path}:{self.line}  [{self.check}] {self.message}"


@dataclass(frozen=True)
class Heading:
    line: int
    level: int
    text: str
    slug: str


@dataclass(frozen=True)
class PageInfo:
    lines: list[tuple[int, str]]
    headings: list[Heading]
    slugs: frozenset[str]


@dataclass(frozen=True)
class LinkRef:
    source: Path
    line: int
    raw_url: str
    is_image: bool


def unfenced_lines(text: str) -> list[tuple[int, str]]:
    """Return (1-based line number, line text) pairs, skipping fenced code blocks."""
    result: list[tuple[int, str]] = []
    in_fence = False
    fence_char = ""
    fence_len = 0
    for lineno, line in enumerate(text.splitlines(), start=1):
        match = _FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_len = len(marker)
                continue
            if marker[0] == fence_char and len(marker) >= fence_len:
                in_fence = False
                continue
        if not in_fence:
            result.append((lineno, line))
    return result


def heading_plain_text(raw: str) -> str:
    """Strip Markdown/Archbee syntax from a heading, leaving the rendered text."""
    text = _DIRECTIVE_RE.sub("", raw)
    text = _MD_IMAGE_ONLY_RE.sub("", text)
    text = _MD_LINK_TEXT_RE.sub(r"\1", text)
    text = _INLINE_CODE_RE.sub(r"\1", text)
    text = _BOLD_STAR_RE.sub(r"\1", text)
    text = _BOLD_UNDER_RE.sub(r"\1", text)
    text = _ITALIC_STAR_RE.sub(r"\1", text)
    text = _ITALIC_UNDER_RE.sub(r"\1", text)
    return text


def github_slug(heading_text: str) -> str:
    """Compute the anchor slug GitHub-flavored Markdown would give this heading.

    Lowercase, drop anything that isn't a letter/digit/underscore/space/hyphen,
    collapse whitespace, then turn spaces into hyphens. Doesn't include the
    numeric `-1`, `-2`, ... suffix GitHub adds for repeated headings on the
    same page -- see `dedupe_slugs` for that.
    """
    plain = heading_plain_text(heading_text).lower()
    plain = _NON_SLUG_RE.sub("", plain)
    plain = re.sub(r"\s+", " ", plain).strip()
    return plain.replace(" ", "-")


def dedupe_slugs(raw_slugs: list[str]) -> list[str]:
    """Apply GitHub's duplicate-heading suffixing: first occurrence bare, then -1, -2, ..."""
    seen: dict[str, int] = {}
    result: list[str] = []
    for slug in raw_slugs:
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.append(slug if count == 0 else f"{slug}-{count}")
    return result


def extract_headings(lines: list[tuple[int, str]]) -> list[Heading]:
    raw: list[tuple[int, int, str]] = []
    for lineno, line in lines:
        match = _HEADING_RE.match(line)
        if match:
            raw.append((lineno, len(match.group(1)), match.group(2)))
    slugs = dedupe_slugs([github_slug(text) for _, _, text in raw])
    return [
        Heading(line=lineno, level=level, text=text, slug=slug)
        for (lineno, level, text), slug in zip(raw, slugs)
    ]


def load_page(path: Path) -> PageInfo:
    text = path.read_text(encoding="utf-8")
    lines = unfenced_lines(text)
    headings = extract_headings(lines)
    return PageInfo(lines=lines, headings=headings, slugs=frozenset(h.slug for h in headings))


def extract_link_refs(source: Path, lines: list[tuple[int, str]]) -> list[LinkRef]:
    refs: list[LinkRef] = []
    for lineno, line in lines:
        for match in _MD_LINK_OR_IMAGE_RE.finditer(line):
            refs.append(
                LinkRef(source, lineno, match.group("url"), is_image=bool(match.group("bang")))
            )
        for match in _ARCHBEE_IMAGE_RE.finditer(line):
            refs.append(LinkRef(source, lineno, match.group("src"), is_image=True))
    return refs


def is_external(url: str) -> bool:
    """True for anything with a URI scheme (http://, https://, mailto:, ...)."""
    return bool(_SCHEME_RE.match(url))


def split_fragment(url: str) -> tuple[str, str | None]:
    if "#" not in url:
        return url, None
    path_part, _, frag = url.partition("#")
    return path_part, unquote(frag) if frag else None


def resolve_path_part(path_part: str, current_file: Path, docs_root: Path) -> Path | None:
    """Resolve a link's path portion (without the fragment) to an absolute path.

    Returns None when `path_part` refers to the current page itself
    (empty, ".", or "./") -- the same-page convention used across these docs.
    """
    if path_part in ("", ".", "./"):
        return None
    if path_part.startswith("/"):
        base, rel = docs_root, path_part[1:]
    else:
        base, rel = current_file.parent, path_part
    return (base / rel).resolve()


def resolve_image_target(path_part: str, current_file: Path, docs_root: Path) -> Path | None:
    """Resolve an image reference the way Archbee actually resolves it.

    Regular internal links resolve relative to the referencing file, and
    that's right for images too when the reference already works out that
    way -- docs/hardware/GPIO-Modules.md's plain Markdown image uses
    "../files/pics/walkie-talkie-module.png", which only makes sense
    relative to its own directory, and it renders fine live.

    But three `::Image[]{src="files/pics/..."}` directives on
    docs/cpu-software/How-to-install-linux-image.md give a bare relative
    path with no leading slash and no "../" -- under file-relative
    resolution that looks for a "files/pics/" folder next to the page
    itself, which doesn't exist, but the images render fine live because
    Archbee falls back to resolving the same path against the docs root.
    So: try the normal file-relative resolution first, and only if that
    doesn't find a file, retry relative to the docs root before giving up.
    """
    target = resolve_path_part(path_part, current_file, docs_root)
    if target is not None and not target.is_file() and not path_part.startswith("/"):
        root_relative = (docs_root / path_part).resolve()
        if root_relative.is_file():
            return root_relative
    return target


def display_path(path: Path, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def find_markdown_files(docs_root: Path) -> list[Path]:
    return sorted(docs_root.rglob("*.md"))


def check_links(md_files: list[Path], docs_root: Path, repo_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    page_cache: dict[Path, PageInfo] = {}

    def get_page(path: Path) -> PageInfo:
        if path not in page_cache:
            page_cache[path] = load_page(path)
        return page_cache[path]

    for md_file in md_files:
        page = get_page(md_file)
        source = display_path(md_file, repo_root)
        for ref in extract_link_refs(Path(source), page.lines):
            if is_external(ref.raw_url):
                continue
            path_part, fragment = split_fragment(ref.raw_url)
            if ref.is_image:
                target = resolve_image_target(path_part, md_file, docs_root)
            else:
                target = resolve_path_part(path_part, md_file, docs_root)

            if target is None:
                target_page: PageInfo | None = page
                target_display = source
            else:
                if not target.is_file():
                    findings.append(
                        Finding(
                            Severity.ERROR,
                            "path",
                            Path(source),
                            ref.line,
                            f"target '{ref.raw_url}' does not resolve to an existing file "
                            f"(resolved: {display_path(target, repo_root)})",
                        )
                    )
                    continue
                target_display = display_path(target, repo_root)
                target_page = get_page(target) if target.suffix == ".md" else None

            if fragment is None or ref.is_image or target_page is None:
                continue
            if fragment not in target_page.slugs:
                known = ", ".join(sorted(target_page.slugs)) or "none"
                findings.append(
                    Finding(
                        Severity.ERROR,
                        "anchor",
                        Path(source),
                        ref.line,
                        f"fragment '#{fragment}' not found in {target_display} "
                        f"(known headings: {known})",
                    )
                )
    return findings


def run(docs_root: Path, repo_root: Path) -> list[Finding]:
    md_files = find_markdown_files(docs_root)
    findings = check_links(md_files, docs_root, repo_root)
    findings.sort(key=lambda f: (str(f.path), f.line, f.check, f.severity.value))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--docs-root", type=Path, default=DEFAULT_DOCS_ROOT, help="Directory to scan (default: docs/)."
    )
    parser.add_argument(
        "--check",
        choices=("anchor", "path"),
        default=None,
        help="Run only this check instead of both. Lets CI wire the anchor "
        "check and the path check into their own steps.",
    )
    args = parser.parse_args(argv)

    docs_root: Path = args.docs_root.resolve()
    repo_root: Path = docs_root.parent

    findings = run(docs_root, repo_root)
    if args.check is not None:
        findings = [f for f in findings if f.check == args.check]
    for finding in findings:
        print(finding)

    errors = [f for f in findings if f.severity is Severity.ERROR]
    file_count = len(find_markdown_files(docs_root))
    print(f"\n{len(errors)} error(s) across {file_count} files scanned.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
