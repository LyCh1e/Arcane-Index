---
type: source
source_type: article
title: "Evaluating Context Compression for AI Agents"
created: 2026-06-21
updated: 2026-06-21
url: https://factory.ai/news/evaluating-compression
authors:
  - Factory.ai
date_published: 2025
confidence: medium
tags:
  - llm
  - context-compression
  - evaluation
  - agentic-ai
related:
  - "[[concepts/context-compression-llm]]"
  - "[[questions/research-context-compression-llm]]"
---

# Evaluating Context Compression for AI Agents (Factory.ai, 2025)

## Summary

Factory.ai's empirical evaluation comparing three production context compression approaches (Factory, OpenAI, Anthropic) on real software engineering sessions, using a probe-based evaluation framework.

> [!gap] This is a first-party evaluation published by Factory.ai, a company with a commercial interest in its own method performing well. Results should be treated as medium confidence pending independent replication.

---

## Dataset

- Hundreds of compression points
- 36,611 messages
- Real-world production software engineering sessions from consenting users

---

## Evaluation Framework

**Probe-based**: rather than measuring ROUGE or BLEU scores, the evaluator asks the compressed summary direct functional questions and grades the answer.

Four probe types:
1. **Recall** — factual retention ("What was the original error message?")
2. **Artifact** — file tracking ("Which files have we modified?")
3. **Continuation** — task planning ("What should be done next?")
4. **Decision** — reasoning preservation ("Why did we choose approach X?")

Graded across six dimensions (0–5 scale) using GPT-5.2 as an LLM judge:
- Accuracy
- Context Awareness
- Artifact Trail
- Completeness
- Continuity
- Instruction Following

---

## Methods Compared

| Method | Approach | Compression Ratio |
|--------|----------|-------------------|
| **Factory** | Anchored iterative summarisation with structured sections (session intent, file modifications, decisions, next steps). New compressions merge into persistent summaries rather than regenerating fully. | 98.6% |
| **OpenAI** | `/responses/compact` endpoint producing opaque, highly compressed representations optimised for reconstruction fidelity | 99.3% |
| **Anthropic** | Structured summaries (7–12k characters) covering analysis, files, pending tasks, and current state; fully regenerated on each compression | ~98% |

---

## Key Results

| Dimension | Factory | OpenAI | Anthropic |
|-----------|---------|--------|-----------|
| Accuracy | **4.04** | 3.43 | ~3.78 |
| Overall | **+0.35 vs OpenAI, +0.26 vs Anthropic** | — | — |
| Artifact Trail | 2.45 | 2.19 | ~2.3 |

**Key finding**: compression ratio does not predict quality. OpenAI compressed 99.3% of tokens yet scored *lower* than Factory at 98.6%. The additional retained tokens in Factory's approach enabled superior task continuation without costly re-fetching.

**Persistent weakness**: artifact tracking (knowledge of which files were modified) is the weakest dimension across *all* three methods (2.19–2.45 / 5). This is an open problem.

---

## Implications for Design

1. **Structure matters more than ratio**: preserving explicit sections (intent, files, decisions) outperforms aggressive opacity
2. **Incremental merging outperforms full regeneration**: anchored iterative summaries accumulate structured knowledge; full regeneration discards earlier structure
3. **Artifact tracking needs dedicated treatment**: summaries alone cannot reliably preserve file modification history; structured external logging (e.g., a changelog file) is needed

---

## Relevance to Wiki

Empirical grounding for the "Production Strategy Comparison" table in [[concepts/context-compression-llm]] and the open questions on artifact tracking in [[questions/research-context-compression-llm]].
