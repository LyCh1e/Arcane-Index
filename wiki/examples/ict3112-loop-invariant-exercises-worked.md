---
type: example
address: c-000161
title: "ICT3112 Loop Invariant Exercises — Worked Proofs"
domain: formal-verification
course: ICT3112
created: 2026-11-25
updated: 2026-11-25
tags: [loop-invariants, invariant-discovery, undo-check, variant, worked-examples, hoare-logic]
---

# ICT3112 Loop Invariant Exercises — Worked Proofs

Condensed from [[sources/ict3112-loop-invariant-exercises-recorded-lecture]]. Method: [[concepts/loop-invariants]].

## 1. Counting down: `s = n(n+1)/2`

`i := n; s := 0; while (i > 0) { s := s + i; i := i − 1 }`

- Trace (`n=4`): `(i,s)` = (4,0), (3,4), (2,7), (1,9), (0,10).
- Shortcut `s = i(i+1)/2` fails the trace at row 1 and the undo-check (`i := 0` gives `s = 0`, not Q).
- Fix: write Q as `n(n+1)/2 − 0·(0+1)/2`, then replace the final value 0: **`I: s = n(n+1)/2 − i(i+1)/2 ∧ 0 ≤ i ≤ n`**.
- Establishment reduces to `n ≥ 0`. Preservation: add `i` to both sides, `(i²+i)/2 − i = (i−1)i/2`. Guard `i>0` gives `i ≥ 1`, hence `0 ≤ i−1`.
- Exit: `i ≤ 0` and `0 ≤ i` give `i = 0`. Variant `i`.

## 2. Odd numbers: `s = n·n` with helper `k`

`i:=0; s:=0; k:=1; while (i<n) { s+=k; k+=2; i+=1 }`

- `I₁: s = i·i ∧ 0≤i≤n` fails preservation: it needs `k = 2i+1`.
- **`I₂: s = i·i ∧ k = 2i+1 ∧ 0≤i≤n`**. The two equations support each other: `s + k = i² + 2i + 1 = (i+1)²`.
- `k = 2i+1` is used only in preservation, not at exit. Variant `n − i`.

## 3. Integer square root

`r := 0; while ((r+1)*(r+1) ≤ n) r := r+1` with Q: `0≤r ∧ r·r≤n ∧ n<(r+1)²`

- Third conjunct of Q is exactly `¬B`, so leave it out: **`I: 0 ≤ r ∧ r·r ≤ n`**.
- Using Q as I fails establishment unless `n = 0`.
- Preservation: `(r+1)² ≤ n` is the guard itself.
- Variant `n − r`; `V ≥ 1` while running uses `r+1 ≤ (r+1)²`, which needs `0 ≤ r`.

## 4. Multiplication by 2 (exam style)

`i := n; s := 0; while (i>0) { s+=2; i−=1 }`, Q: `s = 2n`, `I: s + 2i = 2n ∧ 0≤i≤n`

- Exit: `i ≤ 0` plus `0 ≤ i` gives `i = 0`. Without `0 ≤ i`: `i=−1`, `s=2n+2` is a counterexample.
- Variant `i`.

## 5. `4n + 1`

`i:=0; s:=1; while (i<n) { s+=4; i+=1 }`, Q: `s = 4n+1`

- Trace column `s − 4i` is constantly 1, so **`I: s = 4i + 1 ∧ 0≤i≤n`**.
- `s = 4i` fails establishment (`1 = 0`) and the undo-check.
- Exit needs `i ≤ n` (counterexample `i=n+1`, `s=4n+5`); `0 ≤ i` is not used at exit or in establishment, so the marking guide accepts an answer without it.
- Variant `n − i`.

## 6. Increment every cell in place

`i := 0; while (i<n) { a[i] := a[i]+1; i := i+1 }`, Pre: `n = sizeof(a) ∧ a = a₀`, Q: `∀k. 0≤k<n ⇒ a[k] = a₀[k]+1`

```
index:   0 … i−1          | i … n−1
holds:   a₀[k] + 1        | a₀[k]
         produced so far  | not touched yet
```

- `I₁` (produced-so-far plus sizes plus bounds) fails at `k = i`: it needs `a[i] = a₀[i]`.
- **`I₂ = (∀k. 0≤k<i ⇒ a[k]=a₀[k]+1) ∧ (∀k. i≤k<n ⇒ a[k]=a₀[k]) ∧ sizeof(a)=n ∧ 0≤i≤n`**.
- Preservation uses [[concepts/select-store-axioms]]: for `k<i` the cell is unchanged; for `k=i` use the untouched fact; for `k>i` unchanged.
- At exit `i = n`, so the second conjunct has an empty range.

## Diagnosis summary

| Symptom | Meaning | Repair |
|---|---|---|
| Trace or undo-check rejects the candidate | Wrong generalisation | Replace the *final value* of the progress variable; make it visible first |
| Establishment fails | Candidate too strong | Drop the conjunct `¬B` gives, or weaken |
| Preservation fails on a state that never occurs | Body needs an untracked fact | Add a helper relation or the "not touched yet" region |
| Exit fails | Bounds missing | Add the bound that turns `¬B` into equality |
