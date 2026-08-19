#!/usr/bin/env python3
"""Convert a plain HTML table or a GFM Markdown pipe-table into Archbee's <table> block format.

Archbee's editor only accepts a specific shape for raw HTML tables:

    <table isTableHeaderOn="true" columnWidths="W1,W2,...">
      <tr>
        <td align="left">
          <p>header cell</p>
        </td>
        ...
      </tr>
      <tr>
        <td>
          <p>body cell</p>
        </td>
        ...
      </tr>
    </table>

Plain HTML tables (one <td>text</td> per cell, no <p> wrapper, no per-table
width/header attributes) get rejected or mis-rendered by Archbee. This script
rewrites a plain table into the required shape. It only relies on the
standard library, and it is intentionally regex-based rather than a full HTML
parser, since the input tables are simple (no nested tables, no colspans).

Markdown input (a GFM pipe table, e.g. from a `| a | b |` block) is first
turned into the same [[cell, cell, ...], ...] row structure a parsed HTML
table would produce -- inline `` `code` ``, `**bold**`, and `[text](url)`
links become their HTML equivalents -- and from that point on it goes through
the exact same normalization/escaping/rendering path as HTML input.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROW_RE = re.compile(r"<tr\b([^>]*)>(.*?)</tr>", re.DOTALL | re.IGNORECASE)
CELL_RE = re.compile(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", re.DOTALL | re.IGNORECASE)

MD_SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
MD_CODE_SPAN_RE = re.compile(r"`([^`]+)`")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
MD_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")


def normalize_cell(html: str) -> str:
    """Collapse the line-wrapped whitespace pandoc leaves inside cells."""
    return re.sub(r"\s+", " ", html).strip()


def split_pipe_row(line: str) -> list[str]:
    """Split one `| a | b |` line into cells, honoring `\\|` as a literal pipe."""
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith(r"\|"):
        line = line[:-1]
    cells = re.split(r"(?<!\\)\|", line)
    return [c.strip().replace(r"\|", "|") for c in cells]


def markdown_inline_to_html(text: str) -> str:
    """Convert the subset of inline Markdown these tables use to HTML tags."""
    code_spans: list[str] = []

    def stash_code(match: re.Match) -> str:
        code_spans.append(match.group(1))
        return f"\x00CODE{len(code_spans) - 1}\x00"

    text = MD_CODE_SPAN_RE.sub(stash_code, text)
    text = MD_LINK_RE.sub(r'<a href="\2">\1</a>', text)
    text = MD_BOLD_RE.sub(r"<strong>\1</strong>", text)
    text = re.sub(
        r"\x00CODE(\d+)\x00", lambda m: f"<code>{code_spans[int(m.group(1))]}</code>", text
    )
    return text


def parse_rows_markdown(source: str) -> list[list[str]]:
    rows = []
    for line in source.splitlines():
        if "|" not in line or not line.strip():
            continue
        if MD_SEPARATOR_RE.match(line):
            continue
        cells = [markdown_inline_to_html(c) for c in split_pipe_row(line)]
        rows.append(cells)
    return rows


def escape_mdx_braces(html: str) -> str:
    """Neutralize literal `{`/`}` so Archbee's MDX/JSX layer doesn't treat
    them as an embedded-expression slot and hand the contents to acorn.

    A backslash escape (`\\{`) does NOT work here: this content lives inside
    a raw <table> block, which MDX parses as JSX, and JSX has no backslash-
    escape mechanism for braces. HTML entities do work, since they aren't
    literal `{`/`}` characters until the browser decodes them for display,
    which happens after MDX/JSX parsing has already finished.
    """
    return html.replace("{", "&#123;").replace("}", "&#125;")


def parse_rows_html(source: str) -> list[list[str]]:
    rows = []
    for attrs, body in ROW_RE.findall(source):
        cells = [normalize_cell(c) for c in CELL_RE.findall(body)]
        rows.append(cells)
    return rows


def default_column_widths(n: int, total: int = 660) -> list[int]:
    base = total // n
    widths = [base] * n
    widths[-1] += total - base * n
    return widths


def render_table(
    rows: list[list[str]],
    column_widths: list[int],
    header_align: str | None,
) -> str:
    if not rows:
        raise ValueError("no <tr> rows found in source")

    widths_attr = ",".join(str(w) for w in column_widths)
    lines = [f'<table isTableHeaderOn="true" columnWidths="{widths_attr}">']

    for row_index, cells in enumerate(rows):
        is_header = row_index == 0
        lines.append("  <tr>")
        for cell in cells:
            attrs = f' align="{header_align}"' if is_header and header_align else ""
            lines.append(f"    <td{attrs}>")
            lines.append(f"      <p>{cell}</p>")
            lines.append("    </td>")
        lines.append("  </tr>")

    lines.append("</table>")
    return "\n".join(lines) + "\n"


def convert(
    source: str,
    column_widths: list[int] | None = None,
    header_align: str | None = "left",
    fmt: str = "html",
) -> str:
    if fmt == "markdown":
        rows = parse_rows_markdown(source)
    elif fmt == "html":
        rows = parse_rows_html(source)
    else:
        raise ValueError(f"unknown format: {fmt!r} (expected 'html' or 'markdown')")

    rows = [[escape_mdx_braces(cell) for cell in cells] for cells in rows]

    n_cols = len(rows[0])
    for cells in rows:
        if len(cells) != n_cols:
            raise ValueError(
                f"inconsistent column count: expected {n_cols}, got {len(cells)} "
                f"in row {cells!r}"
            )
    widths = column_widths or default_column_widths(n_cols)
    if len(widths) != n_cols:
        raise ValueError(f"--column-widths has {len(widths)} entries, table has {n_cols} columns")
    return render_table(rows, widths, header_align)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", type=Path, help="path to the source table (HTML or .md, kept unmodified)"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="output path (default: <input stem>.archbee.html next to the input)",
    )
    parser.add_argument(
        "--format",
        type=str,
        default="auto",
        choices=["auto", "html", "markdown"],
        help='source format (default: auto, sniffed from the input extension: '
        ".md/.markdown -> markdown, anything else -> html)",
    )
    parser.add_argument(
        "--column-widths",
        type=str,
        default=None,
        help="comma-separated pixel widths, one per column (default: even split summing to 660)",
    )
    parser.add_argument(
        "--header-align",
        type=str,
        default="left",
        choices=["left", "center", "right", "none"],
        help='align attribute added to header <td> cells (default: left; "none" omits it)',
    )
    return parser.parse_args()


def detect_format(path: Path) -> str:
    return "markdown" if path.suffix.lower() in (".md", ".markdown") else "html"


def main() -> None:
    args = parse_args()
    source = args.input.read_text(encoding="utf-8")

    fmt = detect_format(args.input) if args.format == "auto" else args.format

    column_widths = None
    if args.column_widths:
        column_widths = [int(w) for w in args.column_widths.split(",")]

    header_align = None if args.header_align == "none" else args.header_align
    output = convert(source, column_widths=column_widths, header_align=header_align, fmt=fmt)

    output_path = args.output or args.input.with_suffix("").with_suffix(".archbee.html")
    output_path.write_text(output, encoding="utf-8")
    print(f"wrote {output_path}")


if __name__ == "__main__":
    main()
