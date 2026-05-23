---
type: concept
title: "SDLC Models"
domain: software-engineering
complexity: medium
source: "[[sources/INF2001-intro-software-engineering]]"
address: c-000049
created: 2026-05-23
updated: 2026-05-23
tags: [concept, software-engineering, sdlc, waterfall, agile, spiral, rup, INF2001]
---

# SDLC Models

A Software Development Life Cycle (SDLC) model is a theoretical description of the phases and their ordering when building software. Choosing the right model matters: the cost of fixing a fault late in the lifecycle can be 100× the cost of fixing it early.

---

## Why SDLC Models Exist

Software development is expensive and often goes wrong. The CHAOS Report (Standish Group) shows that the majority of projects are challenged or fail outright — with large projects performing worst (only 6 % fully successful in FY2011–2015).

Key reasons for failure:
- Requirements misunderstood or not collected rigorously
- No working software until the very end (late feedback)
- Cost of fixing faults grows exponentially as the lifecycle advances
- Maintenance accounts for ~67 % of total lifetime cost

A defined process forces teams to make systematic decisions and provides management with a basis for tracking progress.

---

## Classical SDLC Phases

Regardless of model, most SDLC activities fall into:

| Phase | Purpose |
|---|---|
| Requirements | Elicit and specify what the software must do |
| Analysis | Refine and model the requirements |
| Design | Architectural + detailed + construction design |
| Implementation | Coding and unit testing |
| Testing (V&V) | Integration, system, and acceptance testing |
| Deployment | Release to production |
| Maintenance | Corrective, perfective, adaptive changes |

---

## The Waterfall Model (1970)

Proposed by Royce (1970). Sequential, document-driven, "Big Design Up Front" (BDUF).

```
Requirements → Analysis → Design → Implementation → Testing → Deployment → Maintenance
```

### Attributes

| The Good | The Bad |
|---|---|
| Simple, easy to understand | Success depends on precise requirements upfront |
| Provides structure for inexperienced teams | No working software until the very end |
| Facilitates project management milestones | Very expensive to revisit a previous phase |
| Deliverables well-defined at each stage | Does not reflect how real projects work |

### When to Use / Not Use

| Use When | Do Not Use When |
|---|---|
| Requirements are well-known and stable | Requirements are likely to change |
| Technology is understood | Novel ideas or new technology |
| New version of an existing product | Tight deadlines with iterative delivery expected |
| Small, simple, low-risk in-house project | Complex, long-term maintenance projects |

---

## Rapid Prototyping Model

A variation of Waterfall that replaces the requirements phase with iterative prototyping.

- **Listen** → **Build prototype** → **Customer test-drives** → cycle until requirements are clear
- Prototype should be quick and **throwaway** — it must not become the product
- Addresses the "customer doesn't know what they want" problem
- **Key failure mode**: prototype-as-product (compromises solidify, deadlines force reuse)
- Still only one final delivery — same drawback as Waterfall at the end

---

## The Spiral Model (1988)

Proposed by Boehm. Combines incremental delivery with explicit risk management. Each cycle of the spiral has four phases:

1. **Determine objectives** — goals, alternatives, constraints
2. **Identify and resolve risks** — risk analysis, prototyping
3. **Development and testing** — depending on risk outcomes
4. **Plan the next iteration** — review and scheduling

The **radius** of the spiral represents accumulated cost; risk analysis is performed in every iteration.

| The Good | The Bad |
|---|---|
| Customer sees product as it evolves | Iterations are very long (6 months–2 years each) |
| Risk management built into every phase | Heavy documentation per iteration |
| Features can be added incrementally | Requires risk-analysis expertise |

### When to Use

- High-risk, large, complex systems
- Completely new ideas where risk cannot be upfront quantified

### Do Not Use

- When progress is urgent or client is unavailable
- Low-risk, low-budget projects (overhead is excessive)

---

## Rational Unified Process (RUP)

Introduced in 2003; closely tied to UML and component-based modelling. RUP is an **adaptable framework**, not a fixed methodology — it is customised for each project.

### Four Business Phases

| Phase | Focus |
|---|---|
| **Inception** | Initial business case, scope, risk assessment, budget/schedule estimate |
| **Elaboration** | Refine requirements, define architecture, refine project plan |
| **Construction** | Implementation, integration testing, operational releases (usually the longest phase) |
| **Transition** | Deployment, user acceptance, corrective fixes, final documentation |

Within each phase, all SDLC workflows (requirements, analysis, design, implementation, testing) are performed — but with varying intensity.

### Key Points

- Architecture- and use case-centric
- Components have well-defined interfaces
- Can deliver value early (show something working at the end of Inception/Elaboration)
- Business process is tied to the development process

| The Good | The Bad |
|---|---|
| Risk mitigation through iterations | Complicated; expensive tooling required |
| Focus on design quality | Only suitable for medium/large projects |
| Can show value early | Extensive documentation overhead |
| Framework allows use of other models | — |

### When to Use

- Medium to large projects where quality of design matters
- When early value delivery is needed
- When engineers have OOP design experience

---

## Agile Methods

Agile is a **mindset** codified in the Agile Manifesto (2001, signed by 17 independent practitioners).

### Agile Manifesto Values

> We value **individuals and interactions** over processes and tools  
> We value **working software** over comprehensive documentation  
> We value **customer collaboration** over contract negotiation  
> We value **responding to change** over following a plan

*Items on the right have value, but items on the left are valued more.*

### Agile Principles

- Embrace change as a fact of life
- Incremental delivery (1–4 weeks per iteration)
- Each increment has real value to stakeholders
- Emphasise test-driven development
- Small, self-organising teams
- Light-weight documentation
- Velocity (past progress) as a planning tool
- Continuous improvement

### Key Characteristics

- **Timeboxed iterations**: fixed time, not fixed features (descoping allowed)
- **No client interference** during an iteration
- Working software is the primary measure of progress
- Common methods: **Scrum**, **Kanban**

| The Good | The Bad |
|---|---|
| Flexible to change; builds the right product | Some rework inevitable (no full upfront design) |
| Early value delivery | Requires close, ongoing client collaboration |
| Customer satisfaction and team ownership | Good automation tooling is a prerequisite |
| Continuous feedback reduces risk | Not every team can adopt Agile values |

### When to Use

- Small to medium projects (or large projects decomposed into components)
- Time-critical applications, uncertain or changing requirements
- New or unfamiliar technology

### Do Not Use

- When the team lacks Agile skills or attitude
- For large systems that cannot be meaningfully decomposed
- When formal documentation is contractually required

---

## SDLC Model Comparison

| Dimension | Waterfall | Rapid Prototyping | Spiral | RUP | Agile |
|---|---|---|---|---|---|
| Delivery | Single, at end | Single, at end | Each iteration | Per phase | Every sprint |
| Requirements upfront? | All required | Prototyped first | Per iteration | Per phase | Evolving |
| Risk management | None explicit | None explicit | Core to model | Present | Via iterations |
| Client involvement | At start | During prototyping | Throughout | At phase ends | Continuous |
| Documentation | Heavy | Heavy | Heavy | Heavy | Light |
| Best project size | Small/simple | Small/medium | Large/complex | Medium/large | Small/medium |

---

## Related Pages

- [[concepts/uml-modelling|UML Modelling]] — models used at each SDLC phase
- [[concepts/requirements-engineering|Requirements Engineering]] — in-depth RE process
- [[concepts/software-design-process|Software Design Process]] — design phase in detail
- [[concepts/scrum-framework|Scrum Framework]] — the dominant Agile method
- [[sources/INF2001-intro-software-engineering|INF2001 Source Index]]
