---
type: concept
title: "Prompt Compression"
created: 2026-06-21
updated: 2026-06-21
tags:
  - llm
  - prompt-compression
  - token-efficiency
  - inference
status: complete
related:
  - "[[concepts/context-compression-llm]]"
  - "[[concepts/kv-cache-compression]]"
  - "[[entities/llmlingua]]"
  - "[[synthesis/research-context-compression-llm]]"
---

# Prompt Compression

## Definition

Prompt compression is the reduction of token count in an input prompt *before* it is sent to a target LLM, with the goal of reducing inference cost and latency whilst preserving the model's ability to answer correctly.

It sits at the application layer (not the model or serving layer) and requires no changes to the target LLM.

---

## Why It Is Needed

- Long prompts lead to prohibitively expensive API costs (token pricing)
- Reasoning ability degrades at large prompt lengths
- The "lost in the middle" effect: important information in the middle of a long context is under-utilised
- Latency increases super-linearly with context length under causal attention

---

## Approaches

### Hard (Extractive) Compression

Remove tokens from the original prompt. The remaining tokens are still drawn from the original vocabulary.

**LLMLingua series (Microsoft)**

| Version | Venue | Key Innovation | Compression Ratio | Speedup |
|---------|-------|----------------|-------------------|---------|
| LLMLingua | EMNLP 2023 | Small LM scores token perplexity; prune low-info tokens via dynamic budget controller | Up to 20× | — |
| LLMLingua-2 | ACL 2024 | Token classification framing; data distilled from GPT-4; task-agnostic | 2–5× | 1.6–2.9× end-to-end |
| LongLLMLingua | — | Question-aware coarse-to-fine; document reordering; adaptive compression ratios | — | +21.4% on long-context benchmarks |

**Evaluator Heads (2025)**
- Training-free
- Identifies specific attention heads ("evaluator heads") that score token salience
- Uses these head outputs to prune tokens at inference time
- No gradient updates or model fine-tuning required

**ContextBudget (2025)**
- Budget-aware context management for long-horizon search agents
- Allocates a token budget across context components and enforces it

### Soft (Generative / Latent) Compression

Encode the prompt into a compact representation (continuous vectors) rather than a shorter discrete token sequence. The target LLM must be able to attend to these vectors, which typically requires at least partial fine-tuning.

| Method | Mechanism | Compression |
|--------|-----------|-------------|
| **Gist Tokens** | Trainable special tokens appended after prompt; attention mask prevents original tokens from being attended to | Up to 26×; −40% FLOPs |
| **AutoCompressor** | Fine-tuned compressor generates summary vectors attended to by a frozen LLM | — |
| **ICAE** (In-Context AutoEncoder) | Encoder–decoder; encoder compresses to memory slots, decoder reconstructs | — |
| **500xCompressor** | Extreme compression; generalised; presented at ACL 2025 | Up to 500× (high confidence: low — single paper, not widely replicated) |
| **K-Token Merging** (2025) | Merges tokens in the latent embedding space rather than the input space | — |

### Retrieval-Augmented Compression

Rather than compressing a large prompt, retrieve only the relevant segments.

- Use dense retrieval (embedding similarity) to select top-k relevant chunks
- AMR (Abstract Meaning Representation) concept distillation: extract semantic concepts, compress via knowledge graph rather than raw text
- EDU (Elementary Discourse Unit) decomposition: split context into discourse units, score each, retain top-scoring units

---

## Evaluation Challenges

> [!gap] Compression method performance is heavily benchmark-dependent. The paper "Compression Method Matters: Benchmark-Dependent Output Dynamics in LLM Prompt Compression" (2025) shows that different methods win on different benchmarks, making general recommendations difficult.

Key metrics:
- **Compression ratio**: tokens retained / original tokens
- **Performance drop**: downstream task accuracy after compression vs. before
- **Latency**: end-to-end wall-clock time
- **Faithfulness**: whether the compressed prompt preserves the factual content of the original

---

## Practical Guidance

1. **For API use with no model changes**: use LLMLingua-2 (open-source, task-agnostic, well-validated at ACL 2024)
2. **For training pipelines where you control the model**: consider Gist Tokens or AutoCompressor for higher compression ratios
3. **For long retrieval-augmented generation**: use LongLLMLingua's question-aware strategy
4. **Compression ratio ≠ quality**: a 99% compression ratio can score *worse* on quality metrics than 98.6% (Source: [[sources/factory-ai-compression-evaluation-2025]])
5. **Test on your task**: benchmark-dependent variance is high; always evaluate on your specific domain before selecting a method
