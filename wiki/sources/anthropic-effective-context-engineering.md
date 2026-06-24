---
type: source
status: established
source_type: article
title: "Effective Context Engineering for AI Agents"
created: 2026-06-21
updated: 2026-06-21
url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
authors:
  - Anthropic Engineering
date_published: 2025
confidence: high
tags:
  - llm
  - context-engineering
  - agentic-ai
  - anthropic
related:
  - "[[concepts/context-compression-llm]]"
  - "[[synthesis/research-context-compression-llm]]"
---

# Effective Context Engineering for AI Agents (Anthropic)

## Summary

Anthropic's engineering blog post distinguishing **context engineering** from prompt engineering, and providing a taxonomy of techniques for managing agent context windows across long-running tasks.

---

## Key Distinctions

| Term | Scope |
|------|-------|
| **Prompt engineering** | Writing effective instructions for a single, discrete task |
| **Context engineering** | Iteratively curating *all* tokens (system instructions, tools, examples, message history) across a multi-turn agentic loop |

---

## Key Concepts

### Context Rot

Performance degrades as context length increases because:
- Transformer attention has O(n²) pairwise relationships, diluting signal
- Models have limited training exposure to very long sequences
- The "lost in the middle" effect causes under-attention to middle-context information

Anthropic recommends "needle-in-a-haystack" style benchmarking to detect context rot in specific use cases.

### Attention Budget

LLMs have finite attention capacity (analogous to human working memory). Every token added depletes this budget. Effective context engineering is largely an exercise in deciding which tokens *deserve* budget.

---

## Taxonomy of Context Operations

### 1. Compaction

Summarise conversation history to reset the context window:
- Take a conversation nearing the context limit
- Summarise its contents
- Reinitiate a new context window containing only the summary

Lightest-touch variant: **tool-result clearing** — strip raw tool outputs from deep history. Agents rarely re-examine past tool outputs, so this loses almost no task-relevant information. Anthropic offers this as a platform beta feature (`clear_tool_uses_20250919` strategy).

### 2. Structured Note-Taking

Agents maintain external memory files (e.g., NOTES.md, to-do lists) outside the context window:
- Written incrementally during task execution
- Retrieved just-in-time at future steps
- Enables persistent memory with minimal per-turn token cost

### 3. Sub-agent Architectures

Specialised sub-agents handle focused sub-tasks with clean context windows:
- Sub-agent returns a condensed summary (1,000–2,000 tokens) to the coordinating agent
- Detailed search context remains isolated within the sub-agent
- Achieves clear separation of concerns

### 4. Just-in-Time Context Retrieval

Rather than pre-loading all data into the system prompt:
- Maintain lightweight identifiers in context
- Load information dynamically at runtime using tools
- Mirrors human cognition: we do not hold all knowledge in working memory; we use external organisation systems

---

## System Prompt Guidance

- Strike a balance at the "right altitude": specific enough to guide, flexible enough not to be brittle
- Organise using XML tags or Markdown headers for clarity
- Provide diverse, canonical examples rather than exhaustive edge-case lists
- Design minimal, non-overlapping tool sets

---

## Key Claim

> [!gap] Anthropic does not provide specific quantitative benchmarks for context rot or compaction quality in this article. The recommendations are based on engineering experience rather than published empirical study.

---

## Relevance to Wiki

Primary reference for the "Practical Recommendations" section in [[concepts/context-compression-llm]] and the Anthropic compaction approach in [[synthesis/research-context-compression-llm]].
