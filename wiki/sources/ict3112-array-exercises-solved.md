---
type: source
address: c-000158
title: "ICT3112 Formal Verification — Array Exercises with Solutions"
domain: formal-verification
source-type: exercise-solutions
course: ICT3112
status: ingested
created: 2026-11-25
updated: 2026-11-25
tags: [ict3112, hoare-logic, arrays, array-read, array-assign, select-store, loop-invariants, exercises, formal-verification]
---

# Source: ICT3112 — Array Exercises with Solutions

**File:** `raw/ICT3112 Array exercises with solutions.md` (text extract of the 10-page PDF "ICT3112 – Array exercises with solutions")

Companion exercise sheet for Module 8 ([[sources/ict3112-hoare-arrays]]). Four fully worked exercises that apply `[ARRAY-READ]`, `[ARRAY-ASSIGN]` and the select–store axioms, first on straight-line code and then inside loops with the recipe from [[sources/ict3112-loop-invariants]].

> [!gap] Sheet intro vs content
> The intro says "the last three exercises" have loops, but the PDF contains only four exercises (two without loops, two with). Exercise 5 is not in the file.

## The rules used

- `[ARRAY-READ]`: `{ Q[x ← E] ∧ def(E) }  x := E  { Q }`
- `[ARRAY-ASSIGN]`: `{ Q[a ← a[I ↦ E]] ∧ def(a[I]) ∧ def(E) }  a[I] := E  { Q }`
- `def(a[I])` is `0 ≤ I < sizeof(a)`; `def(E)` is the conjunction of one `def(b[J])` per array read in E, or `true`.
- Select–store: `a[I ↦ E][J] = E` if `J = I`, else `a[J]`. Full treatment in [[concepts/select-store-axioms]].
- wp is calculated from the last statement to the first. Arrays with different names are different arrays.

## The four exercises

| # | Program | Key result |
|---|---|---|
| 1 | `x := a[i+1] - a[i]`, Q: `x + a[i] = a[i+1]` | The substitution gives `true`; wp is only the definedness: `0 ≤ i ∧ i+1 < sizeof(a)`. Weakening the precondition to `0 ≤ i < sizeof(a)` breaks it: `a = [4,7]`, `i = 1` reads `a[2]` |
| 2 | `x := 2*a[j]; a[i] := x`, Q: `a[i] ≥ a[j]` | R2 = `(j = i ∨ x ≥ a[j]) ∧ 0 ≤ i < sizeof(a)`; R1 = `(j = i ∨ a[j] ≥ 0) ∧ bounds`. Valid under `a[j] > 0`; **fails** under `a[i] > 0` (`i=0, j=1, a=[3,−2]` ends as `[−4,−2]`, so `−4 ≥ −2` is false) |
| 3 | Dot product loop over `a` and `b` | `I: s = Σ(k=0..i−1) a[k]·b[k] ∧ sizeof(a)=n ∧ sizeof(b)=n ∧ 0≤i≤n`; variant `n − i` |
| 4 | `b[i] := 2*a[i]` loop | `I: (∀k. 0≤k<i ⇒ b[k]=2·a[k]) ∧ sizeof(a)=n ∧ sizeof(b)=n ∧ 0≤i≤n`; variant `n − i` |

## Ideas worth keeping

- **Three steps for a write:** substitute, select–store, definedness. The parentheses matter: the definedness conjunct must hold in both cases of the disjunction (Exercise 2).
- **Case split on indices:** when the program does not say whether `j = i`, keep both cases, then simplify `(j=i ∧ x≥x) ∨ (j≠i ∧ x≥a[j])` to `j = i ∨ x ≥ a[j]`.
- **Why `a[i] > 0` is the wrong precondition (Exercise 2):** it describes the old value of the cell being overwritten. The `j ≠ i` case needs a fact about `a[j]`.
- **Size facts go into the invariant (Exercises 3, 4):** inside the body only `I` and the guard are available, and the reads/writes need `def(a[i])`, `def(b[i])`. Nothing writes the sizes, so they are preserved for free.
- **No "not touched yet" conjunct needed** when the loop only reads `a` and fully overwrites `b` (contrast [[examples/ict3112-loop-invariant-exercises-worked]] Exercise 6, where the body reads the cell it writes).
- **Empty ranges:** `Σ(k=0..−1)` is 0 and `∀k. 0≤k<0 ⇒ …` is true, which gives establishment.
- **Quantifier under a write (Exercise 4):** after substituting `b[i ↦ 2·a[i]]` the case `k = i` is always true, so only `0 ≤ k < i` is left and it matches the invariant.
- **Wrong guard `i ≤ n`:** preservation fails at `0 ≤ i < sizeof(a)` for `i = n`, which is the out-of-bounds read `a[n]`, found without running the program.
- **Aliasing:** the proof is valid only because `a` and `b` are different arrays. If both point to the same memory in C, `b[i] := 2*a[i]` also changes `a[i]` and the postcondition holds only when every element is 0. This returns in the Frama-C pointer labs ([[concepts/acsl-contract-strength-and-pointer-memory]]).

## Related

- [[examples/ict3112-array-exercises-worked]] — condensed proofs
- [[concepts/select-store-axioms]], [[concepts/hoare-logic]], [[concepts/loop-invariants]]
- [[sources/ict3112-loop-invariant-exercises-recorded-lecture]] — the other new exercise sheet
