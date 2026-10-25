---
type: example
title: "ICT3112 Assignment 1 — Bounded Leaderboard, ACSL Specification (94/94 proved)"
domain: formal-verification
course: ICT3112
status: established
created: 2026-10-24
updated: 2026-10-24
sources: [ict3112-assignment1-leaderboard-brief]
tags: [frama-c, acsl, assignment, binary-search, behaviors, loop-invariants, separated, cvc5]
---

# ICT3112 Assignment 1 — Bounded Leaderboard

Brief: [[sources/ict3112-assignment1-leaderboard-brief]]. Pattern summary: [[concepts/acsl-sorted-array-insert-pattern]]. Files: `Labs/Assignment1/ICT3112_Lab1_Chiyung.c` (annotated), `explanation.md` (what was added and why), `Testing-Guide.md` (how to reproduce), `leaderboard.c` (original).

## Result

`frama-c -wp -wp-rte -wp-fct insert_position,submit -wp-prover alt-ergo,z3,cvc5 -wp-timeout 30 ICT3112_Lab1_Chiyung.c` → **94 / 94 goals proved** (uncached run: Qed 45, Alt-Ergo 40, CVC5 4, Z3 3, Terminating 1, Unreachable 1). `gcc` build prints `3 0 -1 | n=5 | 95 90 80 80 80`, matching the brief's trace. `diff` against `leaderboard.c` shows 121 lines added and none changed or removed.

With **Alt-Ergo alone it is 92 / 94**: the two post-loop `assert non_increasing(...)` goals time out. CVC5 (or Z3) closes them in about 1.7 s.

## The specification, in short

**`insert_position`** — `requires \valid_read(scores+(0..n-1)); n >= 0; non_increasing(scores,0,n)`; `assigns \nothing`; `ensures 0 <= \result <= n`, left of `\result` is `>= x`, from `\result` on is `< x`. Loop: `0 <= lo <= hi <= n`; left of `lo` is `>= x`; from `hi` on is `< x`; `loop assigns lo, hi`; `loop variant hi - lo`. At exit `lo == hi`, so the two invariants cover the whole array, which is the postcondition.

**`submit`** — `requires cap >= 1; 0 <= *n <= cap; \valid(n); \valid(scores+(0..cap-1)); \separated(n, scores+(0..cap-1)); non_increasing(scores,0,*n)`; `assigns *n, scores[0..cap-1]`; `ensures non_increasing(scores,0,*n)`.
- `behavior rejected`: `assumes *n == cap && scores[cap-1] >= x` → `\result == -1`, `*n` unchanged, array unchanged, `assigns \nothing`.
- `behavior accepted`: `assumes *n < cap || (*n == cap && scores[cap-1] < x)` → `scores[\result] == x`, new size `\old(*n) < cap ? \old(*n)+1 : cap`, prefix unchanged, suffix equals old cells shifted by one (`scores[k] == \old(scores[k-1])`).
- `complete behaviors; disjoint behaviors;`
- Shift loop (`for i = last; i > p; i--`): `p <= i <= last`; cells above `i` hold `\at(scores[k-1], LoopEntry)`; cells `0..i` unchanged; cells past `last` unchanged; `loop assigns i, scores[p+1..last]`; `loop variant i - p`.
- Ten helper `assert`s split the final sortedness goal: before `scores[p] = x` (prefix unchanged, suffix shifted, prefix `>= x`, suffix `< x`), and after (`scores[p] == x`, `non_increasing` on `[0,p)` and on `[p,*n)`).

## Decisions worth remembering

| Decision | Reason |
|---|---|
| `\valid_read` for `insert_position`, `\valid` for `submit` | The first takes `const int[]` and only reads; the second writes |
| Array validity up to `cap`, not `*n` | `submit` can grow the board by one cell |
| `\separated(n, scores + (0..cap-1))` | Otherwise the shift loop could overwrite `*n` (the brief's `n == &scores[3]` example) |
| `cap >= 1` | With `cap == 0`, `cap - 1` is an invalid index and `*n <= cap` forces an empty board that can never accept |
| Rejected iff full **and** `scores[cap-1] >= x` | Ties lose: the older equal score keeps its place, so an equal score cannot displace the last one |
| `>=` before and `<` after the rank in `insert_position` | That is the tie rule written as a postcondition |
| `\at(..., LoopEntry)` in the shift-loop invariants | Names the values before the loop without needing a label |

## Honest gaps

- **Spec direction:** the assignment's method is English first, LLM translates, never feed the code to the LLM. Here the spec was derived by reading the code and the brief together, then the English comments were attached to each annotation. Re-explain each in your own words before the quiz.
- **GUI not observed:** the proof was run from the command line. `frama-c-gui` was launched twice (the first window vanished when the launching WSL shell exited, see [[learning/frama-c-wsl-install-gotchas]]), but the WP Goals panel was never inspected, so the "required GUI command" outcome is unconfirmed.
- Quiz part 2 (changed code) is untested; if a line of the code changes, re-check the `last` computation, `p == cap` test and the shift loop bounds first.
