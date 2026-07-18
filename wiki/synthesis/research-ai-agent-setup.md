---
type: synthesis
address: c-000118
title: "Research: Setting Up AI Agents"
created: 2026-07-19
updated: 2026-07-19
tags: [research, ai-agents, architecture, production, frameworks, 2026]
status: complete
related:
  - concepts/ai-agent-architecture
  - resources/ai-agent-frameworks
  - concepts/ai-workflows
  - concepts/ai-workflow-orchestration
  - sources/furmanets-ai-agents-2026
  - sources/alice-labs-agent-frameworks-2026
sources:
  - "[[sources/furmanets-ai-agents-2026]]"
  - "[[sources/alice-labs-agent-frameworks-2026]]"
---

# Research: Setting Up AI Agents

## Overview

Two rounds of research (5 searches, 5 fetches) across practitioner blogs, framework documentation, Microsoft Azure Architecture Center, and production deployment guides. The dominant finding: most naive agent setups fail in production because they use chat logs as state, add vector DBs as the first memory layer, write plans as prose, skip evals, and bolt on guardrails last. The correct order is inverted.

---

## Key Findings

- **Start with the simplest level**: Direct model call → single agent with tools → multi-agent. Each step up adds cost, latency, and failure modes. Most enterprise use cases are solved by a single agent with a bounded tool set. (Source: Microsoft Azure Architecture Center)
- **State is not chat history**: A typed `AgentState` JSON object (goal, plan, steps, memory refs, policy) enables deterministic transitions, replay, and debugging. Unbounded chat logs don't. (Source: [[sources/furmanets-ai-agents-2026]])
- **Memory is not a vector DB**: Layer working → conversation summaries → task artefacts → structured long-term DB. Vector retrieval is correct for documentation/recall, wrong for facts, permissions, and transactions. (Source: [[sources/furmanets-ai-agents-2026]])
- **The ReAct loop** (Reason → Act → Observe → repeat) is the dominant single-agent planning pattern; plans stored as JSON enable mid-execution re-planning rather than committing to one upfront plan. (Source: multiple)
- **Trajectory evaluation is mandatory**: Eval on task success, tool correctness, step count, cost, and policy compliance in CI before every deployment. 20–50 realistic cases is the minimum dataset. (Source: [[sources/furmanets-ai-agents-2026]])
- **7 guardrails** must be designed before production: capability gating, HITL for irreversible actions, secrets boundary, prompt injection resilience, rate limiting, sandboxing, policy-as-code. (Source: [[sources/furmanets-ai-agents-2026]])
- **Framework landscape consolidation (2026)**: All 7 major frameworks now support MCP; A2A protocol adoption is crossing 150+ organisations; Microsoft merged Semantic Kernel + AutoGen into Agent Framework 1.0. (Source: [[sources/alice-labs-agent-frameworks-2026]])
- **LangGraph 1.0** is the production default for stateful controllable workflows; **Claude Agent SDK** for Anthropic-native hierarchical agents; **CrewAI** for rapid role-based prototyping; **Microsoft Agent Framework 1.0** for .NET/enterprise. (Source: [[sources/alice-labs-agent-frameworks-2026]])

---

## Key Entities

- **LangGraph** (LangChain) — graph-based agent orchestration; GA Oct 2025; production at Uber/LinkedIn/Klarna
- **Claude Agent SDK** — Anthropic's production agent framework with deepest MCP integration
- **CrewAI** — role-based multi-agent framework; v1.14.6; fast prototyping
- **Microsoft Agent Framework 1.0** — merger of Semantic Kernel + AutoGen; native A2A; GA April 2026
- **Mem0** — memory extraction and retrieval layer for agents
- **Letta** — persistent long-term memory runtime (core + archival + recall)
- **Langfuse** — open-source agent tracing and evaluation
- **Andrii Furmanets** — practitioner author of the 2026 agent architecture guide
- **Alice Labs** — published the 7-framework production comparison

---

## Key Concepts

- [[concepts/ai-agent-architecture]] — control loop, 4 building blocks, memory layers, tool contracts, ReAct, evals, guardrails, production patterns
- [[resources/ai-agent-frameworks]] — 7-framework comparison with decision table, protocol landscape, observability pairings
- [[concepts/ai-workflows]] — workflow vs agent distinction; 5 Anthropic patterns (context: agents sit at the top of the complexity spectrum)
- [[concepts/mcp-model-context-protocol]] — MCP enables tool interoperability across all frameworks

---

## Contradictions

- **Multi-agent vs. single agent**: Multiple sources advocate starting with a single agent. The framework comparison articles naturally lean toward multi-agent patterns (that is their subject). There is no contradiction in practice: single agent is the correct default, multi-agent is justified only when single agent demonstrably fails.
- **Vector memory**: Some memory framework marketing leads with vector DBs as the solution; the practitioner guide explicitly warns against this. Consensus: vector retrieval is a supplement to structured state, not a replacement.

---

## Open Questions

- What is the operational cost difference between LangGraph Platform (managed), CrewAI+, and self-hosted deployments at scale? Needs a cost benchmark page.
- How does the **A2A protocol** compare to **MCP** for cross-agent communication? Both are now supported natively by most frameworks — a dedicated comparison concept page would be valuable.
- What are production failure modes and post-mortems for agent systems? Few public case studies exist (most are internal).
- How does **human-in-the-loop** design change agent UX patterns compared to fully autonomous agents? Deserves its own concept page.

---

## Sources

- [[sources/furmanets-ai-agents-2026]]: Andrii Furmanets, 2026 — production agent architecture patterns
- [[sources/alice-labs-agent-frameworks-2026]]: Alice Labs, June 2026 — 7-framework comparison (18+ production deployments)
- Microsoft Azure Architecture Center — AI Agent Orchestration Patterns: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- Agent Components — Prompt Engineering Guide: https://www.promptingguide.ai/agents/components
- Speakeasy — Agentic Application Architecture Patterns: https://www.speakeasy.com/mcp/using-mcp/ai-agents/architecture-patterns/
