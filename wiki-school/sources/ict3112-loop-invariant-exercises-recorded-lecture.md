---
type: source
address: c-000159
title: "ICT3112 Formal Verification — Loop Invariant Exercises for the Recorded Lecture"
domain: formal-verification
source-type: exercise-solutions
course: ICT3112
status: ingested
created: 2026-11-25
updated: 2026-11-25
tags: [ict3112, hoare-logic, loop-invariants, invariant-discovery, variant, exercises, formal-verification, undo-check]
---

# Source: ICT3112 — Loop Invariant Exercises for the Recorded Lecture

**File:** `raw/ICT3112 Loop invariant exercises for the recorded lecture.md` (text extract of the 13-page PDF)

Six solved exercises that follow the six-step recipe from [[ict3112-loop-invariants]] (Q and progress variable, trace, generalise, bounds, three obligations, variant). Exercises 1 to 3 and 6 each break the "obvious" shortcut and show how to repair it. Exercises 4 and 5 are exam-style (marking-guide wording).

## The six exercises

| # | Loop | Invariant | Variant | Lesson |
|---|---|---|---|---|
| 1 | `i:=n; s:=0; while i>0 {s+=i; i-=1}`, Q: `s = n(n+1)/2` | `s = n(n+1)/2 − i(i+1)/2 ∧ 0≤i≤n` | `i` | Final value of `i` is 0, so "replace n by i" gives the wrong candidate `s = i(i+1)/2` |
| 2 | Odd numbers with helper `k`, Q: `s = n*n` | `s = i·i ∧ k = 2i+1 ∧ 0≤i≤n` | `n − i` | First candidate lacks a fact about `k`, so preservation fails |
| 3 | Integer square root, Q: `0≤r ∧ r·r≤n ∧ n<(r+1)²` | `0≤r ∧ r·r≤n` | `n − r` | Drop the conjunct that `¬B` already gives |
| 4 | `s += 2; i -= 1`, Q: `s = 2n` | `s + 2i = 2n ∧ 0≤i≤n` | `i` | `0 ≤ i` is needed at exit because `¬B` gives only `i ≤ 0` |
| 5 | `s := 1; s += 4`, Q: `s = 4n+1` | `s = 4i + 1 ∧ 0≤i≤n` | `n − i` | `i ≤ n` is needed at exit; `0 ≤ i` is not used (marking guide accepts its absence) |
| 6 | `a[i] := a[i] + 1` in place, Q: `∀k. 0≤k<n ⇒ a[k] = a₀[k]+1` | adds `∀k. i≤k<n ⇒ a[k] = a₀[k]` | `n − i` | "Not touched yet" slot is required when the body reads the cell it writes |

## New techniques and checks

- **Undo-check:** substitute the final value of the progress variable back into the candidate. If you do not get Q, reject it. This catches shortcut errors the trace may not.
- **General rule for step 3:** replace the *final value of the progress variable*, not "n". When the loop counts down, make the final value visible by subtracting a term that is zero at exit: `Q: s = n(n+1)/2 − 0·(0+1)/2`.
- **Conserved quantity reading:** `s + i(i+1)/2 = n(n+1)/2` (done plus still to do = total).
- **Partial replacement:** when Q mentions `n` twice (`n * n`), the trace decides which occurrences become `i` (`s = i·i`, not `s = i·n`).
- **Helper variables:** a variable in the body that is not in Q (here `k`) often needs its own relation in the invariant, in the "other relations" slot.
- **Drop a conjunct (Exercise 3):** if Q is a conjunction, compare each conjunct with `¬B`. The one `¬B` gives at exit stays out; using Q itself as I is too strong (establishment holds only for `n = 0`).
- **Where the guard is used:** Exercise 1 uses it for the lower bound `0 ≤ i−1`; the exam question uses it for the upper bound `i+1 ≤ n`. Exercise 3's guard supplies the whole second conjunct of preservation.
- **Variant needs the bounds too:** in Exercise 3, `r+1 ≤ (r+1)²` uses `0 ≤ r`, so the lower bound earns its place twice.
- **Diagnosis cheat-sheet:** preservation fails because the body needs a fact about a changing variable that I does not track.
- **Template slots for I:** produced so far, not touched yet, other relations, bounds.

## Counterexample states (useful in exam answers)

- Missing `0 ≤ i` (Ex. 1): `i = −2`, `s = n(n+1)/2 − 1` satisfy the equation and `i ≤ 0`, but `s ≠ n(n+1)/2`.
- Missing `k = 2i+1` (Ex. 2): `i=0, s=0, k=5, n=3` passes `I₁` and the guard, yet after one pass `s = 5 ≠ 1·1`.
- Missing `0 ≤ i` (Ex. 4): `i = −1`, `s = 2n+2`.
- Missing `i ≤ n` (Ex. 5): `i = n+1`, `s = 4n+5`.
- Missing "not touched yet" (Ex. 6): `n=3, i=1, a₀=[5,2,7], a=[6,9,7]` gives `a[1] = 10`, but `a₀[1]+1 = 3`.

## Related

- [[ict3112-loop-invariant-exercises-worked]] — condensed proofs
- [[loop-invariants]] — updated with these refinements
- [[select-store-axioms]] — used in Exercise 6
- [[ict3112-array-exercises-solved]] — the other new exercise sheet
