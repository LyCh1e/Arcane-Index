---
type: concept
address: c-000162
title: "Select–Store Axioms"
domain: formal-verification
status: established
created: 2026-11-25
updated: 2026-11-25
sources: [ict3112-array-exercises-solved, ict3112-hoare-arrays, ict3112-loop-invariant-exercises-recorded-lecture]
tags: [select-store, arrays, array-assign, hoare-logic, weakest-precondition, formal-verification, ict3112]
---

# Select–Store Axioms

The two axioms that tell you what a **read of an updated array** returns. They are what turns the substitution `Q[a ← a[I ↦ E]]` from [ARRAY-ASSIGN] into a formula you can reason about.

```
a[I ↦ E][J] = E        if J = I     (read the cell that was written)
a[I ↦ E][J] = a[J]     if J ≠ I     (any other cell keeps its old value)
```

`a[I ↦ E]` is the array `a` where position `I` now holds `E`. The update changes one cell, never the number of cells: `sizeof(a[I ↦ E]) = sizeof(a)`.

## Three steps for `a[I] := E`

1. **Substitute.** Replace every occurrence of `a` in Q by `a[I ↦ E]`. Other arrays are untouched (different names are different arrays).
2. **Select–store.** Simplify each read of the updated array with the axioms. If the program does not tell you whether the read index equals `I`, keep **both cases** and join them: `(J = I ∧ …) ∨ (J ≠ I ∧ …)`.
3. **Definedness.** Add `def(a[I]) ∧ def(E)`, i.e. `0 ≤ I < sizeof(a)` and one `def(b[J])` per array read inside `E`. Put the whole simplified formula in parentheses before conjoining, because the definedness condition must hold in both cases.

## Worked pattern — two reads of the same updated array

Q: `a[i] ≥ a[j]`, program `a[i] := x`.

- Left read, index `i`: `a[i ↦ x][i] = x`.
- Right read, index `j`: case `j = i` gives `x`, case `j ≠ i` gives `a[j]`.
- Joined: `(j=i ∧ x≥x) ∨ (j≠i ∧ x≥a[j])`, which simplifies to `j = i ∨ x ≥ a[j]`.
- With definedness: `(j = i ∨ x ≥ a[j]) ∧ 0 ≤ i < sizeof(a)`.

## Under a quantifier

For `∀k. 0 ≤ k < i+1 ⇒ b[i ↦ v][k] = P(k)` keep both cases per `k`. The case `k = i` gives `v = P(i)`. If that is true by construction (e.g. `v = 2·a[i]`, `P(k) = 2·a[k]`), only `0 ≤ k < i` remains, which is already the old invariant. If it is **not** true by construction, the invariant must already say something about cell `i`, which is the "not touched yet" conjunct (`∀k. i ≤ k < n ⇒ a[k] = a₀[k]`) in [[ict3112-loop-invariant-exercises-worked]] Exercise 6.

## Pitfalls

- **Wrong-cell precondition.** A fact about the old `a[i]` does not help the case `j ≠ i`; the precondition has to constrain `a[j]`.
- **Aliasing.** Step 1 leaves other arrays alone only if they are really different. In C two pointers can share memory, and then a write through one changes reads through the other. Frama-C handles this with `\separated` ([[acsl-contract-strength-and-pointer-memory]]).
- **Off-by-one definedness.** `0 ≤ i < sizeof(a)` does not give `i + 1 < sizeof(a)`; a read of `a[i+1]` needs its own `def`.

## Related

- [[hoare-logic]] — [ARRAY-READ] and [ARRAY-ASSIGN] rules
- [[loop-invariants]] — array loops need processed and unprocessed regions
- [[ict3112-array-exercises-solved]], [[ict3112-hoare-arrays]]
