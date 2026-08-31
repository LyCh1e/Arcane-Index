---
type: source
title: "ICT3112 SVV — Lecture 6.0: Blackbox Testing — Introduction and Use Case Testing"
source_file: "raw/ICT3112 Software Verification and Validation - L6_0_Blackbox_Testing_Intro_and_UseCaseTesting.md"
domain: software-verification-validation
tags: [ict3112, svv, blackbox-testing, use-case-testing, functional-testing]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 6.0: Blackbox Testing — Intro + Use Case Testing

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Blackbox Testing Definition

> "A procedure to derive and/or select test cases based on an analysis of the specification, either functional or non-functional, of a component or system **without reference to its internal structure**."

---

## Five Blackbox Techniques

1. **Use Case Testing**
2. **Equivalence Partitioning**
3. **Boundary Value Analysis**
4. **Decision Table Testing**
5. **State Transition Testing**

---

## Use Case Testing

### Objective

Design test cases that execute user **scenarios** — the system is tested from the user's point of view.

- Focuses on functional system characteristics from the user's perspective
- Derived from use cases or business processes

### Use Case Requirements

A use case must be: readable, correct, specific, clear, complete, stable, up-to-date, and well-documented.

### Use Case Definition

> A "series of transactions between a user and system that yields a tangible result."

### Use Case Components

| Component | Description |
|-----------|------------|
| **Actors** | Users or external systems that interact with the system |
| **Preconditions** | Conditions that must be true before the use case executes |
| **Postconditions** | State of the system after the use case completes |
| **Primary system flow** | The main (happy path) sequence of actor actions and system responses |
| **Alternative flows** | Deviations from the primary flow (error cases, alternate paths) |

### Pros of Use Case Testing

- Describes real use of the system (convenient for end users/customers)
- Can describe business flow excluding technical details, or at the system level
- Can represent a type of process flow model (similar to data-flow diagrams, cause-effect graphs)

---

## Resource Management System — Worked Example

### Use Case Overview

| Field | Detail |
|-------|--------|
| **Overview** | Student requests to loan an item |
| **Actors** | Student, PO (Procurement Officer) |
| **Preconditions** | Student is logged into the system and has selected to request a resource |
| **Postconditions** | The loan request is sent to the PO |

### Primary System Flow

| Actor Actions | System Responses |
|--------------|-----------------|
| 1. Student enters item details | 2. System checks eligibility and passes the request |
| 3. Student selects item from list | 4. System displays loan request to PO |

**Alternative Flow A-1**: Student is ineligible for item loan:
- System displays failed eligibility message to student (flow diverges at step 2)

---

## Scenario-Based Test Cases

| Test Case | Initial State | Test Data | Expected Results |
|-----------|--------------|-----------|-----------------|
| **TC#1: Valid loan request** | Student logged in, on request page | Item type: MSP430; Item ID: 001; Time: ASAP | 1. System grants eligibility; 2. Allows selection of item 001; 3. Displays loan request to PO |
| **TC#2: Invalid loan (alternative)** | Student logged in, on request page | Item type: Chemical X; Time: ASAP | 1. System fails eligibility; 2. Displays failed eligibility message |

---

## What Scenarios Can Detect

1. Defects derived from **real-world use** of the system
2. **Integration defects** caused by interaction and interface of different components
3. System states that the system can enter but **cannot leave** (stuck states — e.g., stuck after failed eligibility check)
4. Defects that would occur in actual use but not in artificial test sequences

---

## Linked Concepts

- [[concepts/blackbox-testing-techniques]] — comprehensive blackbox reference (use case, EP, BVA, decision tables, state transition)
- [[concepts/software-testing-fundamentals]] — testing levels and types
