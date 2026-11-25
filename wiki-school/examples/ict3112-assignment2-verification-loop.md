---
type: example
status: established
title: "ICT3112 Assignment 2: AI-Assisted Verification Loop"
tags: [ict3112, frama-c, acsl, ai-agents, verification, python]
created: 2026-11-10
---

# ICT3112 Assignment 2: AI-Assisted Verification Loop

Python application that verifies C programs using Frama-C and AI agents (Claude via `claude -p`).

## Architecture

```
main.py                  # Entry point with CLI args
verifier/
  config.py              # YAML config loading
  c_parser.py            # tree-sitter C parsing (functions + marker comments)
  agents.py              # LLM agent calls via claude -p CLI
  frama_c.py             # Frama-C runner via WSL
  guards.py              # Guard checks (no axiom/admit, contracts unchanged)
  state.py               # JSON state persistence for resume
  loop.py                # Main verification loop orchestrator
prompts/
  describer.txt          # Describes functions without /*! marker
  annotator.txt          # Adds ACSL annotations
  repair.txt             # Fixes unproved goals
```

## Key Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Conversation mode | New per call | Self-contained, logged, no state leaks |
| Repair scope | All unproved goals at once | Better context for interdependent fixes |
| Program scope | Whole program to agents | Cross-function contracts need full view |
| C parsing | tree-sitter | Handles comments in strings, multi-line functions |
| Duplicate detection | SHA-256 hash | Prevents infinite oscillation |
| Agent tools | Disabled (--max-turns 1) | Frama-C always run by application |

## Marker

`/*!` — treated as ordinary C comment by Frama-C and gcc (unlike `/*@` which is ACSL).

## Running Frama-C from Windows Python

```python
cmd = ['wsl.exe', '-d', 'Ubuntu', '-e', 'bash', '-c',
       f'eval "$(opam env --switch=frama)" && frama-c {args}']
subprocess.run(cmd, ...)
```

Path conversion: `C:\foo\bar.c` → `/mnt/c/foo/bar.c`

## Agent Call Pattern

```python
cmd = [_resolve_command('claude'), '-p',
       'Answer the request given on standard input.',
       '--output-format', 'json', '--max-turns', '1']
proc = subprocess.run(cmd, input=message.encode(), capture_output=True)
# Outer JSON has 'result' field; parse inner JSON from that
```

## Guard Checks

1. No `admit`, `axiom`, `axiomatic` in program text
2. No new function declarations without body (strip comments first to avoid ACSL false positives)
3. Contracts unchanged unless decision is `fix_contract`
4. Contract comparison uses `frama-c -print -ocode` for normalization

## Verified Results

Figures from `logs/` and `workspace/state_*.json` (runs of 2026-11-10; time = state `start_time` to last log entry):

| Benchmark | Goals | Verification runs | Agent calls | Time (s) |
|---|---|---|---|---|
| `swap.c` | 11/11 | 1 | 1 | 12 |
| `max_value.c` | 8/8 | 1 | 1 | 13 |
| `copy_array.c` | 19/19 | 1 | 1 | 17 |
| `abs_value.c` | 11/11 | 1 | 2 (first annotation altered code, rejected) | 40 |
| `array_max.c` | 22/22 | 1 | 1 | 48 |
| `sum_bug.c` | 19/19 | 2 | 2 | 100 |

## Lessons

- **Verified does not mean correct.** In `sum_bug.c` (loop `i <= n`, comment "first n elements") the three unproved goals after annotation were signed-overflow goals, not the bug. The array-access goals were already proved, so the Annotator's first contract already required `\valid_read(a + (0 .. n))`, matching the loop instead of the comment. The Repair agent fixed overflow with `fix_contract` and the run ended at 19/19. Nothing in the loop compares contract with English comment except the user review, so a contract that matches the code produces no failing goal. The first report draft misattributed this to the repair agent adapting the contract to the bug.
- **Check report numbers against the logs.** The first draft's table for `swap`, `array_max` and `copy_array` (iterations, agent calls, times) did not match the saved logs; only `max_value`, `abs_value` and `sum_bug` did.
- **Coverage gap.** Every benchmark already had a `/*!` comment, so the Describer agent was never exercised.
