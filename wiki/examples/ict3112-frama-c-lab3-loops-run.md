---
type: example
title: "ICT3112 Frama-C Lab 3 — Loops: Run Results and Tested Failure Claims"
domain: formal-verification
course: ICT3112
created: 2026-11-03
updated: 2026-11-03
tags: [frama-c, acsl, wp, loop-invariants, loop-assigns, loop-variant, termination, behaviors, lab]
---

# Lab 3 Loops: run results (Frama-C 33.0, Alt-Ergo 2.6.4, WSL Ubuntu)

Slides: [[sources/ict3112-frama-c-lab3-loops]]. Theory: [[concepts/loop-invariants]]. Files: `Labs/lab3/lab3-examples 2/`. Command per file: `frama-c -wp -wp-rte -wp-cache none file.c`, default 2 s timeout, on throwaway copies so no `.frama-c` folder lands in the labs.

## Examples: all match the README

| File | Slides | Proved | Not proved |
|---|---|---|---|
| loop1.c | 2–3 | 5/6 | terminates |
| loop2.c | 7–8 | 5/7 | `assert h == 42`, terminates |
| loop3.c | 9 | 7/8 | terminates |
| loop4.c | 10 | 8/9 | terminates |
| loop5.c | 13–14 | **10/10** | |
| sar1.c | 17 | 1/4 | 2 `rte_mem_access`, terminates |
| sar2.c | 18–20 | 16/18 | invariants 2 and 3 preserved |
| sar3.c | 21 | **20/20** | |
| find.c | 30 | **18/18** | |
| find_incomplete.c | 31 | 17/18 | `complete_found_not_found` |
| find_overlap.c | 31 | 16/18 | `disjoint_found_not_found`, `found_ensures` |

## Exercises, including the slides' "what fails if" claims

Each wrong variant was built from the solution file with one change. All five claims hold.

| Exercise | Starter | Solution | Wrong variant | Result | Fails on |
|---|---|---|---|---|---|
| ex1_double | 2/5 | 8/9 | only `0 <= i <= 10` | 4/7 | `assert s == 20`, overflow on `s + 2`, terminates |
| ex2_bonus | 7/11 | 11/12 | `loop assigns i;` | 11/13 | `loop_assigns_part2`, terminates |
| ex3_mod3 | 6/7 | **9/9** | `loop variant n - k;` | 8/9 | `loop_variant_decrease` |
| ex4_fill | 1/5 | **14/14** | `0 <= k <= i` | 12/14 | invariant 2 established and preserved |
| ex5_clip | 1/7 | **20/20** | no invariant for `i <= k < n` | 16/18 | invariants 2 and 3 preserved |

ex1 and ex2 stop at one unproved goal because they have no variant, as the README says.

**Why ex4 needs no "untouched cells" invariant but ex5 does:** `fill`'s postcondition never mentions the old values and its body never reads the array. `clip`'s guard reads `a[i]`, and its invariants compare with `\at(a[k], Pre)`, so WP must know unprocessed cells still hold their original values.

## Extra checks beyond the slides

| Test | Result | Lesson |
|---|---|---|
| `while(1){}` then `assert \false` | 3/4 | The assert is proved (the point after the loop is unreachable) but `terminates` is not. Frama-C 33 no longer reports this as fully proved, which refines the "partial correctness" note in [[examples/ict3112-frama-c-lab2-loops]] |
| `x = 7; while(x > 0) x -= 3;` with `loop variant x`, exit at `x == -2` | 9/9 | A variant may go negative on exit: Positive is checked only when the guard holds |
| Termination goal outside `main` | `search_and_replace`, `mod3`, `fill`, `clip` all report it | Slide 3 says "`main`", but it applies to any function with a loop lacking a variant |

## Traps

- **`loop invariant` must directly precede its loop.** `lab3-solutions/exercises/ex1_double.c` is an annotated copy (not the handout version): the first annotation sits above the declarations and a second block sits inside the loop body, with invariants on a `j` that does not exist. Frama-C stops at `syntax error ... before or at token: int`, `Frama-C aborted: invalid user input`, so no goals run.
- **`%` on negative numbers:** my first variant test used `x % 3 == 1` and failed preservation, because C's `-2 % 3` is `-2`. Using `(x + 2) % 3 == 0` keeps the operand non-negative.
- **False goals report `Timeout`, not `Failed`,** as with `n - k` and `loop assigns i`. Classify them as in [[concepts/acsl-contract-strength-and-pointer-memory]] §6.
- **CLI and GUI names differ:** `typed_main_terminates` is Termination-condition, `loop_invariant_2_preserved` is Invariant (preserved), `loop_variant_decrease` is Loop variant at loop (decrease), `complete_found_not_found` is Complete behaviors.

## Folder layout (2026-11-03)

| Path | Contents |
|---|---|
| `lab3/lab3-examples 2/` | Full set; identical to `lab3-examples - Copy.zip` (`diff -r`) |
| `lab3/lab3-examples/` | Older subset, the 8 `loop*`/`sar*` files |
| `lab3/lab3-solutions/` | Starters and solutions; only `exercises/ex1_double.c` differs (see Traps) |
| `lab3/exercises/` | **Not this deck:** the completed pointer exercises `ex1_copy`–`ex6_next` from [[examples/ict3112-frama-c-lab3-pointers-run]], re-run 2026-11-03, all fully proved |
