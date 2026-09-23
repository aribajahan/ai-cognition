#!/usr/bin/env python3
"""Plant known failures to prove corpus_audit.py detects them."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
FILES = (
    "data/ai_cognition_evidence_table.csv",
    "data/benefit_side_studies.csv",
    "data/perplexity_evidence_table.csv",
    "data/corpus_census.json",
)
DOCUMENTS = ("data/README.md", "synthesis.md", "field-notes.md")


class CorpusAuditPositiveControls(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for relative in FILES + DOCUMENTS:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / relative, target)
        (self.root / "scripts").mkdir(exist_ok=True)
        shutil.copy2(REPO / "scripts/corpus_audit.py", self.root / "scripts/corpus_audit.py")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_audit(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/corpus_audit.py"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_current_tables_pass(self) -> None:
        self.assertEqual(self.run_audit().returncode, 0)

    def test_wrong_overlap_label_fails(self) -> None:
        table = self.root / FILES[2]
        text = table.read_text(encoding="utf-8")
        table.write_text(text.replace("yes (benefit-side),belief change", "no,belief change", 1), encoding="utf-8")
        result = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("overlap label", result.stderr)

    def test_stale_census_fails(self) -> None:
        census = self.root / FILES[3]
        saved = json.loads(census.read_text(encoding="utf-8"))
        saved["perplexity_records"] += 1
        census.write_text(json.dumps(saved), encoding="utf-8")
        self.assertNotEqual(self.run_audit().returncode, 0)

    def test_historical_record_is_ignored(self) -> None:
        noise = self.root / "research/perplexity/runs/old.csv"
        noise.parent.mkdir(parents=True, exist_ok=True)
        noise.write_text("old,incorrect,count\n", encoding="utf-8")
        self.assertEqual(self.run_audit().returncode, 0)

    def test_stale_maintained_document_fails(self) -> None:
        document = self.root / DOCUMENTS[0]
        text = document.read_text(encoding="utf-8")
        document.write_text(text.replace("64", "73", 1), encoding="utf-8")
        result = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing current census claim", result.stderr)


if __name__ == "__main__":
    unittest.main()
