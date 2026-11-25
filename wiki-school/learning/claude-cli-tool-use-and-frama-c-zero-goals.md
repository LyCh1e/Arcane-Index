---
type: learning
title: "claude -p agent loops: tool_use exit 1, and a failed Frama-C run read as 0 goals"
domain: tooling
status: resolved
created: 2026-11-17
tags: [claude-cli, frama-c, agent-loop, ict3112, assignment2]
---

# claude -p tool_use failures and the 0-goal false "VERIFIED"

Context: ICT3112 Assignment 2 (AI verification loop), 18 benchmarks. See [[frama-c-wsl-install-gotchas]].

| Symptom | Cause | Fix |
|---|---|---|
| `claude -p ... --max-turns 1` exits with code 1, empty stderr, at random (about half the runs) | The model tried a tool call. With one turn the CLI stops with `stop_reason: "tool_use"` (`subtype: error_max_turns`) and the reason is on **stdout** JSON, not stderr | `--max-turns 3 --disallowed-tools "Bash,Read,Edit,Write,Glob,Grep,WebFetch,WebSearch,Task,Agent,Skill,NotebookEdit,TodoWrite,ToolSearch"`. `--tools ""` is dropped through the `.cmd` wrapper; `--tools <name>` was unreliable. Always log the JSON `result`/`stop_reason` on failure |
| Loop prints `VERIFIED` with `0/0 goals proved` | Frama-C aborted with a **multi-line** kernel error (`[kernel] file:16:` then `syntax error:`). The single-line regexes matched nothing, so "no errors, no goals" looked like success | A non-zero Frama-C exit must always be an error, with the output tail as the message. Also treat 0 total goals as failure |
| Annotator fails after exactly 600 s | Hard-coded agent timeout; a 400-line program needs 430-590 s for the first annotation | Make the timeout a config value |

Also learnt: a proved contract is not a correct program. 4 of 8 small benchmarks verified with a contract that encoded the seeded bug (`a[k] >= 0` added, `k + 2 < n`, first instead of last index, weak completeness). Compare the final contract with the English comment.

Update 2026-11-18: the timeout is now `claude.timeout` in `config.yaml` (1800 s; `agents.py` reads it, default 600). With it, the first annotation of L4 took 801 s and L2 580 s, so 600 s was too tight for 400-line programs. Final 18-benchmark result: 13 proved (8 level 1, 5 level 2), none of the 4 level 3 programs within 10 iterations.
