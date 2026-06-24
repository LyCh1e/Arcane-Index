---
type: synthesis
title: "Research: AI Workflows"
created: 2026-06-23
updated: 2026-06-23
tags:
  - research
  - ai-engineering
  - agents
  - workflows
  - orchestration
status: developing
related:
  - "[[concepts/ai-workflows]]"
  - "[[concepts/ai-workflow-orchestration]]"
  - "[[concepts/mcp-model-context-protocol]]"
  - "[[concepts/retrieval-augmented-generation]]"
  - "[[concepts/context-compression-llm]]"
sources:
  - "[[sources/anthropic-building-effective-agents]]"
  - "[[sources/aws-agentic-ai-patterns-2025]]"
---

# Research: AI Workflows

## Overview

An AI workflow is an intelligent, end-to-end system that uses LLMs, tools, memory, and retrieval to understand inputs, make decisions, and execute tasks with minimal human intervention. Unlike rule-based automation (RPA), which follows static IF/THEN logic on structured data, AI workflows handle unstructured inputs and reason about context. The field has matured rapidly: Gartner predicts 40% of enterprise applications will embed task-specific AI agents by end of 2026, up from less than 5% in 2025, and the AI agents market is growing at 46.3% CAGR. The canonical design reference is Anthropic's *Building Effective Agents* (December 2024), which defines the vocabulary and five core patterns the industry has broadly adopted.

---

## Key Findings

- **The workflow vs. agent distinction is foundational.** A workflow uses predefined code paths; an agent lets the LLM dynamically direct its own process. Workflows are more reliable, cheaper, and easier to debug. Use agents only when the task is genuinely open-ended and you cannot predict the subtasks needed. (Source: [[sources/anthropic-building-effective-agents]])

- **The augmented LLM is the atomic building block.** Every AI workflow is built around an LLM enhanced with retrieval ([[concepts/retrieval-augmented-generation]]), tools (callable functions), and memory (short-term context, long-term external stores). Modern frontier models natively generate search queries, select tools, and decide what to retain.

- **Anthropic's five patterns cover the vast majority of production workflows.** Prompt Chaining (sequential), Routing (conditional dispatch), Parallelisation (concurrent/voting), Orchestrator–Workers (dynamic delegation), Evaluator–Optimiser (iterative refinement). These compose into more complex architectures. (Source: [[sources/anthropic-building-effective-agents]])

- **Orchestration tools solve three distinct problems — picking the wrong category is the most common mistake.** Agent orchestration (LangGraph, LlamaIndex), durable execution (Temporal, Prefect), data/batch pipelines (Airflow, Dagster). The winning production pattern: Dagster/Airflow for data, Temporal for application durability, LangGraph inside the service for agent logic.

- **Multi-agent systems are accelerating.** Gartner reported a 1,445% surge in multi-agent enquiries from Q1 2024 to Q2 2025. The emerging patterns are specialist swarms (planners, executors, reviewers), puppeteer orchestrators coordinating specialist agents, and event-driven reactive architectures.

- **AI workflows and RPA are complementary, not competing.** RPA is the "hands" (deterministic execution on structured data); AI is the "brain" (contextual reasoning on unstructured inputs). Combined systems achieve 2–3× greater automation coverage. Global RPA market: $28.3B (2025); AI agents: $7.8B (2025), growing toward $52.6B by 2030.

- **Observability requires LLM-native tooling.** Standard APM does not surface LLM failure modes. The minimal observable unit is a span (one LLM call, tool call, retrieval, or handoff). LangSmith is the deepest option for LangChain/LangGraph stacks; Helicone is the fastest to install (proxy, one URL change); Langfuse is open-source with a generous free tier.

- **MCP is the standardised tool layer for AI workflows.** [[concepts/mcp-model-context-protocol]] servers are the backends that agentic workflow tool calls reach — effectively the standardised protocol layer beneath the orchestration framework. MCP and agentic workflows are converging architecturally.

- **Context compression applies when workflow history overflows the window.** [[concepts/context-compression-llm]] — summarisation, prompt compression, KV cache eviction — manages the accumulating context of multi-step workflows.

---

## Key Entities

- **Anthropic**: published the canonical *Building Effective Agents* guide (Dec 2024) defining the 5 workflow patterns.
- **LangChain / LangGraph**: most widely adopted agent orchestration framework (130K+ GitHub stars).
- **LlamaIndex**: event-driven, document-heavy workflow orchestration; 48K GitHub stars.
- **Temporal**: durable execution engine for long-running, failure-prone workflows.
- **CrewAI, AutoGen**: role-based and conversational multi-agent frameworks.
- **LangSmith, Langfuse, Helicone**: LLM-native observability platforms.
- **Gartner**: reported 1,445% surge in multi-agent enquiries; predicts 40% enterprise AI agent embedding by 2026.

---

## Key Concepts

- [[concepts/ai-workflows]]: full definition, the 5 Anthropic patterns, component layers, workflow vs. agent distinction, RPA comparison.
- [[concepts/ai-workflow-orchestration]]: tool taxonomy across four categories, decision guide, observability tooling.

---

## Contradictions

- **LangChain vs. LlamaIndex framing**: Some sources position them as competing frameworks; authoritative sources clarify they solve different primary problems — LangGraph for agentic branching/state; LlamaIndex for data retrieval pipelines. They are often used together.

- **Agent vs. workflow boundary**: The industry has not fully settled on where a "workflow" becomes an "agent". Anthropic's definition (predefined paths vs. dynamic LLM control) is the clearest, but many real systems are hybrids. Treat the distinction as a spectrum, not a binary.

---

## Open Questions

- At what task complexity does the move from workflow to autonomous agent become justified, and how do you measure it empirically?
- Will OpenTelemetry for LLMs emerge as a standard, or will LangSmith/Langfuse/Helicone remain fragmented?
- How will human-in-the-loop patterns standardise for regulated industries (healthcare, finance, legal)?
- Will MCP become the universal tool protocol layer beneath all orchestration frameworks, or will proprietary tool interfaces persist?
- Can workflow reliability be formally specified and verified, or will it always require empirical testing on real inputs?

---

## Sources

- [[sources/anthropic-building-effective-agents]]: Anthropic, Dec 2024 — canonical 5-pattern guide.
- [[sources/aws-agentic-ai-patterns-2025]]: AWS Prescriptive Guidance, Jul 2025 — three-layer framework, cloud implementation patterns.

---

## Research Metadata

| Field | Value |
|---|---|
| Rounds | 3 |
| Web searches | 6 |
| Sources fetched | 2 |
| Pages created | 5 |
| Date | 2026-06-23 |
