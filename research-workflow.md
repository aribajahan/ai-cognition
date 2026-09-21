# Using AI research tools in this project

## The question I gave the tools

I gave Claude Science and Perplexity the same opening question: map the empirical research on how AI affects adult cognition, including memory, learning and skill, judgment, and related measures. I asked for verifiable citations, sample sizes, explicit limits, and a distinction between correlation and causation.

I then used the tools differently. Claude Science became the main research workbench: it assembled the initial corpus, extracted study-level fields, and produced the question map. I used Perplexity in agentic computer mode as an independent route through the same question, then for targeted checks where the first corpus was thin or uncertain.

This was not a controlled head-to-head. Claude Science received more follow-up work over a longer period, and the tools had different source access and output surfaces. The comparison records how they behaved in this project.

## What each tool made possible

| Work in this project | Claude Science | Perplexity in computer mode | What still required my judgment |
|---|---|---|---|
| Build a corpus | Produced a structured 64-record corpus across two retrieval passes. | Produced an independent map with partial overlap and additional leads. | Decide which sources belonged in scope and run a benefit-side retrieval when the first pass tilted toward harm. |
| Inspect individual studies | Extracted design, sample, measures, findings, access status, and limitations into tables. | Retrieved some sources the first environment could not access. | Read the source basis, distinguish an abstract from full text, and decide how much weight a record could carry. |
| Find gaps | Made the absence of unaided and delayed outcomes visible across the map. | Found a delayed-retention preprint that meant the first map's universal absence claim had to be narrowed. | Change the conclusion without treating one unpublished, weakly documented study as a settled answer. |
| Check integrity | A requested number-drift audit caught unsupported numbers and mislabeled statistics in the map. | Flagged a retracted education meta-analysis and named source-access limits in its output. | Verify corrections and retractions, decide which claims to remove, and preserve the audit trail. |

## Four moments that changed the work

### 1. The original question shaped the corpus

My first Claude Science prompt was framed around how AI might damage cognition. The first retrieval pass mostly returned harm-oriented studies. I ran a second, benefit-side pass before drawing conclusions. The correction was simple but important: a search question can bias the evidence it retrieves.

### 2. A second tool found a study the first one had declared absent

The original question map stated that no adult study tested recall after a delay. Perplexity surfaced a 45-day delayed-retention randomized trial. Its own source notes also raised reasons for caution: the paper was an unpublished preprint, authorship was not clear on the abstract page, and the reported sample and test statistic suggested unexplained attrition.

That changed the claim. The evidence gap is still very large, but a universal absence claim was too strong. The right response was to narrow the conclusion and retain the source-status caveat.

### 3. Source access changed what I could say about a headline study

Claude Science could not retrieve the primary PDF for Gerlich's widely cited 2025 paper on AI use and critical thinking. Perplexity reached an alternate publisher-hosted PDF. It confirmed that the paper used eight self-report Likert items rather than a scored critical-thinking assessment. That matters because the study is often invoked as direct evidence that AI lowers critical-thinking ability.

The tools did not settle the interpretation. They made a source-access difference visible, and the primary text gave me grounds to describe the paper more precisely.

### 4. Polished artifacts can hide unresolved errors

Claude Science produced an impressive-looking interactive map. Review found five instances where plain-language rewriting had introduced unsupported numbers or relabeled an effect-size statistic, and a later audit found branch headers whose counts described a different grouping from the displayed studies. Perplexity also surfaced a retracted meta-analysis that had accumulated substantial citations.

The lesson was practical: a polished research artifact raises the risk that a reader, including me, will mistake legibility for verification. The checks that caught the errors were explicit audits, not defaults.

## What I learned about the workflow

The two tools were complementary. Claude Science was better suited to building a deep, inspectable corpus once I had a structured question and data fields. Perplexity was useful as an independent retrieval and verification route; it surfaced different studies, reached some different sources, and volunteered more uncertainty in its agentic output.

Neither tool gave me the literature. Both produced coherent answers with coverage gaps that were hard to see from the answer alone. Running the same question through a second system made some of those gaps visible. It did not prove that the combined result was complete.

The work that remained mine was deciding what a study had actually measured, how far a source could support a claim, when a missing source should limit the conclusion, and when the evidence contradicted the starting premise. Those decisions are reflected in the synthesis, evidence tables, and source-verification pass.

## Product questions this raised

- How might a research tool show the records it screened out, the sources it could not reach, and the gaps in the corpus it built?
- How might it preserve prose analysis as reliably as it preserves generated tables and figures?
- Which checks should run automatically before a user receives a polished artifact: source access, retraction status, count reconciliation, and numeric traceability?
- How can the interface distinguish a map of what was found from an argument about what the evidence establishes?
