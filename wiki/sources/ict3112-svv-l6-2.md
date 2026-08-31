---
type: source
title: "ICT3112 SVV — Lecture 6.2: Blackbox Testing — Decision Table Testing and State Transition Testing"
source_file: "raw/ICT3112 Software Verification and Validation - L6_2_Blackbox_Testing_DecisionTableTesting_and_StateTransitionTesting.md"
domain: software-verification-validation
tags: [ict3112, svv, blackbox-testing, decision-table, state-transition-testing]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 6.2: Decision Table Testing and State Transition Testing

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Decision Table Testing

### Purpose

- Precise way to model complicated logic
- Useful basis for test design
- Associates decisions (system conditions) with actions to be performed
- Decisions and actions are True/False (Yes/No)

### Structure

```
             Rule 1   Rule 2   Rule 3
Decision 1   Yes/No   Yes/No   Yes/No
Decision 2   Yes/No   Yes/No   Yes/No
Decision 3    ----    Yes/No   Yes/No   ← unreachable decision for this rule
Action 1     Yes/No   Yes/No   Yes/No
Action 2     Yes/No   Yes/No   Yes/No
```

Each **column** (Rule) defines a unique combination of conditions that results in the execution of specific actions.

---

## Decision Table — Movie Ticket Pricing (Example 1)

Rules: Basic price $20; students get 10% discount; people under 21 get 5% discount; discounts are accumulative.

| Condition | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|-----------|--------|--------|--------|--------|
| Is the customer a student? | Yes | Yes | No | No |
| Aged below 21? | Yes | No | Yes | No |
| **Give discount up to:** | **15%** | **10%** | **5%** | **None** |

Test cases: one input per column, e.g.:
- Rule 1: student aged 19 → 15% discount
- Rule 2: student aged 25 → 10% discount
- Rule 3: non-student aged 18 → 5% discount
- Rule 4: non-student aged 25 → no discount

---

## Decision Table — Movie System Validation (Example 2)

System checks movie ID validity (3 digits, 100–300), then payment validity:

| Condition | Rule 1 | Rule 2 | Rule 3 |
|-----------|--------|--------|--------|
| Movie ID is valid? | N | Y | Y |
| Is payment valid? | — | N | Y |
| **Show welcome screen** | **Y** | **N** | **N** |
| **Reject payment** | **N** | **Y** | **N** |
| **Supply movie tickets** | **N** | **N** | **Y** |

Test cases:
- Rule 1: Movie ID = 332 (out of range) → show welcome screen
- Rule 2: Movie ID = 113 (valid), card = "12" (invalid) → reject payment
- Rule 3: Movie ID = 209 (valid), card = "12345678" (valid) → supply ticket

---

## Decision Table Constraints

Source: Boris Beizer, *Software Testing Techniques*

1. The order in which conditions are evaluated does **not** affect the resulting action
2. The order in which rules are evaluated does **not** affect the resulting action
3. Once a rule is satisfied and an action taken, no other rule needs to be examined
4. If multiple actions result from one rule, the order of those actions is ignored
5. For **n binary decisions**: there should be **2ⁿ cases** considered (maximum)
6. Find test input values that force each test to result in the specified action

---

## State Transition Testing

### Purpose

Test design technique in which test cases are designed to execute **valid and invalid state transitions** in a system.

### Applications

- Testing protocols between systems, humans and machines, and between system modules
- User transaction flows where transactions can stay in the system indefinitely (e.g., online users)
- High-level control functions within an OS (e.g., security handling of read/write permissions)

### Components

| Component | Definition |
|-----------|-----------|
| **State** | A combination of attributes/conditions of interest; a set of variables with specific values characterising a unique situation. Includes initial, final states; may have a duration. |
| **Transition** | As a result of an input/event, the system's state changes. Transitions link states (can return to the same state). |
| **Input / Event** | Causes transitions; marked beside directional arrows. Considered instantaneous phenomena. |
| **Output / Action** | Associated with every combination of input and transition. |

---

## Door Lock Face Recognition — Worked Example

### State Diagram

**States**:
- **S1**: Wait for Recognised Face
- **S2**: Face Recognised, Door Unlocked
- **S3**: Wait to Activate System

**Transitions**:

| Current State | Input | Output | Next State |
|--------------|-------|--------|------------|
| S1 | Face = unrecognised (FU) | System keeps door locked (DL) | S1 |
| S1 | Face = recognised (FR) | System unlocks door (UD) | S2 |
| S2 | Door reclosed (DR) | Sensors activated (SA) | S3 |
| S2 | Set lock off (SLO) | Sensors disabled & alarm off (SD&AO) | ??? (unspecified) |
| S3 | No face detected (NFD) | System idle (SI) | S3 |
| S3 | Face detected (FD) | System on (SO) | S1 |

**Note**: Row 3 (S2 + SLO) shows an **unspecified behaviour** — S1 doesn't capture the state after this transition. A real system must define this.

### Learning from State Diagrams

- **Unspecified behaviours** and transitions
- **Unreachable states** (no path leads to them)
- **Dead states** (no exit path exists)

---

## 0-Switch Coverage (All Transitions)

Test one case per state transition:

| TC | Start | Input | Expected Output | Finish |
|----|-------|-------|-----------------|--------|
| 1 | S1 | FU | DL | S1 |
| 2 | S1 | FR | UD | S2 |
| 3 | S2 | DR | SA | S3 |
| 4 | S2 | SLO | SD&AO | (unspec) |
| 5 | S3 | NFD | SI | S3 |
| 6 | S3 | FD | SO | S1 |

6 test cases achieve 0-switch coverage.

---

## 1-Switch Coverage (All Unique Transition Pairs)

Also called **switch coverage** — tests every unique pair of consecutive state transitions. Self-loops (S1→S1→S1, S3→S3→S3) are excluded per ISTQB/SELA definition.

10 test cases achieve 1-switch coverage (see full table in lecture slides).

**Note**: The course follows the ISTQB/SELA (Software Education Labs) definition; T.S. Chow's original definition may differ slightly.

---

## Linked Concepts

- [[concepts/blackbox-testing-techniques]] — comprehensive blackbox reference (all five techniques)
- [[concepts/test-design-techniques]] — EP, BVA, decision tables, state transition overview
