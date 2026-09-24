#!/usr/bin/env python3
"""Audit the published 110-source question map's structural contract."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


MAP_PATH = Path("question-map/index.html")
REQUIRED_IDS = {"search", "role", "timing", "clear", "status", "no-results", "map"}


class IdCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.append(attributes["id"] or "")


def audit(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    collector = IdCollector()
    collector.feed(text)
    found_ids = set(collector.ids)

    for required_id in sorted(REQUIRED_IDS - found_ids):
        errors.append(f"missing control id: {required_id}")
    if len(collector.ids) != len(found_ids):
        errors.append("contains duplicate HTML ids")

    cards = re.findall(r'<article class="study-card"[^>]*>', text)
    branches = re.findall(r'<section class="branch" data-branch>', text)
    subquestions = re.findall(r'<button class="subquestion-toggle"[^>]*>', text)
    info_buttons = re.findall(r'<button class="info"[^>]*>', text)
    takeaway_texts = re.findall(r'<p class="takeaway">(.*?)</p>', text, flags=re.DOTALL)
    views = Counter(re.findall(r'data-view="([^"]+)"', "\n".join(cards)))

    expected_counts = {
        "study appearances": (len(cards), 111),
        "branches": (len(branches), 9),
        "collapsible subquestions": (len(subquestions), 50),
        "statistic explanations": (len(info_buttons), 6),
        "study takeaways": (text.count('class="takeaway"'), 111),
        "full study descriptions": (text.count('class="study-description"'), 111),
        "source-basis disclosures": (text.count("<dt>Source basis</dt>"), 111),
    }
    for label, (actual, expected) in expected_counts.items():
        if actual != expected:
            errors.append(f"contains {actual} {label}; expected {expected}")

    expected_views = Counter({"ai_studies": 86, "other_technology_studies": 15, "cognitive_psychology_studies": 10})
    if views != expected_views:
        errors.append(f"appearance view counts are {dict(views)}; expected 86/15/10")

    required_text = (
        "While writing",
        "110 source records",
        "Is something missing?",
        "Questions still unanswered",
        "Protocol — no results",
        'title="Open study"',
        'content:" ↗"',
        "branches.forEach(other=>",
        "branch.querySelectorAll('.subquestion-toggle')",
        "[hidden]{display:none!important}",
    )
    for required in required_text:
        if required not in text:
            errors.append(f"missing required map contract: {required!r}")
    if text.count("Questions still unanswered") != 9:
        errors.append("every branch must contain a Questions still unanswered section")
    unanswered_sections = re.findall(r'<section class="unanswered">.*?</section>', text, flags=re.DOTALL)
    if len(unanswered_sections) != 9 or any("<li>" not in section for section in unanswered_sections):
        errors.append("every unanswered section must contain at least one question")
    if text.count('class="retracted"') != 1:
        errors.append("expected exactly one visibly retracted card")
    if text.count('class="reviewing"') != 1 or text.count("Corrected analysis under review") != 1:
        errors.append("expected exactly one neutral corrected-analysis-under-review badge")
    if "grid-template-columns:repeat(3,minmax(0,1fr))" not in text:
        errors.append("summary cards are not fixed to three columns on wide screens")
    if "repeat(4" in text:
        errors.append("four-column grid found in map")
    required_corrections = (
        "Harder tasks, easier-to-check explanations, and larger accuracy incentives reduced overreliance",
        "their gains were statistically indistinguishable from human-authored hints",
        "the cross-sectional survey cannot establish direction or cause",
        "a corrected analysis is under review after reproducibility problems in the public dataset",
        "extra spliced rows were found in the public dataset",
        "Among 28 participants, default and guided GPT produced nearly identical factual-recall scores",
        "scored 57.5% on a 20-item retention test",
        "20-item suctioning-knowledge questionnaire",
        "four ways AI can affect learning—inversion",
        "Among 69 learners ages 10–17",
        "In a randomized study of 52 junior developers",
        "neutral-control conversations produced no change",
        "after AI was removed with 45-day follow-up",
        "after AI was removed with six-week follow-up",
        '<label class="sr-only" for="role">Evidence role</label>',
        '<label class="sr-only" for="timing">Outcome timing</label>',
    )
    for required in required_corrections:
        if required not in text:
            errors.append(f"missing audited correction: {required!r}")
    forbidden_stale_copy = (
        "Incentives increased overreliance",
        "impaired learning",
        "AI use predicts skill atrophy",
    )
    for stale in forbidden_stale_copy:
        if stale in text:
            errors.append(f"contains superseded map copy: {stale!r}")
    process_phrases = (
        "verified in analysis",
        "Moved from ",
        "included as theory context",
        "included as synthesis context",
        "belongs with the",
        "Compares GPT",
        "Three preregistered randomized experiments compare",
    )
    for phrase in process_phrases:
        if any(phrase in takeaway for takeaway in takeaway_texts):
            errors.append(f"takeaway contains internal process language: {phrase!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    errors = audit(args.root.resolve() / MAP_PATH)
    if errors:
        print("Question-map audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Question-map audit passed: 110 sources, 111 appearances, 9 branches.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
