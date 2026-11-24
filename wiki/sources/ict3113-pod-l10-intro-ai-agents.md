---
type: source
title: "ICT3113 POD — L10: Introduction to AI Agents"
address: c-000145
domain: performance-engineering
source-type: lecture-slides
course: ICT3113
status: ingested
created: 2026-11-24
updated: 2026-11-24
tags: [ict3113, lecture, ai-agents, agent-harness, react, think-act-observe, tools, context, verification, ollama]
---

# Source: ICT3113 Lecture 10 — Introduction to AI Agents

**File:** `raw/ICT3113 Performance Optimisation and Design - Lec10 Introduction to AI Agents.md`
**Presenter:** A/Prof Donny Soh, ICT Cluster, Singapore Institute of Technology
**Type:** 25-slide lecture deck (footers read "n / 25")
**Concept pages:** [[concepts/agent-harness]] · related: [[concepts/ai-agent-architecture]]

> [!key-insight] One question drives the lecture
> How does a language model that only receives and produces text become an agent that can carry out tasks? Answer: **agent = model + harness**. Only the *think* step calls the model; acting, observing, checking and stopping are ordinary code.

---

## Summary

- A model on its own has four limits: **one call**, **no persistent memory**, **no actions**, **no feedback**.
- Who chooses the next step separates a **chatbot** (the user), a **workflow** (predetermined program logic) and an **agent** (the model). Claude Code is an agent.
- An agent is given a task and picks its own steps. A run ends with a checked result, a failure report, or a handover to a person.
- The loop is **think → act → observe → think again**, following ReAct (Yao et al., 2023).
- A harness has **six components**: agentic loop, tools, instructions, context and memory, environment, verification.
- Each component affects performance: model calls and run time, tool feedback and retries, tokens per call, context size, safety boundaries, reliability against extra work.
- Demo: the same small model (llama3.2 on Ollama) is asked for the p95 of a 5,000-row CSV. Alone it cannot open the file; inside a harness it finds **1,163.7 ms** in five steps.

## Slide guide

| Slide | Topic | Key content |
|---|---|---|
| 1–4 | Title, contents, outcomes, Part 1 divider | Five learning outcomes: model vs chatbot vs workflow vs agent; the loop; model vs harness; six components; trace one run |
| 5 | Model on its own | Text in, text out; cannot open files, apply a patch, run tests or see the result |
| 6 | Chatbot, workflow or agent | Table of who chooses the next step and who executes it |
| 7 | What an agent does | Given a goal not a list of steps; three ways a run ends; Schluntz and Zhang (2024) |
| 8 | Think, act, observe | Seven-step failing-test trace (10 → 1 → 0); the first fix was needed but not enough |
| 9 | Agent = model + harness | Table of which stage the model runs and which the harness runs; Trivedy (2026) |
| 10–11 | Part 2 divider; six components | Components placed against the loop; Meng et al. (2026, preprint) split a harness differently |
| 12 | The demo | llama3.2 in Ollama; `data/results.csv` (5,000 generated values); `bare.py` against `agent.py` |
| 13 | Run 1, model alone | Cannot access the file, invents column names, offers pandas code; right answer 1,163.7 ms |
| 14 | Run 2, in a harness | Five steps ending in a verified answer; a short Python program would do this faster |
| 15 | Open `agent.py` | Component-to-function map and a command to try for each |
| 16–21 | One slide per component | What it is, why it is needed, the demo, a failing-test example |
| 22 | One run step by step | Prompt tokens per step: 188, 248, 274, 340, 404 (1,454 total); only the *think* column is the model |
| 23 | Why the harness matters | Per-component effect on performance; same model, different harness |
| 24–25 | Summary, references | Five takeaways; seven references |

## Figures worth remembering

| Item | Figure |
|---|---|
| Demo answer | p95 of `response_ms` = 1,163.7 ms (4,750th of 5,000, nearest rank) |
| Step limit in the demo | 8 |
| Prompt tokens per step | 188, 248, 274, 340, 404 = 1,454 |
| Instruction-cost example (made-up numbers) | 1,500 tokens × 12 steps = 18,000; halving saves 9,000 |
| Failing-test trace | Expected \$90; got \$810, then \$81, then \$90 (pass) |

## Notes

- The data file is **generated for the lecture**, not measured, and the lecture says your run may take different steps.
- The slides say the task does not need an agent: a short program could compute the p95 without a model. The task is small so that each part is visible.
- The agent's folder check is "a simple example of access control", not a complete security sandbox.
- The deck predates the **Agentic AI Performance** planned topic in [[areas/performance-optimisation-design]]; it introduces the harness but does not yet measure agent loops under load.
