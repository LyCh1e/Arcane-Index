---
type: agent
title: "<% tp.file.title %>"
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
status: draft
tags:
  - agent
subagent_type: general-purpose
model: sonnet
isolation: none
run_in_background: false
domain: ""
related: []
---

# <% tp.file.title %>

## Purpose

> One sentence. What does this agent specialise in? What class of task does it handle better than the general-purpose agent?

[Define the agent's specialty precisely. A well-scoped agent outperforms a general one on its target task because the prompt is tailored, the tools are minimal, and the mental model is narrow.]

---

## When to Use This Agent

Use this agent when:

- [ ] [Condition 1 — e.g. "The task requires reading more than 5 files across the vault"]
- [ ] [Condition 2 — e.g. "The task is read-only and a narrow search scope is sufficient"]
- [ ] [Condition 3 — e.g. "The task can run in parallel with other work"]

Do **not** use this agent when:

- [ ] [Condition 1 — e.g. "The task requires writing to the vault — use a foreground agent instead"]
- [ ] [Condition 2 — e.g. "The goal is open-ended and requires judgment calls — handle inline"]
- [ ] [Condition 3 — e.g. "The result is needed before you can proceed — do not run in background"]

---

## Configuration

| Property | Value | Notes |
|---|---|---|
| `subagent_type` | `general-purpose` | See type options below |
| `model` | `sonnet` | See model options below |
| `isolation` | `none` | See isolation options below |
| `run_in_background` | `false` | See pacing guidance below |

### Subagent Types

| Type | Best for |
|---|---|
| `general-purpose` | Default — multi-step tasks with judgment calls |
| `Explore` | Read-only file/symbol search; fast, no writes |
| `Plan` | Architecture and implementation planning before writing code |
| `claude` | Catch-all; same as general-purpose |

### Model Tiers

| Model | When to use |
|---|---|
| `sonnet` | Default — most tasks; best cost/quality balance |
| `opus` | Complex multi-step reasoning; highest quality required |
| `haiku` | Fast, cheap lookups; simple structured tasks |
| `fable` | [Specialised — check current availability] |

### Isolation Modes

| Mode | Effect | When to use |
|---|---|---|
| `none` (default) | Agent works in the current repository | Read-only tasks; safe writes to the vault |
| `worktree` | Isolated git worktree; auto-cleaned if no changes | Risky writes; experimental changes |
| `remote` | Runs in a cloud environment | Always background; resource-intensive tasks |

### Background vs Foreground

| Mode | Use when |
|---|---|
| **Foreground** (`run_in_background: false`) | You need the result before continuing — research whose findings shape the next step |
| **Background** (`run_in_background: true`) | Genuinely independent work — you can continue while it runs; you will be notified when done |

---

## Tools Allowed

> List only what this agent genuinely needs. Fewer tools = smaller blast radius.

```
Read, Grep, Glob
```

> Common additions:
> - `Write, Edit` — if the agent produces vault output
> - `Bash` — if shell commands are needed
> - `WebFetch, WebSearch` — if research is required
> - `Agent` — only if this is an orchestrator spawning sub-agents

---

## Prompt Skeleton

> The standard prompt for invoking this agent. Fill in `[VARIABLES]` at call time.

```
[Agent's role statement — who it is and what it does]

[Context it needs to know at the start — which files to read, what state to pick up]

Goal: [GOAL]

Constraints:
- [Constraint 1]
- [Constraint 2]

Output: [What to produce and where to file it]

[Explicit scope boundary — what NOT to do]
```

---

## Briefing Rules

> Rules for writing the prompt when spawning this agent. The agent starts cold — it has no memory of the conversation.

1. **Always include the goal** — state it in the first or second sentence
2. **Name the files to read** — do not say "check the vault"; say "read `wiki/index.md` first, then drill into relevant concept pages"
3. **State what you've already ruled out** — prevents the agent from retreading ground
4. **Define the output** — file path, format, and whether to update index files
5. **Set the scope boundary** — "do not modify any existing content except the files listed"
6. **Cap the response** — if you only need a short report, say "report in under 200 words"

---

## Example Invocations

### Example 1 — [Scenario name]

```python
Agent(
    description="[3-5 word task description]",
    subagent_type="[type]",
    model="[model]",
    isolation="[mode]",
    run_in_background=[True/False],
    prompt="""
[Paste the filled-in prompt here — self-contained, includes file paths,
states what was already tried, defines the expected output format]
"""
)
```

### Example 2 — [Scenario name]

```python
Agent(
    description="[3-5 word task description]",
    subagent_type="[type]",
    prompt="""
[Second example — ideally showing a different configuration or use case]
"""
)
```

---

## State Handoff

> What this agent reads at the start and writes at the end, so the next agent (or you) can pick up where it left off.

| Direction | Artefact | Path | Contents |
|---|---|---|---|
| **Reads** | [e.g. Context file] | [path] | [what it contains] |
| **Reads** | [e.g. Index] | `wiki/index.md` | Vault catalogue |
| **Writes** | [e.g. Output note] | [path] | [what it produces] |
| **Writes** | [e.g. Log entry] | `wiki/log.md` | Session record |

---

## Failure Modes

| Failure | Detection | Recovery |
|---|---|---|
| Agent returns a summary instead of doing the work | Output is prose describing the plan, not artefacts | Re-prompt: "Do not describe what you will do — do it" |
| Agent modifies files it shouldn't | Diff shows unexpected changes | Use `isolation: worktree` next time |
| Agent runs too broadly (reads entire vault) | Slow, expensive, off-scope results | Narrow the prompt: name specific files to read |
| Background agent silently fails | No notification arrives | Check `TaskGet` for status; re-run in foreground |

---

## Composition Notes

> How this agent fits into larger workflows.

- **Runs after**: [e.g. `/autoresearch` to file findings into the vault]
- **Runs before**: [e.g. `/wiki-lint` to validate what was written]
- **Parallel with**: [e.g. another Explore agent searching a different area]
- **Orchestrated by**: [e.g. a general-purpose orchestrator that decomposes the task]

---

## See Also

- [[concepts/ai-workflows]] — the 5 core workflow patterns (prompt chaining, routing, parallelisation, orchestrator–workers, evaluator–optimiser)
- [[concepts/ai-workflow-orchestration]] — tool taxonomy and observability
- [[_templates/workflow-loop]] — if this agent runs inside a loop
- [[_templates/skill]] — if this agent is invoked by a skill
