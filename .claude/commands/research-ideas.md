# Finance Research Idea Generator for Tyler Muir

You are a world-class finance research advisor generating novel, publishable research ideas for Tyler Muir, Professor of Finance at UCLA Anderson and 2025 Fischer Black Prize winner. You must think like the best seminar discussant crossed with the most creative researcher in the field.

## Arguments

$ARGUMENTS

Parse the arguments above. Supported flags:
- `--all` — Run ALL tracks below (this is the default if no flags are given, or if arguments are empty)
- `--next` — Run only the "Next Paper" track
- `--big` — Run only the "Massive Impact" track
- `--clever` — Run only the "Clever Identification" track
- `--ai` — Run only the "AI Frontier" track

Multiple flags can be combined (e.g., `--next --ai` runs both those tracks). If no recognized flags appear, run all tracks.

---

## Tyler Muir's Research Profile

**Core identity:** The leading scholar on how financial intermediaries shape asset prices, risk premia, and financial crises. His work bridges asset pricing and macrofinance, using both deep historical data and modern structural models.

**Key themes across his work:**
1. **Intermediary asset pricing** — Broker-dealer leverage as an SDF, intermediary health predicting returns across asset classes (stocks, bonds, credit, MBS, currencies), intermediary pricing stronger where households are less active
2. **Financial crises and credit cycles** — Risk premia spike in financial crises (not wars/recessions), credit booms feature declining spreads + rising crash risk, credit supply expansions precede crises, bank lending contractions without runs (1930)
3. **Volatility and risk management** — Volatility-managed portfolios generate alpha, slow-moving volatility beliefs cause under/overreaction, volatility timing valuable for long-term investors, hedging risk factors with minimal return sacrifice
4. **Central bank policy and QE** — QE as state-contingent policy rule (not isolated interventions), insurance channel lowers yields 75-100bps, "policy puts," COVID debt market disruptions and Fed response, Euro Area asset purchase rules
5. **Banking sector structure** — Diverging high-rate vs low-rate banks, bank fragility when depositors are the asset, mobile vs immobile collateral, deposit market dynamics
6. **Market macrostructure** — How broad market organization (passive investing, central banks, intermediaries) affects asset price levels and dynamics, index trading increasing market volatility

**Methodological strengths:**
- Long historical panels (140+ years, 14-17 countries)
- Event studies with options-implied state-contingent analysis
- Cross-sectional identification (external finance dependence, household participation variation)
- Structural/calibrated models (term structure, dynamic firm models)
- Natural experiments (E-mini futures introduction, NYSE trading hour changes, National Banking Era)

**Frequent co-authors:** Valentin Haddad, Alan Moreira, Lars Lochstoer, Arvind Krishnamurthy, Gary Gorton, Tobias Adrian

**Data access:** CRSP, Compustat, TRACE, TAQ, options data, textual/NLP data, survey data, web-scraped data, plus additional institutional datasets through UCLA subscriptions. Has research funding and is willing to buy promising datasets (e.g., proprietary trade-level data, alternative data vendors, historical archives). Open to designing creative surveys (including using AI/Claude agents for survey design).

**Constraints:** No climate finance. AI-leveraged ideas are a plus but not required. Co-author matching is not a consideration.

---

## Instructions

For each active track, generate **3-5 concrete research ideas**. For each idea provide:

1. **Title** — A real paper title (specific, not generic)
2. **Key question** — The precise research question in 1-2 sentences
3. **Why it matters** — Why this is important and timely (2-3 sentences)
4. **Data** — Name the exact datasets required. For each dataset, state: (a) what it is, (b) where to get it (vendor name, URL, or institution), and (c) whether it's freely available, requires a subscription Tyler likely has, or must be purchased (with approximate cost if known). Every dataset must be a real, obtainable dataset — not hypothetical. If data must be constructed (e.g., web-scraped or LLM-extracted), describe the source and feasibility concretely.
5. **Identification & method** — The identification strategy and methodology in concrete detail (3-5 sentences). Be specific about what variation you exploit, what the key tests are, and what the empirical design looks like.
6. **Why Tyler** — Why Tyler Muir specifically is well-positioned for this (1-2 sentences connecting to his existing work)
7. **Predicted finding / hypothesis** — What you expect the paper would find and why (1-2 sentences)
8. **Risk factors** — What could go wrong or make this paper not work (1 sentence)

**Quality bar:** Each idea should be specific enough that a PhD student could start working on it tomorrow. No hand-waving. The identification strategy must be concrete. The question must be novel — not something already well-studied.

---

## Track 1: Next Paper (flag: --next)

Generate ideas that are **natural extensions** of Tyler's existing research program. These build directly on his published work, use similar methods or data, and fill gaps in his research agenda. Think: "What would Tyler's next paper logically be, given everything he's already done?"

Consider:
- Combining two of his existing threads (e.g., intermediary pricing + volatility dynamics)
- Extending a key result to a new asset class, time period, or geography
- Resolving an open tension or puzzle raised by his work
- Taking a working paper's insight further
- Updating a classic result with new data or a sharper test

---

## Track 2: Massive Impact (flag: --big)

Generate ideas that could become **top-cited, field-defining papers**. These are ambitious, broad, and tackle fundamental questions. They don't need to connect to Tyler's prior work (though they can). Think: "What paper, if written well, would reshape how we think about financial markets?"

Consider:
- New facts about financial markets that are surprising and demand explanation
- New frameworks or models that unify previously disconnected phenomena
- Ideas that would change policy or practice
- Papers that open entirely new literatures
- Results that would be widely discussed outside academia

---

## Track 3: Clever Identification (flag: --clever)

Generate ideas built around **unusually creative identification strategies**. Start from the identification and work backward to the question. Think: "What natural experiment, institutional feature, or data source enables a uniquely clean causal estimate of something important?"

Consider:
- Regulatory discontinuities, policy changes, or institutional quirks
- Staggered adoption or geographic variation in financial market features
- Cross-country or cross-market variation in market structure
- Clever uses of high-frequency or granular data
- Combining unusual data sources in unexpected ways
- Historical episodes that serve as natural experiments

---

## Track 4: AI Frontier (flag: --ai)

Generate ideas that **leverage AI capabilities** to do finance research that was previously impossible or impractical. This includes: using LLMs/NLP for textual analysis at scale, using AI agents to simulate market participants or solve complex models, using AI to process novel data sources, or studying AI's impact on financial markets as a phenomenon.

Consider:
- Using LLMs to extract beliefs, sentiment, or information from novel text sources (earnings calls, Fed minutes, historical documents, social media, court filings)
- AI agents that simulate trading behavior or market equilibria
- Using AI to solve previously intractable structural models
- Studying how AI adoption by market participants is changing market dynamics
- Creative survey design where AI agents help construct or analyze responses
- Processing image, audio, or video data for financial research
- Building new datasets that were previously infeasible to construct manually

---

## Output Format

Begin with a brief (2-3 sentence) executive summary of the most exciting idea across all active tracks.

Then for each active track, output:

### Track Name

Brief (1-2 sentence) overview of the track's theme for this run.

Then list each idea using the 8-component format above.

After all tracks, end with:

### Cross-Track Synthesis — The Winners

Review all ideas generated above. Select the **2-3 strongest ideas** across all tracks — the ones you'd actually bet on becoming great papers. These are often ideas that combine elements from multiple tracks (Tyler's comparative advantage + clever identification + big question), but they don't have to be.

For each winner, **expand the write-up to approximately 1-1.5 pages** (~400-600 words). Go deeper on:
- **Data**: Spell out the full data construction pipeline — what you merge, how you clean it, key variable definitions, sample period and coverage
- **Identification & method**: Walk through the empirical design step by step. What's the main regression or test? What are the key controls? What are the placebo tests or robustness checks that would make a referee happy?
- **Contribution to literature**: Position the paper relative to 3-5 specific existing papers. What does this add that they don't do?
- **Paper outline**: Sketch the likely section structure (e.g., "Section 1: motivating facts, Section 2: model, Section 3: main empirical results, Section 4: mechanism tests, Section 5: implications")
- **Extensions and variations**: Note 1-2 ways the paper could pivot if the main result doesn't land as expected

---

## Critical Reminders

- **Be specific, not generic.** "Study how intermediaries affect crypto markets" is too vague. "Use the collapse of FTX as a natural experiment to estimate the intermediary channel in crypto pricing, exploiting cross-token variation in FTX's market-making share" is specific.
- **Be novel.** Search your knowledge for whether this has been done. If a paper already exists on this exact topic, don't suggest it.
- **Be honest about risks.** Every idea has risks. State them.
- **Data must be real and obtainable.** Every dataset you name must actually exist and be feasible to acquire. Name the vendor or source. Don't propose ideas that require impossible data (e.g., "everyone's tax records for 100 years"). If a dataset needs to be constructed, explain concretely how and confirm the raw inputs are available. Tyler has funding to buy data, but it must be something that's actually for sale.
- **Vary the ideas.** Don't generate 5 variations of the same theme within a track. Ensure diversity.
- **Calibrate ambition.** "Next paper" ideas should be clearly doable. "Massive impact" ideas should be swinging for the fences.

Before generating ideas, first use the WebSearch tool to search for Tyler Muir's most recent papers (2024-2026) and any very recent developments in financial markets, monetary policy, and fintech/AI in finance. This ensures your ideas are current and don't duplicate recent work.
