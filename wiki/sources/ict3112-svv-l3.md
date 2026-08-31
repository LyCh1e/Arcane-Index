---
type: source
title: "ICT3112 SVV — Lecture 3: Static Analysis"
source_file: "raw/ICT3112 Software Verification and Validation - L3_Static_Analysis.md"
domain: software-verification-validation
tags: [ict3112, svv, static-analysis, code-inspection, code-review, walkthrough]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 3: Static Analysis

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Definition

**Static Analysis / Static Testing**: testing of a component or system at the specification or implementation level, *without executing the code*.

**IEEE 1028-1997**: "A process or meeting during which a software product is examined by project personnel, managers, users, customers, user representatives, or other interested parties for comment or approval."

Two primary options: **Reviews** (inspections) and **Code Inspections**.

---

## Key Quotes

- **Inspection (Fagan 1976)**: "Inspections are a formal, efficient, and economical method of finding errors in design and code."
- **Technical Reviews (Freedman and Weinberg 1986)**: "…to provide management with reliable information as to the quality of the intermediate products being produced."
- **Structured Walkthrough (Yourdon 1985)**: "It is simply a peer group review of any product."

---

## Benefits of Static Testing

1. Early detection of defects
2. Defects are cheaper to correct early
3. Reduction in dynamic testing time and cost
4. Reduction in maintenance costs
5. Improved development productivity
6. Improved communications
7. Earlier or on-time delivery of high-quality products

**Source**: Fagan, "Advances in Inspections," *IEEE Transactions on Software Engineering*

---

## Four Review Types (Formality Spectrum)

| Type | Formality | Led By | Documentation | Key Purpose |
|------|-----------|--------|---------------|-------------|
| **Ad Hoc Review** | Informal | N/A (informal) | Optional | Quick defect detection; inexpensive |
| **Walkthrough** | Partially formal | Author of the product | Optional | Learning, understanding, identifying defects |
| **Technical Review** | Semi-formal | Trained moderator or technical expert | Required | Discuss, make decisions, find defects, check compliance |
| **Inspection** | Formal | Moderator (not the author) | Formal report required | Finding defects; quantitative quality data collection |

### Ad Hoc Review
- Informal, no fixed process
- Examples: code review by team lead; test case review by colleagues
- May include pair programming or technical lead review
- Main purpose: inexpensive, earliest possible defect detection

### Walkthrough
- Led by the author
- Uses scenarios, dry runs, peer groups
- Preparation meeting and documentation optional
- Can vary from informal to very formal in practice
- Examples: review of hardware architecture design, Microsoft Office usability principles

### Technical Review
- Documented; defect identification process required
- Led by a moderator; preparation meeting required
- Focus: technical content; discussions, decisions, alternatives evaluation
- Examples: DB schema review, software requirements specification, software design description, test documentation, build/installation procedures, release notes

### Inspection (Fagan 1976)
- Involves peer examination
- Formally led by a moderator (not the author)
- Includes metrics (defects found, inspection rate, etc.)
- Formal process based on rules and supporting checklists
- Has entry and exit criteria
- Preparation meeting required; formal follow-up process
- Main purpose: finding defects
- Examples: formal code inspection with group leader resulting in an inspection report; test scenario design review by designers group

---

## Code Inspection

### Purpose
- Examine source code to discover anomalies and defects
- Intended for **defect detection**, not correction
- Very effective for discovering errors early
- Saves time and money — earlier detection = lower correction cost

### Code Inspection Checklist — Fault Classes

| Fault Class | Static Analysis Checks |
|-------------|----------------------|
| **Data faults** | Variables used before initialisation; variables declared but never used; variables assigned twice without use between assignments; possible array bound violations; undeclared variables |
| **Control faults** | Unreachable code; unconditional branches into loops |
| **Input/Output faults** | Variables output twice with no intervening assignment |
| **Interface faults** | Parameter type mismatches; parameter number mismatches; non-usage of function return values; uncalled functions and procedures |
| **Storage management faults** | Unassigned pointers; pointer arithmetic |
| **Exception management faults** | Have all possible error conditions been taken into account? |

---

## Code Inspection Tools

- Automatically analyse code before execution
- Locate defects hard to find during dynamic testing (dead code, deadlocks, etc.)
- Used by developers before and during unit/integration testing
- Example tool: **ReSharper** (for C# / JetBrains)

### Tool Benefits
1. Early detection of defects
2. Early warning about suspicious code using metrics (e.g., code complexity)
3. Can identify defects hard to find during dynamic testing
4. Detecting dependencies and inconsistencies in code or design
5. Improved maintainability of code and design
6. Leads to future improvements and prevention of defects
7. Supported by some compilers

---

## Linked Concepts

- [[concepts/whitebox-testing-techniques]] — whitebox testing including control flow and data flow
- [[concepts/software-testing-fundamentals]] — testing fundamentals including static vs dynamic testing
- [[concepts/static-code-analysis]] — SAST tools and static analysis tooling details
- [[concepts/software-verification-and-validation]] — V&V context
