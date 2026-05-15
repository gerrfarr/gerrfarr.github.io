---
title: CLArXivR
date: 2025-01-01
draft: false
summary: "Filtering arXiv noise with comprehension, not just recommendations — contextual paper summaries that explain how new work relates to a researcher's existing interests."

tags:
  - AI for Science
  - LLM systems
  - evaluation
  - tooling
---

In some fields the arXiv now sees hundreds of new preprints every day. No working researcher can read all of them, and most existing tools stop at recommendation — surfacing a ranked list of papers that look superficially related to what you've read before. That helps with discovery, but it doesn't solve the harder problem: actually reading enough of each paper to know whether and how it matters for *your* work.

**CLArXivR** adds a comprehension layer on top of recommendation. For each new preprint, the system reads the paper in the context of the researcher's own work and produces a contextual summary that answers questions an expert actually cares about — *does this overlap with what I'm doing? does it build on it, contradict it, or extend it in a direction worth following up?* The goal is to skip past generic abstracts and deliver the kind of read you'd want from a thoughtful colleague who knows your work.

Once you commit to summarising at that level of detail, the load-bearing properties shift. **Faithfulness** (the system doesn't say things the paper didn't) and **relevance** (the summary highlights what *this* researcher needs, not generic findings) become the things to design and engineer around — and most of the technical effort goes into the evaluation frameworks needed to measure both, and the iteration loops that let them improve together rather than at each other's expense.

**Coming soon** — currently in private alpha. If you work in a field with a high preprint volume and would like early access, [get in touch](mailto:gfarren@lbl.gov?subject=CLArXivR%20early%20access).
