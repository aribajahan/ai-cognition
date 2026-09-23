# Data guide

## Current corpus

The public data now preserves each research environment's source records and the combined table used
to build the question map. The counts were verified from parsed CSV rows on September 23, 2026.

- The Claude Science first-pass table contains **45 study records**. Its original 46th row was a
  correction notice rather than a study.
- The Claude Science benefit-side table contains **24 records**. Seven overlap with the first pass,
  leaving **62 unique Claude Science source records**.
- The Perplexity table contains **64 source records**. **16 also appear** in the Claude Science
  corpus, leaving **48 Perplexity-only records**.
- The combined table reconciles those overlaps into **110 unique source records**. It is the source
  table for the current question map.

`corpus_census.json` is the machine-readable census. Run `python3 scripts/corpus_audit.py` from the
repository root before publishing changed counts or tables.

## Source and synthesis tables

| File | Rows | What it contains |
|---|---:|---|
| [`claude_science_first_pass_records.csv`](claude_science_first_pass_records.csv) | 45 | Claude Science's first retrieval pass across memory, learning and skill, judgment, and brain or physiological measures. |
| [`claude_science_benefit_side_records.csv`](claude_science_benefit_side_records.csv) | 24 | Claude Science's second pass on benefits and countervailing evidence. Seven records overlap with the first pass. |
| [`perplexity_source_records.csv`](perplexity_source_records.csv) | 64 | Records surfaced across nine Perplexity runs. Sixteen overlap with the Claude Science corpus. |
| [`combined_source_records.csv`](combined_source_records.csv) | 110 | The canonical cross-tool table, with overlap reconciled and provenance retained for every record. |
| [`combined_question_map_placements.csv`](combined_question_map_placements.csv) | 110 | The reviewed question, sub-question, evidence role, and relationship assigned to every canonical source. One source appears twice in the rendered map because it answers two questions. |

## Analysis tables

| File | Rows | What it contains |
|---|---:|---|
| `construct_map.csv` | 62 | Coding of the task, claimed capacity, actual measure, and inference gap for the Claude Science corpus. |
| `critical_thinking_construct_audit.csv` | 7 | Studies commonly used to support claims about AI and critical thinking. |
| `dissociation_coding.csv` | 50 | Coding for whether outcome type predicts the direction of a reported result. |
| `preai_offloading_studies.csv` | 51 | Earlier research on offloading cognition to GPS, automation, calculators, spell-check, search, and other tools. |

## Reading the fields

The tool-specific tables preserve the fields produced during each search, so their schemas differ.
The combined table normalizes the fields needed for cross-tool analysis: citation, publication status,
source access, design, sample, population, exposure, measures, finding, limitation, outcome timing,
evidence role, and provenance.

`outcome_timing` distinguishes performance measured with assistance from performance measured after
the tool was removed. An outcome measured after removal may still be an immediate post-test. It does
not by itself establish a durable effect.

The tables are a study index and audit trail. The studies differ too much in their tasks,
populations, interventions, measures, and source access to pool every row into one effect estimate.
Rows based on abstracts or metadata carry less detail than records extracted from full papers.

The construct, dissociation, and map-placement fields are project coding developed with AI
assistance and reviewed by Ariba Jahan. They make the analytical choices inspectable; they are not
independent ratings by multiple researchers.
