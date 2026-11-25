---
type: concept
title: "Requirements Engineering"
domain: software-engineering
course: ICT2113
complexity: high
tags: [re, srs, bcic, mccall, irtm, heavyweight-rcm]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000002
---

# Requirements Engineering

Requirements Engineering (RE) is the heavyweight Requirements Change Management (RCM) approach: a systematic, document-driven discipline for capturing, formalising, and controlling what a system must do. It is the difference between building the wrong system perfectly and building the right system imperfectly — RE argues that the former failure mode is far more expensive.

## The Five RE Activities

RE is not a single step but a lifecycle of five interlocked activities:

| Activity | What happens | Key output |
|----------|-------------|-----------|
| **Eliciting** | Extract needs from stakeholders via interviews, workshops, observation | Raw requirements list |
| **Analysing** | Resolve conflicts, remove ambiguity, identify gaps | Conflict resolution report |
| **Specifying** | Write formal documents (PS, SRS) | Problem Statement, SRS |
| **Validating** | Check specs against actual stakeholder needs | Validation report, sign-offs |
| **Managing** | Track, version, and control changes over project life | iRTM, change log |

These activities are iterative, not sequential — validation findings loop back to elicitation.

## Problem Statement (PS) vs SRS

The **Repository** is the version-controlled store of all RE artefacts. It contains two primary documents:

### Problem Statement (PS)
- Short (1–3 pages), stakeholder-facing
- Defines the problem, context, and scope in business language
- Excludes implementation details
- Audience: client, project sponsor, management

### Software Requirements Specification (SRS)
- Comprehensive, developer-facing
- IEEE 830 / ISO/IEC 29148 standard structure
- Contains: functional requirements, non-functional requirements, constraints, assumptions
- Audience: developers, testers, architects
- Must be **complete, consistent, unambiguous, verifiable, traceable**

## BCIC Framework

The **BCIC framework** is a technique for analysing raw requirements gathered during elicitation:

1. **Breakdown** — decompose compound requirements into atomic statements
2. **Clarify** — remove ambiguous language ("fast", "user-friendly", "secure") by quantifying
3. **Interpret** — determine the intent behind stated requirements; surface hidden requirements
4. **Categorise** — classify as functional (what the system does) or non-functional (how well it does it)

BCIC is applied during the Analysing activity and produces cleaner input to the Specifying activity.

## Mag7 Quality Features

The Mag7 are the seven most commonly examined requirement quality attributes:

1. **Correct** — accurately reflects stakeholder intent
2. **Unambiguous** — one and only one interpretation
3. **Complete** — no missing information
4. **Consistent** — no contradictions internally or across the document
5. **Ranked** — prioritised by importance/stability
6. **Verifiable** — a test can confirm or deny it
7. **Traceable** — can be traced to its source and forward to design/test

## McCall's Software Quality Model

McCall's model (1977) organises software quality into three **perspectives** and eleven **features**:

### Three Perspectives

| Perspective | Question | Features |
|------------|----------|----------|
| **Product Operation** | How well does it run? | Correctness, Reliability, Efficiency, Integrity, Usability |
| **Product Revision** | How easily can it change? | Maintainability, Testability, Flexibility |
| **Product Transition** | Can it move to a new environment? | Portability, Reusability, Interoperability |

### Eleven Quality Features

- **Correctness** — does it meet specifications?
- **Reliability** — does it fail within acceptable rates?
- **Efficiency** — does it use minimal resources?
- **Integrity** — does it resist unauthorised access?
- **Usability** — how much effort does a user need?
- **Maintainability** — how much effort to locate and fix defects?
- **Testability** — how much effort to test it?
- **Flexibility** — how much effort to modify it?
- **Portability** — how much effort to move it to a new environment?
- **Reusability** — can components be reused elsewhere?
- **Interoperability** — how much effort to couple it to another system?

## iRTM — Incremental Requirements Traceability Matrix

The **iRTM** maps every requirement to four columns:
1. **Source** — the stakeholder or document that generated it
2. **Requirement ID** — unique identifier in the SRS
3. **Design artefact** — which module/component implements it
4. **Test case** — which test verifies it

Benefits:
- **Impact analysis** — when a requirement changes, the iRTM shows everything affected
- **Coverage verification** — confirms every requirement has a test
- **Audit trail** — demonstrates traceability to auditors and clients

The "Incremental" qualifier means the matrix is populated progressively as the project evolves, not all at once upfront.

## Three Change Mitigation Strategies

Requirements will change. RE provides three strategies to manage this:

1. **Requirements Baseline** — freeze the SRS at a defined point; all subsequent changes go through formal change control
2. **Change Control Board (CCB)** — a committee that evaluates, approves/rejects, and prioritises change requests
3. **Version Control of RE Artefacts** — store PS, SRS, and iRTM in a VCS so changes are auditable

## Relation to Lightweight RCM

Heavyweight RE is appropriate for safety-critical systems, large distributed teams, fixed-price contracts, and regulated industries. For iterative, customer-collaborative projects, see [[lightweight-rcm]] for User Stories and UseCase 2.0. The two approaches share the goal of accurate requirements but differ radically in ceremony and documentation overhead.

## See Also

- [[lightweight-rcm]] — agile alternative with User Stories and UseCase 2.0
- [[ICT2113-software-modelling]] — source course
- [[needfinding-and-task-analysis]] — HCI needfinding methods overlap with RE elicitation
