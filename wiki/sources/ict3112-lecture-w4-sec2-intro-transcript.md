---
type: source
title: "ICT3112 — Week 4 Lecture: Second Half Module Intro (Transcript)"
domain: formal-verification
course: ICT3112
format: lecture-transcript
lecturer: "Dr David Sanan"
date: 2026-10-22
tags: [ict3112, hoare-logic, weakest-precondition, deductive-verification, frama-c, llm-integration, module-dynamics, assessment]
---

# ICT3112 — Week 4 Lecture: Second Half Module Intro

Lecture transcript from the first session of the second half of ICT3112 Software Verification and Validation. Delivered live; lower signal-to-noise than slide notes due to real-time speech.

---

## Module Dynamics for the Second Half (Weeks 4–6)

### Change from Previous Year

The module previously covered Weeks 1–3 (Hoare Logic) and Weeks 4–6 (SPIN/Promela model checking). The second half has been **replaced** with an extended Hoare Logic block covering:

- **Week 4 (this week):** sequential composition and assignment (revision + exercises)
- **Week 5:** conditional branching + deeper loop rules
- **Week 6:** loops and arrays

Model checking (Promela/SPIN) has been dropped in response to student feedback that the module was overloaded.

### Why the Extension Matters

Even in the age of LLMs, understanding invariants and formal specifications is valuable:
- You will increasingly provide *specifications* (preconditions, postconditions, invariants) to tools and agents.
- LLMs produce better results when prompted with a precise architecture / design *before* open-ended coding.
- The professor's advice for industry and for IWSP capstone: **design the system architecture first, then use the LLM**.

### Lecture Format

Lectures are practical (solving exercises from the exercise sheets). Watch the videos for theory; bring questions to the lecture.

---

## Lab Methodology Change

In previous years: students wrote ACSL annotations (preconditions, postconditions, invariants) directly in Frama-C's logic syntax.

**New approach (this cohort):**
1. Think about the specification in *natural language* — what variables must satisfy, what the invariant means.
2. Feed the natural-language description to an LLM.
3. LLM translates to ACSL logic.
4. Paste the ACSL output into the C file.
5. Run Frama-C/WP to check correctness.
6. If Frama-C rejects the spec, feed the error back to the LLM and iterate.

**Rationale:** practise the skill of *specifying* systems precisely (which transfers to LLM prompting in the real world), while not requiring students to hand-write complex logic syntax.

---

## Project (Weeks 4–6)

A multi-agent automated verification pipeline:

```
User input (natural-language system specification)
     │
     ▼
Agent 1 — split input into functions / modules
     │
     ▼
Agent 2 — translate each module spec into ACSL logic
     │
     ▼
Frama-C / WP — verify each function
     │
     ├─ PASS → done
     └─ FAIL → feedback string
                    │
                    ▼
              Agent 3 — refine ACSL logic using feedback
                    │ (loop until verification passes)
                    ▼
              Frama-C / WP — re-verify
```

Students implement this pipeline. The project is introduced in Week 5. Due end of Week 6.

---

## Assessment Structure (Second Half)

| Item | Scope | Week |
|---|---|---|
| **Quiz 1** | Assignments + conditional branching only | Week 3 |
| **Lab assessment** | Frama-C lab exercises | Week 3 |
| **Quiz 2** | Loops + arrays (harder) | Week 6 |
| **Project** | LLM + Frama-C automated pipeline | Week 6 |

Quiz 1 is described as "very easy"; Quiz 2 is substantially harder.

---

## Implication Refresher (Warmup Exercises)

The professor covered the truth table for A ⟹ B and motivated it set-theoretically:

| A | B | A ⟹ B |
|---|---|--------|
| F | F | T |
| F | T | T |
| T | F | **F** |
| T | T | T |

**Set-theoretic view:** `A ⟹ B` is valid iff the set denoted by A is a subset of the set denoted by B.

- **False** = ∅ (empty set). Strongest assertion — eliminates all states.
- **True** = full domain (e.g. all natural numbers). Weakest assertion — no information.
- `∅ ⊆ S` for any S, so **False implies everything**.
- `S ⊆ full domain` for any S, so **everything implies True**.
- `true ⟹ P` is invalid in general (`full domain ⊄ S` unless P = True).
- `P ⟹ false` is invalid in general (`S ⊄ ∅` unless P = False).

Key identities verified in lecture:

| Formula | Valid? | Reason |
|---|---|---|
| `False ⟹ True` | ✓ | ∅ ⊆ full domain |
| `False ⟹ P` | ✓ | ∅ ⊆ any set |
| `P ⟹ True` | ✓ | any set ⊆ full domain |
| `True ⟹ P` | ✗ (generally) | full domain ⊄ arbitrary set |
| `P ⟹ False` | ✗ (generally) | arbitrary set ⊄ ∅ |
| `X = X+1 ⟹ True` | ✓ | LHS is False (∅), False ⟹ anything |
| `X = X+1 ⟹ Y = Y+1` | ✓ | Both False; ∅ ⊆ ∅ |
| `X>Y ⟹ X<Y` | ✗ | disjoint sets; neither includes the other |
| `A∧B ⟹ A` | ✓ | intersection ⊆ A |
| `A∧B ⟹ B` | ✓ | intersection ⊆ B |
| `A ⟹ A∨B` | ✓ | A ⊆ union |
| `A∨B ⟹ A` | ✗ | union ⊄ A generally |
| `A∧B ⟹ A∨B` | ✓ | intersection ⊆ union |
| `A∨B ⟹ A∧B` | ✗ | union ⊄ intersection generally |

---

## First Worked Exercise (Sequential Composition)

**Claim:** `{A > 2}  A := A*2;  B := A+1  {B > 5}`

**Method:** bottom-up (postcondition → precondition). See [[learning/hoare-logic-bottom-up-proof-method]] for the full explanation and why top-down is forbidden.

**Step 1 — wp of `B := A+1` w.r.t. `B > 5`:**

Substitute B ← A+1 in postcondition:

```
A+1 > 5
```

This is the intermediate assertion R and the postcondition for Step 2.

**Step 2 — wp of `A := A*2` w.r.t. `A+1 > 5`:**

Substitute A ← A*2 in intermediate assertion:

```
A*2 + 1 > 5
```

This is the weakest precondition of the whole sequence.

**Step 3 — Check precondition implies WP:**

```
A > 2  ⟹  A*2 + 1 > 5
```

Simplify RHS: `A*2 + 1 > 5` ↔ `A*2 > 4` ↔ `A > 2`. ✓

The original triple is **correct**.

---

## Related Pages

- [[concepts/hoare-logic]] — full rule set and WP calculus
- [[learning/hoare-logic-bottom-up-proof-method]] — why bottom-up is mandatory and how to apply it
- [[examples/ict3112-hoare-exercises-worked]] — full worked exercise collection
- [[examples/ict3112-frama-c-labs-0-2]] — Frama-C lab sessions
