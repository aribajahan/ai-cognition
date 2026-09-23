#!/usr/bin/env python3
"""Check the public question map's fixed data and interaction contract."""

from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path


MAP_PATH = Path("question-map/index.html")
REQUIRED_IDS = {
    "study-search",
    "timing-filter",
    "publication-filter",
    "clear-filters",
    "filter-status",
    "no-results",
}
REQUIRED_TEXT = (
    "194 eligible participants",
    "316 condition-level pre-test observations",
    "Direct link to ",
    "control.setAttribute('aria-label'",
    "button.setAttribute('aria-expanded'",
    "51 study appearances shown",
)
FORBIDDEN_TEXT = ("194–316*", "check the paper")


class IdCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.append(attributes["id"] or "")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    path = args.root.resolve() / MAP_PATH
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    collector = IdCollector()
    collector.feed(text)
    found_ids = set(collector.ids)
    for required_id in sorted(REQUIRED_IDS - found_ids):
        errors.append(f"{MAP_PATH} is missing control id: {required_id}")
    if len(collector.ids) != len(found_ids):
        errors.append(f"{MAP_PATH} contains duplicate static ids")

    for required in REQUIRED_TEXT:
        if required not in text:
            errors.append(f"{MAP_PATH} is missing required text: {required!r}")
    for forbidden in FORBIDDEN_TEXT:
        if forbidden in text:
            errors.append(f"{MAP_PATH} still contains retired text: {forbidden!r}")

    appearances = text.count('<div class="snode"')
    if appearances != 51:
        errors.append(f"{MAP_PATH} contains {appearances} study appearances; expected 51")

    if errors:
        print("Question-map audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Question-map audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
