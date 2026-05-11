---
type: source-index
title: "INF2002 Human Computer Interaction"
course: INF2002
institution: SIT
raw: "raw/INF2002 Human Computer Interactions Notes.md"
domain: hci
topics: [ucd, needfinding, task-analysis, usability, prototyping]
ingested: 2026-05-11
---

# INF2002 — Human Computer Interaction

HCI studies how people interact with computers and how to design systems that are effective, efficient, and satisfying. The course is deliberately interdisciplinary — drawing on cognitive psychology, sociology, and design — and argues that ignoring users in the design process produces systems that are technically correct but practically unusable.

## Course Overview

The course moves from "what is HCI and why does it matter" → historical context and failures → user-centred design methodology → data gathering (needfinding) → task analysis → prototyping and evaluation. The thread throughout is: **design for humans, validated by humans**.

## Key Topics

### HCI Definition & Scope

HCI is the study of how people interact with computational systems and how to design those interactions. **UI** (User Interface) is the technical layer; **UX** (User Experience) encompasses the full interaction including emotion, expectation, and context.

Key distinction: a system can have a polished UI and terrible UX (e.g., a form that looks clean but asks for information in confusing order).

### History of HCI

- **1945** — Vannevar Bush's Memex: conceptual hypertext machine, "As We May Think"
- **1963** — Ivan Sutherland's Sketchpad: first GUI, direct manipulation concept
- **1968** — Doug Engelbart's "Mother of All Demos": mouse, windows, hypertext, video conferencing
- **1970s–80s** — WIMP paradigm (Windows, Icons, Menus, Pointer) at Xerox PARC → Apple Lisa/Mac
- **1991** — Mark Weiser's ubiquitous computing: computing embedded in the world, invisible to the user
- **2007–present** — Touch revolution (iPhone), voice interfaces, wearables, AR/VR

### Design Failures That Killed People

The course uses real disasters to argue for rigorous HCI:
- **Air Inter Flight 148 (1992)** — Mode confusion: pilots entered descent rate when the system expected flight path angle
- **Anton Yelchin (2016)** — Jeep Grand Cherokee gear selector provided no tactile feedback; car rolled back after "park"
- **Hawaii Missile Alert (2018)** — Dropdown UI with no confirmation allowed an employee to send a real emergency alert by accident

These are not software bugs — they are HCI failures.

### User-Centered Design (UCD)

UCD's three core principles (ISO 9241-210):
1. **Early focus on users and tasks** — involve real users from day one
2. **Empirical measurement** — test prototypes with real users, measure performance and satisfaction
3. **Iterative design** — design → prototype → test → redesign

See [[hci-fundamentals]] for UCD process, personas, paper prototypes, and usability testing.

### Needfinding

Before designing, you must understand what users actually need — not what they say they want. The five core needfinding questions: Who are the users? What are their goals? What tasks do they perform? What are their pain points? What is the context of use?

Methods: observation, ethnography, surveys, interviews, focus groups. Each has different strengths. See [[needfinding-and-task-analysis]].

### Task Analysis

Task analysis decomposes what users do into structured representations:
- **HTA** (Hierarchical Task Analysis) — tree decomposition with plans
- **TDH** (Task Decomposition Hierarchy) — uses XOR/AND/OR operators for branching
- **Knowledge-based analysis** — distinguishes declarative knowledge (what) from procedural knowledge (how)

### Prototyping

Low-fidelity (paper, sketches) → medium-fidelity (wireframes, Figma) → high-fidelity (interactive prototype). Earlier, cheaper feedback catches more expensive design errors.

## Concept Pages

| Concept | Description |
|---------|-------------|
| [[hci-fundamentals]] | Definition, history, failures, UCD, personas, prototyping |
| [[needfinding-and-task-analysis]] | All needfinding methods, task analysis techniques |

## Related Courses

- [[ICT2113-software-modelling]] — Needfinding methods feed directly into RE elicitation
- [[INF2007-mobile-app-development]] — HCI principles apply to every Compose screen designed
