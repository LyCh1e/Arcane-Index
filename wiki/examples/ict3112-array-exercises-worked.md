---
type: example
address: c-000160
title: "ICT3112 Array Exercises — Worked Proofs"
domain: formal-verification
course: ICT3112
created: 2026-11-25
updated: 2026-11-25
tags: [hoare-logic, arrays, array-read, array-assign, select-store, dot-product, loop-invariants, worked-examples]
---

# ICT3112 Array Exercises — Worked Proofs

Condensed from [[sources/ict3112-array-exercises-solved]]. Rules: see [[concepts/select-store-axioms]].

## 1. Two reads, no write

`{ 0 ≤ i ∧ i+1 < sizeof(a) }  x := a[i+1] − a[i]  { x + a[i] = a[i+1] }`

- Substitution: `a[i+1] − a[i] + a[i] = a[i+1]` reduces to `true`.
- Definedness: `0 ≤ i+1 < sizeof(a) ∧ 0 ≤ i < sizeof(a)`, which simplifies to `0 ≤ i ∧ i+1 < sizeof(a)`.
- So wp equals the precondition (`P ⇒ P`). With only `0 ≤ i < sizeof(a)`, `i = sizeof(a) − 1` reads out of bounds (`a=[4,7]`, `i=1`).

## 2. Read then write

`{ 0≤i<sizeof(a) ∧ 0≤j<sizeof(a) ∧ a[j]>0 }  x := 2*a[j];  a[i] := x  { a[i] ≥ a[j] }`

| Step | Result |
|---|---|
| R2 = wp(`a[i] := x`, Q) | `(j = i ∨ x ≥ a[j]) ∧ 0 ≤ i < sizeof(a)` |
| R1 = wp(`x := 2*a[j]`, R2) | `(j = i ∨ a[j] ≥ 0) ∧ 0 ≤ i < sizeof(a) ∧ 0 ≤ j < sizeof(a)` |
| Precondition ⇒ R1 | `a[j] > 0` gives `a[j] ≥ 0`, so the disjunction holds in both cases |

Swap to `a[i] > 0` and it fails when `j ≠ i`: `i=0, j=1, a=[3,−2]` gives `x = −4`, `a = [−4,−2]`, and `−4 ≥ −2` is false.

## 3. Dot product loop

```
{ sizeof(a)=n ∧ sizeof(b)=n }
i := 0; s := 0;
while (i < n) { s := s + a[i]*b[i]; i := i + 1; }
{ s = Σ(k=0..n−1) a[k]·b[k] }
```

- Trace (`a=[2,−1,3]`, `b=[4,5,1]`): `s` = 0, 8, 3, 6.
- `I: s = Σ(k=0..i−1) a[k]·b[k] ∧ sizeof(a)=n ∧ sizeof(b)=n ∧ 0≤i≤n`. The sizes are in `I` because the body needs `def(a[i])` and `def(b[i])`.
- Establishment: empty sum is 0; `0 ≤ n` because a size is never negative.
- Preservation: split the last term, `Σ(k=0..i) = Σ(k=0..i−1) + a[i]·b[i]`, then replace the first part by `s`. `i+1 ≤ n` comes from the guard (integers), not from `i ≤ n`.
- Exit: `¬(i<n)` with `i ≤ n` gives `i = n`.
- Variant: `n − i`.
- Guard `i ≤ n` instead: `def(a[n])` is `n < n`, which fails.

## 4. Writing into a second array

```
{ sizeof(a)=n ∧ sizeof(b)=n }
i := 0; while (i < n) { b[i] := 2*a[i]; i := i + 1; }
{ ∀k. 0≤k<n ⇒ b[k] = 2·a[k] }
```

- `I: (∀k. 0≤k<i ⇒ b[k]=2·a[k]) ∧ sizeof(a)=n ∧ sizeof(b)=n ∧ 0≤i≤n`.
- Preservation: substitute `b[i ↦ 2·a[i]]`; for `k = i` the formula is `2·a[i] = 2·a[i]`, so only `0≤k<i` remains.
- Definedness: `0 ≤ i < sizeof(b)` and `0 ≤ i < sizeof(a)` follow from the guard and the size facts.
- Variant: `n − i`.
- If `a` and `b` alias, `b[i] := 2*a[i]` also writes `a[i]` and the spec requires `a[k] = 2·a[k]`, true only for zeros.

## Exam-style checklist for array loops

1. Put `sizeof(...) = n` facts in `I`.
2. Write the processed region as a bounded `∀`.
3. Add the unprocessed region if the body reads a cell it writes (see [[examples/ict3112-loop-invariant-exercises-worked]] Ex. 6).
4. Use the guard for `i + 1 ≤ n` and for `i < sizeof(a)`.
5. Variant `n − i` (or `sizeof(a) − i`).
