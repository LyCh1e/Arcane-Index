---
type: source
address: c-000116
title: "AI Agents in 2026: Tools, Memory, Evals, and Guardrails — Andrii Furmanets"
source_type: blog-post
author: Andrii Furmanets
date_published: 2026-01-01
url: https://andriifurmanets.com/blogs/ai-agents-2026-practical-architecture-tools-memory-evals-guardrails
confidence: high
domain: ai-engineering
created: 2026-07-19
updated: 2026-07-19
tags: [source, ai-agents, architecture, memory, evals, guardrails, production]
related:
  - concepts/ai-agent-architecture
  - resources/ai-agent-frameworks
---

# AI Agents in 2026: Tools, Memory, Evals, and Guardrails — Andrii Furmanets

**URL:** https://andriifurmanets.com/blogs/ai-agents-2026-practical-architecture-tools-memory-evals-guardrails  
**Type:** Technical blog post  
**Confidence:** High — specific, production-verified patterns; referenced by multiple practitioner communities

---

## What This Source Contributes

The primary reference for [[concepts/ai-agent-architecture]]. Provides a practitioner's production-tested framework for agent setup with emphasis on what goes wrong in naive implementations (chat-log state, vector-only memory, one-shot planning, no evals, no guardrails).

---

## Key Claims

- A production agent is a **control loop**, not a chat: read state → plan → execute → observe → update → repeat
- State should be a typed `AgentState` object (reducer pattern), not an unbounded chat log — enables replay and deterministic debugging
- Memory has 4 layers: working, conversation, task/artefacts, long-term structured DB — vector search is only correct for documentation/recall, not for critical facts or transactions
- Tools are strict APIs: JSON Schema input, structured `{ ok, data, error, meta }` output, idempotency keys for side effects
- Plans should be stored as **JSON data structures** (not prose) to enable mid-execution re-planning
- Trajectory evaluation is mandatory: task success, tool correctness, step count/cost, policy compliance — evaluated in CI with deterministic mocks
- 7 guardrails: capability gating, HITL, secrets boundary, prompt injection resilience, rate limiting, sandboxing, policy-as-code
- MVP build order: tool contracts → state reducer → tracing → eval dataset → policy gating → memory layers (in that sequence; adding vectors first is a common trap)

---

## Notable Quotes

> "A production agent is a **control loop** that repeatedly plans and acts using tools, observes results, updates state, and continues until it reaches a goal or hits budgets/timeouts."

> "State ≠ Chat History. Memory ≠ Vector DB. Planning ≠ One Perfect Plan. Evaluation ≠ Optional. Guardrails ≠ Afterthought."

---

## Concepts Linked

- [[concepts/ai-agent-architecture]] — primary concept page built from this source
