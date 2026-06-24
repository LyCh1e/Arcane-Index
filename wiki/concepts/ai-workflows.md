---
type: concept
title: "AI Workflows"
created: 2026-06-23
updated: 2026-06-23
tags:
  - ai-engineering
  - agents
  - workflows
  - llm
  - orchestration
domain: ai-engineering
complexity: high
related:
  - "[[concepts/ai-workflow-orchestration]]"
  - "[[concepts/mcp-model-context-protocol]]"
  - "[[concepts/retrieval-augmented-generation]]"
  - "[[synthesis/research-ai-workflows]]"
sources:
  - "[[sources/anthropic-building-effective-agents]]"
  - "[[sources/aws-agentic-ai-patterns-2025]]"
---

# AI Workflows

## Definition

An **AI workflow** is an intelligent, end-to-end system that uses one or more LLMs — combined with tools, memory, and retrieval — to understand inputs, make decisions, and execute tasks with minimal human intervention. Unlike traditional automation, which follows static IF/THEN rules on structured data, AI workflows are adaptive: they handle unstructured inputs (natural language, PDFs, emails), reason about context, and dynamically route or sequence actions.

---

## Workflows vs. Agents: The Critical Distinction

Anthropic's canonical definition (2024) draws a precise line:

| | Workflow | Agent |
|---|---|---|
| **Control** | Predefined code paths | LLM dynamically directs its own process |
| **Predictability** | Steps are fixed at design time | Steps are determined at runtime |
| **Best for** | Known, decomposable tasks | Open-ended problems with unpredictable steps |
| **Reliability** | Higher — deterministic paths | Lower — LLM decides, can make unexpected choices |
| **Cost** | Lower — fewer LLM calls | Higher — more reasoning loops |

**Rule of thumb**: start with a workflow. Only move to a fully autonomous agent when the task is genuinely open-ended and you cannot predict the steps needed. (Source: [[sources/anthropic-building-effective-agents]])

---

## The Augmented LLM: Foundation of All AI Workflows

The primitive building block of any AI workflow is an **augmented LLM** — a model enhanced with:

- **Retrieval**: the ability to search external knowledge (RAG — see [[concepts/retrieval-augmented-generation]])
- **Tools**: callable functions — APIs, databases, code executors, web search
- **Memory**: short-term (context window), long-term (external stores), episodic (past interactions)

Modern frontier models (Claude, GPT-4o, Gemini) natively generate search queries, select tools, and decide what to retain. The augmented LLM is not a metaphor — it is the literal unit you build around.

---

## Core Components of an AI Workflow

### 1. Intake Layer
Converts unstructured input into structured data. Reads emails, PDFs, Slack messages, forms, or voice. Extracts entities, intents, sentiment, and structured fields. This is where NLP and document intelligence live.

### 2. Decision Layer
Evaluates the structured input against business rules, historical patterns, risk levels, and SLA constraints. Determines the next best action — not by keyword matching but by contextual reasoning.

### 3. Action Layer
Executes decisions across external systems: updating CRM records, creating tickets, drafting responses, running code, querying databases, calling APIs, generating reports.

### 4. Orchestration Layer
Sequences and coordinates steps, manages state across tool calls, handles retries and failures, routes between sub-agents or specialised models.

---

## The Five Anthropic Workflow Patterns

Published in *Building Effective Agents* (Anthropic, December 2024). These are the fundamental reusable patterns for composing AI workflows. (Source: [[sources/anthropic-building-effective-agents]])

---

### Pattern 1 — Prompt Chaining

```
Input → LLM₁ → Output₁ → LLM₂ → Output₂ → ... → Final Output
```

Each LLM call processes the output of the previous step. Appropriate when a task can be decomposed into a fixed, sequential sequence of subtasks.

**Example**: Generate marketing copy → pass to translation model → pass to tone-checking model.

**Use when**: The task has clear sequential stages, each small enough to fit in one model call.

---

### Pattern 2 — Routing

```
Input → Classifier LLM → Route A (simple/fast)
                       → Route B (complex/powerful)
                       → Route C (domain-specialist)
```

An LLM or classifier reads the input and directs it to the appropriate handler. Enables specialised prompts per input type and cost-optimised model selection.

**Example**: Customer queries → simple billing questions go to Claude Haiku + FAQ lookup; complex complaints go to Claude Sonnet + CRM access.

**Use when**: Inputs vary enough that a single handler is suboptimal for all cases.

---

### Pattern 3 — Parallelisation

Two sub-patterns:

**Sectioning**: Break a task into independent subtasks and run them simultaneously.
```
          ┌── LLM_A (subtask 1) ──┐
Input ────┤── LLM_B (subtask 2) ──├──► Aggregator → Output
          └── LLM_C (subtask 3) ──┘
```

**Voting**: Run the same task multiple times independently, then take majority or best result.
```
Input ────┬── LLM_1 ──┐
          ├── LLM_2 ──├──► Voting/Selection → Final Output
          └── LLM_3 ──┘
```

**Use when**: Subtasks are independent (sectioning), or when higher confidence requires multiple perspectives (voting).

---

### Pattern 4 — Orchestrator–Workers

```
         Orchestrator LLM
         (decomposes task, plans)
              │
    ┌─────────┼─────────┐
    ▼         ▼         ▼
Worker A   Worker B   Worker C
(tool call)(LLM call)(retrieval)
    │         │         │
    └─────────┼─────────┘
              ▼
         Orchestrator LLM
         (synthesises results)
```

A central orchestrator LLM dynamically plans the task decomposition at runtime and delegates to worker LLMs or tools. The orchestrator synthesises the results.

**Use when**: Task complexity means you cannot predict the subtasks needed in advance. Multi-file code changes, multi-source research, complex data analysis.

---

### Pattern 5 — Evaluator–Optimiser

```
Input → Generator LLM → Draft Output
                              │
                     Evaluator LLM (critiques)
                              │
                    (meets criteria?) ──NO──► Generator LLM (refine)
                              │
                             YES
                              ▼
                          Final Output
```

One LLM generates; a second evaluates and provides feedback; the loop continues until quality criteria are met.

**Use when**: Clear evaluation criteria exist and iterative refinement produces measurable improvement. Literary translation, code correctness, complex search queries.

---

## AI Workflows vs. Traditional Automation

| Dimension | Traditional Automation / RPA | AI Workflow |
|---|---|---|
| **Input type** | Structured data, fixed schemas | Unstructured: text, PDFs, email, voice |
| **Logic** | Hardcoded IF/THEN rules | Contextual reasoning, LLM decisions |
| **Adaptability** | Brittle to input variation | Adapts to novel inputs |
| **Failure mode** | Breaks when UI or data format changes | Can hallucinate or over-reason |
| **Best for** | High-volume, stable, deterministic tasks | Variable, judgement-intensive tasks |

**2025 consensus**: RPA and AI workflows are complementary. RPA is the "hands" (execution); AI is the "brain" (judgement). Combined systems achieve 2–3× greater automation coverage than either alone. Global RPA market: $28.3B (2025). AI agents market: $7.8B (2025), growing at 46.3% CAGR toward $52.6B by 2030.

---

## Agentic Workflow Patterns (beyond the 5 primitives)

Emerging patterns from production deployments:

**Specialist swarms**: Instead of one general agent, deploy swarms of specialist agents (planner, executor, reviewer, critic). The orchestrator routes tasks to the relevant specialist.

**Puppeteer / Meta-agent**: A high-level orchestrator ("puppeteer") coordinates multiple specialist agents. Gartner reported a 1,445% surge in multi-agent system enquiries from Q1 2024 to Q2 2025.

**Event-driven coordination**: Agents react to events (a new file uploaded, a ticket created, a threshold crossed) rather than running on a schedule. Enables reactive, real-time workflows.

**Human-in-the-loop checkpoints**: Workflows pause at defined decision points requiring human approval before proceeding. Critical for high-stakes or irreversible actions.

---

## Design Principles

From Anthropic's *Building Effective Agents* (2024):

1. **Simplicity first**: do not build the most sophisticated system — build the right system. Start with the simplest workflow that works.
2. **Transparency**: explicitly display the agent's planning and reasoning steps so failures are diagnosable.
3. **Document your tools carefully**: the agent-computer interface (tool descriptions, parameter names, return formats) determines whether the agent uses tools correctly.
4. **Prefer workflows over agents** for well-understood tasks — agents introduce non-determinism; workflows do not.

---

## Observability

Production AI workflows require dedicated observability tooling beyond traditional APM. See [[concepts/ai-workflow-orchestration]] for the tool landscape. Key metrics: trace per LLM call, token cost per workflow run, tool call latency, faithfulness of retrieved context, task success rate.

---

## Cross-Domain Connections

- **RAG**: [[concepts/retrieval-augmented-generation]] is the retrieval component of an augmented LLM and is used in nearly every AI workflow that needs external knowledge.
- **MCP**: [[concepts/mcp-model-context-protocol]] is the standardised protocol layer through which AI workflows access tools and resources — MCP servers are the tool backends that workflow agents call.
- **Context compression**: [[concepts/context-compression-llm]] applies when workflow history or retrieved context exceeds the context window.

---

## Open Questions

- At what task complexity does the move from workflow to agent become justified, and how do you measure it?
- How will human-in-the-loop patterns standardise as AI workflows enter regulated industries (healthcare, finance, legal)?
- Can workflow reliability be formally verified, or will it always require empirical testing against real inputs?
