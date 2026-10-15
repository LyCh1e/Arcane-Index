---
type: source
title: "ICT3112 Formal Verification — Loop Invariants: Discovering and Recipe (Module 7)"
domain: formal-verification
source-type: lecture-notes
course: ICT3112
status: ingested
created: 2026-10-15
updated: 2026-10-15
tags: [ict3112, hoare-logic, loop-invariants, invariant-discovery, weakest-precondition, formal-verification, generalisation, trace-method, dr-david-sanan]
---

# Source: ICT3112 Formal Verification — Loop Invariants (Module 7)

**Files (15 parts):**
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Discovering Loop Invariants.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Discovering Loop Invariants - 0b.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Discovering Loop Invariants - 1a.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Discovering Loop Invariants - 2a.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Discovering Loop Invariants - 2b.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - 0a.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - 0b.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - Example 1a.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - Example 1b.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - Example 2.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - Example 3a.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - Example 3b.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - exercises.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - tips a.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 7 - Recepy for Loop Invariants - tips b.md`

**Presenter:** Dr. David Sanan, Singapore Institute of Technology

---

## Summary

Module 7 addresses the hardest part of loop verification: *where does the invariant come from?* The "Discovering" section explains what invariants are, why they cannot be found by simply unfolding iterations, and what the four proof obligations mean. The "Recipe" section gives a five-step heuristic (Q, Trace, Generalise, Bounds, Check) that produces correct invariant candidates for the loops typical of this course, and walks through three extended worked examples.

---

## What Invariants Are and Why They Matter

An invariant is a predicate *I* that is a *snapshot* of the loop state at every loop-head: it must hold before the first iteration and must be preserved by each body execution.

- **Not unique:** multiple invariants can be valid for the same loop; the choice affects what postcondition you can prove.
- **Specification role:** `{I} WHILE B DO c {I ∧ ¬B}` — the invariant is the loop's contract. It states what the loop assumes on entry and guarantees on exit.
- **Why unfolding does not work:** for a 64-bit integer variable, a worst-case loop could have 2⁶⁴ iterations. Invariants reduce an unbounded unfolding to exactly four finite checks.

---

## Four Proof Obligations

To prove `{P} WHILE B DO c {Q}` using invariant *I* and variant *E*:

| Obligation | Statement | Meaning |
|---|---|---|
| **Establishment** | P ⇒ I | The invariant holds before the first iteration |
| **Preservation** | {I ∧ B} c {I} | One arbitrary iteration keeps the invariant |
| **Exit** | I ∧ ¬B ⇒ Q | When the guard is false the invariant gives the postcondition |
| **Termination** | I ∧ B ⇒ E ≥ 0; {I ∧ B ∧ E = n} c {I ∧ E < n} | The variant is non-negative while the loop runs and strictly decreases each iteration |

Establishment and Exit come from the Consequence Rule; Preservation is the core loop check.

---

## The Five-Step Recipe for Finding Invariants

Finding and checking are separate activities. The recipe is a *heuristic* that works for the loops in this course; checking is always mechanical.

### Step 1 — Start from the Postcondition (Q)

Identify the *progress variable* (the counter that moves from initial to final value) and the *result variable* (the one constrained by *Q*). The postcondition is the material from which the invariant is built.

### Step 2 — Trace the Values at the Loop Head

Construct a table showing the values of the key variables at each loop-head for a small concrete example. Identify the pattern — what formula holds in every row?

### Step 3 — Generalise the Postcondition

Replace the *final value* of the progress variable in *Q* with the progress variable itself. This turns "the result at the end" into "the result so far". Sanity check: substituting the final value back must recover *Q* exactly.

**Example:** `{n ≥ 0} i := 0; s := 0; while (i < n) { i := i + 1; s := s + i; } {s = n(n+1)/2}`
- Q says `s = n(n+1)/2`. At exit, `i = n`.
- Generalise: replace *n* (the final value of *i*) with *i* to get `s = i(i+1)/2`.

### Step 4 — Add Bounds for the Counter

Append the range of the counter: `0 ≤ i ≤ n` (or whatever fits the loop). This ensures Establishment and Exit work cleanly.

Full invariant: `I ≡ s = i(i+1)/2  ∧  0 ≤ i ≤ n`

### Step 5 — Check

Verify the four obligations mechanically using WP:
- **Establishment:** `n ≥ 0 ⇒ wp(i := 0; s := 0, I)` — compute wp backwards and check.
- **Preservation:** `{I ∧ B} body {I}` — compute `wp(body, I)` and check `I ∧ B ⇒ wp(body, I)`.
- **Exit:** `I ∧ ¬B ⇒ Q` — substitute `i = n` from `¬B ∧ bounds`.
- **Termination:** variant `E = n − i`; show `I ∧ B ⇒ E ≥ 0` and `wp(body, E < E₀) = n − (i+1) < E₀`.

---

## Which Occurrences of *n* to Replace

When *Q* mentions *n* multiple times, only replace occurrences that represent *the final value of the progress variable*. Occurrences that represent a *constant of the problem* (e.g., the amount added each iteration) remain. The trace and the preservation check resolve any ambiguity: use the candidate that satisfies preservation.

---

## Worked Examples (three from the lecture)

### Example 1 — Triangular Sum
`{n ≥ 0} i := 0; s := 0; while (i < n) { i := i + 1; s := s + i; } {s = n(n+1)/2}`
- I ≡ `s = i(i+1)/2  ∧  0 ≤ i ≤ n`, E = `n − i`

### Example 2 — Repeated Addition (multiplication)
`{n ≥ 0 ∧ m ≥ 0} i := 0; p := 0; while (i < n) { p := p + m; i := i + 1; } {p = n · m}`
- I ≡ `p = i · m  ∧  0 ≤ i ≤ n`, E = `n − i`

### Example 3 — Maximum Element (array)
`{1 ≤ n ≤ length(A) ∧ m = A[0] ∧ i = 1} while (i < n) { if (A[i] > m) m := A[i]; i := i + 1; } {m = max(A[0..n−1])}`
- I ≡ `m ≥ A[k] for all 0 ≤ k < i  ∧  m = A[j] for some 0 ≤ j < i  ∧  1 ≤ i ≤ n`, E = `n − i`

---

## Concept Pages Generated

- [[concepts/loop-invariants]] — discovery recipe, proof obligations, and variant reasoning
