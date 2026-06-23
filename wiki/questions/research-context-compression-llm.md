---
type: synthesis
title: "Research: Context Compression of Chats with Large Language Models"
created: 2026-06-21
updated: 2026-06-21
tags:
  - research
  - llm
  - context-compression
  - memory-management
  - ai-engineering
status: developing
related:
  - "[[concepts/context-compression-llm]]"
  - "[[concepts/kv-cache-compression]]"
  - "[[concepts/prompt-compression]]"
  - "[[entities/llmlingua]]"
sources:
  - "[[sources/acon-context-compression-agents]]"
  - "[[sources/anthropic-effective-context-engineering]]"
  - "[[sources/factory-ai-compression-evaluation-2025]]"
  - "[[sources/kv-cache-compression-review-2025]]"
---

# Research: Context Compression of Chats with Large Language Models

## Overview

Context compression addresses the fundamental constraint that all transformer-based LLMs face: a finite context window. As chat histories, agentic task logs, and retrieval corpora grow, token counts balloon — driving up cost, latency, and (counterintuitively) *degrading* model quality through context rot. The field has matured rapidly in 2024–2025, with production APIs, open-source libraries, and dozens of academic papers now available. Five main technique families exist, operating at different layers of the stack.

---

## Key Findings

- **Five distinct technique families** address context compression at different levels: dialogue memory summarisation, prompt compression (token-level), KV cache compression (tensor-level), soft prompt / latent compression, and retrieval-based just-in-time loading. (Source: [[concepts/context-compression-llm]])

- **KV cache can consume up to 70% of GPU memory** during long-context inference, making it the dominant bottleneck on the serving side. KV cache compression is primarily a serving-layer concern, not an application-layer one. (Source: [[sources/kv-cache-compression-review-2025]])

- **LLMLingua-2 achieves 3–6× faster compression** than its predecessor and reduces end-to-end latency by 1.6–2.9× at 2–5× compression ratios, with task-agnostic generality. It is the most practical off-the-shelf hard prompt compression library as of 2024. (Source: [[entities/llmlingua]])

- **Higher compression ratio does not equal higher quality.** OpenAI's method compresses 99.3% of tokens but scores 0.35 points *lower* than Factory's 98.6%-compression anchored iterative method on production software engineering tasks. (Source: [[sources/factory-ai-compression-evaluation-2025]])

- **Task-specific compression guidelines outperform generic ones** for agentic contexts. ACON achieves 26–38% peak token reduction whilst maintaining or improving accuracy compared to uncompressed baselines, using guidelines optimised via contrastive failure analysis. (Source: [[sources/acon-context-compression-agents]])

- **Context rot is real and measurable**: performance degrades before the context limit is reached, due to O(n²) attention dilution and the "lost in the middle" effect. This makes proactive compression the correct strategy, not reactive truncation. (Source: [[sources/anthropic-effective-context-engineering]])

- **Gist tokens** achieve up to 26× compression and 40% FLOPs reduction, but require model fine-tuning, limiting their use to settings where the deployer controls the model. (Source: [[concepts/prompt-compression]])

- **Mem0's selective memory formation** achieves 80–90% token cost reduction and 26% relative response quality improvement compared to basic chat history management, by storing key facts rather than compressing everything. (Confidence: medium — figures from vendor blog, not independently replicated)

- **Artifact tracking is an open problem**: all evaluated production compression methods score poorly (2.19–2.45 / 5) on tracking which files have been modified during an agentic session. Summaries alone are insufficient; structured external logs are needed. (Source: [[sources/factory-ai-compression-evaluation-2025]])

---

## Key Entities

- [[entities/llmlingua]]: Microsoft Research open-source prompt compression library; three versions (2023–2024); the dominant tool for hard extractive compression
- **Mem0**: production memory management framework; hierarchical memory; persistent across sessions; sub-50ms retrieval
- **Factory.ai**: AI coding agent company; developed anchored iterative summarisation; conducted the 2025 multi-provider compression evaluation
- **Anthropic**: provides compaction API, tool-result clearing beta, and context engineering guidance; also authored the ACON-adjacent compression research through Claude SDK

---

## Key Concepts

- [[concepts/context-compression-llm]]: master taxonomy of all five technique families
- [[concepts/kv-cache-compression]]: serving-layer KV tensor compression; three primary strategies; top methods: PyramidKV, ChunkKV, KVQuant
- [[concepts/prompt-compression]]: application-layer input token reduction; LLMLingua series; Evaluator Heads; soft compression (Gist Tokens)
- **Context rot**: quality degradation as context grows, even below the nominal context limit; primary motivation for compression
- **Anchored iterative summarisation**: compression method that merges new summaries into a persisted structured document rather than regenerating; superior to full-regeneration approaches

---

## Contradictions

- [[sources/factory-ai-compression-evaluation-2025]] shows OpenAI's 99.3%-compression method scoring *lower* than Factory's 98.6%-compression method, contradicting the naive assumption that more compression = worse quality and that less compression = better quality. The relationship is non-monotonic and depends heavily on *what* is preserved, not just *how much*.

- The adaptive context compression paper (Fofadiya & Tiwari, 2025) claims "consistent improvements" across all benchmarks. This is a strong claim; such uniformity is unusual and may reflect the specific benchmark selection (LOCOMO, LOCCO, LongBench) rather than universal superiority. (Confidence: low — single paper, no independent replication found)

---

## Open Questions

- **Artifact tracking**: no current compression method reliably preserves knowledge of file modifications, command executions, or state changes in agentic tasks. How can structured state tracking be integrated with natural-language compression?

- **Compression method selection**: benchmark-dependent variance is high ("Compression Method Matters: Benchmark-Dependent Output Dynamics", 2025). How does a practitioner select the right method without expensive per-task evaluation?

- **Soft prompt compression at scale**: Gist Tokens and AutoCompressor show strong compression ratios, but require fine-tuning. Is there a viable path to training-free latent compression with comparable ratios?

- **KV cache compression for chat**: most KV cache compression research targets single-pass long documents or single-step reasoning. Extension to multi-turn chat (where KV grows incrementally across turns) is under-studied.

- **Long-term identity and preference retention**: current methods focus on task-level context (what are we doing right now?). Retaining user identity, preferences, and long-term knowledge across hundreds of sessions is largely unsolved.

---

## Sources

- [[sources/acon-context-compression-agents]]: Kang et al. (2025) — ACON framework for agentic context compression
- [[sources/anthropic-effective-context-engineering]]: Anthropic Engineering (2025) — context engineering taxonomy and best practices
- [[sources/factory-ai-compression-evaluation-2025]]: Factory.ai (2025) — multi-provider production compression evaluation
- [[sources/kv-cache-compression-review-2025]]: Review paper (ACM AIIP 2025) — systematic KV cache compression survey
- LLMLingua-2: Pan et al., ACL 2024 — https://arxiv.org/abs/2403.12968
- Mem0 blog: https://mem0.ai/blog/llm-chat-history-summarization-guide-2025
- Adaptive context compression: Fofadiya & Tiwari (2025) — https://arxiv.org/abs/2603.29193
