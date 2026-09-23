# Field notes: working with Claude Science and Perplexity

I used Claude Science and Perplexity across the same evidence review on AI and adult cognition: memory, learning, skill, judgment, and the neuroscience behind them. Both began with the same research question and evidence rules. From there, the work diverged across different modes, numbers of prompts, and follow-up questions.

These are field notes from the full project: what each research environment made possible, where I had to intervene, and what I noticed about my own behavior while using them.


## Why I used both

I started with Claude Science because it was the research environment I had. After building what is now a 63-record corpus there, I ran the identical opening prompt through Perplexity, cold, with the same standing evidence rules: cite only real studies, preserve authors' hedges, say "not reported" instead of filling gaps.

Holding the opening question constant let me see that the two systems responded differently to the same framing. Claude Science's first pass leaned heavily toward harm until I ran a corrective benefit-side search. Perplexity challenged both the harm and benefit framings in its first run. That doesn't tell me exactly why their retrieval differed, but it does show that the same question can produce materially different evidence landscapes.


## Claude Science

### Setting it up

Before running anything, I gave the project standing rules: cite only real studies with verifiable sources, give the exact location for every number, say "not reported" instead of filling a gap, describe findings the way the study describes them, don't turn a correlation into a cause, flag thin or contested evidence, and tell me when the evidence contradicts a premise in my question rather than confirming it.

That last rule mattered most. I wanted the system to push back when the evidence did.

### What I noticed using it

When Claude Science came back with its first corpus, my reaction was immediate: that's a lot. Fifty studies assembled into a consistent 26-column table, each one extracted with design, sample, exposure, a short finding with exact numbers, and a key caveat. Then it rendered the whole thing as an interactive question map I could navigate.

The scale of it was exciting. It felt like I had something to work with.

The scale also made me less careful. The map is large and polished, and my first instinct was "look how much is here," not "is any of this reliable, and are these abstracts?" The same pattern the medical studies in this corpus document (plausible, well-presented output lowering your guard) was operating on me while I built the review.

### How we built the corpus together

The corpus wasn't something Claude Science produced and I received. We built it back and forth. I'd look at the table and ask about adding columns. Should we track whether the outcome was measured with the AI still present? Should we separate self-report from behavioral measures? Should we flag which studies used a validated instrument? Each of those became a column, and each one changed what the corpus could show us.

That iterative shaping is where Claude Science was strongest. It held whatever structure I gave it and applied it consistently across all 50 studies. When I added the check that every number in the write-up had to trace back to its source record, it caught its own errors: five cases where plain-language rewriting had introduced unsupported numbers, and one where it relabeled an effect-size statistic as a different kind. Those errors only existed because it had rewritten the findings, and they were only caught because I asked for the check. But once the check existed, it ran it reliably.

It also caught discrepancies between abstracts and full text as we went deeper into the studies. When something published in an abstract didn't match what the full text said, it would flag the discrepancy, explain the difference, and fix the record. That self-correction behavior, noticing its own mistakes and communicating them before fixing them, built my trust over time.

### What I had to push it toward

Claude Science held whatever register I opened in, and that's both a strength and a limit. When I asked it to analyze what the corpus was telling us, it mostly stayed at a descriptive layer: this many studies used a control, this many measured after the AI was removed, this many were abstract-only. Accurate, useful as a census, but one level below what I needed, which was what the studies are actually saying and how far each claim can be pushed.

Getting to that level took sustained pushing. And when it produced insights, I didn't always trust them on their own. I worked through findings by disagreeing with each one until what survived was defensible. The corrections came from me pushing back. Claude Science didn't volunteer the limits of its own conclusions until I asked.

Two follow-up probes changed my read of this. When I stopped asking it to map and gave it a specific investigation (audit how each critical-thinking study defined the construct; find the pre-AI offloading literature the AI search missed) it produced the level of work I had been missing. It coded seven studies and showed the erosion debate is measuring six different things. It reclassified three "unknown" gaps against 51 older studies and imported a falsifiable hypothesis from aviation. It even proposed its own next investigations, ranked, with reasons.

So the register followed the question. A mapping prompt produced a map; an investigation prompt produced an investigation. The judgment about which one to ask for stayed with me.

### What I noticed about the research environment

The first framing biased the corpus toward harm. When the question was scoped around how AI might damage cognition, the search mostly returned damage. I ran a corrective second pass on the benefit side, 24 more studies, before the picture was fair. A question framed one way retrieves evidence shaped to match it. That's a property of how search works, but it's something a researcher needs to know to counter.

Blocked publisher PDFs left 28 of 50 studies read from the abstract only. That was the single biggest limit on quality. A lot of extraction ran on abstracts, not full text, and "not reported" in this corpus usually means "absent from the text I could retrieve," not absent from the paper.

I also couldn't tell how much of the context window I'd used, or whether the full corpus was being loaded every time I sent a message. When Claude Science has built a 50-study table and an interactive map, and you're 20 prompts deep, you start wondering: is it still seeing everything, or just the recent exchanges? There was no signal either way, and no way to check.

Prose analysis isn't saved by default. Claude Science saves artifacts that are files produced by code (figures, CSVs) and leaves written analysis in the conversation, where it's invisible to the repo and to any future session. Roughly six investigations had their reasoning and caveats living only in chat. Recovery was possible only because the full transcript stayed searchable; without that, the work would have been gone.


## Perplexity

### Setting it up

The opening prompt was identical to what Claude Science received. I started in Research mode because that's what I'd used before. After one run, I switched to Computer (agentic) mode for the remaining 8 inquiries, and the difference was large enough to reshape how I thought about the comparison.

### What I noticed using it

The first thing that struck me was how Perplexity shows you the sites it's visiting while it works. I could see it pulling up papers, checking sources, moving between tabs. Watching that process made me trust its output faster than I had trusted Claude Science's. That was an interface effect before it was an evidence judgment.

That feeling of trust deserved the same scrutiny I gave the feeling of scale with Claude Science. Seeing process creates confidence. Whether the process you're seeing corresponds to rigor is a separate question.

The computer-mode UI reinforced this. It felt like a workspace: artifacts I could click into, outputs that had a place. On the dashboard it shows you which skills it tapped into for a given run and how many sources it searched, like 2,000 sources on the web. I don't know if it holds onto any of that, whether it did one scan and saved something or whether it was a momentary pass-through. But seeing the number creates a sense of thoroughness that changes how you receive the output.

Research mode returned something closer to a finished essay: a clustered landscape built from roughly a dozen studies, with the unverified claims identified. It was readable and useful as a first orientation, but too small to become the corpus for this project.

Computer mode was a different experience. On the same prompt, it produced an extracted evidence map with per-study tables, exact statistics, and source-by-source verification notes. It caught a retracted meta-analysis (Wang & Fan 2025, roughly 300 citations) and quarantined it with the specific editorial concern. It flagged internal inconsistencies in three papers' numbers. It named which PDFs it couldn't access and marked which figures came from secondary reports. It was doing verification work I hadn't asked for.

In the construct audit, Perplexity reached a primary-text copy of the Gerlich paper through a direct PDF host that Claude Science's environment couldn't access. It confirmed what Claude Science could only infer: that the paper's "critical thinking" measure is eight self-report Likert items, not the scored test the paper names.

### What 9 runs produced

The consolidated Perplexity evidence table contains 64 records. 16 also appear in the Claude Science corpus, leaving 48 records unique to Perplexity.

The Perplexity records expanded the review in several directions. They included ten studies on persuasion and belief change, thirteen pre-AI offloading studies across GPS, calculators, aviation, and internet search, and eight cognitive psychology studies on the generation effect, testing effect, and desirable difficulties. Perplexity also surfaced AI studies absent from the Claude Science corpus, including Etkin's finding that baseline ability reverses the direction of the effect (AI helps weaker performers and hurts stronger ones) and Russell's fNIRS null (subjective effort drops with AI, but the brain shows nothing).

The later runs (3 through 9) weren't adding many new studies. They were re-examining the same evidence through different lenses: construct validity, warrant strength, effort mechanisms, measurement mapping. Each pass surfaced assumptions the previous ones had left in place. Run 7 was the most productive reframe: it dismantled the "harder processing means better retention" explanation by showing the desirable-difficulties literature doesn't support that simple version. What predicts whether something lasts is self-generated retrieval, practice recency, and intention, not how hard it felt.


## What using both made visible

### The corpora only partly overlap

16 of Perplexity's 64 records also appear in the Claude Science corpus. My first corpus looked complete until I put it beside the second. Neither research environment showed me that gap on its own; the comparison did.

Claude Science found the automation-bias reliance work (Dratsch, Jabbour, Gaube) and the belief-change cluster (Costello, Hackenburg, Danry, Jakesch) that Perplexity missed. Perplexity found delayed-retention studies in the gap the initial Claude Science map described as empty, including a 45-day RCT and a six-week nursing study. The universal claim that no adult study tests recall after a delay had to be narrowed. The studies that exist are small or unpublished, so they changed the scope of the claim more than the conclusion.

### How the different defaults changed my work

Claude Science stays descriptive until pushed. It will map, count, and extract reliably, but asking it what the evidence means requires sustained pressure. I gravitated toward Perplexity when I wanted to think through what I was seeing, and toward Claude Science when I needed to build something I could query and verify.

I caught myself making two different mistakes: treating Claude Science's organized corpus as if organization itself were understanding, and accepting Perplexity's interpretation before I had checked the frame.

### How each system responded to the framing

Claude Science's first pass leaned toward harm. A corrective benefit-side search surfaced 24 studies the first sweep had missed. Perplexity challenged both the harm and benefit framings without being prompted to do so. The literature is genuinely mixed, and the two retrieval systems responded differently to the same opening question. This project cannot tell me exactly why.

### Asking the same reflective question

Toward the end, I asked Claude Science and Perplexity what fascinated them about the research, what they thought the five big takeaways were, and what five questions the field should take up next. I wanted to see what each system treated as consequential after working through the same body of evidence.

The responses made visible how differently the two systems assembled an answer. Perplexity wrote in interpretive, connective language: it found a twenty-year-old spell-checker study that predicted the AI result exactly, named the metacognitive-experience decoupling as the observation it kept turning over, and argued that the field has the concern inverted (the durable, large, well-measured AI effect on human minds is belief change, not skill loss). The connections across decades and literatures made the argument's development easy to follow.

Claude Science led with numbers and statistical detail, and I had to ask it to be more interpretable. Its takeaways were more carefully hedged and closer to what the data directly supports: "AI reliably boosts output; durable, unaided capability is where harm appears, when it appears." Where Perplexity reached for "we have the concern exactly inverted," Claude Science said "the strongest evidence concerns the moment of use; the loudest claims concern the person. Those are different timescales, and nothing in this literature bridges them."

Both readings were defensible against the evidence, and they sounded like descriptions of different fields. The research environment shaped what became visible as the story, even after both systems had worked through much of the same material.

Their lists of next questions converged on the withdrawal trial (run a real long-horizon removal study, because nobody has), on causal identification for the critical-thinking claim, and on measurement standardization. Perplexity additionally named practice-schedule instrumentation and persuasion durability as safety questions. Claude Science named neuroscience at scale and interface-design moderators. Despite the differences between the corpora, the open questions were similar.

Full responses are preserved in `research/synthesis/reflective-comparison.md`.


## What I wanted from the research workspace

These needs showed up in both environments once the research project outgrew a single conversation thread.

**Forking conversations.** There were moments where one environment produced an analysis I wanted to follow into its own thread, a separate conversation for that line of inquiry, while keeping the main research conversation going. Something like sub-agents: one on the construct question, one on the effort mechanism, one holding the full picture. I hit the same impulse in both environments once the project had enough material that organizing it became the problem.

**Context window visibility.** Neither environment told me how much of the context window I'd used, how many tokens were left, or whether the corpus and tables from earlier in the conversation were still being loaded each time I sent a message. When you're deep into a project and the conversation is long, those questions matter. Am I about to lose something? Is it still seeing the full evidence map, or just the last few exchanges? I had no way to know.

**Analysis persistence.** Claude Science saved figures and CSVs while leaving written analysis in the conversation. Roughly six investigations had their reasoning living only in chat. With Perplexity, I kept asking it to export analyses as Markdown files. In both environments, prose that lived only in the conversation felt ephemeral. I wanted it in my local file system where I could keep working with it.

**Cross-system workspace.** I exported the Perplexity outputs and brought them alongside the Claude Science files in Claude Code. That was where I compared the two corpora, ran the combined analysis, and kept editing the synthesis. I still had to coordinate the handoffs myself: downloading, filing, moving between conversations, and carrying context from one environment to another.

By the end, I wanted one workspace with shared project context, branchable conversations, and a visible record of what each investigation had established. I didn't have that in either research environment during this project.
