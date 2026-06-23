---
type: entity
entity_type: tool
title: "LLMLingua"
created: 2026-06-21
updated: 2026-06-21
tags:
  - llm
  - prompt-compression
  - microsoft-research
  - open-source
status: active
related:
  - "[[concepts/prompt-compression]]"
  - "[[concepts/context-compression-llm]]"
  - "[[questions/research-context-compression-llm]]"
---

# LLMLingua

## Overview

LLMLingua is an open-source prompt compression library developed by **Microsoft Research**. It is the most widely adopted hard (extractive) prompt compression toolkit, with versions published at EMNLP 2023 and ACL 2024.

- **GitHub**: https://github.com/microsoft/LLMLingua
- **Licence**: MIT
- **Organisation**: Microsoft Research

---

## Versions

### LLMLingua (EMNLP 2023)

The original system. Uses a small, cheap LM (e.g., LLaMA-7B) to score each token's perplexity; tokens with low perplexity (i.e., easily predicted from context, therefore low information content) are removed.

Three-stage pipeline:
1. **Dynamic budget controller**: allocates per-component compression ratios (instruction, demonstrations, question) based on an overall target ratio
2. **Iterative token-level compression**: removes low-perplexity tokens iteratively until budget is met
3. **Distribution alignment**: uses instruction-tuned model variants to maintain semantic fidelity

Key result: up to **20× compression** with minimal downstream performance loss.

### LLMLingua-2 (ACL 2024)

Addresses LLMLingua's task-dependence. Reformulates compression as **binary token classification**: for each token, predict "keep" or "drop" using a model distilled from GPT-4 annotations.

Advantages:
- Task-agnostic: trained once, applicable to any task
- 3–6× faster than LLMLingua
- Reduces end-to-end latency by **1.6–2.9×** at 2–5× compression ratios

Training data: GPT-4 generates an extractive text compression dataset; a small BERT-class model learns the keep/drop decision.

### LongLLMLingua

Extension for long-context scenarios (e.g., 100k-token retrieval-augmented generation).

Key innovations:
- **Question-aware coarse-to-fine compression**: first selects relevant document sections, then compresses at token level within those sections
- **Document reordering**: reorders retained chunks to maximise recency-biased attention
- **Adaptive compression ratios**: allocates more tokens to high-relevance sections

Result: up to **+21.4% performance** on long-context benchmarks whilst using substantially fewer tokens.

---

## Usage Pattern

```python
from llmlingua import PromptCompressor

llm_lingua = PromptCompressor(
    model_name="microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank",
    use_llmlingua2=True,
)

compressed = llm_lingua.compress_prompt(
    context,
    instruction=instruction,
    question=question,
    target_token=200,
)
```

---

## Limitations

- Hard (extractive) compression cannot introduce new phrasing; it can only remove tokens, which may create grammatically incomplete spans
- Performance degrades sharply at extreme compression ratios (>10×) on tasks requiring precise factual recall
- LLMLingua-2 requires the target task to be representable via keep/drop at the token level; some tasks (e.g., code) are sensitive to token-level gaps
