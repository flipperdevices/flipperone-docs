#!/usr/bin/env python3

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_open_tasks import generate_page, make_summary


class GenerateOpenTasksTest(unittest.TestCase):
    def test_make_summary_strips_markdown_artifacts(self):
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

    def test_make_summary_uses_explicit_fallback(self):
        self.assertEqual(make_summary(""), "No description provided.")

    def test_generate_page_renders_empty_sections_and_comments_header(self):
        issues = [
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

        page = generate_page(issues, existing_created_at="Wed Apr 08 2026 17:29:37 GMT+0000 (Coordinated Universal Time)")

        self.assertIn("# 🔌 Hardware tasks", page)
        self.assertIn("The Hardware sub-project currently has no open `help wanted` tasks.", page)
        self.assertIn("# 🐧 Linux (CPU Software) tasks", page)
        self.assertIn("<p><strong>Comments</strong></p>", page)


if __name__ == "__main__":
    unittest.main()
