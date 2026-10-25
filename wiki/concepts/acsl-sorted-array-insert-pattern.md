---
type: concept
title: "ACSL Pattern: Binary Search and Ordered Insertion"
domain: formal-verification
status: established
created: 2026-10-24
updated: 2026-10-24
sources: [ict3112-assignment1-leaderboard-brief]
tags: [acsl, frama-c, binary-search, sorted-array, shifting-loop, behaviors, loop-invariants]
---

# ACSL Pattern: Binary Search and Ordered Insertion

A reusable recipe for specifying code that searches a sorted array and inserts into it. Worked instance: [[examples/ict3112-frama-c-assignment1-leaderboard]]. Background: [[concepts/loop-invariants]], [[concepts/hoare-logic]], [[resources/frama-c]].

## 1. Sortedness as a predicate

```acsl
predicate non_increasing{L}(int *a, integer l, integer u) =
  \forall integer i, j; l <= i <= j < u ==> a[i] >= a[j];
```
`u` is excluded. Use it as a `requires` (input sorted) and an `ensures` (still sorted).

## 2. Binary search: the "known zones" invariant

Keep an unexamined window `[lo, hi)`:
1. `0 <= lo <= hi <= n` (bounds)
2. left of `lo`: property P holds (`scores[k] >= x`)
3. from `hi` on: property not-P holds (`scores[k] < x`)
4. `loop assigns lo, hi`; `loop variant hi - lo`

At exit `lo == hi`, so the left and right zones tile the array and the invariants imply the postcondition. The `>=` / `<` split encodes the tie rule (equal goes left, so a new element lands after equals).

## 3. Shifting loop (insert at `p`, moving a suffix down by one)

For `for (i = last; i > p; i--) a[i] = a[i-1];` use `\at(.., LoopEntry)`:
- cursor range `p <= i <= last`
- cells above `i`: `a[k] == \at(a[k-1], LoopEntry)` (already shifted)
- cells `0..i`: unchanged
- cells past `last`: unchanged
- `loop assigns i, a[p+1 .. last]`; `loop variant i - p`

## 4. Accept / reject behaviors

Write the rejection condition as an `assumes` on the state (`full && a[cap-1] >= x`), the acceptance condition as its negation, and add `complete behaviors; disjoint behaviors;` so Frama-C checks that they cover every valid call without overlap.

## 5. Aliasing

If the size is passed by pointer, add `\separated(n, a + (0 .. cap-1))`. Without it the loop's writes to `a[i]` might change `*n`.

## 6. Proving "still sorted" after the insert

The single goal `non_increasing(a, 0, *n)` is hard for SMT provers. Split with `assert`s: prefix unchanged and `>= x`; suffix equals old cells shifted and `< x`; then after `a[p] = x`, sortedness of `[0,p)` and of `[p,*n)` separately. If Alt-Ergo still times out, add provers: `-wp-prover alt-ergo,z3,cvc5 -wp-timeout 30` (CVC5 closed the two stubborn goals here).

## Pitfalls

- Strict vs non-strict comparison decides which of equal elements wins; the postcondition must match the code.
- Allocate validity to the **capacity**, not the current size, when the function can grow the structure.
- Check the edge `cap == 0` (index `cap - 1`) and the full-board case separately.
