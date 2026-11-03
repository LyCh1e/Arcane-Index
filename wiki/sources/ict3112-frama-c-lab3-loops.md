---
type: source
title: "ICT3112 Frama-C Lab 3 — Loop Verification (Invariants, Assigns, Variants, Arrays, Behaviours)"
domain: formal-verification
source-type: lab-handout
course: ICT3112
status: ingested
created: 2026-11-03
updated: 2026-11-03
tags: [ict3112, frama-c, acsl, wp, loop-invariants, loop-assigns, loop-variant, termination, arrays, behaviors, llm-translation, lab]
---

# Source: ICT3112 Lab 3 — Loop Verification in Frama-C

**File:** `Labs/lab3/ICT3112 - Lab3 - Loops.pdf` (31 slides, Frama-C 33 / Ivette, exported 2026-11-03). Code: `Labs/lab3/lab3-examples 2/`, which has 11 example files, `exercises/` (5 starters), `solutions/` (5 `_sol.c`) and a `README.txt` mapping files to slides.

This is the current slide-deck version of the loops topic. The older handout is `Labs/lab2/Lab2-Loops.pdf` ([[examples/ict3112-frama-c-lab2-loops]]); this deck adds the Termination-condition goal, the LLM exercises and behaviours.

Run results: [[examples/ict3112-frama-c-lab3-loops-run]]. Theory: [[concepts/loop-invariants]], behaviours in [[concepts/acsl-contract-strength-and-pointer-memory]].

## Slide map

| Slides | Topic | File |
|---|---|---|
| 2–3 | Loop invariants: established + preserved | `loop1.c` |
| 4 | Literal-translator LLM prompt (same method as Labs 1 and 2) | |
| 5–6 | Exercise 1: invariant relating two variables | `ex1_double.c` |
| 7–8 | Why `h` is unknown after the loop | `loop2.c` |
| 9 | `loop assigns` | `loop3.c` |
| 10 | `LoopEntry` and `LoopCurrent` | `loop4.c` |
| 11–12 | Exercise 2: writing a `loop assigns` | `ex2_bonus.c` |
| 13–14 | Termination: `loop variant` | `loop5.c` |
| 15–16 | Exercise 3: finding a variant | `ex3_mod3.c` |
| 17–23 | Search and replace: contract, `\forall` invariants, the third invariant | `sar1–3.c` |
| 24–25 | Exercise 4: `\forall` invariant over an array | `ex4_fill.c` |
| 26–27 | Exercise 5: applying search and replace | `ex5_clip.c` |
| 28–31 | Behaviours: `assumes`, `complete`, `disjoint` | `find*.c` |

## What the slides teach

1. **Invariants** produce two goals: *established* (holds when the loop is reached) and *preserved* (holds again after the body). After the loop WP knows only the invariant and the false guard: `0 <= i <= 30` and `!(i < 30)` give `i == 30`.
2. **Termination-condition.** Frama-C 33 asks for it, and it stays unproved until the loop has a variant. The slide says "`main`"; the runs show it applies to any function with such a loop.
3. **Missing `loop assigns`.** WP replaces the loop with its specification and assumes it may change everything, warning `Missing assigns clause (assigns 'everything' instead)`. In the goal, `h_0` is the unknown value of `h` after the loop. `loop assigns i` fixes it and adds its own goal, which checks the body writes nothing else. `\at(h, LoopCurrent) == \at(h, LoopEntry)` gives the same fact about `h`.
4. **A missing `loop assigns` can break an invariant, not just a later assert** (Exercise 2). `bonus` becomes unknown at each iteration, so `total == 3 * i` is not preserved. Listing too little fails too: `loop assigns i` alone fails the Loop assigns goal because the body writes `total`.
5. **Variants** produce two goals: *Positive* (not negative at the start of each iteration) and *Decrease* (strictly smaller each iteration). `30 - i` counts the remaining iterations. The wrong direction fails: `n - k` grows in `mod3`.
6. **Shape of a `\forall` invariant:** `\forall index; range (using the loop index) && condition ==> property`. Range `0 <= j < i` covers the cells already processed; `\at(array[j], Pre)` is the value at the call.
7. **The third invariant** (slides 21–23): `\forall j; i <= j < length ==> array[j] == \at(array[j], Pre)`. The code is correct but the specification is incomplete. Without it, the invariants would allow iteration `i` to overwrite a later cell `j` holding `old_value` with `new_value + 1`. When `i` reaches `j` the guard is false, nothing is written, and the invariant breaks. Deck's rule: **"A loop invariant must always say what happens with all the elements, even those that the loop does not modify."**
8. **Behaviours** (slides 28–31). Top-level `requires` and `assigns` apply to every call. `assumes` selects a case and is evaluated in the pre-state, like `\old`. Each behaviour's `ensures` holds only where its `assumes` held. `complete behaviors` proves `P ==> A1 || A2`; `disjoint behaviors` proves `P ==> !(A1 && A2)`. **These two goals check only the specification, not the code.** Without `complete`, some calls may have no case and the contract guarantees nothing about them; without `disjoint`, overlapping cases must both hold. Both clauses can name their behaviours (`complete behaviors case_1, case_2;`). The keyword is spelled `behavior`.

## Exercises (solutions are in the deck)

| Exercise | Answer |
|---|---|
| 1 `ex1_double` | `0 <= i <= 10`, `s == 2 * i` |
| 2 `ex2_bonus` | `loop assigns i, total;` |
| 3 `ex3_mod3` | `loop variant k;` |
| 4 `ex4_fill` | `0 <= i <= n`; `\forall size_t k; 0 <= k < i ==> a[k] == v`; `loop assigns i, a[0 .. n-1]`; `loop variant n - i` |
| 5 `ex5_clip` | Same shape as search and replace: two `\forall` invariants before `i`, one for `i <= k < n`, plus range, assigns and variant |

## Checked for embedded instructions

Clean. Text layer read in full, all 31 slides reviewed including the 16 with screenshots, and no near-white, tiny or invisible text in any of the 2,599 text-draw operations. See [[learning/prompt-injection-in-lab-handout-pdf]]. The slide 4 prompt is a visible part of the students' method, not text aimed at an assistant reading the deck.
