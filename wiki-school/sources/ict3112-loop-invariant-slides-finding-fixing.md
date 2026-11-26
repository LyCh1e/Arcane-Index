---
type: source
address: c-000163
title: "ICT3112 Formal Verification — Loop Invariant Slides: Drawing the Data and Repairing Candidates"
domain: formal-verification
source-type: lecture-slides
course: ICT3112
status: ingested
created: 2026-11-27
updated: 2026-11-27
tags: [ict3112, loop-invariants, invariant-discovery, four-slot-template, too-weak, too-strong, witness, formal-verification]
---

# Source: ICT3112 — Loop Invariant Slides (Drawing the Data and Repairing Candidates)

**File:** `raw/images/ict3112-loop-invariant-slides-2026-11-27.md` (transcription of five slide screenshots; images in `_attachments/images/ict3112-loop-invariant-slide-1.png` to `-5.png`)

Five slides from the ICT3112 loop-invariant material. The first two give a picture-based method for building a candidate and a four-slot template; the last three classify the ways a candidate fails and map each failing check to a repair.

## Slide 1 — Drawing the data

1. Draw the data and mark where the progress variable is.
2. Write what is true in each region of the picture.
3. Add the bounds of the progress variable.

```
0                     i                     n
+---------------------+---------------------+
|       visited       |     not visited     |
+---------------------+---------------------+
 what Q asks for,       what is still true here,
 restricted to here     usually the original values
```

`I = (visited) ∧ (not visited) ∧ (0 ≤ i ≤ n)`. For an array sum, the visited region gives `s = A[0] + ⋯ + A[i−1]`, the not-visited region says nothing because the loop only reads `A`, and the bounds are `0 ≤ i ≤ n`.

## Slide 2 — The four-slot template

| Loop | Visited | Not visited | Other relations | Bounds |
|---|---|---|---|---|
| Countdown with a counter | — | — | `c + x = C + X` | `x ≥ 0` |
| Integer division | — | — | `a = b·q + r` | `0 ≤ r` |
| Array sum | `s = A[0] + ⋯ + A[i−1]` | — (only reads `A`) | — | `0 ≤ i ≤ n` |
| Zero-fill | `A[k] = 0` for `k < i` | `A[k] = A₀[k]` for `k ≥ i` | — | `0 ≤ i ≤ m` |
| Reverse in place | front and back swapped | middle: `A[k] = A₀[k]` | `l + r = n − 1` | on `l` and `r` |
| Selection sort | sorted prefix | — | `perm(A, A₀)`, prefix ≤ rest | `0 ≤ i ≤ n` |

The bounds slot is always filled. Facts that are not about a single region belong in the other-relations slot.

## Slide 3 — Four common mistakes

| Mistake | Symptom |
|---|---|
| Too weak | True and preserved, but `I ∧ ¬B` does not imply Q |
| Too strong | Close to Q, but false before the first iteration |
| Missing bounds | The loop's equation is found, but not the facts that fix the counter's final value |
| Missing extra facts | In max or search loops one equation is not enough; facts about the prefix, or a witness, are also needed |

## Slides 4 and 5 — Repairing a failed candidate

Method: (1) name the failing check, (2) write a concrete state with a value for every variable, (3) ask what the state shows, (4) change the candidate and re-check all three conditions.

- A candidate that **rejects a real state** is too strong, so it must be weakened. Establishment failures give this kind of state.
- A candidate that **accepts a wrong state** is too weak, so the fact that rules the state out must be added. Preservation and exit failures give this kind of state.

| Check that fails | Bad state | Problem | Repair |
|---|---|---|---|
| Establishment | A real state at the first loop head that the candidate rejects | Too strong | Weaken: replace constants by progress variables |
| Preservation | Satisfies `I ∧ B`, but not `I` after one pass | Missing extra facts | Add the fact that the body needs |
| Exit | Satisfies `I ∧ ¬B`, with the counter beyond its final value | Missing bounds | Add the range of the counter |
| Exit | Satisfies `I ∧ ¬B`, with a wrong result | Too weak | Add the result computed so far, or a witness |

Each repair can break another condition, so all three must be checked again after every change.

> [!key-insight] What is new relative to the existing pages
> [[loop-invariants]] already listed the template slots and a three-row failure table. These slides add the region picture as the way to fill the visited and not-visited slots, a worked slot table for six course loops, and a split of exit failures into **missing bounds** (counter past its final value) and **too weak** (wrong result, fixed by adding a witness or the partial result).

## Related

- [[loop-invariants]] — updated with the region method, slot table and repair table
- [[ict3112-loop-invariants]] — Module 7 lecture notes
- [[ict3112-loop-invariant-exercises-recorded-lecture]], [[ict3112-loop-invariant-exercises-worked]] — exercises that use the same slots
- [[select-store-axioms]] — needed for preservation when the body writes an array
