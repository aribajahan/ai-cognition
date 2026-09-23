#!/usr/bin/env python3
"""Plant known failures to prove question_map_audit.py detects them."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from question_map_audit import MAP_PATH, audit


REPO = Path(__file__).resolve().parents[1]


class QuestionMapAuditPositiveControls(unittest.TestCase):
    def check_mutation(self, old: str, new: str, expected: str) -> None:
        source = (REPO / MAP_PATH).read_text(encoding="utf-8")
        self.assertIn(old, source)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "map.html"
            path.write_text(source.replace(old, new, 1), encoding="utf-8")
            self.assertTrue(any(expected in error for error in audit(path)))

    def test_current_map_passes(self) -> None:
        self.assertEqual(audit(REPO / MAP_PATH), [])

    def test_missing_card_is_caught(self) -> None:
        self.check_mutation('class="study-card"', 'class="removed-card"', "study appearances")

    def test_missing_branch_is_caught(self) -> None:
        self.check_mutation('class="branch" data-branch', 'class="removed-branch" data-branch', "branches")

    def test_missing_subquestion_is_caught(self) -> None:
        self.check_mutation('class="subquestion-toggle"', 'class="removed-subquestion"', "collapsible subquestions")

    def test_missing_stat_explanation_is_caught(self) -> None:
        self.check_mutation('class="info"', 'class="removed-info"', "statistic explanations")

    def test_missing_takeaway_is_caught(self) -> None:
        self.check_mutation('class="takeaway"', 'class="removed-takeaway"', "study takeaways")

    def test_missing_description_is_caught(self) -> None:
        self.check_mutation('class="study-description"', 'class="removed-description"', "full study descriptions")

    def test_four_column_summary_is_caught(self) -> None:
        self.check_mutation("repeat(3,minmax(0,1fr))", "repeat(4,minmax(0,1fr))", "three columns")

    def test_hidden_retraction_is_caught(self) -> None:
        self.check_mutation('class="retracted"', 'class="neutral"', "visibly retracted")

    def test_missing_hidden_state_is_caught(self) -> None:
        self.check_mutation("[hidden]{display:none!important}", "[hidden]{display:block}", "hidden")


if __name__ == "__main__":
    unittest.main()
