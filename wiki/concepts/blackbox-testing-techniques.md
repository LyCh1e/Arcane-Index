---
type: concept
title: "Blackbox Testing Techniques"
domain: software-verification-validation
complexity: high
status: established
created: 2026-08-31
updated: 2026-08-31
tags: [blackbox-testing, equivalence-partitioning, boundary-value-analysis, decision-table, state-transition-testing, use-case-testing, ict3112]
---

# Blackbox Testing Techniques

Blackbox testing derives test cases from the **specification** (functional or non-functional) without reference to the internal structure of the code. It focuses on *what* the system does, not *how* it does it. Applied at all testing levels, but most commonly at system and acceptance testing.

---

## Definition

> "A procedure to derive and/or select test cases based on an analysis of the specification, either functional or non-functional, of a component or system **without reference to its internal structure**."

---

## Five Blackbox Techniques

| Technique | Best For |
|-----------|---------|
| **Use Case Testing** | Testing end-to-end user scenarios; integration defects; flow-based defects |
| **Equivalence Partitioning** | Reducing test cases while maintaining coverage; all test levels |
| **Boundary Value Analysis** | Defects at the edges of valid/invalid input ranges |
| **Decision Table Testing** | Complex logic with multiple condition combinations |
| **State Transition Testing** | Systems with explicit states (FSMs, protocols, UIs) |

---

## 1. Use Case Testing

### Purpose

Design test cases that execute user **scenarios** — tests the system from the user's perspective, not the developer's.

- Derived from use cases or business processes
- Focuses on functional characteristics as experienced by end users

### Use Case Components

| Component | Description |
|-----------|------------|
| **Actors** | Users or external systems interacting with the system |
| **Preconditions** | Conditions that must hold before execution |
| **Postconditions** | State of the system after execution |
| **Primary system flow** | The happy-path sequence of actor actions and system responses |
| **Alternative flows** | Deviations from the primary flow (errors, exceptions, alternate paths) |

### What Scenario-Based Tests Detect

1. Defects arising from **real-world usage** patterns
2. **Integration defects** at the boundary of different components
3. **Dead-end states** — states the system can enter but cannot exit
4. Defects invisible in isolated unit tests but visible in realistic end-to-end flows

### Worked Example — Resource Loan System

| Field | Detail |
|-------|--------|
| Use case | Student requests to loan an item |
| Actors | Student, Procurement Officer (PO) |
| Preconditions | Student logged in; on "request resource" page |
| Postconditions | Loan request sent to PO (happy path) |

**Primary flow**: student enters item details → system checks eligibility → student selects item → system displays request to PO.

**Alternative flow A-1**: student is ineligible → system displays failed eligibility message.

**Test Cases**:

| TC | Data | Expected |
|----|------|---------|
| TC#1: Valid loan | Type: MSP430; ID: 001; Time: ASAP | System grants eligibility; displays request to PO |
| TC#2: Invalid loan | Type: Chemical X; Time: ASAP | System fails eligibility; displays error message |

---

## 2. Equivalence Partitioning (EP)

### Purpose

Minimise the number of test cases while maintaining broad requirements coverage.

### Mechanism

- Divide the input domain into groups (**equivalence partitions**) where every value in a group is expected to produce the same result
- Test one representative value per partition — testing one member is assumed equivalent to testing all members

### Example 1 — Integer Input 0 to 100

```
─────────────────────────────────────────────
Invalid 1   |      Valid      |   Invalid 2
  x < 0     |   0 ≤ x ≤ 100  |    x > 100
─────────────────────────────────────────────
 e.g. −10        e.g. 50        e.g. 110
```

**Minimum test set**: 3 test cases (one per partition).

### Example 2 — Binary Search in an Unsorted Array of 10 Positive Integers < 99

| Partition | Description | Example |
|-----------|------------|---------|
| Valid, found | `precondition = true` and element IS in array | 12 |
| Valid, not found | `precondition = true` and element is NOT in array | 95 |
| Precondition false | Input outside valid range | −19, 150, 1000 |

### EP Advantages / Disadvantages

| Advantages | Disadvantages |
|-----------|--------------|
| Easy to analyse | Excludes some inputs |
| Applicable at all test levels | No rule for selecting the specific value within a partition |
| Minimises test cases | No guarantee all elements of a partition are treated identically |
| Can partition both inputs and outputs | Very limited focus on interactions |

---

## 3. Boundary Value Analysis (BVA)

### Purpose

Design test cases specifically targeting **boundary values** — defects cluster at the edges of input ranges.

**Complements EP**: BVA selects max and min values of each partition boundary.

### Mechanism

- Select values **at** and **just beyond** each boundary
- Cover both valid and invalid boundaries for both input and output conditions

### Example 1 — Integer 0 to 100

| Value | Type |
|-------|------|
| 0 | Valid lower boundary |
| 100 | Valid upper boundary |
| −1 | Invalid lower boundary (just below) |
| 101 | Invalid upper boundary (just above) |

Extended (three-value boundary): also test 1 (low+1) and 99 (high−1) to exercise values just inside the valid range.

### Example 2 — String Input: First Name (1–10 Capital Letters, A–Z)

| Test Value | Type | Boundary Tested |
|-----------|------|----------------|
| "G" (1 char) | Valid | Lower string length |
| "A" (ASCII 65) | Valid | Lower ASCII character |
| "BORDERNAME" (10 chars) | Valid | Upper string length |
| "Z" (ASCII 90) | Valid | Upper ASCII character |
| null / empty | Invalid | No input (null boundary) |
| "@" (ASCII 64) | Invalid | Just below 'A' |
| "FAKEBIGNAME" (11 chars) | Invalid | Just above upper length |
| "[" (ASCII 91) | Invalid | Just above 'Z' |

**Key principle**: test ASCII boundary and string length boundary in **separate test cases** — combining them obscures which boundary caused the failure.

### Example 3 — Date Input (dd/mm/yyyy)

Assumptions: no older than 120 years; not beyond today + 31 days.

| Field | Valid Low | Valid High | Invalid Low | Invalid High |
|-------|-----------|-----------|-------------|-------------|
| dd | 1 | days_in_month | 0 | days_in_month + 1 |
| mm | 1 | 12 | 0 | 13 |
| yyyy | today − 120y | today + 31d | today − 121y | today + 32d |

*Remember leap years when testing dd with mm=2.*

### Example 4 — Time Input (HH:MM, 24-hour clock)

| Field | Valid Low | Valid High | Invalid Low | Invalid High |
|-------|-----------|-----------|-------------|-------------|
| HH | 00 | 23 | −01 | 24 |
| MM | 00 | 59 | −01 | 60 |

### Four General BVA Rules

| Rule | Guidance |
|------|---------|
| **1** | For a range of values: create valid tests at each end; invalid tests just beyond each end. Consider output conditions too. |
| **2** | For values without a specified range: use min and max values plus one below and one above. |
| **3** | For sets of values: test each value in the set and the set's size. For files: test first and last records. |
| **4** | For any extreme input or output condition: test each of them. |

**Output boundary example**: billing report must not exceed 6,000,000 subscribers.
- Valid outputs: 0 and 6,000,000
- Invalid outputs: −1 and 6,000,001

### BVA Advantages / Disadvantages

| Advantages | Disadvantages |
|-----------|--------------|
| Applicable at all test levels | Excludes some inputs |
| Can expose UI and input handling problems | Does not consider combinations of input values |
| Very clear guidelines for test design | |
| Capable of identifying a high number of defects | |

---

## 4. Decision Table Testing

### Purpose

Model complex logic precisely. Particularly valuable when multiple conditions combine to produce different outcomes.

### Structure

Each **column** (Rule) defines a unique combination of condition values that results in a specific set of actions.

```
             Rule 1   Rule 2   Rule 3
Condition 1   Y/N      Y/N      Y/N
Condition 2   Y/N      Y/N      Y/N
Condition 3   ─────    Y/N      Y/N    ← irrelevant (cannot be reached)
─────────────────────────────────────
Action 1      Y/N      Y/N      Y/N
Action 2      Y/N      Y/N      Y/N
```

**n binary conditions → maximum 2ⁿ rules to consider.**

### Example 1 — Movie Ticket Pricing

Basic price $20; student 10% discount; under-21 5% discount; discounts accumulative.

| Condition | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|-----------|--------|--------|--------|--------|
| Student? | Yes | Yes | No | No |
| Aged < 21? | Yes | No | Yes | No |
| **Discount** | **15%** | **10%** | **5%** | **None** |

### Example 2 — Movie System Validation

| Condition | Rule 1 | Rule 2 | Rule 3 |
|-----------|--------|--------|--------|
| Movie ID valid? | N | Y | Y |
| Payment valid? | — | N | Y |
| Show welcome screen | Y | N | N |
| Reject payment | N | Y | N |
| Supply ticket | N | N | Y |

### Decision Table Constraints

1. Condition evaluation order does not affect the resulting action
2. Rule evaluation order does not affect the resulting action
3. Once a rule is satisfied and an action is taken, no further rules are examined
4. If a rule triggers multiple actions, action order is ignored
5. **n binary decisions → 2ⁿ maximum cases**
6. Find input values that force each rule (column) to execute

---

## 5. State Transition Testing

### Purpose

Test design technique for systems with explicit **states** — design test cases that exercise valid and invalid state transitions.

### Applications

- Testing communication protocols (system-to-system, human-to-machine, module-to-module)
- User transaction flows where sessions persist (e.g., online users)
- High-level OS control functions (e.g., security handling of read/write permissions)

### Components

| Component | Definition |
|-----------|-----------|
| **State** | A unique situation in the system defined by a set of variables with specific values. Includes initial and final states; states may have a duration. |
| **Transition** | The system changes state in response to an input/event. Transitions link states and can return to the same state. |
| **Input / Event** | Causes a transition. Considered instantaneous in the model (e.g., a user action). Marked beside directional arrows. |
| **Output / Action** | Associated with every input+transition combination. |

### Learning from State Diagrams

Before writing tests, map the system as a state diagram and identify:
- **Unspecified transitions** — inputs that arrive in states where the system has no defined response
- **Unreachable states** — states with no path leading to them
- **Dead states** — states with no exit transition

### Worked Example — Face Recognition Door Lock

**States**: S1 (Wait for Recognised Face), S2 (Face Recognised, Door Unlocked), S3 (Wait to Activate System)

| From | Input | Output | To |
|------|-------|--------|----|
| S1 | Face unrecognised (FU) | Door stays locked (DL) | S1 |
| S1 | Face recognised (FR) | Door unlocked (UD) | S2 |
| S2 | Door reclosed (DR) | Sensors activated (SA) | S3 |
| S2 | Set lock off (SLO) | Sensors disabled & alarm off (SD&AO) | ??? ← unspecified |
| S3 | No face detected (NFD) | System idle (SI) | S3 |
| S3 | Face detected (FD) | System on (SO) | S1 |

### 0-Switch Coverage (All Transitions)

One test case per state transition:

| TC | Start | Input | Expected Output | Finish |
|----|-------|-------|-----------------|--------|
| 1 | S1 | FU | DL | S1 |
| 2 | S1 | FR | UD | S2 |
| 3 | S2 | DR | SA | S3 |
| 4 | S2 | SLO | SD&AO | (unspecified) |
| 5 | S3 | NFD | SI | S3 |
| 6 | S3 | FD | SO | S1 |

**6 test cases** achieve 0-switch coverage.

### 1-Switch Coverage (All Consecutive Transition Pairs)

Tests every unique **pair** of consecutive transitions. Self-loops (e.g., S1→S1→S1) are excluded.

**10 test cases** achieve 1-switch coverage (per ISTQB/SELA definition).

| Coverage | Also called | TCs | What it covers |
|---------|------------|-----|---------------|
| 0-switch | All-transitions | 6 | Every individual transition once |
| 1-switch | Switch coverage | 10 | Every unique pair of consecutive transitions |

*Note*: The course follows ISTQB/SELA's definition. T.S. Chow's original n-switch definition may include self-loops differently.

---

## Comparing the Five Techniques

| Technique | When to use | Strength | Limitation |
|-----------|------------|---------|-----------|
| Use Case Testing | System/acceptance; user-centric flows | Detects real-world and integration defects | Requires well-documented use cases |
| Equivalence Partitioning | All levels; large input domains | Efficient; minimises test cases | No guarantee all partition members behave identically |
| Boundary Value Analysis | All levels; any ranged input | High defect yield at boundaries; clear guidelines | Ignores input combinations |
| Decision Table | Complex multi-condition logic | Exhaustive coverage of condition combinations | Exponential growth with many conditions |
| State Transition | Protocol, FSM, UI flows | Exposes missing/dead/unspecified states | Requires a complete state model |

---

## Related Concepts

- [[concepts/test-design-techniques]] — overview of EP, BVA, decision tables, state transition, and whitebox coverage
- [[concepts/software-testing-fundamentals]] — testing levels where blackbox is applied (system, acceptance)
- [[concepts/software-verification-and-validation]] — V&V context
- [[concepts/whitebox-testing-techniques]] — complementary structure-based testing
