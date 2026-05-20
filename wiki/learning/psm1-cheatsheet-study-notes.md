---
type: learning
title: "PSM I Cheatsheet — Study Notes"
domain: agile-project-management
skill: scrum
status: active
source: "github.com/ambaena/scrum-psm1-cheatsheet"
tags: [scrum, agile, psm1, psm, exam-prep, cheatsheet, agile-manifesto, scaled-scrum]
updated: 2026-05-19
---

# PSM I Cheatsheet — Study Notes

Ingested from [ambaena/scrum-psm1-cheatsheet](https://github.com/ambaena/scrum-psm1-cheatsheet). Covers PSM I-specific nuances, the Agile Manifesto, Scaled Scrum, exam strategy, and the full definitions glossary. Cross-reference [[learning/scrum-open-assessment-study-notes]] and [[learning/scrum-master-exam-study-notes]] for question-bank drills, and [[scrum-framework]] for the complete framework reference.

---

## Readiness Check

Before sitting the PSM I assessment:

- ✅ Consistently pass practice exams with scores close to 100 %
- ✅ Complete 3–5 Scrum Open Assessments in a row with **100 % in under 6–8 minutes each**
- ❌ Reading the Scrum Guide alone is **not** enough

---

## Agile Manifesto

Scrum is built on the foundation of the Agile Manifesto's 12 principles, grouped across four categories:

### Project
- Satisfy customers through **early and continuous delivery** of valuable working software
- **Welcome changing requirements**, even late in development
- Deliver working software **frequently** — weeks rather than months; prefer shorter cycles
- Maintain a **sustainable development pace** indefinitely
- **Working software** is the primary measure of progress

### Product
- **Simplicity** is essential — maximise the amount of work not done
- Continuous attention to **technical excellence and good design** enhances agility

### People
- **Face-to-face conversation** is the most efficient and effective method of conveying information
- **Business people and developers** must work together daily throughout the project
- **Self-organising teams** produce the best architectures, requirements, and designs
- Build projects around **motivated individuals** — give them the environment, support, and trust they need

### Process
- At **regular intervals**, the team reflects on how to become more effective, then tunes and adjusts its behaviour accordingly

> The Agile Manifesto values and principles are testable on the PSM I — know the four categories and which principle belongs where.

---

## The Scrum Big Picture

```
Artifacts            Events                          Accountabilities
─────────────        ────────────────────────────    ────────────────────
Product Backlog  →   Sprint (container)              Product Owner (1)
  ↳ Product Goal       Sprint Planning               Scrum Master (1)
Sprint Backlog   →     Daily Scrum                   Developers (<10)
  ↳ Sprint Goal        Sprint Review
Increment        →     Sprint Retrospective
  ↳ Def. of Done
```

---

## PSM I — Key Nuances Not to Miss

### Invalid Sprint Types

The following Sprint types are **explicitly invalid** in Scrum — they do not exist in the framework:

| Invalid Type | Why It's Wrong |
|---|---|
| **Hardening / Stabilisation Sprint** | Every Increment must already meet the DoD — quality is built in per Sprint, not deferred |
| **Sprint 0** | No "warm-up" Sprint before real work; the first Sprint produces a usable Increment |
| **Release Sprint** | Releasing is not a Sprint-end gate; Increments may be released at any time |
| **Design Sprint** | Design is an ongoing activity within every Sprint, not a dedicated phase |

> These appear as distractors in PSM I questions. Any answer option containing these terms is wrong.

---

### Product Backlog Ordering Factors

The Product Owner orders the Product Backlog considering all of:
- **Value** — business benefit delivered
- **Risk** — uncertainty and dependencies
- **Size** — effort required
- **Dependencies** — prerequisites between items

> Ordering is not purely by value. Risk and dependencies are equally valid reasons to elevate or defer an item.

---

### Product Backlog — Additional Rules

- **Developers are allowed to update the Product Backlog** (e.g. adding technical tasks, refining estimates) — but the **Product Owner remains accountable**
- The Product Owner **must possess authority** to make backlog decisions — a PO without authority cannot do the job
- Product Backlog is organised from **Epics → User Stories** as items become nearer to the top

**Three methods for monitoring Product Backlog progress:**

| Method | Direction | Shows |
|---|---|---|
| **Burn-down chart** | Top → Bottom | Remaining work and estimated remaining work over time |
| **Burn-up chart** | Bottom → Top | Completed work and total remaining work |
| **Cumulative flow chart** | Layered | Work in each state over time; reveals bottlenecks |

---

### Daily Scrum — Role Clarity

| Person | Participation Rule |
|---|---|
| **Developers** | Required — they own and run the Daily Scrum |
| **Scrum Master** | **Ensures the event occurs** — does **not** conduct or run it |
| **Product Owner** | **Does not participate** — unless actively working on Sprint Backlog items, in which case they participate *as a Developer* |

> The Daily Scrum is not a technical problem-solving meeting. Problem-solving happens after the event, separately.

---

### Sprint Review — Undone Work

> **Undone work is NOT presented at the Sprint Review.**

Only work that meets the Definition of Done constitutes a valid Increment. Incomplete items return to the Product Backlog — they are not showcased as partial progress.

---

### Sprint Retrospective — Full Scope

The Retrospective inspects:
- Individuals
- Interactions
- Processes
- Tools
- **Definition of Done** (whether it should be updated)

It also discusses:
- What went well
- What problems were encountered and how they were (or were not) resolved
- **Team composition** — whether the team structure is working

---

### Scrum Master Startup Actions (New Team)

When a Scrum Master works with a brand-new Scrum Team, the initial facilitation actions are:

1. **Introduce developers to each other** — discuss skills and backgrounds
2. **Have the Product Owner explain** the product, business needs, history, and goals
3. **Facilitate developers discussing** their development approach

---

## Scaled Scrum

When multiple Scrum Teams work on the same product:

| Rule | Detail |
|---|---|
| Product Owner | **One per Product Goal / Product Backlog** — shared across all teams |
| Product Backlog | **One** — single source of truth for all teams |
| Increment | **One integrated Increment** — all teams contribute to one combined Increment |
| Synchronisation | Teams **need not synchronise** — coordination happens through shared backlog and events |
| Definition of Done | **Shared** — applies to all teams as a minimum; teams may make it stricter but not weaker |

> The "one Product Owner, one Product Backlog" rule is non-negotiable regardless of how many teams are involved.

---

## IKIWISI and YAGNI

Two acronyms that appear in PSM I questions:

| Acronym | Meaning | Implication |
|---|---|---|
| **IKIWISI** | "I Know It When I See It" | Customers often cannot fully specify requirements up front — empiricism accommodates this |
| **YAGNI** | "You Ain't Gonna Need It" | Do not build features until they are actually needed — avoids waste |

---

## Full Definitions Glossary

| Term | Definition |
|---|---|
| **Scrum** | A mechanism to optimise value delivery and guide changes in complex environments |
| **Effectiveness** | Delivering the **right product** |
| **Efficiency** | Optimal team and people **performance** |
| **Agility / Be Agile** | Responding to change |
| **Product** | A vehicle to deliver value; has a clear boundary, known stakeholders, and defined users or customers (service, physical product, or abstract) |
| **Product Vision** | The ultimate reason for creating the product |
| **Product Strategy** | How the product vision will be realised |
| **Epics** | Short reminders of product features; briefly describe large product features |
| **User Stories** | Describe small Product Backlog items in user-facing terms |
| **Story Point** | A unit of measure expressing the overall effort required to implement a Product Backlog item |
| **Planning Poker** | A consensus-based, gamified estimation technique where team members reveal estimates simultaneously to avoid anchoring bias |
| **Upcoming Capacity** | The available developer hours for the Sprint |
| **Definition of Ready** | Criteria defining when a Product Backlog item is sufficiently refined and ready for selection into a Sprint |
| **WIP** | Work In Progress |
| **Cone of Uncertainty** | Describes how uncertainty about scope decreases after each iteration as more is learned |
| **Technical Debt** | The consequences of poor software development practices — shortcuts taken now that must be paid back later |
| **Bottom-up Intelligence** | Insights and decisions that emerge from the people doing the work, rather than being imposed from management |
| **IKIWISI** | "I Know It When I See It" — customers often cannot articulate requirements until they see a working product |
| **YAGNI** | "You Ain't Gonna Need It" — do not build features until they are actually required |

---

## Exam Strategy — PSM I Open-Book Approach

### Before the Assessment
1. Read the Scrum Guide at least **twice**
2. Read a cheatsheet (ideally one you compiled yourself)
3. Review questions you failed in recent practice assessments
4. Complete at least **one Scrum Open Assessment** as a warm-up immediately before sitting

### During the Assessment — Two-Computer Setup

> The PSM I is an **open-book** assessment. Scrum prevents copying statements for Google lookup, but you can search.

**Computer 1 — Answering questions**

**Computer 2 — Reference materials (prepared in advance):**
- Scrum Guide open with **search** functionality ready
- Favourite cheatsheet open with search
- Dictionary window (especially useful for non-native English speakers)
- Google window for verifying question statements

### Loop Strategy

**First loop:** Move fast. Flag uncertain questions with the marker feature — do not waste time on difficult questions.

**Second loop:** Return to flagged questions. Use remaining time for research via Google and reference materials.

> The PSM I passing score is **85 %**. Time management and a clear two-pass strategy are critical.

---

## Quick Pre-Exam Checklist

| Area | Key Rule |
|---|---|
| Invalid Sprint types | Hardening, Sprint 0, Release Sprint, Design Sprint — **none are valid** |
| Undone work at Sprint Review | **Never presented** |
| Daily Scrum conductor | **Developers** — SM only ensures it happens |
| PO at Daily Scrum | **Does not attend** unless working Sprint Backlog items |
| Scaled Scrum PO | **One** per Product Goal regardless of team count |
| Scaled Scrum DoD | **Shared** across all teams (minimum standard) |
| PO ordering factors | Value + Risk + Size + Dependencies |
| Developers update PB? | **Yes** — PO remains accountable |
| PO must have | **Authority** |
| Invalid Scrum terminology | No Project Manager, no Sprint 0, no Release Sprint |
| Agile Manifesto category for "welcome change" | **Project** |
| Agile Manifesto category for "simplicity is essential" | **Product** |
| Agile Manifesto category for "face-to-face conversation" | **People** |
| Agile Manifesto category for "regular retrospection" | **Process** |

---

## Related

- [[learning/scrum-open-assessment-study-notes]] — 30-question Scrum Open bank (29/30, 96.7 %)
- [[learning/scrum-master-exam-study-notes]] — 80-question CSM/PSM/ACP prep with 40-row reference table
- [[scrum-framework]] — complete Scrum framework concept page
- [[sources/scrum-guide-2020]] — canonical source
