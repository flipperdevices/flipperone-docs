#!/usr/bin/env python3
"""
Generate docs/Open-tasks.md from GitHub issues labeled "help wanted"
across all Flipper One sub-project repositories.

Output is Archbee-flavored Markdown matching the design of the page on
https://docs.flipper.net/one/open-tasks — YAML frontmatter, per-section
HTML tables (with isTableHeaderOn / columnWidths), and `:::hint{type="info"}`
blocks linking to the sub-project's task tracker, contribution guide,
and GitHub repository.

Requires: `gh` CLI (https://cli.github.com/) authenticated with GitHub.

Usage:
    python3 tools/generate_open_tasks.py                      # write to stdout
    python3 tools/generate_open_tasks.py --out docs/Open-tasks.md
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from textwrap import shorten

# Sub-project definitions, in display order. Emojis match the sidebar
# in archbee.json. Contribution-guide URLs use the `#how-to-contribute`
# anchor on the corresponding "About …" page on docs.flipper.net/one.
SECTIONS = [
    {
        "slug": "flipperdevices/flipperone-hardware",
        "title": "Hardware",
        "emoji": "🔌",
        "description": "Electrical hardware development: printed circuit boards (PCBs), antennas, and everything related to the electrical design.",
        "task_tracker": "https://github.com/orgs/flipperdevices/projects/9",
        "contribution_guide": "https://docs.flipper.net/one/hardware/about#how-to-contribute",
        "github_repo": "https://github.com/flipperdevices/flipperone-hardware",
    },
    {
        "slug": "flipperdevices/flipperone-mechanics",
        "title": "Mechanics",
        "emoji": "⚙️",
        "description": "Mechanical design: enclosures, buttons, connectors, and everything related to the physical construction.",
        "task_tracker": "https://github.com/orgs/flipperdevices/projects/15",
        "contribution_guide": "https://docs.flipper.net/one/mechanics/about#how-to-contribute",
        "github_repo": "https://github.com/flipperdevices/flipperone-mechanics",
    },
    {
        "slug": "flipperdevices/flipperone-linux-build-scripts",
        "title": "Linux (CPU Software)",
        "emoji": "🐧",
        "description": "Build system for the Linux firmware: U-Boot, kernel, root filesystem, and bootable images for the RK3576.",
        "task_tracker": "https://github.com/orgs/flipperdevices/projects/11",
        "contribution_guide": "https://docs.flipper.net/one/cpu-software/about#how-to-contribute",
        "github_repo": "https://github.com/flipperdevices/flipperone-linux-build-scripts",
    },
    {
        "slug": "flipperdevices/flipperone-mcu-firmware",
        "title": "MCU Firmware",
        "emoji": "🕹️",
        "description": "Firmware for the RP2350 co-processor: FreeRTOS, display, buttons, touchpad, LEDs, and power management.",
        "task_tracker": "https://github.com/orgs/flipperdevices/projects/8",
        "contribution_guide": "https://docs.flipper.net/one/mcu-firmware/about#how-to-contribute",
        "github_repo": "https://github.com/flipperdevices/flipperone-mcu-firmware",
    },
    {
        "slug": "flipperdevices/flipperone-ui",
        "title": "User Interface",
        "emoji": "🎨",
        "description": "User interface design: operating modes, on-screen graphics, device prints, and FlipCTL.",
        "task_tracker": "https://github.com/orgs/flipperdevices/projects/12",
        "contribution_guide": "https://docs.flipper.net/one/user-interface/about#how-to-contribute",
        "github_repo": "https://github.com/flipperdevices/flipperone-ui",
    },
    {
        "slug": "flipperdevices/flipperone-testing",
        "title": "Testing",
        "emoji": "🧪",
        "description": "Hardware validation and test scripts: temperature monitoring, power, CPU, GPU, network, and disk tests.",
        "task_tracker": "https://github.com/orgs/flipperdevices/projects/14",
        "contribution_guide": "https://docs.flipper.net/one/testing/about#how-to-contribute",
        "github_repo": "https://github.com/flipperdevices/flipperone-testing",
    },
    {
        "slug": "flipperdevices/flipperone-docs",
        "title": "Docs",
        "emoji": "📚",
        "description": "Developer documentation published at docs.flipper.net/one.",
        "task_tracker": "https://github.com/orgs/flipperdevices/projects/10",
        "contribution_guide": "https://docs.flipper.net/one/resources/about-docs#how-to-contribute",
        "github_repo": "https://github.com/flipperdevices/flipperone-docs",
    },
]

LABEL = "help wanted"
ORG = "flipperdevices"
SCRIPT_URL = "https://github.com/flipperdevices/flipperone-docs/blob/public-release/tools/generate_open_tasks.py"


def fetch_issues() -> list[dict]:
    """Fetch all open `help wanted` issues across the org via the `gh` CLI."""
    result = subprocess.run(
        [
            "gh", "search", "issues",
            "--owner", ORG,
            "--label", LABEL,
            "--state", "open",
            "--limit", "200",
            "--json", "repository,title,number,url,body,commentsCount",
        ],
        capture_output=True, text=True, check=True,
    )
    return json.loads(result.stdout)


def load_issues_from_file(path: Path) -> list[dict]:
    """For local testing without `gh`: load a JSON array of issues from a file."""
    return json.loads(path.read_text(encoding="utf-8"))


def _clean_summary_line(line: str) -> str:
    """Remove Markdown/HTML fragments that make issue summaries hard to scan."""
    line = re.sub(r"`([^`]+)`", r"\1", line)
    line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)
    line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)
    line = re.sub(r"</?[^>]+>", "", line)
    line = re.sub(r"[*_~]+", "", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip(" -–—:;")


def make_summary(body: str, max_len: int = 120) -> str:
    """Pull the first meaningful line of an issue body and shorten it."""
    if not body:
        return "No description provided."
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)  # strip HTML comments
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(("![", "<", "http://", "https://", "#")):
            continue
        line = line.lstrip("*_-•> ")
        line = _clean_summary_line(line)
        if len(line) < 5:
            continue
        return shorten(line, width=max_len, placeholder="...")
    return "No description provided."


def html_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
    )


def archbee_timestamp(dt: datetime) -> str:
    """Match Archbee's frontmatter format: `Wed Apr 08 2026 17:29:37 GMT+0000 (Coordinated Universal Time)`."""
    return dt.strftime("%a %b %d %Y %H:%M:%S GMT+0000 (Coordinated Universal Time)")


def parse_existing_created_at(path: Path | None) -> str | None:
    """Preserve `createdAt` from an existing Open-tasks.md, if present."""
    if not path or not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^createdAt:\s*(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def _content_equal_ignoring_updated_at(a: str, b: str) -> bool:
    """True if two page renderings differ only in the `updatedAt:` frontmatter line.

    The timestamp bumps on every run, so without this the workflow would commit
    a noise-only diff every hour.
    """
    pattern = re.compile(r"^updatedAt:.*$", flags=re.MULTILINE)
    return pattern.sub("updatedAt: -", a) == pattern.sub("updatedAt: -", b)


def render_section(section: dict, issues: list[dict]) -> str:
    lines: list[str] = []
    lines.append(f"# {section['emoji']} {section['title']} tasks")
    lines.append("")
    lines.append(section["description"])
    lines.append("")

    if issues:
        # Render an issue table if there is at least one "help wanted" issue

        lines.append('<table isTableHeaderOn="true" columnWidths="536,125">')
        lines.append("  <tr>")
        lines.append('    <td align="left">')
        lines.append("      <p><strong>Task</strong></p>")
        lines.append("    </td>")
        lines.append('    <td align="center">')
        lines.append("      <p><strong>Comments</strong></p>")
        lines.append("    </td>")
        lines.append("  </tr>")

        for issue in sorted(issues, key=lambda i: i["number"], reverse=True):
            title = html_escape(issue["title"])
            url = html_escape(issue["url"])
            comments = issue["commentsCount"]
            summary = make_summary(issue.get("body", ""))

            lines.append("  <tr>")
            lines.append('    <td align="left" colSpan="1" rowSpan="1">')
            lines.append(f'      <p>🟢 <a href="{url}">{title}</a></p>')
            lines.append(f"      <p>{html_escape(summary)}</p>")
            lines.append("    </td>")
            lines.append('    <td align="center" colSpan="1" rowSpan="1">')
            lines.append(f"      <p>💬 {comments}</p>")
            lines.append("    </td>")
            lines.append("  </tr>")

        lines.append("</table>")

    else:
        # If there are no open "help wanted" issues, give the reader general guidance
        lines.append(f"The {section['title']} sub-project currently has no open `help wanted` tasks. ")


    lines.append("")
    lines.append(':::hint{type="info"}')
    lines.append(f"Learn what's going on in the {section['title']} sub-project:")
    lines.append("")
    lines.append(f"- [Project board]({section['task_tracker']})")
    lines.append(f"- [Contribution guide]({section['contribution_guide']})")
    lines.append(f"- [GitHub repository]({section['github_repo']})")
    lines.append(f"- [All open tasks]({section['github_repo']}/issues/)")
    lines.append(":::")
    return "\n".join(lines)


def generate_page(issues: list[dict], existing_created_at: str | None = None) -> str:
    by_repo: dict[str, list[dict]] = {}
    for issue in issues:
        repo_full = issue["repository"]["nameWithOwner"]
        by_repo.setdefault(repo_full, []).append(issue)

    now = datetime.now(timezone.utc)
    created_at = existing_created_at or archbee_timestamp(now)
    updated_at = archbee_timestamp(now)

    out: list[str] = []
    out.append("---")
    out.append("title: 🚧 Open tasks")
    out.append("slug: open-tasks")
    out.append("docTags: ")
    out.append(f"createdAt: {created_at}")
    out.append(f"updatedAt: {updated_at}")
    out.append("---")
    out.append("")
    out.append(f"<!-- Auto-generated by tools/generate_open_tasks.py — do not edit manually. Source: {SCRIPT_URL} -->")
    out.append("")
    out.append(
        "This page highlights open tasks across all Flipper One sub-project repositories that "
        "need community help or feedback. Each task corresponds to an issue labeled `help wanted` "
        "in its respective GitHub repository."
    )
    out.append("")
    out.append(
        "All tasks on this page are organized by sub-project and include a title, a short "
        "description, the number of comments, and a link to the task on GitHub. Each sub-project "
        "is managed by a team that defines its own contribution process — please review these "
        "guidelines before contributing."
    )
    out.append("")
    out.append(':::hint{type="info"}')
    out.append("Before you join an open task:")
    out.append("")
    out.append("- Read [How to start](./How-to-join.md#how-to-start).")
    out.append("- Study the task description and existing comments.")
    out.append("- When you comment on the task, add concrete evidence: screenshots, logs, measurements, code, design files, or links.")
    out.append(":::")
    out.append("")
    out.append("***")
    out.append("")

    for section in SECTIONS:
        repo_issues = by_repo.get(section["slug"], [])
        if section != SECTIONS[0]:
            out.append("***")
            out.append("")
        out.append(render_section(section, repo_issues))
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=None,
                        help="Write output to this path. Defaults to stdout.")
    parser.add_argument("--existing", type=Path, default=None,
                        help="Existing Open-tasks.md to read createdAt from. "
                             "Defaults to --out (if set) or docs/Open-tasks.md relative to this script.")
    parser.add_argument("--input-json", type=Path, default=None,
                        help="Load issues from this JSON file instead of calling `gh` (for testing).")
    args = parser.parse_args()

    default_existing = Path(__file__).resolve().parent.parent / "docs" / "Open-tasks.md"
    existing_path = args.existing or args.out or default_existing
    existing_created_at = parse_existing_created_at(existing_path)

    issues = (load_issues_from_file(args.input_json)
              if args.input_json else fetch_issues())
    page = generate_page(issues, existing_created_at=existing_created_at)

    if args.out:
        if args.out.exists():
            existing_text = args.out.read_text(encoding="utf-8")
            if _content_equal_ignoring_updated_at(existing_text, page):
                # Nothing of substance changed — leave the file alone so the
                # workflow doesn't commit a timestamp-only diff.
                return 0
        args.out.write_text(page, encoding="utf-8")
    else:
        sys.stdout.write(page)
    return 0


if __name__ == "__main__":
    sys.exit(main())
