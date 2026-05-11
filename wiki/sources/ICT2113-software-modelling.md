---
type: source-index
title: "ICT2113 Software Modelling & Analysis"
course: ICT2113
institution: SIT
raw: "raw/ICT2113 Software Modelling & Analysis Notes.md"
domain: software-engineering
topics: [requirements-engineering, uml, agile, user-stories, usecase-2.0]
ingested: 2026-05-11
---

# ICT2113 — Software Modelling & Analysis

Software Modelling & Analysis (SMA) covers the theory and practice of capturing, analysing, and communicating software requirements before a single line of production code is written. The course argues that most project failures originate in poor requirements — ambiguous, incomplete, or untested — rather than in implementation defects.

## Course Overview

The module is split across two broad philosophies: **heavyweight Requirements Change Management (RCM)** — the traditional, document-driven approach — and **lightweight RCM** — the agile, story-driven approach. Understanding both is necessary because real projects mix them.

## Key Topics

### Requirements Engineering (RE)

RE is the systematic process of defining what a system must do. The five RE activities are:

1. **Eliciting** — gathering raw needs from stakeholders
2. **Analysing** — resolving conflicts, removing ambiguity
3. **Specifying** — writing formal documents (PS, SRS)
4. **Validating** — checking specs against real needs
5. **Managing** — tracking and controlling changes

See [[requirements-engineering]] for the full deep-dive including BCIC analysis, McCall's quality model, and iRTM.

### Problem Statement & SRS

The **Problem Statement (PS)** is a short, stakeholder-facing document that defines scope and context. The **Software Requirements Specification (SRS)** is the full technical artefact that developers implement against. Both live in the **Repository** — a version-controlled store of all RE artefacts.

### Lightweight RCM

User Stories and UseCase 2.0 replace heavy spec documents in agile contexts. See [[lightweight-rcm]] for:
- XP User Stories (3C's, INVEST, Connextra format)
- UseCase 2.0 (Jacobson's parent-UC / Story / Slice model, 8-step process)
- Heavyweight vs lightweight comparison
- Fragmentation debt

### UML Diagrams

The course covers structural and behavioural UML:
- **Use Case Diagrams** — actors, use cases, include/extend relationships
- **Class Diagrams** — classes, attributes, methods, relationships (see [[oop-four-pillars]])
- **Sequence Diagrams** — message flows over time
- **Activity Diagrams** — workflows and decision points

### Quality Models

**McCall's Software Quality Model** organises quality into 3 perspectives (Product Operation, Product Revision, Product Transition) across 11 quality features (Correctness, Reliability, Efficiency, Integrity, Usability, Maintainability, Testability, Flexibility, Portability, Reusability, Interoperability). The **Mag7** are the 7 features most commonly examined.

### iRTM

The **Incremental Requirements Traceability Matrix** maps every requirement to its source, design artefact, and test case — providing end-to-end traceability and impact analysis for change requests.

## Concept Pages

| Concept | Description |
|---------|-------------|
| [[requirements-engineering]] | Full RE lifecycle, BCIC, McCall, iRTM |
| [[lightweight-rcm]] | User Stories, UseCase 2.0, comparison table |

## Related Courses

- [[INF1009-object-oriented-programming]] — UML class diagrams, OOP relationships
- [[INF2002-human-computer-interaction]] — Needfinding feeds into RE elicitation
