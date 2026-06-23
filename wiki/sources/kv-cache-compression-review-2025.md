---
type: source
source_type: paper
title: "KV Cache Compression for Inference Efficiency in LLMs: A Review"
created: 2026-06-21
updated: 2026-06-21
url: https://arxiv.org/abs/2508.06297
authors:
  - (Multiple — review paper, authors not extracted)
date_published: 2025-08
venue: "arXiv / ACM AIIP 2025"
confidence: high
tags:
  - llm
  - kv-cache
  - inference-efficiency
  - survey
related:
  - "[[concepts/kv-cache-compression]]"
  - "[[concepts/context-compression-llm]]"
  - "[[synthesis/research-context-compression-llm]]"
---

# KV Cache Compression for Inference Efficiency in LLMs: A Review (2025)

## Summary

A systematic survey of KV cache compression techniques, published in proceedings of the 4th International Conference on Artificial Intelligence and Intelligent Information Processing (ACM AIIP 2025). Provides the definitive taxonomy of the field as of mid-2025.

---

## Motivation

The KV cache is the dominant memory consumer during LLM inference. As context lengths extend to hundreds of thousands of tokens, KV cache memory can reach 70% of total GPU memory. This bottleneck limits:
- The number of concurrent requests a server can handle
- The maximum context length achievable within a given GPU budget
- The feasibility of long-context use cases on consumer hardware

---

## Taxonomy

Three primary families:

### Selective Token Strategies
Decide which KV entries to evict or retain based on importance signals:
- Attention score–based eviction (most common)
- Entropy-guided retention
- Semantic chunk–based retention (ChunkKV)

### Quantisation
Reduce numerical precision of stored tensors:
- INT8: near-lossless for most tasks
- INT4 / fractional-bit: higher risk of cumulative error at long contexts

### Attention Compression / Layer Sharing
Reduce redundancy across layers or heads:
- Cross-layer KV sharing
- Per-head selective retention (retrieval heads vs. other heads)

---

## Key Techniques

| Method | Family | Key Idea |
|--------|--------|---------|
| PyramidKV | Selective | Fewer tokens retained at higher layers (pyramidal funnelling) |
| ChunkKV | Selective | Semantic chunks as the unit of eviction |
| RocketKV | Selective | Two-stage: coarse then fine-grained retention |
| RazorAttention | Selective | Identifies "retrieval heads" that require full KV |
| KVzip | Selective | Query-agnostic compression with reconstruction capability |
| KVQuant | Quantisation | Fine-grained per-channel, per-token quantisation for 10M token contexts |
| Q-Palette | Quantisation | Fractional-bit optimal bit allocation across layers (NeurIPS 2025) |
| KVSharer | Layer Sharing | Shares KV across layers with dissimilar attention patterns |
| KeepKV | Selective + Periodic | Periodic lossless compression cycles |
| EVICPRESS | Selective + Quantisation | Joint eviction and quantisation |

---

## Future Directions

The review identifies three main gaps:
1. **Hybrid optimisation**: most methods use a single strategy; combining eviction + quantisation + sharing has not been systematically studied
2. **Adaptive dynamic strategies**: current methods apply fixed policies; task-aware dynamic adjustment is under-explored
3. **Hardware–software co-design**: KV layout should be designed with GPU memory hierarchy in mind (HBM latency vs. SRAM bandwidth)

---

## Relevance to Wiki

Primary reference for [[concepts/kv-cache-compression]] and the KV cache section of [[concepts/context-compression-llm]].
