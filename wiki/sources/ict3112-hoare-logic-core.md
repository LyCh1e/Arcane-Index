---
type: source
title: "ICT3112 Formal Verification — Hoare Logic Core Rules (Modules 0–6)"
domain: formal-verification
source-type: lecture-notes
course: ICT3112
status: ingested
created: 2026-10-15
updated: 2026-10-15
tags: [ict3112, hoare-logic, formal-verification, axiomatic-semantics, weakest-precondition, skip-rule, assignment-rule, consequence-rule, sequential-composition, conditional-rule, loop-rule, dr-david-sanan]
---

# Source: ICT3112 Formal Verification — Hoare Logic Core Rules (Modules 0–6)

**Files:**
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 0 - Introduction - Copy.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 1 - Hoare Logic and Skip Rule - Copy.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 2 - Assignment Rule.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 3 - Consequence Rule.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 4 - Sequential Composition Rule.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 5 - Conditional Rule.md`
- `raw/ICT3112 Software Verification and Validation - ICT3112 - 6 - Loops.md`

**Presenter:** Dr. David Sanan, Singapore Institute of Technology

---

## Summary

Modules 0–6 build the complete Hoare Logic proof system for a simple imperative language from the ground up. Module 0 motivates formal verification with historical failures (Therac-25, Ariane 5, Patriot missile) and establishes the verification vs. validation distinction. Modules 1–6 each introduce one inference rule — SKIP, ASSIGN (with Dijkstra's Weakest Precondition Calculus), CONSEQUENCE, SEQ, IF, and WHILE — providing the full toolkit for verifying partial correctness of straight-line and looping programmes.

---

## Learning Outcomes

- Explain why formal methods are necessary and how they differ from testing.
- Read and construct Hoare triples `{P} C {Q}`.
- Apply all six inference rules to check or construct a proof.
- Use Dijkstra's `wp` calculus to mechanically derive weakest preconditions for sequences.
- Prove loop partial correctness using a loop invariant and the WHILE rule.
- Use a loop variant to prove termination.

---

## Module Coverage

### Module 0 — Introduction to Formal Verification

- Historical failures: Therac-25 (arithmetic overflow → patients irradiated), Ariane 5 (conversion overflow → £370 M loss), Patriot missile (clock desynchronisation → 28 soldiers killed), blockchain exploits ($3.6 bn stolen in 2022).
- Core argument: testing is incomplete; formal methods can prove zero errors.
- Taxonomy: Validation (are we building the right thing?) vs. Verification (are we building it right?).
- Logic hierarchy: Propositional Logic → First-Order Logic → Hoare Logic → Temporal Logic.

### Module 1 — Hoare Logic and Skip Rule

- **Hoare triple** `{P} C {Q}`: if *P* holds before executing *C*, and *C* terminates, then *Q* holds afterwards.
- Assertions as sets of states: `{x = 0 ∧ y = 1}` denotes every state satisfying those equalities.
- Operational semantics sketch: configurations `⟨program, state⟩` step to `⟨SKIP, final_state⟩`.
- **[SKIP]** `{Q} SKIP {Q}` — SKIP leaves the state unchanged; any postcondition that held before still holds after.
- SKIP fills a missing ELSE branch: `IF B THEN c` desugars to `IF B THEN c ELSE SKIP`.

### Module 2 — Assignment Rule and Weakest Precondition Calculus

- **[ASSIGN]** `{Q[x ← E]} x := E {Q}` — the precondition is *Q* with every free occurrence of *x* replaced by the expression *E*.
- Intuition: to end in a state satisfying *Q*, we need the expression *E* to already satisfy *Q* before the assignment executes.
- Key examples: `{y + z = c} x := y + z {x = c}`, `{y + 1 = 2} y := y + 1 {y = 2}` simplifies to `{y = 1}`.
- **Dijkstra's Weakest Precondition Calculus:**
  - `wp(x := E, Q) = Q[x ← E]`
  - The *wp* is the *largest* (weakest) set of states from which *C* is guaranteed to terminate in a state satisfying *Q*.
  - `∀P. (P ⇒ wp(C, Q)) ⇒ {P} C {Q}`

### Module 3 — Consequence Rule

- Motivation: [ASSIGN] always gives the weakest precondition. To verify a stronger given precondition (or a weaker postcondition), we need a bridge.
- **[CONSEQUENCE]** `P → P'   {P'} c {Q'}   Q' → Q  ⊢  {P} c {Q}`
  - Weaken the precondition: if `P → P'` and `{P'} c {Q}` then `{P} c {Q}`.
  - Strengthen the postcondition: if `{P} c {Q'}` and `Q' → Q` then `{P} c {Q}`.
- Example: to verify `{x > 120} x := x + 1 {x > 101}`, ASSIGN gives `{x > 100}` as precondition; then `x > 120 → x > 100` closes the gap.

### Module 4 — Sequential Composition Rule

- **[SEQ]** `{P} c₁ {R}   {R} c₂ {Q}  ⊢  {P} c₁; c₂ {Q}` — an intermediate assertion *R* serves as both the postcondition of *c₁* and the precondition of *c₂*.
- For *n* instructions, apply SEQ recursively from the last statement to the first.
- **WP for sequences:** `wp(c₁; c₂, Q) = wp(c₁, wp(c₂, Q))` — compute from right to left.
- Worked three-instruction example (variable-swap via `c := a + b; a := a - c; b := b + a`): calculate *R₃*, *R₂*, *R₁* by back-propagating wp, then show `P → R₃` via the consequence rule.

### Module 5 — Conditional Rule

- **[IF]** `{P ∧ B} c₁ {Q}   {P ∧ ¬B} c₂ {Q}  ⊢  {P} IF B THEN c₁ ELSE c₂ {Q}`
- Intuition: each branch sees the precondition *P* plus the truth-value of the guard, so both branches must independently reach *Q*.
- **WP for conditionals:** `wp(if B then c₁ else c₂, Q) = (B ⇒ wp(c₁, Q)) ∧ (¬B ⇒ wp(c₂, Q))`
- Worked example: `{x + y = 0} if (x = y) then x := y + 1 else x := 1 − x {x = y + 1}`.

### Module 6 — Loop Rule and Termination

- **[WHILE]** `{I ∧ B} c {I}  ⊢  {I} WHILE B DO c {I ∧ ¬B}`
  - Requires a *loop invariant* I: a predicate true before each iteration that is preserved by the body.
  - Postcondition is `I ∧ ¬B` (invariant still holds, guard is now false).
- **Extended rule with consequence:** `P ⇒ I   {I ∧ B} c {I}   I ∧ ¬B ⇒ Q  ⊢  {P} WHILE B DO c {Q}`
- **WP for loops:** precondition = I, plus the checks `(B ∧ I) ⇒ wp(c, I)` and `(¬B ∧ I) ⇒ Q` in every state.
- **Termination / Variant:** `{I ∧ B ∧ (E = n)} c {I ∧ E < n}   I ∧ B ⇒ E ≥ 0  ⊢  terminates`
  - The variant *E* must be non-negative when the loop runs and must strictly decrease each iteration.
- Worked examples: `while (x > 0) x := x − 1` with invariant `x ≥ 0`; a counter loop `{i = 0} while (i < 10) i := i + 1` with invariant `i ≤ 10` and variant `10 − i`.

---

## Concept Pages Generated

- [[concepts/hoare-logic]] — full treatment of all six rules and WP calculus
- [[concepts/loop-invariants]] — loop invariants, the four proof obligations, and the discovery recipe
