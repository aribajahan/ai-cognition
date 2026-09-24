# AI and cognition

While writing [Cognitive Endurance](https://www.unmissables.xyz/p/cognitive-endurance-2), I kept seeing claims that AI was weakening memory, learning, and critical thinking. I wanted to know what those claims were based on. So I built an evidence review around a narrower question: what has research actually measured about AI's effect on cognition, and how far can the findings go?

I found that studies grouped under “AI and cognition” were answering different questions. Some measure the work people produce while AI is available. Others test what a person can do after it is removed. Some measure confidence or perceived effort and call that critical thinking. Others measure recall, the ability to apply something later, decision accuracy, or belief change. The findings appear to contradict one another partly because the studies are measuring different things.

I built the review with Claude Science and Perplexity, then checked what each study had measured and narrowed claims that went beyond those measures. This synthesis separates the findings supported by multiple studies from early results that still need to be tested. It also records what researchers have not studied yet. I wanted a baseline I could return to as the field changed: a dated snapshot that shows which conclusions strengthen, weaken, or change as new studies arrive. The project is a structured evidence review and research record, not a systematic review or meta-analysis.

## The short version

- **Current studies tell us much more about performance during AI use than about durable, unaided ability.** Immediate practice gains and later independent skill require different tests.
- **The way a person uses AI can change the result.** Guided tutoring and self-generation-first workflows have produced different outcomes from interfaces that supply answers for direct adoption.
- **Reliance becomes dangerous when the AI is wrong.** Clinicians, radiologists, and participants in misinformation studies have followed or been influenced by incorrect recommendations and explanations.
- **Starting skill may change who benefits.** Several studies find larger gains among less experienced or lower-performing people, while one randomized crossover study found that the same AI reading aids helped lower performers and hurt higher performers.
- **Some belief changes remain measurable after the interaction ends.** AI conversations and writing assistance can move what people report believing. The direction depends on what the system argues. The longest result in this corpus has a corrected analysis under review after reproducibility problems in the public dataset.

The long-term question remains open. A few studies now measure outcomes weeks later, so the answer is no longer “nobody has tested this.” The available studies use short, narrow interventions and do not establish what months and years of ordinary AI use do to memory, judgment, or skill.

## What this review includes

This review draws on three evidence tables. Claude Science produced a 45-record first pass and a 24-record benefit-side pass; seven sources appear in both, leaving 62 unique records in that set. Perplexity produced a separate 64-record table that includes AI-era studies, older research on cognitive offloading, meta-analyses, and reviews. 16 Perplexity records also appear in the Claude Science corpus, leaving 48 Perplexity-only records.

I have kept the Claude and Perplexity tables separate because they were built from different searches and do not contain the same kinds of sources. Adding their row counts together would double-count some studies and treat reviews as if they were additional experiments. Keeping them separate also preserves provenance: readers can see which research environment surfaced each source and how it entered the review.

I also examined 51 older studies on GPS, cockpit automation, calculators, spell-check, and web search. They show what earlier researchers measured when people handed part of a cognitive task to technology: what stopped being practiced, what people could still do without the system, and whether a skill returned. They do not establish the effects of current AI systems.

Most of the AI studies involve adults. I also included a small number of studies with younger participants when they directly addressed the question, including the high-school mathematics experiment discussed later. A result from one high school, one profession, or one laboratory task should not be assumed to apply to everyone.

Full text is available for 21 of the 24 benefit-side records and 37 of the 45 first-pass records. Three benefit-side records and eight first-pass records remain abstract-only. The [methods](methods.md) and [public data tables](data/) preserve the access basis where it was recorded and identify the gap for Perplexity-only records.

## What counts as evidence of cognition

“Cognition” covers capacities that need different measures. A faster answer, a better essay, confidence in one’s performance, and the ability to solve a similar problem later are four different outcomes.

| Capacity | What it means here | Evidence needed |
|---|---|---|
| Memory | Retaining and retrieving information after an experience. | Recall or recognition without AI, ideally after a delay. |
| Learning and skill | Being able to perform independently after practice. | An unaided transfer or performance test, followed by a later test when possible. |
| Judgment | Evaluating a recommendation, detecting an error, and deciding what to do. | Decisions with known-correct answers, including cases where the AI is wrong. |
| Attention and cognitive control | Directing focus, monitoring progress, and resisting distraction. | Behavioral attention measures, observed monitoring behavior, or validated instruments. |
| Metacognition | Knowing what you understand and how much help you need. | Confidence compared with actual performance. |
| Output performance | The speed, quality, or accuracy of work produced with AI. | The work completed while AI is available. |

The current construct table compares the capacity each paper claimed to study with what it actually measured. It contains 62 records; five clearly measured the capacity named in the paper, and 14 named a validated instrument in the text available at the time. I reviewed the model-assisted coding myself; it was not independently coded by multiple researchers. The table predates some later full-text retrieval, so its coding remains a dated project assessment rather than an independent rating exercise.

The seven-study critical-thinking audit found studies using the same term for self-reported work behaviors, confidence ratings, essay recall, and coded argument quality. Several only show that two things occurred together; they cannot tell us whether AI caused the difference. Some do not test a person’s critical-thinking ability at all. The scope is narrower than the headline claim: a survey of how people feel about their thinking can describe their perception, but it cannot show whether their reasoning ability changed.

## Assisted performance and independent ability are separate outcomes

AI often improves the work produced while it is available. Noy and Zhang found that professionals completed writing tasks 40% faster and produced work rated 18% higher in quality with ChatGPT. Brynjolfsson, Li, and Raymond studied a staggered workplace rollout across 5,172 customer-support agents and found a 15% average productivity increase, with larger gains among novice and lower-skilled workers. In both studies, people completed more or better work while they had AI assistance.

Noy and Zhang did not test later unaided performance. Brynjolfsson, Li, and Raymond examined rare software outages and found that some exposed workers remained faster without live recommendations, especially after longer exposure and among workers who had followed the suggestions more closely. The outage result suggests learning, but it comes from a noisy observational comparison that may include differences in the chats workers handled.

The studies that separate practice from later performance show why the distinction matters. In the high-school mathematics field experiment, the unguarded GPT interface improved practice and lowered later exam performance; the guided tutor improved practice and removed the penalty. In a preregistered experiment with 900 randomized participants, people who directly adopted AI answers scored lower than the no-AI group on an unaided reasoning task 15 to 20 minutes later, an adjusted difference of −0.38 and an effect size of *d* = −0.28. The self-generation-first group appeared to score slightly above the no-AI group, but the difference was no longer statistically reliable after the researchers corrected for making multiple comparisons.

The strongest positive learning result also came from a designed tutor. In a crossover study of 194 eligible Harvard undergraduates, students using an AI tutor had a median post-test score of 4.5 compared with 3.5 after an active classroom lesson. The adjusted effect size was 0.63. The study measured short-term course learning in a setting supported by expert-built prompts, instructional videos, and prewritten solutions. It does not show that any chatbot will outperform teaching.

For product teams, this leads to a practical question: what does the interface require the person to generate, retrieve, check, and revise before it supplies an answer?

*Sources: [Bastani et al. 2025](https://doi.org/10.1073/pnas.2422633122); [Liu et al. 2026](https://doi.org/10.3389/fpsyg.2026.1910545); [Kestin et al. 2025](https://doi.org/10.1038/s41598-025-97652-6); [Noy and Zhang 2023](https://doi.org/10.1126/science.adh2586); [Brynjolfsson, Li, and Raymond 2025](https://doi.org/10.1093/qje/qjae044).*

## Results depend on whether AI is right and whether people catch its mistakes

When AI is correct, its assistance can improve a decision. When it is wrong, people often follow it.

Across 106 experiments and 370 effects published through June 2023, human–AI combinations performed below the better solo performer on average, with Hedges’ *g* = −0.23. The average hid substantial variation. Creative tasks were more likely to show gains; decision tasks were more likely to show losses. Combinations tended to improve when the human outperformed the AI alone and decline when the AI was stronger.

Clinical studies show what that looks like. In one randomized experiment with 457 clinicians, standard AI recommendations raised diagnostic accuracy by 2.9 percentage points while systematically biased recommendations lowered it by 11.3 points. Explanations did not remove the harm. Radiologists in a separate study were correct about 80% of the time when the purported AI was correct and between 19.8% and 45.5% when it was wrong, depending on experience.

The same problem appears outside expert work. A preregistered false-memory experiment found that a generative chatbot produced an average of 1.82 immediate false memories per participant, compared with 0.54 in the control condition. The difference remained visible one week later. In misinformation studies, deceptive AI explanations moved belief in false and true headlines beyond the effect of an incorrect label alone.

These studies tell us what happens when people receive a wrong recommendation during a task. They do not show that ordinary AI use permanently weakens judgment. They do show that a fluent explanation or professional expertise does not guarantee that someone will catch the mistake.

This is a calibration problem. Trust is well calibrated when confidence in the AI rises and falls with the quality of its recommendation. In these studies, it often did not.

*Sources: [Vaccaro, Almaatouq, and Malone 2024](https://doi.org/10.1038/s41562-024-02024-1); [Jabbour et al. 2023](https://doi.org/10.1001/jama.2023.22295); [Dratsch et al. 2023](https://doi.org/10.1148/radiol.222176); [Chan et al. 2024](https://doi.org/10.48550/arxiv.2408.04681); [Danry et al. 2025](https://doi.org/10.1145/3706598.3713408).*

## Self-report cannot substitute for behavioral outcomes

Self-report remains useful for experience: whether a system felt easy, demanding, trustworthy, or satisfying. It cannot stand in for a behavioral measure of memory, reasoning, or skill.

In two experiments using LSAT reasoning questions, AI improved performance and participants still overestimated how well they had done. The overestimation effect was large in both experiments (*d* = 0.93 and *d* = 1.17). In a separate study of 20 adults, participants said their workload fell when they used AI. Measures of brain activity, heart rate, heart-rate variability, and electrodermal activity did not show a corresponding change.

Feeling more effort is not proof that more learning happened either. A 2018 meta-analysis of 25 articles and 3,135 participants reported that making material harder to read increased learning time (*d* = 0.52) and made people think they had learned less (*d* = −0.43), while recall (*d* = −0.01) and transfer (*d* = 0.03) remained near zero. A later reproducibility critique found that the near-zero transfer result survived plausible reanalysis but identified coding and effect-size problems that make the recall estimate less secure. A task can feel easier without producing better learning, and it can feel harder without producing better learning.

How hard a task feels tells us too little about what a person will remember. Effort remains an unproven mechanism, not an explanation for the mixed AI results. Future studies need to record what the person generated, what they retrieved from memory, what they practiced, and what they knew they would need to do later.

*Sources: [Fernandes et al. 2024](https://doi.org/10.48550/arxiv.2409.16708); [Russell et al. 2025](https://arxiv.org/abs/2506.04167); [Xie et al. 2018](https://doi.org/10.1007/s10648-018-9442-x); [Grinschgl et al. 2021](https://doi.org/10.1177/17470218211008060).*

## Starting skill changes who benefits in some studies

Aggregate averages can conceal people moving in opposite directions.

In a randomized crossover study of 195 college-aged adults, four GPT-based reading aids improved comprehension among people who scored lower before the study, with effects ranging from *d* = 0.45 to 0.86. The same aids worsened comprehension among people who started with higher scores, with effects from *d* = 0.33 to 0.83. The relationship between starting score and AI benefit was *r* = −0.785. The study used the same test to sort people into groups and calculate who benefited, which makes the size of the difference harder to interpret.

The customer-support rollout found a related workplace pattern: productivity rose 30% among less-skilled and less-experienced agents, while experienced and higher-skilled agents saw smaller gains. The study was observational. Its outage analysis found suggestive evidence of retained speed gains without live recommendations, but it cannot establish how each group’s underlying skill changed.

Baseline ability may be a moderator, meaning it changes who benefits from the same form of assistance. Studies should report results separately for people with different starting levels of skill. The current evidence does not establish a universal rule that AI helps novices and harms experts.

*Sources: [Etkin et al. 2025](https://doi.org/10.3389/feduc.2025.1506752); [Brynjolfsson, Li, and Raymond 2025](https://doi.org/10.1093/qje/qjae044).*

## AI can shift reported beliefs beyond the interaction

The clearest delayed effects in this review concern what people believe.

In a study of 2,190 participants, a personalized evidence-based dialogue with GPT-4 Turbo reduced belief in a chosen conspiracy theory by about 20%, and the reduction remained at the two-month follow-up. *Science* published an [expression of concern](https://doi.org/10.1126/science.aej2383) after extra spliced rows were found in the public dataset and screening criteria were applied inconsistently between the manuscript and published analysis pipeline. The authors submitted a corrected analysis and report that the results remain similar in direction, statistical significance, and substantive size; *Science* is evaluating it. A later preregistered experiment with 955 participants found that short conversations reduced confidence in conspiracy theories and other unsupported beliefs whether the speaker was presented as an AI or a human expert.

Other studies found that AI could also move beliefs toward slanted or false claims. An opinionated writing assistant shifted the views participants expressed in their writing and in a later attitude survey, with a treatment effect of *d* = 0.34. In three large experiments covering 19 language models and 707 political issues, prompting and post-training methods increased persuasion while systematically lowering factual accuracy. An information-dense prompt raised the average persuasive effect from 8.34 to 10.60 percentage points.

These studies do not show that AI generally improves or degrades judgment. They show that AI can change what people report believing, that some changes remain after the conversation ends, and that making a system more persuasive can make it less accurate.

*Sources: [Costello, Pennycook, and Rand 2024](https://doi.org/10.1126/science.adq1814); [Boissin et al. 2025](https://doi.org/10.1093/pnasnexus/pgaf325); [Jakesch et al. 2023](https://doi.org/10.1145/3544548.3581196); [Hackenburg et al. 2025](https://doi.org/10.1126/science.aea3884).*

## What happens after AI is removed

My first search suggested that almost no studies tested people after AI was removed, especially after a delay. A later search found three studies that changed that claim.

In André Barcaui's published trial, 120 undergraduate business students were randomized to prepare a presentation with unrestricted ChatGPT or with traditional resources. Of the 85 students who completed a surprise test 45 days later, the ChatGPT group scored 57.5% and the traditional group scored 68.5% (*d* = 0.68). Attrition was substantial but balanced between groups, and the traditional group spent more time studying.

A working paper by Zara Contractor and Germán Reyes found a result in the other direction. College students had 35 minutes to learn an unfamiliar topic and write an essay, with AI allowed or forbidden. Of the 211 students who attended the first session, 204 returned about one week later. The AI-allowed group scored 5.1 percentage points higher on the unaided delayed test, an effect of 0.27 standard deviations. Only 68% of the students assigned to the AI group used it.

The six-week nursing study tested a different kind of intervention. It combined ChatGPT with standardized prompts, peer discussion, comparison against clinical guidelines, instructor monitoring, and correction. The study randomized 34 students and analyzed 32. The intervention group had a median score of 65 on the six-week knowledge test, compared with 55 in the control group (*p* = .044). The pilot was small, the follow-up was remote and unsupervised, and the intervention cannot isolate the effect of ChatGPT from the surrounding teaching design.

Delayed evidence now exists, and its direction varies with the task and the way AI is used. These studies cover one week, 45 days, and six weeks after brief interventions. They do not tell us what happens after months or years of ordinary AI use.

Older research on cockpit automation measured different parts of a skill separately instead of treating pilot performance as one outcome. In a simulator study of 16 airline pilots, manual flying remained largely intact while participants had more difficulty tracking position, choosing navigation steps, and recognizing instrument failures. I tested whether the AI studies showed the same pattern, with execution holding up while supervision weakened. They did not. Positive and negative results appeared across both types of outcome, and there were too few studies to treat the lack of a pattern as decisive.

The aviation research still points to a useful question: what stops being practiced once AI becomes available? Current AI studies rarely track that change over time.

*Sources: [Barcaui 2025](https://doi.org/10.1016/j.ssaho.2025.102287); [Contractor and Reyes 2026](https://arxiv.org/abs/2607.08849); [Sezgunsay, Polat, and Kılıcer 2026](https://doi.org/10.1186/s12909-026-09483-2); [Casner et al. 2014](https://doi.org/10.1177/0018720814535628); [project dissociation coding](data/dissociation_coding.csv).*

## What remains unanswered

The research has not established how repeated, everyday AI use changes memory, judgment, or skill over months and years. It does not show whether a person’s unaided ability returns after they stop relying on AI. Few studies test whether using AI more often produces a larger effect. Older adults and people with cognitive impairments are also rarely included.

The next studies should:

- define the capacity before choosing the task;
- measure baseline ability and report results by starting skill;
- distinguish output quality, self-report, behavior, and independent performance;
- sustain AI exposure long enough for a practice pattern to change;
- remove AI and test immediately and again after a meaningful delay;
- record what participants generated, retrieved, checked, and stopped practicing;
- compare AI with the alternatives people would actually use, including search, a colleague, a textbook, a checklist, or a tutor.

Product teams can act on the evidence that already exists. They can decide what a system supplies, what it asks the person to work through, when it exposes uncertainty, and how it helps someone detect a wrong answer. Those choices change what people practice while the system is present.
