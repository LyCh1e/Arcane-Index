---
type: example
title: "ICT3112 Frama-C Lab 1 — First Steps (Contracts, Pointers, Behaviors)"
domain: formal-verification
course: ICT3112
created: 2026-10-20
updated: 2026-10-20
tags: [frama-c, acsl, contracts, pointers, behaviors, lab]
---

# Lab 1 — Starting to Work with Frama-C

Overview: [[examples/ict3112-frama-c-labs-0-2]]. Cheat sheet: [[resources/frama-c]]. Files: `Labs/lab1/*.c`. All run with `frama-c -wp -rte`.

## Contracts and overflow (`abs.c`, 12/12)

- `ensures \result >= 0` alone is provable, but `-val` overflows for `INT_MIN` (two's complement range is asymmetric). RTE adds `-2147483647 <= val`; WP leaves it Unknown until we add `requires INT_MIN < val`.
- "Unknown/Timeout" never means the property is false — it may be a missing precondition or a hard goal.
- A call that certainly violates a precondition (`abs(INT_MIN)`) puts `False` in the assumptions, so everything after it is "proved". Swapping the order of calls shows this.
- `==>` (implication) and `<==>` (equivalence) are ACSL connectors; `A ==> B` is `!A || B`.

## Specification quality (`max.c`, 9/9)

`ensures \result >= a && \result >= b` is proved, yet `return INT_MAX;` also satisfies it and `assert c == 42` fails at the call site. Adding `\result == a || \result == b` pins the result to the exact max. A spec is a *set* of allowed outputs; make it as small as the intent.

## Inconsistent preconditions (`inconsistent.c`)

`requires a < 0 && a > 0; ensures \false;` is "proved" vacuously. `-wp-smoke-tests` finds it (Failed smoke-test = the precondition is unsatisfiable). A passing smoke test does not prove the contract is consistent.

## Pointers (`swap.c` 15/15, `plus5_incr.c` 16/16)

- `\old(e)` only in postconditions; `\at(e, Label)` anywhere (`Pre`, `Here`, `Old`, `Post`, `LoopEntry`, `LoopCurrent`, C labels). The label propagates into sub-terms: `\at(x[*p],Pre)` also reads `*p` at `Pre`.
- Dereferencing needs `\valid(p)` (read/write) or `\valid_read(p)` (read only; writing through it fails RTE). `\valid(p + (0..n-1))` covers a range.
- Unspecified side effects: WP assumes a call may change anything, so `assert h == 42` after `swap` fails until `assigns *a, *b` is added. `assigns \nothing` for pure functions.
- Aliasing: `incr_a_by_b(a, b)` with `a == b` breaks `*b == \old(*b)`; fix with `requires \separated(a, b)`. The `assigns` clause was fine either way.
- Added `requires INT_MIN <= *a + *b <= INT_MAX` to remove the overflow goal the lab sets aside.

## Behaviors (`abs_behaviors.c`, 10/10)

`behavior pos: assumes 0 <= val; ensures ...` plus `complete behaviors; disjoint behaviors;`. `val > 0` in `pos` makes it incomplete (misses 0); `val <= 0` in `neg` makes it non-disjoint. Put `assigns` before the behaviors, not inside them (WP handles per-behavior `assigns` poorly).

## Method

Write the contract from the intended meaning first, then add the preconditions that C's types force; testing a spec with calling code is a cheap way to see if it is strong enough.
