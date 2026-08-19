# table_to_archbee

Converts a plain HTML table or a GFM Markdown pipe-table into the specific
`<table>` shape Archbee's editor accepts.

## Usage

```
python3 convert_table_html.py <input> [-o OUTPUT] [--format {auto,html,markdown}]
                               [--column-widths W1,W2,...] [--header-align {left,center,right,none}]
```

- `input` — path to the source table. Left unmodified.
- `-o/--output` — defaults to `<input stem>.archbee.html` next to the input.
- `--format` — defaults to `auto`, sniffed from the extension
  (`.md`/`.markdown` → markdown, anything else → html).
- `--column-widths` — comma-separated pixel widths, one per column. Defaults
  to an even split summing to **660** — that's the `columnWidths` total used
  by every other working table in this docs repo (the content column
  appears to be ~660px wide), and tables whose widths sum well past that
  have been observed collapsing to a single stacked column on import. Match
  that budget unless you've confirmed otherwise.
- `--header-align` — `align` attribute added to header-row `<td>`s. Defaults
  to `left`; pass `none` to omit the attribute entirely.

Markdown input supports the inline syntax these tables actually use:
`` `code` ``, `**bold**`, `[text](url)`, and `\|` for a literal pipe inside a
cell. It does not implement full CommonMark — nested emphasis, images, etc.
aren't handled. Both source formats funnel through the same
normalize → escape-braces → render pipeline, so a Markdown table and an
equivalent HTML table produce byte-identical output.

## Examples

```
# From a Markdown pipe table
python3 convert_table_html.py table.md --column-widths 55,85,365,155

# From plain/pandoc HTML, explicit output path
python3 convert_table_html.py table.html -o out.html --header-align center
```

## Known limitations

- Regex-based, not a real HTML/Markdown parser. Assumes simple tables: no
  nested tables, no `colspan`/`rowspan`, one line of Markdown per logical
  row (a cell can still contain wrapped/multi-line content in the HTML
  path — pandoc-style line wrapping inside `<td>` is collapsed).
- The first row is always treated as the header row.
- All rows must have the same number of columns, or conversion fails loudly
  rather than guessing.

## Why this exists

Archbee docs are MDX under the hood: raw HTML in a page (like a `<table>`
block) is parsed as JSX, not passed through verbatim. That has two
consequences a plain table doesn't satisfy:

- **Shape.** Archbee expects `isTableHeaderOn`/`columnWidths` attributes on
  `<table>`, and each cell's content wrapped in its own `<p>`. A bare
  `<td>text</td>` table (e.g. pandoc output, or what a Markdown table
  naively becomes) gets rejected or mis-rendered.
- **Literal `{`/`}` breaks import.** Since the table is parsed as JSX, any
  `{...}` inside it is treated as an embedded JavaScript expression and
  handed to `acorn` (a JS parser). If the content between the braces isn't
  valid JS — e.g. a plain-text list like `{03,38,50,80}` — Archbee's import
  fails with `Could not parse expression with acorn`. A backslash escape
  (`\{`) does **not** fix this: JSX has no such escape mechanism. The fix is
  an HTML entity (`&#123;` / `&#125;`), which isn't a literal `{`/`}`
  character until the browser decodes it for display — i.e. after MDX/JSX
  parsing has already finished. This script does that escaping for you
  automatically.
