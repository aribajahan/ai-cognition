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
    views = Counter(re.findall(r'data-view="([^"]+)"', "\n".join(cards)))

    expected_counts = {
        "study appearances": (len(cards), 111),
        "branches": (len(branches), 9),
        "collapsible subquestions": (len(subquestions), 50),
        "statistic explanations": (len(info_buttons), 6),
        "study takeaways": (text.count('class="takeaway"'), 111),
        "full study descriptions": (text.count('class="study-description"'), 111),
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
    if text.count('class="retracted"') != 1:
        errors.append("expected exactly one visibly retracted card")
    if "grid-template-columns:repeat(3,minmax(0,1fr))" not in text:
        errors.append("summary cards are not fixed to three columns on wide screens")
    if "repeat(4" in text:
        errors.append("four-column grid found in map")
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
