---
type: concept
status: established
title: "Software Project Management"
domain: software-engineering
complexity: medium
source: "[[sources/INF2001-intro-software-engineering]]"
address: c-000051
created: 2026-05-23
updated: 2026-05-23
tags: [concept, software-engineering, project-management, wbs, estimation, gantt, INF2001]
---

# Software Project Management

The application of knowledge, skills, tools, and techniques to project activities to meet project requirements (PMBOK, 7th ed.). In software, this spans scoping, planning, staffing, organising, directing, and controlling the development of an acceptable system within time and budget constraints.

---

## Core Project Management Activities

1. **Negotiate scope** — agree on what will and will not be built
2. **Identify tasks** — break work into concrete deliverables
3. **Estimate task duration** — predict effort and time
4. **Specify inter-task dependency** — determine sequencing constraints
5. **Assign resources** — allocate people, tools, and infrastructure
6. **Direct team effort** — coordinate execution
7. **Monitor and control progress** — compare actuals to plan
8. **Assess project results** — post-project review and lessons learnt

---

## Work Breakdown Structure (WBS)

Breaking a project into smaller tasks makes them more feasible, easier to estimate, and easier to track.

### Rules

| Rule | Description |
|---|---|
| **100 % coverage** | WBS must include all work; nothing is outside the WBS |
| **Mutually exclusive** | No overlap between elements — each unit of work appears once |
| **Outcomes, not actions** | Elements represent deliverables, not activities |
| **Max 6 sub-tasks** | No task should have more than six immediate children |

### Hierarchy

```
0. Project Goal
├── 1. Phase 1
│   ├── 1.1 Activity 1.1
│   └── 1.2 Activity 1.2
│       ├── 1.2.1 Task
│       └── 1.2.2 Task
├── 2. Phase 2
└── 3. Phase 3
```

### Decomposition Criteria — When to Stop

Stop decomposing when each leaf task meets **all** of the following:

- Only one owner can be assigned
- Clearly defined output exists
- Quality can be monitored via performance criteria
- Communicates the work to the accountable person
- Duration is between **2 and 20 working days** (≤ 1 person-week of effort)
- Risk of being forgotten is minimised

### Forgotten Tasks Checklist

Delays are more often caused by forgotten tasks than inaccurate estimates. Always include:
- Planning the project itself
- Approval cycles and sign-offs
- Key meetings (kickoff, milestone reviews)
- Client / management interfaces
- Quality inspections and defect fixing
- Training
- Test planning, development, and execution
- Project reviews and project closing

---

## Gantt Chart

A horizontal bar chart showing tasks against time. Each bar represents a task's start date, duration, and end date.

- Visualises **schedule** and **parallel work** at a glance
- Shows which tasks are on the critical path
- Tracks actual progress against baseline
- Commonly created in tools such as Microsoft Project, Google Sheets, or Jira

---

## Planning & the Cone of Uncertainty

Estimation accuracy improves as the project progresses through the SDLC.

```
Requirements phase:   estimate $1M → actual range $0.25M–$4.00M  (4× uncertainty)
End of requirements:  estimate $1M → actual range $0.50M–$2.00M  (2× uncertainty)
End of analysis:      estimate $1M → actual range $0.67M–$1.50M  (1.5× uncertainty)
```

**Implication**: the earliest appropriate time for detailed planning is **after the specification (analysis) phase is complete**.

Key principle: *estimate → plan → work → refine estimate → adjust plan → continue*.

Accumulating historical data from past projects dramatically improves future estimates.

---

## Software Size Estimation

Effort and cost are derived from size estimation:

```
Size → Effort → Cost
```

### Lines of Code (LOC)

- Simple to count, but problematic:
  - Code is a small fraction of total project effort (requirements, design, testing, deployment are excluded)
  - Different languages produce very different LOC for the same functionality
  - Ambiguous definition: executable lines only? data declarations? blank lines?

### Function Points (FP)

- Count functional transactions (inputs, outputs, queries, files, interfaces)
- Language-independent; derived from the requirements specification
- More predictive than LOC for early estimates

### Use Case Points (UCP)

- Derived from the use case diagram
- Weights actors (simple/average/complex) and use cases (simple/average/complex)
- Adjust for technical and environmental factors
- Well-suited to object-oriented, use case-driven projects

---

## Effort and Cost Estimation

All estimation is uncertain; the goal is a **credible range** that allows for risk contingency:

| Factor | Notes |
|---|---|
| **Team experience** | Unfamiliar technology adds overhead |
| **Requirements volatility** | Changing requirements inflate effort non-linearly |
| **Complexity** | Algorithms, integrations, and data-intensive work cost more |
| **Reuse** | Existing components reduce effort but add integration cost |

> **Accurate estimation is critical** — an inaccurate estimate can lose credibility, lose money, or lose the contract.

---

## Related Pages

- [[concepts/sdlc-models|SDLC Models]] — project management activities vary by model
- [[concepts/uml-modelling|UML Modelling]] — use case diagrams feed UCP estimation
- [[concepts/software-configuration-management|Software Configuration Management]] — version control and CI/CD support the execution phase
- [[concepts/scrum-framework|Scrum Framework]] — Agile alternative to plan-driven PM (velocity, burn-down, Sprint Planning)
- [[sources/INF2001-intro-software-engineering|INF2001 Source Index]]
