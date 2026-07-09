---
type: workflow
title: "<% tp.file.title %>"
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
status: draft
tags:
  - workflow
domain: ""
pattern: ""
complexity: medium
trigger: manual
runs: once
related: []
---

# <% tp.file.title %>

## Purpose

> One sentence. What does this workflow accomplish when it completes successfully?

[Define the end-state. Unlike a loop, this workflow runs **once** from trigger to completion — it does not repeat or iterate.]

---

## Pattern

> Which of the 5 Anthropic patterns does this workflow implement?

- [ ] **Prompt Chaining** — fixed sequence of LLM steps; each step's output is the next step's input
- [ ] **Routing** — a classifier step dispatches the input to one of several specialised downstream steps
- [ ] **Parallelisation (Sectioning)** — input is split into independent chunks; steps run concurrently and results are merged
- [ ] **Parallelisation (Voting)** — the same task is run multiple times in parallel; results are compared or voted on
- [ ] **Orchestrator–Workers** — a central step dynamically decomposes the task and delegates to worker steps; workers report back for synthesis

> Workflows use these patterns once. If you need the pattern to *repeat until a condition is met*, use `_templates/workflow-loop.md` instead.

See [[concepts/ai-workflows]] for pattern details and when to choose each.

---

## Trigger

> What starts this workflow?

- [ ] **Manual** — user explicitly invokes it (e.g. `/workflow-name` or a button in Obsidian)
- [ ] **Event** — triggered by an external event (e.g. a file appearing in `raw/`, a webhook, a CI result)
- [ ] **Scheduled** — runs on a cron schedule
- [ ] **Chained** — output of another workflow or skill triggers this one

**Trigger condition:** [Describe exactly what must be true for the workflow to start]

**Input artefacts:** [What files, parameters, or data must exist before the workflow can run]

---

## Steps

> Each step is atomic. Define what it receives, what it does, and what it produces. Steps hand off to each other via artefacts — not via shared memory.

### Step 1 — [Name]

| Property | Value |
|---|---|
| **Agent** | `general-purpose` / `Explore` / `Plan` / `claude` / inline |
| **Model** | `sonnet` / `opus` / `haiku` |
| **Runs in background** | `false` / `true` |
| **Isolation** | `none` / `worktree` |

**Input:** [What this step receives — file path, data format, prior step's output]

**Action:** [What this step does — one clear unit of work]

**Output:** [What this step produces and where it writes it]

**Prompt sketch:**
```
[Draft the prompt for this step — self-contained; names the input artefact,
describes the task, specifies the output format and file path]
```

---

### Step 2 — [Name]

| Property | Value |
|---|---|
| **Agent** | |
| **Model** | |
| **Runs in background** | |
| **Isolation** | |

**Input:** [Output of Step 1 / path / format]

**Action:**

**Output:**

**Prompt sketch:**
```
[Step 2 prompt]
```

---

### Step 3 — [Name]  *(add or remove steps as needed)*

| Property | Value |
|---|---|
| **Agent** | |
| **Model** | |
| **Runs in background** | |
| **Isolation** | |

**Input:**

**Action:**

**Output:**

**Prompt sketch:**
```
[Step 3 prompt]
```

---

## Data Flow

> Map how artefacts move between steps. Every step should read from a named path and write to a named path — no implicit shared state.

```
[Trigger input]
       │
       ▼
  ┌─────────┐
  │ Step 1  │ ──writes──▶ [artefact-1-path]
  └─────────┘
                               │
                               ▼
                          ┌─────────┐
                          │ Step 2  │ ──writes──▶ [artefact-2-path]
                          └─────────┘
                                          │
                                          ▼
                                     ┌─────────┐
                                     │ Step 3  │ ──writes──▶ [final-output-path]
                                     └─────────┘
```

> For parallel branches, show them side by side converging at a merge step.

---

## Branching Logic  *(remove if not applicable)*

> If the workflow has conditional paths (routing pattern), define the decision rules here.

| Condition | Branch taken |
|---|---|
| [e.g. Input is a URL] | → Step 2A: WebFetch |
| [e.g. Input is a local file] | → Step 2B: Read |
| [e.g. Neither] | → Abort with message to user |

---

## Parallelisation  *(remove if not applicable)*

> If steps run concurrently, define which steps can run in parallel and how their outputs are merged.

**Steps that can run in parallel:** Step [N], Step [M]
**Merge step:** Step [X] — receives outputs from both and combines them into [merged artefact]
**Merge strategy:** [e.g. concatenate, vote, synthesise with an LLM step]

---

## Completion Definition

> How do you know the workflow has finished successfully? Unlike a loop, there is no stopping condition — the workflow terminates when the final step produces its output.

**Done when:** [e.g. "Step 3 has written `wiki/synthesis/[topic].md` and updated `wiki/index.md`"]

**Final output artefacts:**
- [ ] [Artefact 1 — path + format]
- [ ] [Artefact 2 — path + format]
- [ ] [Artefact 3 — path + format]

---

## Error Handling

> What happens if a step fails? Define the recovery path for each step.

| Step | Failure mode | Recovery |
|---|---|---|
| Step 1 | [e.g. Input file missing] | [e.g. Halt and notify user with missing path] |
| Step 2 | [e.g. WebFetch returns 404] | [e.g. Skip and continue with partial data; flag in output] |
| Step 3 | [e.g. Write fails due to permissions] | [e.g. Write to temp path and notify user] |

**On unrecoverable error:** [e.g. "Halt, write partial output to `wiki/synthesis/[topic]-partial.md`, notify user of the last completed step"]

---

## Integration Points

> How this workflow connects to other skills, workflows, or external systems.

| Integration | Type | Notes |
|---|---|---|
| [e.g. `/autoresearch`] | Predecessor — feeds input | [Run autoresearch first; this workflow processes the output] |
| [e.g. `wiki-lint`] | Successor — validates output | [Run lint after this workflow completes] |
| [e.g. GitHub Actions] | External trigger | [CI result triggers Step 1] |

---

## Failure vs Loop Distinction

> Sanity check — confirm this is a workflow, not a loop.

- [ ] This workflow runs **once** per trigger — it does not retry or re-execute steps automatically
- [ ] There is no "stopping condition" — the workflow ends when the final step completes
- [ ] No `ScheduleWakeup` is needed — steps execute sequentially without pausing for external state
- [ ] If any of the above is false → use `_templates/workflow-loop.md` instead

---

## Run Log

| Date | Duration | Steps completed | Result | Notes |
|---|---|---|---|---|
| <% tp.date.now("YYYY-MM-DD") %> | — | 0 / [N] | — | First run |

---

## See Also

- [[_templates/workflow-loop]] — use instead if the workflow needs to repeat until a condition is met
- [[_templates/agent]] — for documenting each step's agent configuration in detail
- [[_templates/skill]] — if this workflow is invoked by a skill
- [[concepts/ai-workflows]] — the 5 core patterns with decision guide
- [[concepts/ai-workflow-orchestration]] — tool choices (LangGraph, Temporal, Dagster) for productionising workflows
