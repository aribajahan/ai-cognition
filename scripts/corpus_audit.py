#!/usr/bin/env python3
"""Compute the corpus census and validate cross-table overlap labels.

This intentionally reads only the maintained CSV tables named below. Historical
runs, transcripts, exports, and archives are never searched.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path


PATHS = {
    "first_pass": Path("data/claude_science_first_pass_records.csv"),
    "benefit_side": Path("data/claude_science_benefit_side_records.csv"),
    "perplexity": Path("data/perplexity_source_records.csv"),
    "combined": Path("data/combined_source_records.csv"),
    "placements": Path("data/combined_question_map_placements.csv"),
    "census": Path("data/corpus_census.json"),
}
DOCUMENTS = {
    Path("data/README.md"): ("contains {first} study records", "contains {benefit} records", "leaving {unique}", "contains {perplexity} source records", "{cross} also appear", "leaving {perplexity_only} Perplexity-only"),
    Path("synthesis.md"): ("{first}-record first pass", "{benefit}-record benefit-side pass", "leaving {unique} unique", "separate {perplexity}-record table", "{cross} Perplexity records", "leaving {perplexity_only} Perplexity-only"),
    Path("field-notes.md"): ("contains {perplexity} records", "{cross} also appear", "leaving {perplexity_only} records unique"),
    Path("question-map/README.md"): ("{unique} unique Claude Science source records",),
}

IDENTIFIER_ALIASES = {
    "10.48550/arxiv.2102.09692": "10.1145/3449287",
    "10.48550/arxiv.2502.11919": "10.1145/3706598.3713133",
}


def normalize_text(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", ascii_value.lower()).strip()


def normalize_identifier(value: str) -> str:
    normalized = (value or "").strip().lower()
    normalized = re.sub(r"^https?://(dx\.)?doi\.org/", "", normalized)
    normalized = re.sub(r"^doi:\s*", "", normalized)
    return IDENTIFIER_ALIASES.get(normalized, normalized)


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def source_keys(row: dict[str, str]) -> set[str]:
    keys: set[str] = set()
    identifier = normalize_identifier(row.get("doi", ""))
    title = normalize_text(row.get("title", ""))
    if identifier:
        keys.add(f"id:{identifier}")
    if title:
        keys.add(f"title:{title}")
    return keys


def unique_sources(rows: list[dict[str, str]]) -> set[str]:
    identifiers: dict[str, str] = {}
    titles: set[str] = set()
    for row in rows:
        identifier = normalize_identifier(row.get("doi", ""))
        title = normalize_text(row.get("title", ""))
        if identifier:
            identifiers[identifier] = title
        elif title:
            titles.add(title)
    return {f"id:{item}" for item in identifiers} | {f"title:{item}" for item in titles}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    first = load_rows(root / PATHS["first_pass"])
    benefit = load_rows(root / PATHS["benefit_side"])
    perplexity = load_rows(root / PATHS["perplexity"])
    combined = load_rows(root / PATHS["combined"])
    placements = load_rows(root / PATHS["placements"])
    claude_keys = set().union(*(source_keys(row) for row in first + benefit))
    combined_unique = unique_sources(first + benefit)

    errors: list[str] = []
    combined_ids = [row.get("canonical_id", "") for row in combined]
    placement_ids = [row.get("canonical_id", "") for row in placements]
    if len(combined) != 110 or len(set(combined_ids)) != 110 or "" in combined_ids:
        errors.append(f"{PATHS['combined']} must contain 110 unique canonical source records")
    if len(placements) != 110 or set(placement_ids) != set(combined_ids):
        errors.append(f"{PATHS['placements']} must contain one reviewed placement for every combined source")
    overlap_count = 0
    for line_number, row in enumerate(perplexity, start=2):
        matched = bool(source_keys(row) & claude_keys)
        labelled = row.get("in_claude_science", "").strip().lower().startswith("yes")
        overlap_count += int(matched)
        if matched != labelled:
            errors.append(
                f"{PATHS['perplexity']}:{line_number}: overlap label is "
                f"{row.get('in_claude_science')!r}, computed match is {matched}: {row.get('title')}"
            )

    census = {
        "claude_first_pass_records": len(first),
        "claude_benefit_side_records": len(benefit),
        "claude_internal_overlap": len(first) + len(benefit) - len(combined_unique),
        "claude_unique_records": len(combined_unique),
        "perplexity_records": len(perplexity),
        "cross_tool_overlap": overlap_count,
        "perplexity_only_records": len(perplexity) - overlap_count,
        "combined_unique_records": len(combined),
        "combined_map_placement_records": len(placements),
    }
    census_path = root / PATHS["census"]
    if not census_path.exists() or json.loads(census_path.read_text(encoding="utf-8")) != census:
        errors.append(f"{census_path} is missing or stale")

    values = {
        "first": census["claude_first_pass_records"],
        "benefit": census["claude_benefit_side_records"],
        "unique": census["claude_unique_records"],
        "perplexity": census["perplexity_records"],
        "cross": census["cross_tool_overlap"],
        "perplexity_only": census["perplexity_only_records"],
    }
    for relative_path, templates in DOCUMENTS.items():
        path = root / relative_path
        if not path.exists():
            errors.append(f"Maintained document missing: {path}")
            continue
        text = re.sub(r"\s+", " ", path.read_text(encoding="utf-8").replace("**", ""))
        for template in templates:
            claim = template.format(**values)
            if claim not in text:
                errors.append(f"{path} is missing current census claim: {claim!r}")

    print(json.dumps(census, indent=2, sort_keys=True))
    if errors:
        print("\nCorpus audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("\nCorpus audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
