---
type: example
title: "ICT3112 Frama-C Labs 0–2 — Install, Contracts, Loops (all proved)"
domain: formal-verification
course: ICT3112
created: 2026-10-20
updated: 2026-10-20
tags: [frama-c, acsl, wp, loop-invariants, contracts, lab]
---

# ICT3112 Frama-C Labs 0–2 (Frama-C 33.0, WP, Alt-Ergo + Z3 + cvc5)

Source files: `Formal Methods/Labs/lab0..lab2/*.c`, runner `run_all.sh`. Related: [[concepts/hoare-logic]], [[concepts/loop-invariants]], [[resources/frama-c]], [[learning/frama-c-wsl-install-gotchas]].

Per-lab notes: [[examples/ict3112-frama-c-lab0-installation]], [[examples/ict3112-frama-c-lab1-first-steps]], [[examples/ict3112-frama-c-lab2-loops]].

Command used for every file: `frama-c -wp -rte -wp-prover alt-ergo,z3 file.c` (lab says `frama-c-gui -wp -rte`; the CLI gives the same goals).

## Results

| File | Content | Goals proved |
|---|---|---|
| lab0/main.c | `swap` + assert (install check) | 14/14 |
| lab1/abs.c | `requires INT_MIN < val` stops `-val` overflow | 12/12 |
| lab1/abs_behaviors.c | `pos`/`neg` behaviors, `complete` + `disjoint` | 10/10 |
| lab1/max.c | needs `\result == a \|\| \result == b`, else `INT_MAX` also satisfies it | 9/9 |
| lab1/swap.c | `assigns *a,*b` keeps global `h == 42` | 15/15 |
| lab1/plus5_incr.c | `assigns \nothing`; `\separated(a,b)` for `incr_a_by_b` | 16/16 |
| lab1/inconsistent.c | `requires a<0 && a>0`; `-wp-smoke-tests` reports **Failed smoke-test** (the intended result) | 3/4 |
| lab2/loop_basic.c | `loop invariant 0<=i<=30; loop assigns i; loop variant 30-i` | 10/10 |
| lab2/loop_h_labels.c | h unchanged via `\at(h,LoopCurrent)==\at(h,LoopEntry)` | 12/12 |
| lab2/add_ten.c | needs `a == \at(a,Pre) + i` to link invariant to postcondition | 12/12 |
| lab2/ex1_invariant.c | `-10 <= x <= 0`, variant `x+10` | 9/9 |
| lab2/ex1_weak_invariant.c | `-100<=x<=100` is inductive but too weak: `x==-10` **times out** (expected) | 9/10 |
| lab2/ex2_variant.c | counter `n` = exact remaining iterations, `x == -20+4*(5-n)` | 14/14 |
| lab2/ex2_variant_simple.c | variant `-x` with `(x+20)%4==0` | 11/11 |
| lab2/ex3_assigns.c | `loop assigns e, x` (run without `-rte`, as the lab says) | 9/9 |
| lab2/ex3_labels.c | no `loop assigns`; label `L:` + `loop invariant h == \at(h,L)` | 9/9 |
| lab2/arrays.c | `search`, `reset`, `search_and_replace` | 47/47 without `-rte`; 51/55 with it |

## Answers to the lab questions

- **1.4.1** `-100 <= x <= 100` *is* a correct invariant (holds on entry, preserved) but too weak: `¬(x>-10) ∧ I` only gives `-100<=x<=-10`, not `x==-10`. Use `-10<=x<=0`.
- **1.4.2** Variant `-x` bounds the iterations; for the exact count add `n` (5 at start, decremented) with invariant `x == -20 + 4*(5-n)`, variant `n`.
- **1.4.3** `loop assigns` is just a shorthand for "everything not listed is unchanged"; the same fact can be written as an invariant on a label. Without either, WP assumes the loop may change anything, so the assertion on `h` fails. Without `loop assigns` the function-level `assigns \nothing` also cannot be proved, so `ex3_labels.c` drops it.
- **`\forall` with `&&` instead of `==>`** claims every `size_t` is in range, which is false, so the invariant is false. For `\exists` use `&&`; an implication would be vacuously true.
- **Infinite loop** proves `assert \false` because `¬True ∧ I ⇒ P` is `False ⇒ P`; with variables the loop is `loop assigns \nothing`.

## Caveat: pointer-alignment RTE goals

With `-rte` on `arrays.c`, four `rte_pointer_alignment` goals time out ("`\aligned` not yet implemented" warning). This is a WP limitation in 33.0, not a proof error; all contract and loop goals are proved (47/47 without `-rte`). `-rte` has no switch to disable alignment checks.

## In-class Exercise 1 — `clamp` (`exercises/ex1_clamp.c`)

Workflow from the slide: English description, ACSL contract (LLM-assisted), `frama-c -wp -wp-rte`, then check the contract says what the English says. Contract: `requires lo <= hi; assigns 
othing; ensures lo <= esult <= hi;` plus behaviors `below` (returns `lo`), `above` (returns `hi`), `inside` (returns `v`), `complete` and `disjoint`. Result: **17/17 proved**, including both assertions in `test`. The hint holds: the range postcondition alone is correct but too weak to prove `a == 10` / `b == 5`; the per-case behaviors give the exact result (same lesson as `max`). Exercises 2–5 (`ex2_midnight`, `ex3_tick`, `ex4_swap`, `ex5_deposit`) are in the folder but not yet done.
