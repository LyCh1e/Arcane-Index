---
type: concept
title: Agent Harness (Agent = Model + Harness)
address: c-000146
domain: ai-engineering
complexity: medium
status: established
created: 2026-11-24
updated: 2026-11-24
sources:
  - ict3113-pod-l10-intro-ai-agents
tags:
  - ai-agents
  - agent-harness
  - react
  - think-act-observe
  - tools
  - context
  - verification
  - environment
  - ict3113
related:
  - "[[ai-agent-architecture]]"
  - "[[ai-workflows]]"
  - "[[mcp-model-context-protocol]]"
  - "[[context-compression-llm]]"
  - "[[ict3113-pod-l10-intro-ai-agents]]"
---

# Agent Harness (Agent = Model + Harness)

A language model takes text in and produces text out. It becomes an **agent** when code around it lets it act and see the results. That surrounding code is the **harness**: **agent = model + harness**. The model makes decisions; the harness manages execution, context, boundaries and completion. For production patterns, memory layers and evaluation, see [[ai-agent-architecture]].

## 1. Why a model alone is not an agent

| Limit | Meaning |
|---|---|
| One call | It gives one response and cannot start another call itself |
| No persistent memory | Anything relevant from earlier must be supplied again |
| No actions | It cannot run code, open a file or call an API |
| No feedback | It does not see what happened after it answered |

## 2. Chatbot, workflow or agent

| | Basic chatbot | AI workflow | AI agent |
|---|---|---|---|
| Given | A question | A task | A task |
| Who chooses the next step | The user | Predetermined program logic | The model |
| Who executes the action | The user | Software | Software |
| Several actions independently | No | Yes | Yes |
| How actions are selected | User instructions | Programmed rules | Model decisions from context |

A person sets the task and the limits; the agent decides how to do it within them. A run can end with a **checked result**, a **failure report** (it ran out of steps and says what it tried) or a **handover** to a person (the next action needs permission).

## 3. The think, act, observe loop

Following ReAct (thought, action, observation), each trip round the loop is one **step**:

| Stage | What happens | Run by |
|---|---|---|
| Task | Receive the task | Harness |
| Think | Interpret the context and choose the next action (as text, e.g. `edit_file("orders.py", 14, ...)`) | **Model** |
| Act | Carry out the action | Harness (no model call) |
| Observe | Capture the result and add it to the context | Harness |
| Finish | Stop and return the answer | Harness, after the model decides it is done or a limit is hit |

**Worked trace (failing test).** Run tests: expected \$90, got \$810. Read `orders.py`: `total = total * 10` on line 14. Fix it: tests now give \$81. Still wrong, so read `discount.py`, fix the discount, run again: \$90, pass. Seven steps; the model, not a programmer, chose to look at a second file after the first fix fell short.

## 4. The six components of a harness

| # | Component | Where in the loop | What it does | Demo (`agent.py`) |
|---|---|---|---|---|
| 1 | **Agentic loop** | The loop arrow | Calls the model repeatedly; stops on completion or a limit | `run_agent()`; step limit of 8 |
| 2 | **Tools** | Act | Actions the model can request: a description it reads plus code that runs | `list_files`, `read_file`, `percentile` |
| 3 | **Instructions** | Think | System prompt and rules sent at **every** call | `INSTRUCTIONS`: "Do not guess" |
| 4 | **Context and memory** | Observe | What is kept, shortened or looked up for the next step | `new_context()`, `memory.json` |
| 5 | **Environment** | Act | Where actions run and what they may reach | `DATA_DIR`, `safe_path()` |
| 6 | **Verification** | Think and Observe | Checks that the work is correct before accepting it | `collect_evidence()`, `verify()` |

The placement is a guide; some components span several stages. Other sources split a harness differently: Meng et al. (2026, preprint, not peer-reviewed) list an execution loop, tool registry, context manager, state store, lifecycle hooks and evaluation interface. [[ai-agent-architecture]] uses a four-block split (control loop, memory, tools, observability); the two are different cuts of the same machinery rather than a disagreement.

### Design points the lecture stresses

- **Tool results steer the next action.** `Error.` tells the model nothing; `Error: No column 'response_time'. Columns are: request_id, response_ms, status.` lets it correct itself. A higher step limit or a "do not repeat yourself" rule does not fix a weak result.
- **Instructions are input at every call.** Cost = instruction tokens × number of steps (made-up example: 1,500 × 12 = 18,000 tokens). Trim waste, not what guides the model.
- **Context is resent in full each call**, so it grows: prompts of 188, 248, 274, 340 and 404 tokens over five steps total 1,454. Too much means more tokens and slower calls; too little means the agent forgets what it did.
- **An enforced limit beats an instruction.** "Only read the data folder" may be ignored; a path check that rejects `../private/notes.txt` cannot be. The folder check is simple access control, not a full sandbox.
- **Verify against the harness's own record**, not by asking the model if it is sure. An answer of 450 with no percentile result is rejected; 1163.7 matching the tool result is accepted.

## 5. Why the harness matters for performance

| Component | What it can affect |
|---|---|
| Agentic loop | Number of model calls and total run time |
| Tools | Execution time, feedback quality, unnecessary retries |
| Instructions | Behaviour and input tokens per call |
| Context and memory | Context size, time per model call, resources used |
| Environment | Boundaries of what the agent can do: safety and control |
| Verification | Reliability, at the cost of some extra work |

The same model in a different harness can behave differently; a better harness helps it finish tasks more reliably with fewer wasted actions. Trade-offs are real: more verification costs time and buys reliability.

## 6. The demonstration

| | Model alone (`bare.py`) | In a harness (`agent.py`) |
|---|---|---|
| Model and question | llama3.2 on Ollama; "What is the p95 response time in `data/results.csv`?" | Same |
| Outcome | Cannot open the file, guesses column names, offers pandas code | 5 steps: wrong column, list files, read file, correct percentile, verified answer |
| Answer | None, or possibly a made-up number | **1,163.7 ms** (4,750th of 5,000 sorted, nearest rank) |

Only the harness changed. The file is generated for the lecture, and the lecture notes that a short Python program would do this faster; the point is to see every component.

## See also

- [[ai-agent-architecture]] — complexity spectrum, memory layers, evaluation, guardrails, production lessons
- [[ai-workflows]] — workflow versus agent
- [[mcp-model-context-protocol]] — standard interface for tools
- [[context-compression-llm]] — shrinking the context an agent resends each call
- [[ict3113-pod-l10-intro-ai-agents]]
