---
type: synthesis
title: "Same Questions, Different Lenses: RE Elicitation ↔ HCI Needfinding"
domains: [software-engineering, hci]
courses: [ICT2113, INF2002]
maturity: established
tags: [requirements-engineering, needfinding, elicitation, hci, ucd, personas, task-analysis, hta, bcic, synthesis]
updated: 2026-05-12
---

# Same Questions, Different Lenses: RE Elicitation ↔ HCI Needfinding

ICT2113 (Requirements Engineering) and INF2002 (HCI) both begin with the same upstream question: **what do people actually need from this system?** They answer it using methods that look remarkably similar — interviews, observation, structured analysis — but serve different purposes and produce different artefacts.

Understanding where they overlap, where they diverge, and how their outputs connect gives a clearer picture of the full pre-design process.

---

## The Shared Upstream Goal

Both disciplines exist to prevent the same mistake:

> **Building the wrong thing well.**

RE frames this as the risk of building a system that satisfies its specification but not its stakeholders. HCI frames it as the risk of building a system that functions correctly but is unusable. Both failures are downstream of the same root cause: insufficient understanding of users and their needs before design begins.

```
RE:   Eliciting → Analysing → Specifying → Validating → Managing
HCI:  Understand context → Specify requirements → Design → Evaluate
           ↑____________________________________________________|

Both are iterative loops. Both treat user understanding as the foundation.
```

---

## Method-by-Method Mapping

### Interviews

| ICT2113 RE | INF2002 HCI |
|------------|-------------|
| **Elicitation interviews** with stakeholders | **Semi-structured interviews** with users |
| Goal: extract functional and non-functional requirements | Goal: discover goals, mental models, pain points |
| Output: raw requirements list → BCIC analysis | Output: qualitative themes → personas, design insights |
| Documents answers in the RE Repository | Documents answers as research data for UCD |

The mechanics are identical: prepare questions, build rapport, probe unexpected answers, note inconsistencies. The framing differs: RE interviews seek *system specifications*; HCI interviews seek *human understanding*. In practice, a single well-designed interview session can serve both purposes.

### Observation

| ICT2113 RE | INF2002 HCI |
|------------|-------------|
| Observation used to discover implicit/tacit requirements that users cannot articulate | **Direct observation** to capture actual behaviour vs stated behaviour |
| Surfaces hidden requirements (users rarely mention the obvious) | Surfaces workarounds, errors, environmental factors |
| Less formally described in RE literature | Formalised with Hawthorne Effect mitigation, indirect variants |

Both disciplines recognise that **users are poor narrators of their own behaviour** — they describe the idealised version, not the actual one. Observation bypasses this.

### Surveys and Questionnaires

| ICT2113 RE | INF2002 HCI |
|------------|-------------|
| Used during elicitation for large stakeholder groups | **Surveys** with Likert/Semantic Differential scales |
| Useful for quantifying requirement priority (Ranked — Mag7) | Useful for measuring attitudes, satisfaction, hypothesis validation |
| Less formalised in RE literature | Formalised with acquiescence bias awareness, piloting |

Both use surveys to scale data collection beyond what interviews can cover. HCI adds more rigour around scale design and bias management.

### Focus Groups / Workshops

| ICT2113 RE | INF2002 HCI |
|------------|-------------|
| **Joint Application Development (JAD) workshops** — structured sessions with stakeholders and developers | **Focus groups** — moderated discussion with 6–10 users |
| Goal: surface conflicts, reach agreement, produce shared understanding | Goal: generate diverse perspectives, test concepts |
| Risk: dominant stakeholders suppress minority needs | Risk: groupthink, Hawthorne Effect amplified socially |

Both warn about the same failure mode: the loudest voice in the room shapes the output, and quieter stakeholders' needs are lost.

### Ethnography

HCI formalises **ethnography** (extended immersive observation, Contextual Inquiry) as a distinct method. RE does not name it separately, but the intent is present: requirements elicitation should involve watching users work in their actual environment, not just interviewing them in a meeting room. The RE concept of *contextual requirements* corresponds directly to the HCI concept of *context of use*.

---

## Where They Diverge: Purpose of the Output

This is the critical difference:

| Dimension | RE (ICT2113) | HCI Needfinding (INF2002) |
|-----------|-------------|--------------------------|
| **Primary output** | Formal SRS with verifiable, traceable requirements | Research insights: personas, task models, pain-point maps |
| **Audience** | Developers, testers, architects | Designers, product team, UX researchers |
| **Success criterion** | Requirements are complete, consistent, unambiguous, verifiable | Designs serve real user goals and mental models |
| **What gets formalised** | Requirement statements with IDs, sources, and test cases | Personas, HTA/TDH models, journey maps |
| **Failure mode** | Missing or ambiguous requirements → wrong system built | Designing for imagined users → unusable system built |

RE asks: *what must the system do?*  
HCI asks: *who will use it, how, and in what context?*

The HCI answer feeds into the RE process — but RE then adds the formal structure (unique IDs, traceability, completeness checks) that raw needfinding data lacks.

---

## How the Outputs Connect

### Personas → Stakeholder Profiles

RE names stakeholders but does not always characterise them richly. HCI's **personas** are the characterisation technique RE lacks:

```
RE:   "Stakeholders: student, instructor, administrator"
HCI:  "Alex (student, 20, uses mobile first, prefers async communication,
        frustrated by slow page loads, goal: submit assignments without
        missing deadlines)"
```

Personas make stakeholder needs concrete enough to write good requirements. A requirement like "the system shall support mobile submission with offline drafting" emerges from Alex's persona, not from a stakeholder label.

### HTA/TDH → Use Cases → Requirements

HCI's task analysis is the structural bridge between needfinding and requirements:

```
Needfinding (HCI)
    Observation, interviews, surveys
        ↓
Task Analysis (HCI)
    HTA: goal → sub-goals → operations → plans
    TDH: AND/XOR/OR branching
        ↓
Use Cases / User Stories (Lightweight RCM)
    Connextra format: "As a [persona], I want [goal], so that [benefit]"
        ↓
Requirements Specification (RE)
    SRS: functional requirements, non-functional requirements, BCIC-processed
        ↓
iRTM: traced to design and test
```

Each step refines the level of abstraction. HTA decomposes what users do; use cases frame it in system interaction terms; RE specifies it formally with constraints and quality attributes.

**Example — "Submit assignment" feature:**

```
HTA leaf: "2.3 Attach file to submission"
  → Use Case: "Student attaches a PDF (≤50 MB) to a submission draft"
  → Functional Requirement: "The system shall accept PDF attachments up to 50 MB per submission"
  → Non-Functional Requirement: "File upload shall complete within 10 seconds on a 10 Mbps connection"
  → iRTM entry: FR-07, traced to UploadController, test TC-07
```

The HTA step is invisible in the final SRS, but the requirement it produces is more precise because the task was decomposed first.

### Pain Points → Gap Analysis → BCIC

HCI needfinding surfaces **pain points** — where existing systems fail users. These map directly onto the **Interpret** step of BCIC:

| HCI Pain Point | BCIC Step | Result |
|----------------|-----------|--------|
| "I can never find my draft submissions" | **Interpret**: the system lacks persistent draft state | Hidden requirement: drafts must persist across sessions |
| "The deadline is shown in the wrong timezone" | **Clarify**: "deadline" is ambiguous — UTC or local? | Requirement: all deadlines shall be displayed in the user's local timezone with UTC offset |
| "I have to re-enter my details every time" | **Interpret**: no session persistence | Requirement: authenticated users' profile data shall pre-populate submission forms |

Pain points are latent requirements. BCIC is the process that turns them into explicit, verifiable requirement statements.

---

## Declarative vs Procedural Knowledge → Requirements for Novices and Experts

HCI's **knowledge-based analysis** (declarative vs procedural knowledge) has a direct RE implication:

- **Novice users** (declarative knowledge) need explicit system guidance → requirements for tooltips, wizards, help text, error recovery
- **Expert users** (procedural knowledge) need efficiency and accelerators → requirements for keyboard shortcuts, bulk operations, API access

RE non-functional requirements like *usability* (McCall) and *learnability* must be decomposed against specific user groups. A usability requirement that satisfies experts may be useless for novices, and vice versa. HCI's knowledge-based lens provides the vocabulary to write differentiated usability requirements.

---

## The UCD Cycle as an RE Sub-process

ISO 9241-210 defines the UCD cycle as:

```
Understand context → Specify requirements → Design solution → Evaluate
```

The "Specify requirements" phase of UCD is where HCI hands off to RE. The UCD specification names usability requirements, user goals, and context constraints. RE's SRS is the formalised, developer-facing version of those constraints.

In a well-integrated project:
- HCI runs the **Understand context** phase (needfinding, personas, task analysis)
- RE runs the **Specify requirements** phase (BCIC, SRS, iRTM)
- Both run the **Validate** phase (HCI: usability testing; RE: stakeholder sign-off)

---

## Key Differences Summary

| | RE (ICT2113) | HCI Needfinding (INF2002) |
|-|-------------|--------------------------|
| **Discipline origin** | Software engineering, systems analysis | Cognitive psychology, ethnography, design |
| **User model** | Stakeholder with needs and priorities | Human with goals, mental models, and context |
| **Output form** | Formal document (SRS, iRTM) | Research artefacts (personas, HTA, insight reports) |
| **Quality standard** | Mag7: complete, consistent, verifiable, traceable | Empirical: validated with real users in context |
| **Validation method** | Stakeholder sign-off, traceability review | Usability testing, observation, iterative redesign |
| **Change management** | Baseline, CCB, version control of SRS | Iterative design cycles; validated prototypes |
| **What it misses alone** | Usability, context of use, mental models | Formal completeness, traceability, non-functional constraints |

Neither discipline is sufficient alone. A system built from a complete SRS without needfinding can be technically correct and deeply unusable. A system designed from rich needfinding data without RE discipline can be usable but incomplete, inconsistent, or untestable.

---

## Summary

```
INF2002 HCI Needfinding              ICT2113 RE Elicitation
──────────────────────────────────────────────────────────────
Understand users (Who? Goals? Context?) ↔ Identify stakeholders + their needs
Observation / Ethnography               ↔ Contextual observation
Semi-structured interviews              ↔ Elicitation interviews
Surveys (Likert / Semantic Diff.)       ↔ Stakeholder surveys
Focus groups                            ↔ JAD workshops
Personas                                ↔ Stakeholder profiles (richer form)
HTA/TDH task decomposition              ↔ Use cases → functional requirements
Pain points                             ↔ BCIC Interpret step → hidden requirements
Declarative/procedural knowledge        ↔ Usability non-functional requirements
UCD: "Specify requirements" phase       ↔ RE Specifying activity (SRS)
Iterative test → redesign               ↔ RE Validating → loop back to Eliciting
```

HCI needfinding and RE elicitation are the same investigation run by two different professions. Their outputs are complementary: needfinding produces human understanding; RE converts that understanding into a formal, verifiable, traceable specification.

---

## See Also

- [[concepts/requirements-engineering]] — BCIC, Mag7, McCall's model, iRTM, 5 RE activities
- [[concepts/needfinding-and-task-analysis]] — observation, interviews, surveys, HTA, TDH
- [[concepts/hci-fundamentals]] — UCD process, personas, usability testing, Nielsen's heuristics
- [[concepts/lightweight-rcm]] — User Stories and UseCase 2.0 bridge HCI task models and RE requirements
- [[sources/ICT2113-software-modelling]] — source for RE concepts
- [[sources/INF2002-human-computer-interaction]] — source for HCI needfinding
