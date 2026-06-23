---
type: concept
title: "KV Cache Compression"
created: 2026-06-21
updated: 2026-06-21
tags:
  - llm
  - kv-cache
  - inference-efficiency
  - memory-management
status: complete
related:
  - "[[concepts/context-compression-llm]]"
  - "[[concepts/prompt-compression]]"
  - "[[questions/research-context-compression-llm]]"
sources:
  - "[[sources/kv-cache-compression-review-2025]]"
---

# KV Cache Compression

## What the KV Cache Is

During transformer inference, every processed token generates a pair of tensors: a **Key** and a **Value** vector (the "KV cache"). These are stored so that subsequent tokens can attend to all previous positions without re-computing them. As context grows, KV cache memory grows linearly with sequence length and can consume **up to 70% of total GPU memory** during long-context inference.

KV cache compression aims to reduce this memory footprint without (or with minimal) loss to output quality.

---

## Three Primary Strategies

### 1. Selective Token Eviction

Identify "unimportant" KV entries and discard them, retaining only high-salience tokens.

| Method | Mechanism | Notes |
|--------|-----------|-------|
| **PyramidKV** | Pyramidal information funnelling — lower layers keep more tokens, higher layers keep fewer | Reflects how attention patterns narrow at higher layers |
| **ChunkKV** | Treats semantic chunks rather than isolated tokens as the unit of compression | Preserves intra-chunk coherence |
| **RocketKV** | Two-stage compression: coarse-grained eviction then fine-grained retention | Targets long-context inference acceleration |
| **RazorAttention** | Identifies "retrieval heads" that need full KV; other heads are compressed | Per-head strategy |
| **KVzip** | Query-agnostic compression with context reconstruction capability | Introduced 2025 |

### 2. Quantisation

Reduce the numerical precision of stored KV tensors.

- Standard tensors use FP16 or BF16
- Quantised caches use INT8, INT4, or fractional-bit representations
- **KVQuant**: designed for 10 million token context lengths; applies fine-grained quantisation per channel and per token
- **Q-Palette** (NeurIPS 2025): fractional-bit quantisers with optimal bit allocation across transformer layers

Trade-off: quantisation can be near-lossless at INT8; aggressive INT4 quantisation introduces error that compounds at long sequences.

### 3. Attention Compression / Layer Sharing

Reduce the number of distinct KV representations across heads or layers.

- **KVSharer**: shares KV caches across layers with dissimilar attention patterns, reducing total storage without eviction
- **Entropy-Guided Caching**: uses per-token attention entropy to decide how many KV entries to retain per layer

---

## Key Insight: Memory vs Quality Trade-off

The trade-off is not linear. Compression methods differ significantly in where quality degrades:

- Eviction methods lose quality when evicted tokens were actually needed for later reasoning steps (hard to predict in advance)
- Quantisation methods are more predictable but add systematic error to all tokens
- Layer-sharing methods depend heavily on whether similar layers genuinely share representational function

---

## Future Directions (2025)

- **Hybrid optimisation**: combine eviction + quantisation + layer-sharing
- **Adaptive dynamic strategies**: adjust compression aggressively based on task type and runtime context
- **Hardware–software co-design**: tailor KV layout to GPU memory hierarchy (HBM vs. SRAM)
- **Task-aware compression**: different tasks need different retention policies (e.g., retrieval tasks need lexical tokens; reasoning tasks need relational tokens)

---

## Relationship to Other Techniques

KV cache compression is *orthogonal* to prompt compression:
- Prompt compression reduces tokens *before* they enter the model
- KV cache compression reduces memory *after* tokens have been processed

They can be combined. In practice, prompt compression is applied at the application layer, whilst KV cache compression is applied at the serving/inference layer (often by the model provider, not the application developer).
