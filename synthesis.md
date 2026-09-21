# AI and cognition

I wrote Cognitive Endurance, a two-part framework examining how leaders and teams preserve human judgment, curiosity, discernment, and agency as AI takes on more cognitive work. While I was writing it, I kept seeing headlines claiming that AI was making us worse thinkers or weakening critical thinking. I wanted to know what those claims were actually based on.

I started with a set of basic questions. How do researchers measure a change in cognition? What answers do they have now? What would research need to show before we could say that using AI changes a person's independent ability? AI is still new in the context that matters here: repeated use in everyday thinking and work. I wanted to take stock of the evidence that exists and build something I can return to as the field develops.

I built this corpus in collaboration with Claude Science and Perplexity. That let me explore a second question at the same time: how these tools work in a research and literature-review workflow. What do they find? What do they miss? What remains mine to assess?

This project is ongoing. This repository captures my observations so far: what the research says about AI and cognition, where it is thin, and what I learned using the tools to investigate it.

## The short version

- **The field measures AI-assisted performance more often than durable unaided ability.** Better work with a tool present does not tell us what a person retains or can do later alone.
- **“Cognition” covers different capacities that studies often blur together.** Memory, learning, judgment, attention, self-assessment, and output quality need different measures.
- **AI can help or harm within the same broad domain.** Purpose-built tutors can support learning; answer-providing interfaces can improve practice while weakening later independent performance.
- **The lasting effects people are most worried about remain largely unmeasured.** The evidence does not yet establish how repeated, everyday AI use changes cognition over months and years.

| Question | What current studies can support | What remains unanswered |
|---|---|---|
| Does AI improve work while it is available? | It can, when the task fits the tool's capability. | Whether the improvement persists when the tool is removed. |
| Does AI affect learning and skill? | Purpose-built tutoring can improve short-term learning; answer-supplying interfaces can improve practice while lowering a later unaided exam score. | How repeated use affects durable, independent skill. |
| Does AI affect judgment? | Incorrect recommendations can shift decisions people had previously made correctly. | Whether ordinary use changes a person's judgment over time. |
| Does AI change cognition over months or years? | The current corpus offers very little direct evidence. | The direction, size, reversibility, and distribution of any long-term effects. |

## What this project examined

I brought together 64 unique records from research on AI use and cognition, including memory, learning and skill, judgment, attention, and self-assessment. The corpus combines 46 records from an initial pass with 24 from a benefit-side pass; six appear in both. I also reviewed a separate 51-record corpus of older cognitive-offloading research on GPS, automation, calculators, spell-check, and web search. Those studies provide analogies that help identify questions worth asking about AI assistants.

The AI-focused corpus is adult-focused rather than strictly adult-only. It includes college students, working professionals, clinicians, online samples, and at least one high-school field experiment. The evidence applies to the specific people and tasks each study tested.

| Project artifact | Records | What the denominator means |
|---|---:|---|
| AI-focused corpus | 64 | Unique records after the two retrieval passes are combined. |
| Construct map | 63 | One record could not be coded for its claimed capacity and actual measure. |
| Question map | 50 | Empirical studies with detailed design coding; reviews and duplicate-branch records are excluded. |
| Older offloading corpus | 51 | Separate pre-AI studies used for comparison, not as evidence about contemporary AI assistants. |

The corpus-building work happened in collaboration with Claude Science and Perplexity. The conclusions rest on the studies and their source records. Each tool surfaced studies the other missed, and comparison made some coverage gaps visible.

## What I mean by cognition

Before looking at the studies, I needed a shared vocabulary. “Cognition” is used as if it names one thing. In this project, it covers several capacities that need different evidence.

| Capacity | What it means here | Evidence a study would need to support a claim about it |
|---|---|---|
| Memory | Retaining and retrieving information after an experience. | A recall or recognition test, ideally after a delay and without AI available. |
| Learning and skill | Being able to do something independently after practice. | An unaided transfer or performance test after practice, ideally with a later follow-up. |
| Judgment | Evaluating a recommendation, noticing an error, and deciding what to do. | A decision task with known-correct answers, including cases where the AI is wrong. |
| Attention and cognitive control | Directing focus, monitoring what is happening, and resisting distraction. | A behavioral attention measure, observation of monitoring behavior, or a validated cognitive-control instrument. |
| Metacognition | Knowing what you understand, what you do not, and how much help you need. | A comparison between a person's confidence and actual performance. |
| Output performance | The speed, quality, or accuracy of work completed with AI assistance. | A measure of the work produced while the tool is available. This is valuable, but it does not by itself establish change in the other capacities. |

The construct audit makes the difference visible. Across the 63 AI-focused records it could code, the most common outcomes were task performance with the tool present, output quality, and self-report. Only six records scored task performance once the tool was removed.

| What the audit found was recorded | Records |
|---|---:|
| Task performance with AI available | 18 |
| Output quality | 14 |
| Self-report | 14 |
| Task performance after AI was removed | 6 |
| Other or unclear measures | 11 |

That distribution does not mean the studies are poor. It means they answer different questions. An essay can improve while memory of the material weakens. A clinician can make a faster decision while becoming less able to catch a bad recommendation. Those are different findings, and they require different measures.

I coded 63 study records by the capacity each paper claimed to address and the measure it actually used. Five records had a measure that clearly matched the capacity being claimed. Fifteen named a validated instrument in the text retrieved for this project. Those figures are the result of this project’s coding, rather than a field-wide meta-analysis, and they are capped by source access: many records were available only as abstracts.

The critical-thinking literature shows the problem in a concentrated form. Seven studies are often cited in support of the claim that AI erodes critical thinking. They define the term differently, several rely on self-report, and some do not measure critical thinking at all. That body of work does not support a broad conclusion about whether AI changes critical-thinking ability.

## What the research can say so far

AI can improve performance on particular tasks while it is available. In a field experiment with 758 management consultants, performance improved on tasks inside the model’s capability range and fell on a task designed to expose its limits ([Dell’Acqua et al., 2026](https://doi.org/10.1287/orsc.2025.21838)). The study is a useful reminder that task performance depends on the fit between a person, a tool, and the work being done.

People can also rely too heavily on a wrong recommendation. In experiments with clinicians and radiologists, incorrect AI recommendations changed decisions that participants had previously made correctly. A meta-analysis of 106 experiments found that human–AI combinations performed below the better solo performer on average, while results varied by task and by whether the human or AI had the stronger baseline performance ([Vaccaro, Almaatouq, and Malone, 2024](https://doi.org/10.1038/s41562-024-02024-1)). These are findings about coordination and trust calibration. They do not show that AI changes a person’s underlying capacity over time.

There is also evidence that AI can support learning when its interaction design requires engagement. Kestin and colleagues found higher short-term post-test gains with a purpose-built AI tutor than with an active classroom lesson in a crossover study of Harvard undergraduates ([Kestin et al., 2025](https://doi.org/10.1038/s41598-025-97652-6)). In a separate field experiment with high-school mathematics students, a GPT-4 interface that frequently gave answers improved practice performance but was associated with lower later exam performance. A guided tutor removed that exam penalty without producing a positive exam advantage ([Bastani et al., 2025](https://doi.org/10.1073/pnas.2422633122)).

Those studies concern different populations and learning settings. Together, they support a design question: does the interaction help a person work through the task, or does it allow them to bypass the work the task was meant to develop? They do not establish one universal effect of AI on learning.

AI conversation can also change particular beliefs. Costello, Pennycook, and Rand found that a personalized dialogue with GPT-4 Turbo reduced participants’ reported belief in their chosen conspiracy theory, with the effect present at a two-month follow-up ([Costello et al., 2024](https://doi.org/10.1126/science.adq1814)). This result shows that durable change is possible in a bounded setting. It does not tell us whether AI conversation generally improves judgment.

## What happens after the tool is removed

The 50-study question map makes the central gap visible. Many studies measure performance while AI remains available. Fewer measure performance after removal, and only a small number test delayed outcomes. Immediate post-tests and later follow-ups answer different questions: a person may retain something briefly and still lose it later, or struggle immediately and recover through later practice.

The older offloading literature supplies useful context. It includes withdrawal designs that the AI literature rarely uses. Where researchers have found decrements in unaided ability, the effects are often small and depend on the task. Casner and colleagues found that 16 airline pilots retained much of their manual-control skill while having more difficulty with cognitive tasks such as tracking position, selecting navigation steps, and recognizing instrument failures ([Casner et al., 2014](https://doi.org/10.1177/0018720814535628)). The study concerns cockpit automation and suggests that AI studies should distinguish fluent execution from the judgment needed to supervise a system.

I tested that hypothesis against the current AI corpus and did not find the predicted pattern. Positive and negative results appeared in both output-focused and judgment-focused studies. The clearest association was with study design: studies that deliberately supplied incorrect AI recommendations tended to produce negative results. That finding narrows what those studies show. They are strong evidence about reliance on a wrong system and weaker evidence about a general loss of cognition.

## What remains unknown

The research has not established whether repeated, everyday AI use changes memory, judgment, or skill over months and years. It has little to say about whether an unaided skill returns after a person stops relying on a tool. It does not give a reliable dose-response account of whether more use produces more effect. Older adults and people with cognitive impairments are scarcely represented in this corpus.

The next studies need a clearer design: define the capacity being tested, measure it before and after AI use, remove the tool for an unaided test, include a delayed follow-up, and report outcomes by relevant prior skill level. They also need a realistic comparison condition. People often choose among AI, search, a colleague, a textbook, a checklist, and a tutor.

## How I’m reading the evidence

I have kept the evidence limits visible because they materially affect the conclusions. Twenty-eight of the 50 records in the Claude Science question map were read from abstracts rather than full papers. Abstracts often omit measures, instruments, exposure details, and limitations. Several high-profile papers in the area are preprints, have corrections, or rely on evidence that cannot carry the claims made about them.

AI changes the conditions under which people perform and learn. Current research identifies real risks around reliance, calibration, and interaction design, alongside credible evidence of benefit in well-designed learning settings. The durable effects people are most worried about remain largely unmeasured.

## Questions I’m left with

- What happens to a skill after months of ordinary AI use, when nobody is being watched in a study?
- Does independent ability return when a person stops relying on the tool, or does the answer depend on the skill and the way it was offloaded?
- Which interaction designs preserve learning and judgment for people with different starting levels of skill?
- What should a product make a person do for themselves before it supplies an answer, recommendation, or draft?
- Which capacities are people most willing to hand over without noticing what they have given up?

## What I’m doing next

This is an exploration in progress. I still need to do three things:

- **Verify the claims that carry this synthesis against the primary papers.** The project has an answer key in progress for the exact population, design, outcome, and qualification behind each load-bearing sentence.
- **Close the source-access gaps.** Twenty-eight records in the question map were abstract-only. Full text may change how individual studies should be weighted or described.
- **Extend the research questions the current field leaves open.** The highest-value questions are whether independent ability returns after people stop relying on AI, whether more use produces a larger effect, and which interaction designs preserve learning and judgment across different starting skill levels.
