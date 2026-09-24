#!/usr/bin/env python3
"""Plant known failures to prove question_map_audit.py detects them."""

from __future__ import annotations

import tempfile
import unittest
import re
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

    def test_missing_source_basis_is_caught(self) -> None:
        self.check_mutation("<dt>Source basis</dt>", "<dt>Retrieval basis</dt>", "source-basis disclosures")

    def test_missing_review_status_is_caught(self) -> None:
        self.check_mutation('class="reviewing"', 'class="neutral"', "corrected-analysis-under-review")

    def test_reversed_vasconcelos_takeaway_is_caught(self) -> None:
        source = (REPO / MAP_PATH).read_text(encoding="utf-8")
        current = "Harder tasks, easier-to-check explanations, and larger accuracy incentives reduced overreliance"
        stale = "Incentives increased overreliance"
        self.assertIn(current, source)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "map.html"
            path.write_text(source.replace(current, stale, 1), encoding="utf-8")
            self.assertTrue(any("superseded map copy" in error for error in audit(path)))

    def test_missing_filter_label_is_caught(self) -> None:
        self.check_mutation(
            '<label class="sr-only" for="role">Evidence role</label>',
            "",
            "missing audited correction",
        )

    def test_empty_unanswered_section_is_caught(self) -> None:
        source = (REPO / MAP_PATH).read_text(encoding="utf-8")
        emptied = re.sub(
            r'(<section class="unanswered"><h3>Questions still unanswered</h3><ul>).*?(</ul></section>)',
            r"\1\2",
            source,
            count=1,
        )
        self.assertNotEqual(source, emptied)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "map.html"
            path.write_text(emptied, encoding="utf-8")
            self.assertTrue(any("at least one question" in error for error in audit(path)))

    def test_internal_process_takeaway_is_caught(self) -> None:
        self.check_mutation("Watching a crime video", "verified in analysis 13", "internal process language")

    def test_stale_urban_metacognition_wording_is_caught(self) -> None:
        self.check_mutation(
            "smaller confidence-performance gaps were associated with more correct expert information",
            "low confidence predicted better use of expert sources",
            "superseded map copy",
        )

    def test_stale_padmakumar_accounting_is_caught(self) -> None:
        self.check_mutation(
            "each writer completed one to three three-essay sessions",
            "38 writers each produced three essays",
            "superseded map copy",
        )

    def test_stale_budzyn_correction_warning_is_caught(self) -> None:
        self.check_mutation(
            "With no concurrent control group, the study cannot establish that AI exposure caused the decline",
            "the corrected table should be consulted before relying on the adjusted odds ratio",
            "superseded map copy",
        )


if __name__ == "__main__":
    unittest.main()
