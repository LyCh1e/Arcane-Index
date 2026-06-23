---
type: source
source_type: paper
title: "ACON: Optimising Context Compression for Long-Horizon LLM Agents"
created: 2026-06-21
updated: 2026-06-21
url: https://arxiv.org/abs/2510.00615
authors:
  - Minki Kang
  - et al.
date_published: 2025-10
venue: "arXiv / OpenReview"
confidence: high
tags:
  - llm
  - context-compression
  - agentic-ai
  - research-paper
related:
  - "[[concepts/context-compression-llm]]"
  - "[[questions/research-context-compression-llm]]"
---

# ACON: Optimising Context Compression for Long-Horizon LLM Agents

## Summary

ACON introduces a unified framework for compressing both *environment observations* and *interaction histories* in long-horizon LLM agents, where context "explodes" as tasks accumulate tool outputs and multi-step history.

The paper's key insight is that **generic compression instructions fail on complex, heterogeneous agent contexts**; compression guidelines must be optimised specifically for the task.

---

## Key Claims

- Task-specific compression guidelines significantly outperform generic prompting baselines. (Confidence: high — verified on three benchmarks)
- Optimised compressors distil effectively into smaller LMs whilst preserving 95%+ of performance. (Confidence: medium — single paper)
- Compressed contexts can *improve* smaller LM agent performance by 20–46% on benchmarks where larger contexts exceed the smaller model's effective window. (Confidence: medium — specific to benchmarks tested)

---

## Compression Mechanisms

**History compression**: when accumulated interaction history exceeds a token threshold, an LLM-based compressor summarises it using task-specific guidelines. The compressor is optimised via *contrastive feedback* — comparing successful uncompressed trajectories against failed compressed ones — rather than gradient-based training.

**Observation compression**: environment observations (e.g., web pages, file listings, tool outputs) are condensed using historical context to determine what is task-relevant.

---

## Taxonomy Used

The paper situates ACON within a three-way taxonomy of LLM compression:

1. **Document/retrieval-based** methods
2. **Dialogue memory summarisation** approaches
3. **Low-level KV cache** techniques

ACON occupies category 2, extended to the agentic setting.

---

## Benchmark Results

| Benchmark | Accuracy | Peak Tokens (Baseline) | Peak Tokens (ACON) | Reduction |
|-----------|----------|------------------------|---------------------|-----------|
| AppWorld | 56.5% | 9,930 | 7,330 | 26% |
| OfficeBench | 72.63% | 7,270 | 4,540 | 38% |
| 8-objective QA | 0.366 EM | — | 0.336 EM | 55% dependency reduction |

---

## Key Contributions

1. Unified framework handling both heterogeneous observation compression and history compression
2. Compression guideline optimisation via failure analysis (contrastive, not gradient-based)
3. Smaller LM distillation of optimised compression behaviour

---

## Relevance to Wiki

Primary empirical grounding for the agentic context compression section of [[concepts/context-compression-llm]].
