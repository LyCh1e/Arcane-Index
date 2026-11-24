# Lecture 10: Introduction to AI Agents

ICT3113 Performance Optimisation and Design

Presented by A/Prof Donny Soh
Programme Leader, Applied Artificial Intelligence
Programme Leader, SITxNVIDIA (SNAIC) AI Training
InfoComm Technology (ICT) Cluster
Singapore Institute of Technology

*Diagrams are described in italics inside square brackets. Slide numbers match the printed footers (n / 25).*

---

## Slide 1: Title

INTRODUCTION TO AI AGENTS
Lecture 10

---

## Slide 2: Contents

**The question for this lecture**

How does a language model that only receives and produces text become an AI agent that can carry out tasks?

**1. Understanding AI agents**
A language model on its own. Chatbot, workflow or agent. What an AI agent does. The think, act, observe loop. Agent = model + harness.

**2. Understanding the harness**
The six components of a harness. A demonstration you can run. What each component does and why it is needed. One run of the agent, step by step. Why the harness matters for performance.

*(Footer: 2 / 25)*

---

## Slide 3: Learning outcomes

By the end of this lecture, you should be able to:

1. Explain the differences between a language model on its own, a chatbot, an AI workflow and an AI agent.
2. Describe how an AI agent works through the think, act, observe loop.
3. Distinguish between what the model does and what the harness does.
4. Explain the purpose of the six components of a harness.
5. Trace and explain one run of a simple AI agent.

*(Footer: 3 / 25)*

---

## Slide 4: Part 1 of 2: Understanding AI agents

*(Section divider repeating the contents slide, with Part 1 highlighted.)*

1. Understanding AI agents: A language model on its own. Chatbot, workflow or agent. What an AI agent does. The think, act, observe loop. Agent = model + harness.
2. Understanding the harness: The six components of a harness. A demonstration you can run. What each component does and why it is needed. One run of the agent, step by step. Why the harness matters for performance.

*(Footer: 4 / 25)*

---

## Slide 5: A language model on its own takes text in and produces text out

*[Diagram: Prompt (text in) → Model → Answer (text out).]*

**Example task**

Fix the failing test in this repository.

**What the model can do**

Write a patch, as text, from whatever code was pasted into the prompt.

**What the model cannot do**

Open the files. Apply the patch. Run the tests. See whether the tests now pass.

### Four limits of a model on its own

1. **One call.** It gives one response. It cannot start another call by itself.
2. **No persistent memory.** Relevant information from earlier interactions must be provided to the model.
3. **No actions.** It cannot run code, open a file or call an API.
4. **No feedback.** It does not see what happened after it answered.

*(Footer: 5 / 25)*

---

## Slide 6: Chatbot, workflow or agent: who chooses the next step?

| | Basic chatbot | AI workflow | AI agent |
|---|---|---|---|
| Given | A question | A task | A task |
| Who chooses the next step? | The user | Predetermined program logic | The model |
| Who executes the action? | The user | Software | Software |
| Can it take multiple actions independently? | No | Yes | Yes |
| How are actions selected? | User instructions | Programmed rules | Model decisions based on context |

Claude Code, used in the labs, is an agent.

*(Footer: 6 / 25)*

---

## Slide 7: An AI agent is given a task and chooses its own steps

It is given a goal, not a list of steps. This slide is what that means. The next slide is how it works.

**1. It is given a task**

Fix the failing test in this repository.
A person sets the task. The agent does not choose its own goal.

**2. It chooses its own steps**

*[Boxes: Read a file, Edit a file, Run the tests.]*
It is not given a full list of steps. These are the actions it can take. It selects its next action.

**3. Examples of how a run can end**

- **A checked result:** The tests pass.
- **A failure report:** It ran out of steps. This is what it tried.
- **A handover to a person:** The next action needs permission.

**Key point.** The person sets the task and the limits. The agent decides how to do it within those limits.

**Source.** Schluntz, E., & Zhang, B. (2024). Building Effective Agents. Anthropic. In an agent, the model directs its own process and its own use of tools.

*(Footer: 7 / 25)*

---

## Slide 8: How an agent works: think, act, observe, and think again

This is the last slide again, with the middle box opened up. One trip round the loop is one step.

*[Diagram: TASK (Given a task) → THINK (Model chooses the next action) → ACT (one of these is carried out: Read a file, Edit a file, Run the tests, Search the code) → OBSERVE (The result is captured) → back to THINK. FINISH (The result is returned) is reached when the model is done, or when the harness says stop.]*

### Seven steps on the task: fix the failing test in this repository

| Step | Think | Act | Observe |
|---|---|---|---|
| 1 | Run the tests. | Tests are run. | Expected $90, got $810. |
| 2 | Read the code for test_total. | orders.py is opened. | Line 14: total = total * 10 |
| 3 | Fix line 14. | orders.py is edited. | The edit is made. |
| 4 | Run the tests to check the fix. | Tests are run. | Expected $90, now got $81. |
| 5 | Still wrong. Read discount.py. | discount.py is opened. | Discount on lines 8 and 21. |
| 6 | Fix the discount. | discount.py is edited. | The edit is made. |
| 7 | Run the tests to check the fix. | Tests are run. | Expected $90, got $90. Pass. |

Steps 4 and 5. The fix to line 14 took $810 to $81. It was needed, but it was not enough. At step 5 a different file is opened.

The loop follows ReAct (Yao et al., 2023): thought, action, observation.

**Pause and answer.** The first fix was not enough. Who decided what to look at next? Did a programmer have to plan for this failure?

*(Footer: 8 / 25)*

---

## Slide 9: Agent = model + harness

The harness is all the code around the model. Only think is a call to the model. The rest is harness code.

*[Diagram: Task (given by a person) → Think (decide the next action) → Act (carry out the action) → Observe (capture the result) → "not finished: think again" back to Think. Finish (return the result) happens "when the model is done or when the harness says stop". Colour key: input from a person, received by the harness; Model; Harness code.]*

| Stage | Description | Executed by | Example: the model wants to change line 14 of orders.py |
|---|---|---|---|
| Task | Receive the task. | Harness | "Fix the failing test in this repository." |
| Think | Interpret the context and decide the next action. | Model | Replies with text: `edit_file("orders.py", 14, "total = total")` |
| Act | Carry out the action. | Harness | Opens orders.py, replaces line 14 and saves it. No model is called. |
| Observe | Capture the result and update the context. | Harness | Captures "The edit is made." and adds it to the context. |
| Finish | Stop and return the final response. | Harness | Not yet. The tests have not been run, so the loop goes round again. |

Observe: the harness captures the test output. Think again: the model interprets that output and decides what to do next. Deciding that the task is complete also happens in a think step. The harness then stops the loop and returns the answer.

**Source.** Trivedy, V. (2026). The Anatomy of an Agent Harness. LangChain.

*(Footer: 9 / 25)*

---

## Slide 10: Part 2 of 2: Understanding the harness

*(Section divider repeating the contents slide, with Part 2 highlighted.)*

1. Understanding AI agents: A language model on its own. Chatbot, workflow or agent. What an AI agent does. The think, act, observe loop. Agent = model + harness.
2. Understanding the harness: The six components of a harness. A demonstration you can run. What each component does and why it is needed. One run of the agent, step by step. Why the harness matters for performance.

*(Footer: 10 / 25)*

---

## Slide 11: One way to split a harness: six components

One useful way to organise a harness. Each component has a main place in the loop.

*[Diagram: the loop Task (given by a person) → Think (decide the next action) → Act (carry out the action) → Observe (capture the result) → Finish (return the result), with the six components placed against it: 1 Agentic loop (at the loop arrow), 2 Tools (at Act), 3 Instructions (at Think), 4 Context and memory (at Observe), 5 Environment (at Act), 6 Verification (at Think and Observe).]*

1. **Agentic loop** (at the loop arrow): Runs the model again and again: think, act, observe. Stops when the task is done or a limit is reached.
2. **Tools** (at Act): The actions the model can ask for. Each tool is a description the model reads, plus code that runs.
3. **Instructions** (at Think): The system prompt and rules. They are sent to the model at every step.
4. **Context and memory** (at Observe): What is kept, shortened or looked up, so the model has what it needs for the next step.
5. **Environment** (at Act): Where the actions run. Usually a sandbox or a copy of the repository.
6. **Verification** (at Think and Observe): Tests and other checks that say whether the work is correct.

The placing is a guide. Some components work across several stages.

**Source.** Sources split a harness in different ways. Meng et al. (2026, preprint, not peer-reviewed) use six different components: execution loop, tool registry, context manager, state store, lifecycle hooks, evaluation interface. doi:10.20944/preprints202604.0428

*(Footer: 11 / 25)*

---

## Slide 12: One demo you can run: a small local model is asked for the p95 in a results file

**The task**

"What is the p95 response time, in milliseconds, in the file data/results.csv?"
One question about one file.

**The model**

llama3.2, running in Ollama. A small model that runs on a laptop. Any small model will do.

**The file**

data/results.csv: 5,000 response times. Generated for this lecture, not measured.

**Pause and answer.** Before the next slide: what do you expect the model to do with this question on its own?

### Two runs, the same model and the same question

1. **The model on its own:** `python bare.py`. The model is sent the question and nothing else.
2. **The same model inside a harness:** `python agent.py`. The complete agent, with the six components from the last slide.

Only the harness changes. If run 2 does better than run 1, it is not because of a better model or a better question.

**Code.** The harness-demo folder: bare.py, agent.py, check_harness.py and two helper files. It needs Python and Ollama, and no other packages.

*(Footer: 12 / 25)*

---

## Slide 13: Run 1, the model on its own: it cannot open the file

**What the model is sent**

"What is the p95 response time, in milliseconds, in the file data/results.csv?"

The name of the file is in the question. The file is not.

**What it cannot do**

- Open data/results.csv.
- Sort 5,000 numbers it has never seen.
- Check its own reply against the file.

**Pause and answer.** Would a bigger, better model get the right number from this question alone?

**What llama3.2 replied (`python bare.py`)**

- "I can't directly access external files or databases."
- It then told me to open the file in a spreadsheet myself.
- It guessed column names such as "p95_response_time". There is no such column.
- It offered some pandas code for me to run.

The task is not done. Another run, or another model, may give a made-up number instead.

**The right answer.** The p95 in the file is 1,163.7 ms: sort the 5,000 values and take the 4,750th (nearest rank). Any other number in the reply was made up.

*(Footer: 13 / 25)*

---

## Slide 14: Run 2, the same model inside a harness: the answer comes from the file

**A run on llama3.2 (`python agent.py`). Your run may take different steps.**

```
[1] percentile("data/results.csv", "response_time", 95)
    Error: No column 'response_time'. Columns are: request_id, ...
[2] list_files
    Files in data: results.csv
[3] read_file("data/results.csv")
    5000 data rows. First lines: request_id,response_ms,status ...
[4] percentile("data/results.csv", "response_ms", 95)
    p95 of response_ms = 1163.7 (row 4750 of 5000 when sorted)
[5] answer 1163.7
    verify: accepted, it matches a tool result
ANSWER: 1163.7 ms   steps: 5
```

**The same in both runs:** The model. The question.

**Different:** In run 2 the model is inside a harness.

**Pause and answer.** The model has not changed. What has been added that lets it complete the task?

Does this task need an agent? No. A short Python program could work out this p95 faster, with no model. The task is small on purpose, so that every part of an agent is easy to see. The next slides open this agent up, one component at a time.

*(Footer: 14 / 25)*

---

## Slide 15: Open agent.py: the six components are in the file, in the same order

The file follows the lecture: the same six names, in the same order.

| Component | In agent.py | What it does there | A command to try |
|---|---|---|---|
| 1 Agentic loop | `run_agent()` | Think, act, observe, as a loop. | `python agent.py --steps 1` |
| 2 Tools | `list_files()` `read_file()` `percentile()` `execute_tool()` | The actions, and what each one sends back. | `python agent.py --weak-tools` |
| 3 Instructions | `INSTRUCTIONS` | The text sent to the model at every step. | (read the text in the file) |
| 4 Context and memory | `new_context()` `add_to_context()` `memory.json` | The messages the model is sent. Notes kept between runs. | `python agent.py --memory` |
| 5 Environment | `DATA_DIR` `safe_path()` | Only files in the data folder can be read. | `python check_harness.py` |
| 6 Verification | `collect_evidence()` `verify()` | The answer is checked before it is accepted. | `python agent.py --no-verification` |

One line runs the language model: `response = call_model(model, context)`. Everything else in the file is ordinary Python.

*(Footer: 15 / 25)*

---

## Slide 16: Agentic loop: the code that calls the model again and again

*[Loop strip: Task, Think, Act, Observe, Finish, with component 1 (Agentic loop) highlighted at the loop arrow and the other components marked in place.]*

**What it is**

The code that runs the agent. It calls the model, carries out the action the model asks for, returns the result, and repeats.

**Why it is needed**

A model answers once. Something has to call it again with the result, and something has to stop the run.

**In our demonstration**

- Each step is one model call and one tool call.
- The run stops on an accepted answer, or at the step limit of 8.
- The step limit stops the agent from running for ever.

**From agent.py: run_agent(), with the print lines left out**

```python
for step in range(1, step_limit + 1):
    # THINK
    response = call_model(model, context)
    if response.is_final_answer:
        accepted, result = verify(response.value, evidence)
        if accepted:
            return finish(response.value)
    else:
        # ACT
        result = execute_tool(response.tool_call)
        # OBSERVE
        add_to_context(context, response, result)
```

Only `call_model()` runs the language model. The rest is ordinary Python.

**In the failing-test example.** Each of the seven steps was one trip round this loop: the model chose an action, the harness carried it out, and the result went back to the model. Claude Code runs the same kind of loop.

*(Footer: 16 / 25)*

---

## Slide 17: Tools: how the model reaches the outside world

*[Loop strip with component 2 (Tools) highlighted at Act.]*

**What it is**

A tool has three parts: a description the model reads, code that does the work, and a result that is sent back to the model.

**Why it is needed**

The model can only read and write text. Tools are the only way it can open a file or run a calculation.

**In our demonstration**

- Three tools: list_files, read_file and percentile.
- percentile sorts the column in code. The model does not do the sum.
- The result text is all the model sees of the file.

### The result is what the model uses to decide its next action

In the run on llama3.2, the model asked for a column that is not in the file:

`percentile("data/results.csv", "response_time", 95)`

| A generic error | An informative error |
|---|---|
| `Error.` | `Error: No column 'response_time'. Columns are: request_id, response_ms, status.` |

With the informative error, the model can choose a better next action.

**In the failing-test example.** A test tool that returns only "Failed" tells the model little. One that returns the failing test, the expected value and the actual value lets it choose the next step. A higher step limit, or a rule saying "do not repeat yourself", does not fix a weak result. The tool has to say what went wrong.

*(Footer: 17 / 25)*

---

## Slide 18: Instructions: text that guides what the model does

*[Loop strip with component 3 (Instructions) highlighted at Think.]*

**What it is**

Text the harness sends to the model with every call. It is often called the system prompt.

**Why it is needed**

Without instructions the model does not know its role, which tools exist, or when to stop. In run 1 it could only guess.

**Instructions can tell the model**

1. What its role is.
2. What tools are available.
3. How to use those tools.
4. What rules it should follow.
5. When it should give a final answer.

**In our demonstration: part of the instructions**

```
You are an agent that answers questions about
files in the data folder.
You cannot see the files yourself. You must use tools.
...
Do not guess. Every number in your answer must
come from a tool result.
```

- **Generic:** "Answer the question."
- **Specific:** "Use the available tools to obtain evidence before answering. Do not guess numerical results."

**Performance.** Instructions are part of the input at every model call. For example, with made-up numbers: 1,500 tokens of instructions over a run of 12 steps is 1,500 × 12 = 18,000 tokens. Halve the instructions and the run sends 9,000 fewer tokens. Their first job is still to guide the model, so do not cut what it needs.

*(Footer: 18 / 25)*

---

## Slide 19: Context and memory: what the model is given at each call

*[Loop strip with component 4 (Context and memory) highlighted at Observe.]*

**What it is**

Context is the information the model is given in its current call. Memory is information the system keeps and can give to the model when needed.

**Why it is needed**

The model remembers nothing between calls. To know what has already happened, it has to be sent that again.

**In our demonstration**

- read_file sends back the row count and the first four lines.
- The 5,000 rows are never sent to the model.
- Memory: `--memory` keeps a note of the column names for the next run.

### How the context grows across model calls

| Call | Context sent |
|---|---|
| Call 1 | Instructions, Task |
| Call 2 | Instructions, Task, Action 1, Result 1 |
| Call 3 | Instructions, Task, Action 1, Result 1, Action 2, Result 2 |

The model is sent all of this again at every call. That is how it knows what has already happened.

In the run on llama3.2, the prompt was 188, 248, 274, 340 and 404 tokens over the five steps: 1,454 in total.

**Performance.** Everything in the context is sent again at every call. Keeping information the model does not need means more tokens and slower calls. Keeping too little means the agent forgets what it has already done.

*(Footer: 19 / 25)*

---

## Slide 20: Environment: where the tools run and what they can reach

*[Loop strip with component 5 (Environment) highlighted at Act.]*

**What it is**

Where the agent's tools run, and what they are allowed to reach. In our demonstration: one folder, read only.

**Why it is needed**

An instruction tells the model what it should not do. An enforced restriction prevents the action from being carried out.

### A request and a limit

- **Instruction:** "Only read files in the data folder." The model may not comply.
- **Environment:** The harness checks every file path and rejects a request outside the folder.

**In our demonstration: a request outside the folder**

The model asks for a file outside the data folder:

`read_file("../private/notes.txt")`

What the harness sends back:

```
Error: '../private/notes.txt' is outside
the data folder. You can only read files
in data.
```

The file is not opened. The model is told why, so it can carry on with the task.

**In Claude Code.** Permissions decide which files it can change and which commands it can run. Our folder check is a simple example of access control. It is not a complete security sandbox.

*(Footer: 20 / 25)*

---

## Slide 21: Verification: the harness checks before it accepts the answer

*[Loop strip with component 6 (Verification) highlighted at Think and Observe.]*

**What it is**

A check the harness makes before it accepts that the task is done.

**Why it is needed**

The model saying it is done does not mean the work is correct. In run 1 it gave a number that never came from the file.

### The answer is accepted only if the evidence matches

| Evidence field | Required |
|---|---|
| File | results.csv |
| Column | response_ms |
| Percentile | 95 |
| Value | the answer equals the number the tool returned |

**In our demonstration (`python check_harness.py`)**

1. An answer of 450 arrives. No tool has been called yet.
2. Rejected: no percentile result supports the answer.
3. The percentile tool is called. It returns 1163.7.
4. An answer of 1163.7 arrives. It matches. Accepted.

The harness checks its own record. It does not ask the model if it is sure.

**In the failing-test example.** The model claims the code is fixed. The harness runs the tests itself. If they fail, the result goes back to the model for another try. A claim of success is not the same as evidence of success.

*(Footer: 21 / 25)*

---

## Slide 22: One run, step by step: what the model does and what the harness does

The run on llama3.2: 5 steps, 1,454 prompt tokens in total. Your run may take different steps.

| Step | The model is sent | Think: the model decides | Act: the harness does | Observe: the result | Then |
|---|---|---|---|---|---|
| 1 | The instructions and the task. 188 tokens. | `percentile("data/results.csv", "response_time", 95)` | Runs the tool. There is no such column. | Error: No column 'response_time'. Columns are: request_id, response_ms, status. | Added to the context. No answer yet: go round again. |
| 2 | The same, plus step 1. 248 tokens. | `list_files` | Lists the data folder. | Files in data: results.csv | Added to the context. |
| 3 | The same, plus step 2. 274 tokens. | `read_file("data/results.csv")` | Opens the file. Returns the row count and four lines. | 5000 data rows. First lines: request_id,response_ms,status ... | Added to the context. |
| 4 | The same, plus step 3. 340 tokens. | `percentile("data/results.csv", "response_ms", 95)` | Sorts 5,000 values and takes the 4,750th. | p95 of response_ms = 1163.7 | Added. Recorded as evidence. |
| 5 | The same, plus step 4. 404 tokens. | `answer 1163.7` | Runs the check: file, column, percentile, value. | Accepted. It matches the evidence. | Stop. Return 1163.7 ms. |

Which operations involve the model? Only the think column. Sending the context, running the tools, recording the results, checking the answer and stopping the run are all done by the harness.

**Pause and answer.** After the error at step 1, the model listed the files and read the file before it tried again. Was that order written in the harness code?

*(Footer: 22 / 25)*

---

## Slide 23: Why does the harness matter for performance?

Each component of the harness affects how the agent performs.

| Component | What it can affect |
|---|---|
| 1 Agentic loop | The number of model calls, and the total time a run takes. |
| 2 Tools | Execution time, the quality of the feedback, and unnecessary retries. |
| 3 Instructions | What the model does, and the input tokens used at every call. |
| 4 Context and memory | The size of the context, the time each model call takes, and the resources used. |
| 5 Environment | The boundaries of what the agent can do: safety and control. |
| 6 Verification | Reliability, at the cost of some extra work. |

**The same model, a different harness.** Two agents that use exactly the same model can behave differently, because their harnesses are designed differently. A better harness can help the same model complete tasks more reliably, with fewer unnecessary actions.

There are trade-offs. For example, more verification takes more time and makes the result more reliable.

*(Footer: 23 / 25)*

---

## Slide 24: Summary

1. **A language model on its own receives text and produces text.** It cannot interact with anything outside itself.
2. **An AI agent is given a goal and selects its actions.** It chooses each action from the information available to it.
3. **An agent can work through a repeated think, act, observe loop.** Each trip round the loop is one step.
4. **Agent = model + harness.** The model makes the decisions. The harness manages execution, context, boundaries and completion.
5. **The design of the harness affects what the agent can do.** It also affects how reliably the agent works, and how much time and how many tokens it uses.

*(Footer: 24 / 25)*

---

## Slide 25: References

1. Kumar, T. (2026). Harnesses in AI: A Deep Dive. IBM, at AI Engineer. youtube.com/watch?v=C_GG5g38vLU. (Another demo of the same idea: a weak model, a browser task, and a harness improved step by step.)
2. Trivedy, V. (2026). The Anatomy of an Agent Harness. LangChain. langchain.com/blog/the-anatomy-of-an-agent-harness. (Agent = model + harness.)
3. Schluntz, E., & Zhang, B. (2024). Building Effective Agents. Anthropic. anthropic.com/research/building-effective-agents. (Workflows and agents.)
4. Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. ICLR 2023. arXiv:2210.03629. (The think, act, observe loop.)
5. Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. NeurIPS 2024. arXiv:2405.15793. (How tool design changes agent results.)
6. Anthropic (2025). Effective Context Engineering for AI Agents. anthropic.com/engineering/effective-context-engineering-for-ai-agents
7. Meng et al. (2026, preprint, not peer-reviewed). Agent Harness for Large Language Model Agents: A Survey. doi:10.20944/preprints202604.0428

*(Footer: 25 / 25)*
