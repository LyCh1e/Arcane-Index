---
type: source
title: "ICT3112 Formal Verification — Hoare Logic Exercises 1–3 (Solved)"
domain: formal-verification
source-type: exercise-solutions
course: ICT3112
status: ingested
created: 2026-10-15
updated: 2026-10-15
tags: [ict3112, hoare-logic, weakest-precondition, loop-invariants, proof-outline, worked-examples, formal-verification]
---

# Source: ICT3112 Formal Verification — Hoare Logic Exercises 1–3 (Solved)

**Files:**
- `raw/ICT3112 Software Verification and Validation - Hoare Logic Exercises - 1 - solved.md`
- `raw/ICT3112 Software Verification and Validation - Hoare Logic Exercises - 2 - solved.md`
- `raw/ICT3112 Software Verification and Validation - Hoare Logic Exercises - 3 - solved.md`

---

## Summary

Three full exercise sets with model solutions, covering every aspect of Hoare Logic taught in ICT3112. Each solution is presented in a structured format: the implication or triple is stated, then proved step by step in a table, then a complete proof outline is given.

**Conventions across all sheets:**
- Primed names (x′, y′) are *logical variables* recording the initial value of a program variable; they are never assigned by the programme.
- Unassigned names (n, m) are constants; substitution leaves them alone.
- All variables are integers unless stated otherwise.
- Loop syntax: `while (B) do { … }`.

---

## Exercise Sheet 1 — Implications, Skip Triples, WP, Sequences, Conditionals, Loops

### Section 1 — Valid Implications

Key patterns:
- `False ⇒ Q` is always valid (false premise).
- `P ⇒ True` is always valid (true conclusion).
- `P ⇒ False` is not valid unless *P* is itself always false.
- To show *not valid*: exhibit one state where the premise is true and the conclusion is false.

### Section 2 — Valid Triples with Skip

`{P} skip {Q}` reduces to checking `P ⇒ Q` (Skip Rule + Consequence).

Key cases: `{x > 0} skip {x ≥ 0}` is valid (`x > 0 ⇒ x ≥ 0`); `{x ≥ 0} skip {x > 0}` is **not** valid (counterexample: x = 0).

### Section 3 — Weakest Preconditions (Sequences and Conditionals)

Method: compute `wp(Sn, Q)` for the last statement, then propagate backwards through each statement.

Selected solutions:

**3a.** `{?} y := x; y := x + x + y; {y = 3·x}`
- Step 2: `wp(y := x + x + y, y = 3·x) = [y ← x + x + y] = x + x + y = 3·x, i.e. y = x`
- Step 1: `wp(y := x, y = x) = [y ← x] = x = x = True`
- Weakest precondition: `True`

**3c.** `{?} if (x − y > 0) then z := x else z := y {z ≤ y ∧ z ≤ x}`
- Then-branch WP: `x ≤ y` (substituting `z ← x`)
- Else-branch WP: `y ≤ x` (substituting `z ← y`)
- Combined: `(x − y > 0 ⇒ x ≤ y) ∧ (x − y ≤ 0 ⇒ y ≤ x) = x ≤ y ∧ y ≤ x = x = y`

### Section 4 — Prove Hoare Triples (Intermediate Assertions)

Method: compute intermediate assertions R₁, R₂, … by applying wp backwards, then verify `P ⇒ R₁`.

**4a.** `{x = x′ ∧ y = y′} k := x + n; x := y − m; y := k + y; {x = y′ − m ∧ y = x′ + n + y′}`
- R3 (before `y := k + y`): `x = y′ − m ∧ k + y = x′ + n + y′`
- R2 (before `x := y − m`): `y = y′ ∧ k = x′ + n`
- R1 (before `k := x + n`): `y = y′ ∧ x = x′`
- Given precondition equals R1 (same conjuncts reordered). ✓

### Section 5 — Proof Outlines and Loop Invariants

**5a.** `{x = x′ ∧ y = y′ ∧ y ≥ 0} while (y > 0) do { x := x + 1; y := y − 1; } {x = x′ + y′}`
- Invariant: `I ≡ x + y = x′ + y′ ∧ y ≥ 0`
- Variant: `E = y`
- Establishment: replace x by x′ and y by y′ → True ✓
- Preservation: wp gives `x + y = x′ + y′ ∧ y ≥ 1`; `I ∧ B` (which includes `y > 0`) implies `y ≥ 1` ✓
- Exit: `y ≥ 0 ∧ y ≤ 0` gives `y = 0`; then `x = x′ + y′` ✓

**5c.** Multiplication by halving and doubling (Russian peasant multiplication):
`{x = x′ ∧ y = y′ ∧ x′ ≥ 0 ∧ y′ > 0} z := 0; while (!(x = 0)) do { if (x mod 2 = 1) then z := z + y else skip; y := y * 2; x := x div 2; } {z = x′ · y′}`
- Invariant: `I ≡ x′ · y′ = x · y + z ∧ x ≥ 0`
- Variant: `E = x`
- Key insight: hint `2 · (x div 2) = x − x mod 2` is used in preservation.

---

## Exercise Sheet 2 — Further Sequences and Loops

Sheet 2 continues the same structure: more sequences with three or four statements, more loops including nested conditionals in the body. Key patterns reinforced:

- When the programme modifies a variable that appears in both the postcondition and elsewhere in the invariant, the substitution can cascade — always substitute systematically.
- When the guard involves `≤` vs. `<`, the exit condition changes and the invariant's bound must account for the off-by-one.

---

## Exercise Sheet 3 — Arrays and Combined Exercises

Sheet 3 adds [ARRAY-READ] and [ARRAY-ASSIGN] to the earlier material. Key patterns:

- Every array read requires a `def(a[i])` guard in the precondition.
- Array write preconditions use the array-update notation `a[i ← E]`.
- Loop invariants over arrays must state the property for all elements examined so far (`∀k. 0 ≤ k < i ⇒ …`) plus the bounds `0 ≤ i ≤ sizeof(a)`.

---

## Examples Page

See [[examples/ict3112-hoare-exercises-worked]] for a condensed set of key worked proofs.
