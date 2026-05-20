---
type: concept
title: "Software Design Process"
domain: software-engineering
course: ICT2112
complexity: high
tags: [software-design, quality-attributes, coupling, cohesion, atam, design-smells, construction-design, architecture-drivers]
updated: 2026-05-12
status: established
created: 2026-05-12
---

# Software Design Process

Software design is both a **process** (a set of activities that produce design artefacts) and a **product** (the artefacts themselves). It bridges requirements and construction, producing the blueprint from which software is built. Good design is essential because *change is the only constant* in software engineering.

---

## The Design Pipeline

```
Architecture Design  →  Detailed Design  →  Construction Design
```

The three phases iterate — architecture decisions constrain detailed design, and detailed design decisions feed back to refine the architecture.

### Architecture Design

Produces the major structural components and their interfaces. Focuses on **non-functional (quality) requirements**. Serves four roles:

| Role | Purpose |
|------|---------|
| **Structural** | Identifies major components and interfaces |
| **Communication** | Shared artefact enabling team reasoning and discussion |
| **Quality** | Examines quality attributes before construction begins |
| **Foundation** | Basis for all subsequent engineering work |

### Detailed Design

The **white-box** view of component internals. Focuses on **functional requirements** and refines the architecture until construction can begin.

**Detailed Design = Interface Design + Component Design**

- **Interface Design** — Specifies how components communicate (not GUI — this means API/method contracts). Standardises access; enables parallel development.
- **Component Design** — Internal structure and behaviour; expressed via class diagrams, sequence diagrams, state diagrams, and activity diagrams.

### Construction Design

Bridges detailed design and actual code. Produces:
- **Flow-based design** — Pseudocode, flowcharts, activity diagrams
- **Table-based design** — Decision tables, state transition tables

**Example: Decision Table**

| Condition | Rule 1 | Rule 2 | Rule 3 |
|-----------|--------|--------|--------|
| Member? | Yes | Yes | No |
| Purchase > $100? | Yes | No | — |
| **Apply 20% discount** | ✓ | | |
| **Apply 10% discount** | | ✓ | |
| **No discount** | | | ✓ |

**Example: State Transition Table**

| Current State | Event | Next State | Action |
|---------------|-------|------------|--------|
| Idle | Start | Processing | Begin operation |
| Processing | Complete | Idle | Log result |
| Processing | Error | Error | Log error |
| Error | Reset | Idle | Clear error |

---

## Architecture Drivers

The **architecture drivers** define the *what* and *why* behind every structural decision:

1. **Primary functionality** — Core use cases the system must support
2. **Design purpose** — Why the system is being built and what it aims to achieve
3. **Quality attributes** — Non-functional requirements (performance, security, maintainability …)
4. **Architectural concerns** — Cross-cutting concerns: logging, error handling, auditing
5. **Architectural constraints** — Technology mandates, budget, time, team skill

> Functional requirements alone do not drive architecture — quality attributes and constraints are equally important.

---

## Quality Attributes (Microsoft Model)

Quality attributes are non-functional properties the system must exhibit.

### User-Facing

| Attribute | Description |
|-----------|-------------|
| **Usability** | How well the system meets user needs, resulting in a good overall experience |

### Run-Time

| Attribute | Description |
|-----------|-------------|
| **Availability** | Proportion of time the system is functional and working |
| **Performance** | Responsiveness of the system |
| **Reliability** | Ability to remain operational over time |
| **Scalability** | Ability to handle increasing load or be readily enlarged |
| **Security** | Capability to prevent malicious or accidental actions |

### Design

| Attribute | Description |
|-----------|-------------|
| **Conceptual Integrity** | Consistency and coherence of the overall design |
| **Maintainability** | Ease with which the system can be changed |
| **Reusability** | Suitability of components for use in other applications |
| **Testability** | Ease with which the system can be tested |

### Design Tactics per Attribute

| Attribute | Tactics |
|-----------|---------|
| **Security** | Authenticate users, limit exposure, limit access, intrusion detection |
| **Testability** | Event logging with enable/disable switch for testers |
| **Maintainability** | Modularisation, abstraction, encapsulation; reduce coupling to prevent ripple effects |
| **Availability** | Redundancy, task monitor, watchdog timer |
| **Performance** | Increase computation efficiency, reduce overhead, introduce concurrency |

---

## Coupling

**Coupling** measures the strength of interconnection between modules. The goal is **low coupling** (loosely coupled) — changes to one module should not cascade to others.

**Scale from tightest to loosest:**

| Type | Description |
|------|-------------|
| **Content** | Module directly references the content of another (e.g., reads/modifies another module's local variables or branches to its labels) — worst |
| **Common** | Modules share a global data area (global variables) |
| **Control** | One module controls the logic of another by passing control flags |
| **Stamp** | Modules share a composite data structure but use only part of it |
| **Data** | Modules share data only through parameter passing — best |

**Decoupling strategies:** Divide and conquer; OOP (inheritance, polymorphism); Dependency Inversion Principle; the architectural patterns in [[software-architecture-patterns]].

---

## Cohesion

**Cohesion** measures how closely related and focused the responsibilities of a single module are. The goal is **high cohesion** — each module does one thing well.

**Scale from highest to lowest:**

| Level | Type | Description |
|-------|------|-------------|
| 1 (highest) | **Informational** | Module performs multiple related operations on a shared data structure |
| 2 | **Functional** | Module performs a single, well-defined function |
| 3 | **Communicational** | Elements operate on the same input or output data |
| 4 | **Procedural** | Elements are related by order of execution |
| 5 | **Temporal** | Elements are related by time of execution (e.g., initialisation routines) |
| 6 | **Logical** | Elements perform logically similar functions, selected by a flag |
| 7 (lowest) | **Coincidental** | Elements have no meaningful relationship — worst |

> Aim for functional or informational cohesion. Coincidental and logical cohesion are symptoms of poor design.

---

## Design Evaluation

### Architecture Evaluation Process

1. Does the architecture satisfy **functional requirements**?
2. Does the architecture satisfy **quality attribute requirements**?
3. Are **architectural constraints** satisfied?
4. Is the design **internally consistent**?
5. Is the design **feasible** to implement?

### Architecture Tradeoff Analysis Method (ATAM)

ATAM is a structured evaluation technique that surfaces architectural tradeoffs before construction begins.

**Nine steps:**
1. Present the ATAM
2. Present business drivers
3. Present the architecture
4. Identify architectural approaches
5. Generate quality attribute utility tree
6. Analyse architectural approaches
7. Brainstorm and prioritise scenarios
8. Analyse architectural approaches again
9. Present results

**ATAM outputs:**
- **Sensitivity points** — Decisions that strongly affect a quality attribute
- **Tradeoffs** — Decisions that positively affect one attribute and negatively affect another
- **Risks** — Potentially problematic architectural decisions
- **Non-risks** — Decisions confirmed as sound

---

## Design Smells

Design smells are symptoms of poor design that indicate deeper structural problems:

| Smell | Symptom |
|-------|---------|
| **Rigidity** | Every change causes a cascade of changes elsewhere |
| **Fragility** | Software breaks in unrelated places when a single change is made |
| **Immobility** | Useful parts cannot be extracted for reuse in other systems |
| **Viscosity** | It is easier to do the wrong thing (hack) than the right thing |
| **Needless Complexity** | Over-engineering; design contains unnecessary elements |
| **Needless Repetition** | Similar code appears in many places (violates DRY) |
| **Opacity** | Code is difficult to understand and reason about |

Design smells often result from violating SOLID principles — see [[solid-and-design-patterns]].

---

## Levels of Software Design

Design decisions exist at multiple levels of granularity:

1. The software **system** as a whole
2. The system is organised into **subsystems**
3. Subsystems are divided into **classes**
4. Classes are divided into **routines and data**
5. The internals of each **routine** are also designed

Each level requires appropriate tools: architecture diagrams for (1–2), UML class and sequence diagrams for (3–4), pseudocode and decision tables for (5).

---

## See Also

- [[software-architecture-patterns]] — Architectural styles and layer patterns that apply these principles
- [[solid-and-design-patterns]] — SOLID principles and GoF design patterns for detailed design
- [[concepts/requirements-engineering]] — Upstream: where design inputs come from
- [[concepts/secure-software-requirements]] — Quality attribute: security requirements
