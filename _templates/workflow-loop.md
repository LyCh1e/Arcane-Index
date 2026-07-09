---
type: workflow-loop
title: "<% tp.file.title %>"
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
status: draft
tags:
  - workflow-loop
domain: ""
agent: general-purpose
pattern: ""
complexity: medium
related: []
---

# <% tp.file.title %>

## Goal

> One sentence. What does this loop accomplish when it succeeds?

[Define the desired end-state precisely. The goal is the stopping condition's counterpart — the loop exits when this is achieved.]

---

## Pattern

> Which of the 5 Anthropic patterns does this loop implement?

- [ ] **Prompt Chaining** — sequential LLM steps, each processing prior output
- [ ] **Routing** — classifier dispatches input to a specialised handler
- [ ] **Parallelisation** — concurrent calls via sectioning or voting
- [ ] **Orchestrator–Workers** — central LLM decomposes and delegates
- [ ] **Evaluator–Optimiser** — generator + evaluator loop until quality threshold met

See [[concepts/ai-workflows]] for pattern details.

---

## Agent Configuration

| Property | Value |
|---|---|
| **Agent type** | `general-purpose` / `Explore` / `Plan` / `claude` |
| **Model** | `sonnet` / `opus` / `haiku` / `fable` |
| **Isolation** | `none` / `worktree` / `remote` |
| **Background** | `false` / `true` |

---

## Allowed Tools

List only what the loop genuinely needs. Fewer tools = smaller blast radius.

```
Read, Write, Edit, Glob, Grep, Bash
```

> Remove any tool not required. Do not include `Agent` unless this is an orchestrator loop.

---

## Loop Prompt

> The instruction that fires on every iteration. Must be self-contained — the agent starts cold each time.

```
<<paste or draft the repeating prompt here>>

Context carried between iterations:
- [State file / scratchpad path if needed]
- [What the agent should read first each wake-up]
- [What the agent should write at the end of each iteration]
```

---

## Iteration Logic

Step-by-step of what one iteration does:

1. **Read state** — [what file or context the agent reads at the start]
2. **Perform action** — [the core task of this iteration]
3. **Evaluate** — [how the agent self-assesses this iteration's output]
4. **Write state** — [what the agent updates before finishing]
5. **Signal continuation or exit** — [how the agent indicates whether to loop again]

---

## Stopping Condition

> When does the loop exit? Be specific — vague conditions lead to infinite loops.

| Condition | Exit type |
|---|---|
| [e.g. All files in `raw/pending/` processed] | Natural completion |
| [e.g. Quality score ≥ 0.85 on evaluator pass] | Success threshold |
| [e.g. 10 iterations reached with no improvement] | Safety cap |
| [e.g. User sends a message interrupting the loop] | Manual interrupt |

**Max iterations:** [N] (hard cap — always set one)

---

## State & Handoff

> What persists between iterations so the next cycle knows where it left off?

| Artefact | Path | Purpose |
|---|---|---|
| Progress file | [e.g. `.loop-state/progress.json`] | Tracks which items are done |
| Scratchpad | [e.g. `wiki/synthesis/loop-scratchpad.md`] | Accumulates findings across iterations |
| Output | [e.g. `wiki/concepts/...`] | Final deliverable being built incrementally |

---

## Pacing (ScheduleWakeup)

> Only fill this if using `/loop dynamic` mode with `ScheduleWakeup`.

| Scenario | Delay |
|---|---|
| Polling external state (CI, deploy, queue) | 60–270 s (stay in cache) |
| Idle between independent tasks | 1200–1800 s |
| Waiting on slow external system | Match external cadence |

**Reason string:** "[One sentence describing what the loop is waiting for — shown to user]"

---

## Expected Output

> What does a successful run produce?

- [ ] [Artefact 1 — e.g. updated wiki concept page]
- [ ] [Artefact 2 — e.g. summary report in `wiki/synthesis/`]
- [ ] [Artefact 3 — e.g. log entry in `wiki/log.md`]

---

## Failure Modes

> Common ways this loop can go wrong and how to detect them.

| Failure | Detection | Mitigation |
|---|---|---|
| Runaway loop (stopping condition never met) | Iteration count exceeds max cap | Hard cap + alert |
| State file corruption | Agent reads inconsistent state | Validate state at start of each iteration |
| Tool failure mid-loop | Bash/Write returns error | Check exit code; write partial state before erroring |
| Context drift (agent forgets goal) | Output diverges from goal | Re-state goal in every iteration prompt |

---

## Run Log

| Date | Iterations | Result | Notes |
|---|---|---|---|
| <% tp.date.now("YYYY-MM-DD") %> | — | — | First run |

---

## Lessons Learned

*(Append after each run)*

-

---

## See Also

- [[concepts/ai-workflows]] — the 5 core patterns (prompt chaining, routing, parallelisation, orchestrator–workers, evaluator–optimiser)
- [[concepts/ai-workflow-orchestration]] — tool taxonomy (LangGraph, Temporal, Dagster)
- [[skills/workflow-loop/SKILL.md]] — use `/workflow-loop` to generate a filled-in version of this template
