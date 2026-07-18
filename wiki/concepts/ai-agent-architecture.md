---
type: concept
address: c-000114
title: "AI Agent Architecture"
domain: ai-engineering
complexity: high
created: 2026-07-19
updated: 2026-07-19
tags: [concept, ai-agents, architecture, ReAct, memory, tools, guardrails, evals, production, orchestration]
related:
  - concepts/ai-workflows
  - concepts/ai-workflow-orchestration
  - concepts/mcp-model-context-protocol
  - resources/ai-agent-frameworks
  - synthesis/research-ai-agent-setup
---

# AI Agent Architecture

An **AI agent** is a system in which an LLM dynamically directs its own process — choosing what to do next, calling tools, observing results, and looping until a goal is met or a budget is exhausted. Unlike a workflow (predefined steps), an agent's execution path is determined at runtime.

---

## The Complexity Spectrum

Before building an agent, consider the minimum complexity required:

| Level | Description | When to use |
|---|---|---|
| **Direct model call** | Single LLM call with a good prompt | Classification, summarisation, one-pass tasks |
| **Single agent + tools** | One agent in a ReAct loop with tool access | Cross-query within one domain; the right default for enterprise use |
| **Multi-agent orchestration** | Specialised agents coordinated by an orchestrator | Cross-domain, parallel specialisation, distinct security boundaries |

> Start with a direct model call. Move up only when the current level demonstrably fails.

---

## 4 Building Blocks of Every Agent

### 1. Control Loop (the "brain")

A production agent is a deterministic **control loop** — not an unbounded chat:

```
Read state → Plan → Execute (tool call) → Observe result → Update state → Repeat
                                                                ↓
                                                     Halt when goal met or budget exhausted
```

State is a structured object (`AgentState`), not a chat log:

```json
{
  "goal": "...",
  "constraints": [...],
  "plan": [{ "id": "step1", "tool": "webSearch", "goal": "Find 3 sources" }],
  "steps": [],
  "memory": { "working": {}, "scratch": "", "long_term_ref": "..." },
  "policy": { "max_steps": 10, "forbidden_tools": [] }
}
```

> **State ≠ Chat history.** Structured state enables replay, debugging, and deterministic transitions.

### 2. Memory (4 Layers)

| Layer | Purpose | Storage | Lifetime |
|---|---|---|---|
| **Working** | Active reasoning; current task facts | State object | Single task |
| **Conversation** | Recent messages + rolling summary | Structured summaries | Session-bounded |
| **Task / Artefacts** | Decisions, outputs, links from this run | JSON + logs | Task-scoped |
| **Long-term** | User preferences, persistent facts | Structured DB | Persistent + audited |

**Vector retrieval fits:** documentation search, historical conversation recall.  
**Vector retrieval does NOT fit:** critical facts, permissions, financial transactions. Use structured DB.

> **Memory ≠ vector DB.** Use layered memory; add vector search only where semantic retrieval genuinely beats a structured query.

Popular memory frameworks: **Mem0**, **Letta** (cloud/self-hosted with core + archival + recall memory), **Amazon Bedrock AgentCore Memory**.

### 3. Tools (APIs with Contracts)

Tools are strict APIs — not free-form function calls. Each tool must define:

```
Input  : JSON Schema validated (typed, no free text)
Output : { ok: bool, data: ..., error: ..., meta: { latency, tokens } }
Side effects: idempotency key required
Budget : timeout, max retries, cost ceiling
```

> Don't let every agent have every tool. Scope tool access per agent per environment — smallest blast radius.

**ReAct pattern** (Reason + Act) — the standard planning loop:

```
Observation → [Think] Reason about what to do next
            → [Act]   Choose a tool and call it
            → [Observe] Receive tool result
            → Repeat until done or halted
```

Plans stored as **JSON structures** (not prose) enable re-planning mid-execution:

```json
{ "steps": [
    { "id": "search", "tool": "webSearch", "goal": "Find 3 credible sources" },
    { "id": "outline", "tool": null,        "goal": "Draft outline from sources" }
]}
```

### 4. Observability (Tracing)

Every step must emit a structured trace:

```json
{ "traceId": "...", "stepId": "2", "tool": "webSearch",
  "args_hash": "...", "duration_ms": 420,
  "result_summary": "...", "model": "claude-sonnet-4-5", "tokens": 812 }
```

This enables offline evaluation, replay, and cost accounting.

---

## Multi-Agent Orchestration Patterns

| Pattern | Also called | When to use |
|---|---|---|
| **Sequential** | Pipeline, prompt chaining | Linear dependencies; each step builds on previous output |
| **Concurrent** | Fan-out/fan-in, scatter-gather | Independent parallel analysis; results aggregated |
| **Supervisor** | Orchestrator–Workers | Dynamic task decomposition; one orchestrator delegates to specialists |
| **Network** | Peer-to-peer | Each agent communicates directly; avoid — unstructured, hard to debug |
| **Handoff** | — | One agent transfers full context to another; useful for domain transitions |

> **Avoid the network pattern in production.** Without a clear coordinator, agent-to-agent communication is unstructured, expensive, and unreliable.

**Supervisor example:**

```
User request
    ↓
Supervisor (decomposes task, delegates, verifies)
    ├──▶ Research Agent (searches, retrieves)
    ├──▶ Analysis Agent (processes findings)
    └──▶ Writer Agent (drafts output)
    ↓
Supervisor synthesises + returns
```

---

## Evaluation (Trajectory-Level)

Evaluate the **full trajectory**, not just the final output:

| Dimension | What to measure |
|---|---|
| **Task success** | Pass/fail with partial credit |
| **Tool correctness** | Right tool chosen; valid arguments; no unnecessary calls |
| **Trajectory quality** | Step count, latency, cost, retry frequency |
| **Safety / policy** | Forbidden tool detection, data leakage, injection resistance |

**Test harness pattern:** Use deterministic tool mocks in CI. Replay traces with fixed seed. Gate deployments on regression failures.

**LLM-as-judge:** Use only with structured rubrics and JSON output, with human auditing on samples.

Evaluation tools: **Langfuse** (open-source tracing), **LangSmith** (LangChain-native), **Maxim AI** (simulation + evals), **Galileo** (hallucination + guardrails), **Arize**, **DeepEval**, **Promptfoo**.

> **Evaluation ≠ optional.** Build your eval dataset (20–50 realistic cases) before shipping. Gate every deployment.

---

## Guardrails Checklist

| Control | What it does |
|---|---|
| **Capability gating** | Allowlist tools per environment (dev/staging/prod) |
| **Human-in-the-loop** | Require approval for irreversible actions (deletion, messaging, charges) |
| **Secrets boundary** | Never raw secrets in context; use short-lived tokens; redact outputs |
| **Prompt injection resilience** | Treat all retrieved/external content as untrusted; separate data from instructions |
| **Rate limiting + budgets** | Token, tool call, and cost ceilings per agent per run |
| **Sandboxing** | Restrict shell/browser tools; log all commands |
| **Policy-as-code** | Machine-readable policies enforced outside the LLM, not by the LLM |

---

## Production Deployment Patterns

| Pattern | Description | Use case |
|---|---|---|
| **Agent as Service** | `/run` + `/stream` API endpoints; agents are internal services | Product-facing assistants, customer tools |
| **Agent in Repo** | Local execution with git/shell/file tools | Developer productivity, coding agents |
| **Supervisor + Workers** | Decompose across specialist workers; supervisor integrates | Complex cross-domain tasks |

---

## 5 Production Lessons

| Lesson | What it means |
|---|---|
| **State ≠ Chat history** | Use reducers; chat logs aren't replayable or queryable |
| **Memory ≠ Vector DB** | Layer working → summaries → artefacts → structured DB; add vectors only where semantic search beats SQL |
| **Planning ≠ One perfect plan** | Iterate shallow plans from execution results; store as JSON, not prose |
| **Evaluation ≠ optional** | Measure trajectories in CI; gate on regressions |
| **Guardrails ≠ afterthought** | Design for failure modes before exposing to real systems, users, or money |

---

## MVP Build Order (1–2 Weeks)

1. Tool contracts + input/output validation
2. State reducer (deterministic transitions; no chat log)
3. Step-level tracing
4. Eval dataset (20–50 realistic cases) + CI harness
5. Policy gating + approval UI for irreversible actions
6. Memory layers (summaries + artefacts before adding vector search)

---

## See Also

- [[concepts/ai-workflows]] — workflow vs agent distinction; 5 Anthropic patterns
- [[concepts/ai-workflow-orchestration]] — LangGraph, Temporal, Prefect, n8n tooling
- [[resources/ai-agent-frameworks]] — LangGraph vs CrewAI vs Claude Agent SDK vs MAF 1.0 (2026 comparison)
- [[concepts/mcp-model-context-protocol]] — MCP for tool interoperability across agents
- [[synthesis/research-ai-agent-setup]] — research summary and open questions
