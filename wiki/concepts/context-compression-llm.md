---
type: concept
title: "Context Compression for LLMs"
created: 2026-06-21
updated: 2026-06-21
tags:
  - llm
  - context-compression
  - memory-management
  - ai-engineering
status: complete
related:
  - "[[concepts/kv-cache-compression]]"
  - "[[concepts/prompt-compression]]"
  - "[[entities/llmlingua]]"
  - "[[synthesis/research-context-compression-llm]]"
sources:
  - "[[sources/acon-context-compression-agents]]"
  - "[[sources/anthropic-effective-context-engineering]]"
  - "[[sources/factory-ai-compression-evaluation-2025]]"
---

# Context Compression for LLMs

## What It Is

Context compression refers to the family of techniques that reduce the number of tokens occupying a large language model's context window during inference or between conversation turns, whilst preserving the information needed to complete the task at hand.

As conversations, agentic tasks, and retrieval-augmented pipelines grow longer, context size drives up memory consumption, latency, and API cost — and actively degrades model quality through a phenomenon known as **context rot** (see below).

---

## Why It Matters

| Problem | Cause |
|---------|-------|
| Memory cost | KV cache can consume up to 70% of GPU memory during long-context inference |
| Latency | Attention cost scales as O(n²) in sequence length |
| Quality degradation | Models lose track of middle-context information ("lost in the middle" effect) |
| API cost | Token pricing makes long histories expensive at scale |

---

## Taxonomy of Approaches

There are five broad families of context compression technique, operating at different levels of the stack.

### 1. Dialogue Memory Summarisation

The model (or a dedicated smaller model) periodically summarises accumulated conversation history, replacing raw turns with a condensed summary.

- **When it triggers**: when token count exceeds a threshold, or on a fixed cadence
- **What it preserves**: intent, decisions, key facts, open tasks
- **What it discards**: verbatim tool outputs, boilerplate, redundant exchange
- **Production implementations**: LangChain `ConversationSummaryMemory`, LlamaIndex `ChatMemoryBuffer`, Anthropic compaction API, Mem0

Key variants:
- *Rolling summary*: new summary merges previous summary + recent turns (Anthropic SDK approach)
- *Anchored iterative summary*: new compression merges into a persisted structured document rather than regenerating from scratch (Factory.ai approach)
- *Selective memory formation*: rather than compressing everything, identify and store specific facts, preferences, and patterns; discard the rest (Mem0 approach)

### 2. Prompt Compression (Token-Level)

Techniques that reduce the token count of the input prompt itself, at inference time, without any model fine-tuning on the receiver side.

- **LLMLingua** (Microsoft, EMNLP 2023): uses a small LM to score token perplexity and prune low-information tokens; achieves up to 20× compression with minimal performance loss
- **LLMLingua-2** (ACL 2024): task-agnostic; formulates compression as token classification; 3–6× faster than prior methods; 1.6–2.9× end-to-end latency reduction at 2–5× compression ratios
- **LongLLMLingua**: adds question-aware coarse-to-fine strategy and document reordering; boosts performance by up to 21.4% on long-context tasks with fewer tokens
- **Evaluator Heads** (2025): training-free; identifies specific attention heads that signal token importance; uses these to prune at inference time with no gradient updates

See [[concepts/prompt-compression]] for the full treatment.

### 3. KV Cache Compression

Rather than compressing the text before it enters the model, KV cache compression operates on the internal key-value tensors produced by the attention mechanism, reducing the memory footprint of already-processed context.

Strategies:
- **Selective token eviction** (PyramidKV, ChunkKV, RocketKV): evict "less important" KV entries based on attention score heuristics
- **Quantisation** (KVQuant): reduce numerical precision of cached tensors (e.g., from FP16 to INT4)
- **Layer sharing** (KVSharer): share KV representations across dissimilar transformer layers

See [[concepts/kv-cache-compression]] for the full treatment.

### 4. Soft Prompt Compression (Latent Compression)

Techniques that learn to encode long prompts into a short sequence of continuous "soft tokens" (dense vectors) rather than discrete tokens. These require fine-tuning or training.

- **Gist Tokens**: trainable special tokens appended after the original prompt; attention mask modified so subsequent tokens attend only to gist tokens; up to 26× compression; 40% FLOPs reduction
- **AutoCompressor**: fine-tuned compressor model generates summary vectors that a frozen LLM can attend to
- **ICAE (In-Context AutoEncoder)**: encoder–decoder architecture; encoder compresses, decoder reconstructs context
- **500xCompressor**: generalised method targeting extreme compression ratios with faithful reconstruction (presented at ACL 2025)

Trade-off: these are the most powerful but require training, making them harder to drop into existing pipelines.

### 5. Retrieval-Based / Just-In-Time Context

Rather than compressing what is in context, this family stores information externally and retrieves only what is relevant for each inference step.

- External vector stores (Pinecone, Chroma, pgvector) with semantic similarity search
- Structured note-taking: agents write NOTES.md / todo files outside the context window, pull them in on demand
- Multi-level memory hierarchies: working memory (current session) + episodic memory (past sessions, in vector store) + semantic memory (general knowledge)
- Vectorised memory: stores past interactions as embeddings; retrieves semantically similar memories at query time

This is often the most scalable approach for long-running agentic systems.

---

## Context Rot

Context rot is the observation that LLM performance degrades as context window length increases, even when the model's nominal context limit is not exceeded. Causes include:

- Transformer attention has O(n²) pairwise relationships; very long contexts dilute attention signal
- Models are trained on shorter sequences than their inference-time context limits
- The "lost in the middle" effect: relevant information in the middle of a large context is systematically under-attended

Compressing or pruning the context is the primary mitigation.

---

## Agentic Context Compression (ACON Framework)

Long-horizon agents face a compound problem: both *observations* (environment outputs) and *interaction histories* accumulate. ACON (2025) addresses this with:

1. **History compression**: LLM-guided summarisation of accumulated interactions when a threshold is exceeded; guided by task-specific compression guidelines optimised through contrastive feedback
2. **Observation compression**: condenses environment observations using historical context to decide what is task-relevant

Results on AppWorld: 56.5% accuracy, 26% peak-token reduction. On OfficeBench: 72.63% accuracy, 38% peak-token reduction.

The key insight: *task-specific* compression guidelines significantly outperform generic prompting.

---

## Production Strategy Comparison (Factory.ai, 2025)

Evaluated across recall, artifact tracking, continuation, and decision-preservation probes:

| Provider | Accuracy | Compression Ratio | Approach |
|----------|----------|-------------------|----------|
| Factory | 4.04 / 5 | 98.6% | Anchored iterative summary, structured sections |
| OpenAI | 3.43 / 5 | 99.3% | Opaque `/responses/compact` endpoint |
| Anthropic | ~3.78 / 5 | ~98% | Structured summary (7–12k chars), full regeneration per compression |

Key finding: higher compression ratio does not equal better quality. All methods scored poorly on *artifact tracking* (file modification history), achieving only 2.19–2.45 / 5.

---

## Practical Recommendations

1. **Start with tool-result clearing**: the cheapest intervention — strip raw tool outputs from deep history, as agents rarely re-examine them. Anthropic now offers this as a platform feature.
2. **Use threshold-triggered summarisation**: compress when token count exceeds 70–80% of context limit.
3. **Prefer retrieval for long-running agents**: persistent vector memory scales further than compression alone.
4. **Use task-specific compression prompts**: generic summarisation loses task-critical detail. Tailor compression guidelines to the domain.
5. **Track what you compress**: all current methods lose artifact trails. Log file modifications and decisions to structured external storage, not just summaries.
