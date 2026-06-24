---
type: source
title: "Building Effective Agents — Anthropic"
source_type: article
author: Anthropic
date_published: 2024-12-01
url: "https://www.anthropic.com/research/building-effective-agents"
confidence: high
ingested: 2026-06-23
tags:
  - ai-engineering
  - agents
  - workflows
  - anthropic
key_claims:
  - Workflows use predefined code paths; agents let the LLM dynamically direct its own process
  - Five core patterns: Prompt Chaining, Routing, Parallelisation, Orchestrator-Workers, Evaluator-Optimiser
  - The foundational building block is the augmented LLM (retrieval + tools + memory)
  - Start with the simplest workflow that works; only use agents when steps cannot be predicted
  - Tool documentation quality determines whether agents use tools correctly
related:
  - "[[concepts/ai-workflows]]"
  - "[[concepts/ai-workflow-orchestration]]"
  - "[[synthesis/research-ai-workflows]]"
---

# Building Effective Agents — Anthropic

## Summary

Anthropic's canonical guide to designing AI agent systems, published December 2024. Defines the foundational vocabulary (workflow vs. agent, augmented LLM) and provides five reusable workflow patterns that cover the majority of production use cases. Widely cited as the most practical and opinionated guide to AI workflow design from a primary AI lab.

## Five Core Patterns

1. **Prompt Chaining** — sequential LLM calls, each processing the prior output. For fixed decomposable tasks.
2. **Routing** — classifier directs input to a specialised handler or model tier. For varied input types.
3. **Parallelisation** — simultaneous LLM calls (sectioning or voting). For independent subtasks or confidence improvement.
4. **Orchestrator–Workers** — central LLM dynamically decomposes and delegates; synthesises results. For tasks with unpredictable subtask structure.
5. **Evaluator–Optimiser** — generator + evaluator loop until quality criteria met. For tasks with clear evaluation criteria and iterative value.

## Key Definitions

- **Workflow**: LLMs and tools orchestrated through predefined code paths.
- **Agent**: LLM dynamically directing its own process and tool usage.
- **Augmented LLM**: foundational building block — model + retrieval + tools + memory.

## Design Principles

- Simplicity > sophistication.
- Transparency: display reasoning steps.
- Invest in tool documentation.
- Prefer workflows over agents for known tasks.

## Confidence Notes

High confidence — primary source from the creating lab, directly describing their internal design philosophy. Consistent with production findings across the community.
