#!/usr/bin/env python3
"""Plant known failures to prove question_map_audit.py detects them."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]


class QuestionMapAuditPositiveControls(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "question-map").mkdir(parents=True)
        (self.root / "scripts").mkdir()
        shutil.copy2(REPO / "question-map/index.html", self.root / "question-map/index.html")
        shutil.copy2(REPO / "scripts/question_map_audit.py", self.root / "scripts/question_map_audit.py")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_audit(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/question_map_audit.py"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )

    def replace_once(self, old: str, new: str) -> None:
        path = self.root / "question-map/index.html"
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_current_map_passes(self) -> None:
        self.assertEqual(self.run_audit().returncode, 0)

    def test_ambiguous_kestin_sample_fails(self) -> None:
        self.replace_once("194 eligible participants", "194–316*")
        result = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("194 eligible participants", result.stderr)

    def test_missing_search_control_fails(self) -> None:
        self.replace_once('id="study-search"', 'id="study-search-removed"')
        result = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("study-search", result.stderr)

    def test_missing_accessible_question_label_fails(self) -> None:
        self.replace_once("control.setAttribute('aria-label'", "control.setAttribute('data-label'")
        result = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("aria-label", result.stderr)

    def test_missing_study_card_fails(self) -> None:
        self.replace_once('<div class="snode"', '<div class="study-node-removed"')
        result = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("study appearances", result.stderr)


if __name__ == "__main__":
    unittest.main()
