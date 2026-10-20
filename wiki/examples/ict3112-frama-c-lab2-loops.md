---
type: example
title: "ICT3112 Frama-C Lab 2 — Verification of Programs with Loops"
domain: formal-verification
course: ICT3112
created: 2026-10-20
updated: 2026-10-20
tags: [frama-c, acsl, loop-invariants, loop-variant, arrays, lab]
---

# Lab 2 — Loops

Overview: [[examples/ict3112-frama-c-labs-0-2]]. Theory: [[concepts/loop-invariants]], [[concepts/hoare-logic]]. Files: `Labs/lab2/*.c`.

## Invariant, assigns, variant

- WP does not infer invariants. After a loop it knows **only** the invariant (plus `loop assigns`), so it must connect to the postcondition: `(¬guard ∧ I) ⇒ Post`. `0 <= i <= 30` (not `< 30`) is needed so the exit gives `i == 30`; the last iteration sets `i` to 30.
- Two VCs per invariant: established and preserved.
- `loop assigns i;` states every other variable is unchanged. Without it `assert h == 42` after the loop fails. The alternative is `loop invariant \at(h,LoopCurrent) == \at(h,LoopEntry)` (`loop_h_labels.c`), or a C label + `h == \at(h,L)` (`ex3_labels.c`). So `loop assigns` is just convenient shorthand; without it the function-level `assigns` can't be proved either.
- Partial correctness is the default: `while(1){}` followed by `assert \false` is proved because the exit condition is `¬True`. `loop variant` (an integer expression ≥ 0 at each iteration start that strictly decreases) adds termination: `loop variant 30 - i`. The variant only bounds iterations (`random_loop` example) and may go negative once on exit.
- Variant proof sketch: from `I ∧ i<30 ∧ 30-i = v` show `30-(i+1) < v`.
- Link invariant and postcondition: `add_ten` needs `a == \at(a,Pre) + i` **and** `i <= 10`; the equality alone allows `i >= 10`.

## Exercises (all proved)

| Exercise | Answer |
|---|---|
| 1.4.1 `x=0; while(x>-10) --x;` | `-10 <= x <= 0`. `-100 <= x <= 100` is valid but too weak to give `x == -10` (the assertion times out in `ex1_weak_invariant.c`). |
| 1.4.2 `x=-20; while(x<0) x+=4;` | `-x` is a variant; with `(x+20)%4==0` it proves `x==0`. For the exact count add `n=5; n--`, invariant `x == -20 + 4*(5-n)`, variant `n`. |
| 1.4.3 loop with `h`, `x`, `e` | `loop assigns e, x;` or label `L` + `loop invariant h == \at(h,L)`. Run without `-rte` as the lab says (`x += e*2` could overflow). |

## Arrays (`arrays.c`, 47/47 without `-rte`)

- `search`: invariant `\forall size_t j; 0<=j<i ==> array[j] != element`; behaviors `in`/`notin`, `complete`+`disjoint`.
- `reset`: invariant everything before `i` is 0; `loop assigns i, array[0..length-1]`.
- `search_and_replace`: needs three `\forall` invariants plus a fourth, `\forall j; i<=j<length ==> array[j] == \at(array[j],Pre)` (the untouched suffix), found by asserting `array[i] == \at(array[i],Pre)` and watching it fail.
- **`\forall` uses `==>`, `\exists` uses `&&`.** With `&&` a `\forall` demands every `size_t` be in range (false); with `==>` a `\exists` is vacuously true for any out-of-range witness.
- Initial invariant proofs are trivial for Qed: with `i = 0` the range `0 <= j < 0` is empty.
- With `-rte`, 4 `rte_pointer_alignment` goals time out (`\aligned` not implemented in WP 33.0); the contract and loop goals are fine.

## Tips

Add intermediate `assert`s to see which fact WP loses; use `-wp-no-simpl` to inspect raw VCs; Qed often proves trivial VCs itself without calling a solver.
