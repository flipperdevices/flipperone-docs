#!/usr/bin/env python3
"""
Generate docs/Open-tasks.md from GitHub issues labeled "help wanted"
across all Flipper One sub-project repositories.

Output is Archbee-flavored Markdown matching the design of the page on
https://docs.flipper.net/one/open-tasks — YAML frontmatter, per-section
HTML tables (with isTableHeaderOn / columnWidths), and `:::hint{type="info"}`
blocks linking to the sub-project's task tracker, contribution guide,
and GitHub repository.

Requires:
    - `gh` CLI (https://cli.github.com/) authenticated with GitHub.
    - Jinja2 (`python3 -m pip install -r requirements.txt`).

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
from typing import TypedDict

from jinja2 import Environment, FileSystemLoader

# Sub-project definitions, in display order. Emojis match the sidebar
# in archbee.json. Contribution-guide URLs use the `#how-to-contribute`
# anchor on the corresponding "About …" page on docs.flipper.net/one.
SECTIONS: list[_Section] = [
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
SECTION_SLUGS = {section["slug"] for section in SECTIONS}
ORG_MEMBER_ASSOCIATIONS = {"MEMBER", "OWNER"}
SCRIPT_URL = "https://github.com/flipperdevices/flipperone-docs/blob/public-release/tools/generate_open_tasks.py"
TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"
TEMPLATE_NAME = "open_tasks.md.j2"


class _Repository(TypedDict):
    nameWithOwner: str

class _Section(TypedDict):
    slug: str
    title: str
    emoji: str
    description: str
    task_tracker: str
    contribution_guide: str
    github_repo: str

class _LinkedPR(TypedDict, total=False):
    number: int
    url: str
    title: str
    isDraft: bool

class _Issue(TypedDict, total=False):
    repository: _Repository
    number: int
    title: str
    url: str
    commentsCount: int
    body: str
    linkedPRs: list[_LinkedPR]

class _DisplayLinkedPR(TypedDict):
    number: int
    url: str
    title: str
    is_draft: bool

class _DisplayIssue(TypedDict):
    number: int
    title: str
    url: str
    summary: str
    comments_count: int
    linked_prs: list[_DisplayLinkedPR]

class _DisplaySection(_Section):
    issues: list[_DisplayIssue]

class _Author(TypedDict, total=False):
    login: str
    is_bot: bool

class _CommunityPR(TypedDict, total=False):
    repository: _Repository
    number: int
    title: str
    url: str
    isDraft: bool
    commentsCount: int
    author: _Author
    authorAssociation: str

class _DisplayCommunityPR(TypedDict):
    number: int
    url: str
    title: str
    repo: str
    author: str
    comments_count: int
    is_draft: bool


def fetch_issues() -> list[_Issue]:
    """Fetch all open `help wanted` issues across the org, each with its `linkedPRs` var."""
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
    issues: list[_Issue] = json.loads(result.stdout)
    for issue in issues:
        issue["linkedPRs"] = fetch_linked_prs(
            issue["repository"]["nameWithOwner"], issue["number"]
        )
    return issues


_LINKED_PRS_QUERY = """
query($owner: String!, $repo: String!, $number: Int!) {
  repository(owner: $owner, name: $repo) {
    issue(number: $number) {
      closedByPullRequestsReferences(first: 10, includeClosedPrs: false) {
        nodes { number url title isDraft }
      }
    }
  }
}
"""


def fetch_linked_prs(repo_full: str, number: int) -> list[_LinkedPR]:
    """Return the open PRs linked to `repo_full#number`."""
    owner, repo = repo_full.split("/", 1)
    result = subprocess.run(
        [
            "gh", "api", "graphql",
            "-f", f"query={_LINKED_PRS_QUERY}",
            "-F", f"owner={owner}",
            "-F", f"repo={repo}",
            "-F", f"number={number}",
        ],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(result.stdout)
    refs = (data.get("data", {}).get("repository", {}) or {}).get("issue") or {}
    nodes: list[_LinkedPR] = (refs.get("closedByPullRequestsReferences") or {}).get("nodes") or []
    return nodes


def is_community_pr(pr: _CommunityPR) -> bool:
    """True if the PR is from a non-org, non-bot author."""
    if pr.get("author", {}).get("is_bot"):
        return False
    return pr.get("authorAssociation", "").upper() not in ORG_MEMBER_ASSOCIATIONS


_LINKED_ISSUE_QUERY = """
query($owner: String!, $repo: String!, $number: Int!) {
  repository(owner: $owner, name: $repo) {
    pullRequest(number: $number) {
      closingIssuesReferences(first: 1) { totalCount }
    }
  }
}
"""


def pr_has_linked_issue(repo_full: str, number: int) -> bool:
    """True if the PR closes or links at least one issue."""
    owner, repo = repo_full.split("/", 1)
    result = subprocess.run(
        [
            "gh", "api", "graphql",
            "-f", f"query={_LINKED_ISSUE_QUERY}",
            "-F", f"owner={owner}",
            "-F", f"repo={repo}",
            "-F", f"number={number}",
        ],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(result.stdout)
    pr = ((data.get("data", {}).get("repository", {}) or {}).get("pullRequest")) or {}
    return ((pr.get("closingIssuesReferences") or {}).get("totalCount") or 0) > 0


def fetch_community_prs() -> list[_CommunityPR]:
    """Fetch open PRs in the sub-project repos that are from community authors and
    not linked to any issue."""
    result = subprocess.run(
        [
            "gh", "search", "prs",
            "--owner", ORG,
            "--state", "open",
            "--limit", "200",
            "--json", "repository,number,title,url,isDraft,commentsCount,author,authorAssociation",
        ],
        capture_output=True, text=True, check=True,
    )
    prs: list[_CommunityPR] = json.loads(result.stdout)
    community: list[_CommunityPR] = []
    for pr in prs:
        repo_full = pr["repository"]["nameWithOwner"]
        if repo_full not in SECTION_SLUGS:
            continue
        if not is_community_pr(pr):
            continue
        if pr_has_linked_issue(repo_full, pr["number"]):
            continue
        community.append(pr)
    return community


def load_issues_from_file(path: Path) -> list[_Issue]:
    """For local testing without `gh`: load a JSON array of issues from a file."""
    return json.loads(path.read_text(encoding="utf-8"))  # type: ignore[no-any-return]


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


def _build_template_sections(issues: list[_Issue]) -> list[_DisplaySection]:
    """Prepare section and issue data for the Open Tasks Jinja template."""
    by_repo: dict[str, list[_Issue]] = {}
    for issue in issues:
        repo_full = issue["repository"]["nameWithOwner"]
        by_repo.setdefault(repo_full, []).append(issue)

    sections: list[_DisplaySection] = []
    for section in SECTIONS:
        rendered_issues: list[_DisplayIssue] = [
            {
                "number": issue["number"],
                "title": html_escape(issue["title"]),
                "url": html_escape(issue["url"]),
                "summary": html_escape(make_summary(issue.get("body", ""))),
                "comments_count": issue.get("commentsCount", 0),
                "linked_prs": [
                    {
                        "number": pr["number"],
                        "url": html_escape(pr["url"]),
                        "title": html_escape(pr["title"]),
                        "is_draft": pr.get("isDraft", False),
                    }
                    for pr in issue.get("linkedPRs", [])
                ],
            }
            for issue in by_repo.get(section["slug"], [])
        ]
        rendered_issues.sort(key=lambda i: i["number"], reverse=True)
        sections.append({**section, "issues": rendered_issues})
    return sections


def _build_community_prs(prs: list[_CommunityPR]) -> list[_DisplayCommunityPR]:
    """Prepare community PR data for the Open Tasks Jinja template."""
    display: list[_DisplayCommunityPR] = []
    for pr in prs:
        repo_full = pr["repository"]["nameWithOwner"]
        repo_short = repo_full.split("/", 1)[1] if "/" in repo_full else repo_full
        display.append({
            "number": pr["number"],
            "url": html_escape(pr["url"]),
            "title": html_escape(pr["title"]),
            "repo": html_escape(repo_short),
            "author": html_escape(pr.get("author", {}).get("login", "")),
            "comments_count": pr.get("commentsCount", 0),
            "is_draft": pr.get("isDraft", False),
        })
    display.sort(key=lambda p: (p["repo"], -p["number"]))
    return display


def _render_open_tasks_template(**context: object) -> str:
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=False,
        keep_trailing_newline=True,
        lstrip_blocks=True,
        trim_blocks=True,
    )
    return env.get_template(TEMPLATE_NAME).render(**context)


def generate_page(
    issues: list[_Issue],
    existing_created_at: str | None = None,
    community_prs: list[_CommunityPR] | None = None,
) -> str:
    now = datetime.now(timezone.utc)
    created_at = existing_created_at or archbee_timestamp(now)
    updated_at = archbee_timestamp(now)

    page = _render_open_tasks_template(
        created_at=created_at,
        updated_at=updated_at,
        script_url=SCRIPT_URL,
        sections=_build_template_sections(issues),
        community_prs=_build_community_prs(community_prs or []),
    )
    return page.rstrip() + "\n"


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
    community_prs = [] if args.input_json else fetch_community_prs()
    page = generate_page(issues, existing_created_at=existing_created_at,
                         community_prs=community_prs)

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
