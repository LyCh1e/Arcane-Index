---
type: learning
title: "Hoare Logic — Bottom-Up Proof Method (and Why Top-Down Fails)"
domain: formal-verification
course: ICT3112
created: 2026-10-22
updated: 2026-10-22
tags: [hoare-logic, weakest-precondition, proof-methodology, bottom-up, assessment-critical]
---

# Hoare Logic — Bottom-Up Proof Method (and Why Top-Down Fails)

> **Assessment-critical:** Dr Sanan stated in the Week 4 lecture that **top-down proofs will receive zero marks** unless perfectly correct, and the exam questions are designed so that top-down will be wrong. Always work **bottom-up**.

---

## What "Bottom-Up" Means

When verifying a Hoare triple `{P}  C  {Q}`:

- **Top-down:** start from P, execute each statement forward, accumulate intermediate assertions towards Q.
- **Bottom-up:** start from Q, apply the [ASSIGN] or other rules *backwards* (right to left through the code), compute intermediate weakest preconditions, arrive at a final WP, then check `P ⟹ WP`.

The **bottom-up direction** is the standard methodology. Dijkstra's `wp(C, Q)` calculus is defined bottom-up.

---

## Why Top-Down Fails

When the variable being assigned *also appears in the assignment expression*, top-down requires introducing an **existential quantifier** to track the old value:

```
// top-down for A := A*2 starting from {A > 2}
// you must say: ∃A₀. A₀ > 2 ∧ A = A₀*2
```

Existential quantification is not part of the introductory Hoare Logic rules taught in this module. Top-down only works cleanly when the assigned variable does *not* appear on the RHS. If you top-down and get it wrong, **you get zero**.

---

## The Bottom-Up Recipe for Sequential Composition

Given `{P}  c₁; c₂; …; cₙ  {Q}`:

1. Start with `R := Q`.
2. Working **right to left**, for each statement `cᵢ`:
   - If `cᵢ` is `x := E`: replace every free occurrence of `x` in `R` with `E`. The result is the new `R`.
   - If `cᵢ` is `IF B THEN c_t ELSE c_f`: apply the [IF] wp formula to `R`.
   - If `cᵢ` is `WHILE B DO c` with invariant `I`: use [WHILE] rule (separate treatment).
3. After processing `c₁`, you have the **weakest precondition** `wp(c₁;…;cₙ, Q)`.
4. Check that `P ⟹ wp(…)`. If yes, the triple is **correct**.

---

## Worked Example from Lecture (Week 4)

**Triple:** `{A > 2}  A := A*2;  B := A+1  {B > 5}`

| Step | Direction | Statement | Current assertion | Substitution | Result |
|---|---|---|---|---|---|
| Start | ← | — | `B > 5` | — | `B > 5` |
| 1 | ← | `B := A+1` | `B > 5` | B ← A+1 | `A+1 > 5` |
| 2 | ← | `A := A*2` | `A+1 > 5` | A ← A*2 | `A*2+1 > 5` |

**WP = `A*2+1 > 5`**. Simplify: `A*2 > 4` ↔ `A > 2`.

Check: `A > 2 ⟹ A > 2`. ✓ Triple is **correct**.

---

## Common Mistakes

| Mistake | Effect |
|---|---|
| Going left-to-right (top-down) | Will introduce existential quantifiers; likely wrong |
| Forgetting to substitute the **assigned variable** (not the RHS) | Wrong result |
| Substituting only the first occurrence of the variable | Wrong — substitute **all free occurrences** |
| Checking `WP ⟹ P` instead of `P ⟹ WP` | Backwards implication; wrong direction |
| Simplifying too early (before the full substitution pass) | May miss terms |

---

## Set-Theoretic Intuition for the Final Implication Check

Hoare Logic assertions denote *sets of states*. `P ⟹ WP` means the set of states where P holds is a *subset* of the set where WP holds. Because P is the **given** precondition and WP is the **weakest** one that makes the code correct, any P that is *at least as strong as* WP (i.e. P's set is smaller or equal) guarantees correctness.

---

## Related Pages

- [[concepts/hoare-logic]] — full rule set, WP calculus table
- [[sources/ict3112-lecture-w4-sec2-intro-transcript]] — lecture where this warning was given
- [[examples/ict3112-hoare-exercises-worked]] — more worked proofs
