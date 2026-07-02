#!/usr/bin/env python3

import json
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_open_tasks import fetch_linked_prs, generate_page, make_summary, _Issue


class GenerateOpenTasksTest(unittest.TestCase):
    def test_make_summary_strips_markdown_artifacts(self) -> None:
        body = """
        <!-- template metadata -->
        # Context

        ![screenshot](image.png)

        **DDR memory init code** is a tiny program that runs during early boot.
        """

        self.assertEqual(
            make_summary(body),
            "DDR memory init code is a tiny program that runs during early boot.",
        )

    def test_make_summary_uses_explicit_fallback(self) -> None:
        self.assertEqual(make_summary(""), "No description provided.")

    def test_generate_page_renders_empty_sections_and_comments_header(self) -> None:
        issues: list[_Issue] = [
            {
                "repository": {
                    "nameWithOwner": "flipperdevices/flipperone-linux-build-scripts"
                },
                "title": "Hardware Video Decoding",
                "number": 13,
                "url": "https://github.com/flipperdevices/flipperone-linux-build-scripts/issues/13",
                "body": "Hardware video decoding is currently supported only in BSP kernel.",
                "commentsCount": 10,
            }
        ]

        page = generate_page(
            issues,
            existing_created_at="Thu Apr 01 2077 17:29:37 GMT+0000 (Coordinated Universal Time)",
        )

        self.assertIn("# 🔌 Hardware tasks", page)
        self.assertIn(
            "The Hardware sub-project currently has no open `help wanted` tasks.", page
        )
        self.assertIn("# 🐧 Linux (CPU Software) tasks", page)
        self.assertIn("<p><strong>Comments</strong></p>", page)

    def test_generate_page_renders_linked_prs(self) -> None:
        issues: list[_Issue] = [
            {
                "repository": {
                    "nameWithOwner": "flipperdevices/flipperone-linux-build-scripts"
                },
                "title": "Hardware Video Decoding",
                "number": 13,
                "url": "https://github.com/flipperdevices/flipperone-linux-build-scripts/issues/13",
                "body": "Hardware video decoding lol.",
                "commentsCount": 10,
                "linkedPRs": [
                    {
                        "number": 99,
                        "url": "https://github.com/flipperdevices/flipperone-linux-build-scripts/pull/99",
                        "title": 'Add "<MPP>" decoder & fixes',
                        "isDraft": True,
                    }
                ],
            }
        ]

        page = generate_page(issues)

        # PR-provided title contains ", <, >, & — all must be HTML-escaped.
        self.assertIn(
            '<p>🔀 <a href="https://github.com/flipperdevices/flipperone-linux-build-scripts/pull/99">#99</a> Add &quot;&lt;MPP&gt;&quot; decoder &amp; fixes (draft)</p>',
            page,
        )

    def test_fetch_linked_prs_parses_nodes(self) -> None:
        payload = {
            "data": {
                "repository": {
                    "issue": {
                        "closedByPullRequestsReferences": {
                            "nodes": [
                                {
                                    "number": 99,
                                    "url": "u",
                                    "title": "t",
                                    "isDraft": True,
                                }
                            ]
                        }
                    }
                }
            }
        }
        with mock.patch("generate_open_tasks.subprocess.run") as run:
            run.return_value = mock.Mock(stdout=json.dumps(payload))
            prs = fetch_linked_prs("flipperdevices/repo", 13)

        self.assertEqual(
            prs,
            payload["data"]["repository"]["issue"]["closedByPullRequestsReferences"][
                "nodes"
            ],
        )
        # owner/repo split correctly passed to gh
        args = run.call_args[0][0]
        self.assertIn("owner=flipperdevices", args)
        self.assertIn("repo=repo", args)
        self.assertIn("number=13", args)

    def test_fetch_linked_prs_handles_missing_issue(self) -> None:
        with mock.patch("generate_open_tasks.subprocess.run") as run:
            run.return_value = mock.Mock(
                stdout=json.dumps({"data": {"repository": {"issue": None}}})
            )
            self.assertEqual(fetch_linked_prs("o/r", 1), [])


if __name__ == "__main__":
    unittest.main()
