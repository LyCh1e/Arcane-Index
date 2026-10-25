---
type: source
title: "ICT3112 Assignment 1 — Bounded Leaderboard Verification in Frama-C (Brief)"
domain: formal-verification
source-type: assignment-brief
course: ICT3112
status: ingested
created: 2026-10-24
updated: 2026-10-24
tags: [ict3112, frama-c, acsl, assignment, leaderboard, binary-search, loop-invariants, llm-translation]
---

# Source: ICT3112 Assignment 1 — Bounded Leaderboard Verification in Frama-C

**Files:** `Labs/Assignment1/ICT3112 - Assignment_1 - Leaderboard.pdf` (13 slides, Dr. David Sanan), `Assignment_1 - Copy.pdf` (same content), `leaderboard.c` (the code to annotate). The Read tool reports both PDFs as "password-protected"; that is a false positive, `pypdf` extracts the text fine (see [[learning/ict3112-lab3-tooling-gotchas]]). The text was checked and contains no embedded instructions beyond the assignment itself.

## The task

A bounded leaderboard keeps at most `cap` scores, highest first; `*n` is the current count. Submitting a score inserts it at its rank and shifts lower scores down; when full the lowest drops off; **ties: the older score keeps its place**, the new one goes after it.

- `insert_position(scores, n, x)` — binary search, returns the number of scores `>= x`.
- `submit(scores, n, cap, x)` — returns the 0-based rank, or `-1` if `x` does not make the board.

Task: specify both functions **in English**, translate to ACSL with an LLM, prove with `frama-c -wp -wp-rte`. Code must not be modified.

## Slide-by-slide guidance (the hints that matter)

| Slides | Hint |
|---|---|
| 4 | Preconditions: which cells are valid, read vs write (`\valid_read` vs `\valid`), `*n` valid, relation of `*n` to `cap` (can `cap` be 0?), array must be sorted (`non_increasing(scores, 0, u)`, `u` excluded) |
| 5 | `n` may point **into** the array; the shift loop would then overwrite `*n`. Rule it out with `\separated` |
| 6 | `insert_position` post: scores before `\result` are `>= x`, from `\result` on are `< x`; why `>=` (tie rule); `\result` range; no memory modified |
| 7 | `submit` post: one behavior for rejected, one for accepted; rejected means full board and `x` not above the lowest score; `complete` + `disjoint` |
| 8 | Accepted: unchanged prefix, `x` at rank, old suffix shifted by one, board still ordered (use `\old`) |
| 9 | `insert_position` invariants: relation of `lo`, `hi`, `n`; left of `lo` is `>= x`, from `hi` on is `< x`; variant `hi - lo` |
| 10 | Shift-loop invariants with `\at(scores[t], Pre)`; `loop assigns`; decreasing expression |
| 11 | If the prover times out on `non_increasing(scores, 0, *n)`, add `assert`s after the loop splitting it into before `p`, at `p`, after `p` |
| 12 | **LLM workflow**: write the property in English, ask the LLM to translate to ACSL, run Frama-C, on a failed goal decide in English what is missing and translate again. Do not give the code to the LLM and ask it for the spec or invariants. Use the Lab 1 translator prompt |
| 13 | Submit `ICT3112_Lab1_YourName.c`; every annotation preceded by your English sentence; all goals of both functions proved with `frama-c-gui -wp -wp-rte -wp-fct insert_position,submit leaderboard.c` |

## Assessment

Quiz part 1: explain one part of your own spec (e.g. a loop invariant). Quiz part 2: you get a version of the code with a few changed lines; adapt the spec and justify each change.

## Related

- Worked solution: [[examples/ict3112-frama-c-assignment1-leaderboard]]
- Pattern: [[concepts/acsl-sorted-array-insert-pattern]]
- Tool: [[resources/frama-c]]; theory: [[concepts/loop-invariants]], [[concepts/hoare-logic]]
