# Data guide

## Included tables

| File | Rows | What it contains |
|---|---:|---|
| `ai_cognition_evidence_table.csv` | 46 | First-pass evidence records across the AI and cognition question. |
| `benefit_side_studies.csv` | 24 | Second-pass records on benefits and countervailing evidence. Six records overlap with the first pass. |
| `construct_map.csv` | 63 | Project coding of the task, claimed capacity, actual measure, and inference gap for the combined AI-focused corpus. One record could not be coded. |
| `critical_thinking_construct_audit.csv` | 7 | Studies commonly used to support claims about AI and critical thinking. |
| `dissociation_coding.csv` | 50 | Coding for the test of whether outcome type predicts whether a study reports a positive or negative result. |
| `preai_offloading_studies.csv` | 51 | Older research on offloading cognition to non-AI tools. |

## Reading the fields

The two broad evidence tables share many fields:

- `citation`, `title`, `authors`, `year`, `venue`, `doi`, and `url` identify the source.
- `pub_status` records whether the retrieved source was a journal article, preprint, or another publication status.
- `text_basis` records what the project could read: full text, abstract, metadata only, or another accessible source.
- `design`, `n`, `population`, and exposure fields describe the study as reported in retrieved text.
- `measures`, `key_finding`, `effect_size`, and `limitations` retain the project’s source-grounded extraction rather than a new meta-analysis.

`unassisted_outcome_flag` is especially important. It indicates whether a study measured an outcome after the AI tool was removed. It does not by itself show a long-term effect: an immediate post-test and a delayed follow-up are different designs.

## How to use the tables

The tables are a study index and audit trail. They support close reading of individual studies and make the project’s coding visible. They do not support pooling every row into a single effect size: the studies differ too much in outcome, task, population, intervention, and source access.

Rows marked abstract-only or metadata-only should be treated as bibliographic leads and high-level descriptions. They carry less evidentiary weight than records drawn from full papers.

## Project coding

The construct and dissociation tables contain judgments made for this project. The coding rules and limitations are described in the selected analyses. In particular, the distinction between an output measure and a measure of a cognitive process can be arguable. Readers should treat those codes as transparent analytical choices that can be inspected and challenged.
