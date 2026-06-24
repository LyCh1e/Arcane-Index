---
type: area
status: established
title: "Human-Computer Interaction"
domain: hci
source: [[sources/INF2002-human-computer-interaction]]
updated: 2026-05-15
tags: [area, hci]
---

# Human-Computer Interaction

**Source**: INF2002 — Human-Computer Interaction, SIT.

---

## What I Know

The study of how people interact with computer systems and how to design interfaces that are usable, accessible, and effective. INF2002 covers design frameworks (Norman's model, Gestalt principles, Fitts' Law), user research methods (interviews, contextual enquiry, observation), prototyping, and usability evaluation.

---

## Concept Pages

| Page | What It Covers |
|------|---------------|
| [[concepts/hci-fundamentals\|HCI Fundamentals]] | Norman's Seven Stages of Action, Gulf of Execution/Evaluation, affordances, signifiers, feedback, conceptual models; Gestalt principles (proximity, similarity, closure, figure/ground); Fitts' Law (movement time); colour theory; typography; WCAG accessibility guidelines |
| [[concepts/needfinding-and-task-analysis\|Needfinding & Task Analysis]] | Needfinding methods (interviews, surveys, observation, contextual enquiry, diary studies), affinity diagramming, personas, scenarios, task analysis (HTA — Hierarchical Task Analysis), storyboarding; low-fi vs high-fi prototyping; usability evaluation (heuristic evaluation, cognitive walkthrough, A/B testing, think-aloud protocols) |

---

## Key Ideas

- **Norman's Action Cycle**: Goal → Plan → Specify → Perform → Perceive → Interpret → Compare — good design closes both gulfs (execution: can the user figure out what to do? evaluation: can the user tell what happened?)
- **Affordances vs signifiers**: an affordance is a relationship between object and user that enables action; a signifier is a perceivable signal that communicates how to use that affordance. A flat plate affords pushing; the label "PUSH" is the signifier
- **Fitts' Law**: MT = a + b · log₂(D/W + 1) — movement time is proportional to log of distance over target width. Implication: large, nearby targets are fastest (Fitt's tip for touch UI design)
- **Gestalt in UI**: proximity groups related controls; similarity signals shared function; closure fills in incomplete shapes (loading spinners); figure/ground separates content from background
- **Needfinding before wireframing**: user research must precede low-fi prototyping; otherwise the design solves the wrong problem. Personas and scenarios translate research findings into actionable design targets
- **Heuristic evaluation is cheap**: five evaluators catch ~75% of usability problems against Nielsen's 10 heuristics — a high return for the cost of five expert sessions before user testing

---

## Cross-Domain Connections

- [[synthesis/re-elicitation-hci-needfinding|RE × HCI Needfinding]] — requirements elicitation (ICT2113) and HCI needfinding use overlapping methods for the same upstream purpose: understanding what users need
- [[concepts/requirements-engineering|Requirements Engineering]] — stakeholder analysis and interview techniques are shared between RE and HCI needfinding
- [[concepts/html-and-css|HTML & CSS]] — WCAG accessibility guidelines from HCI directly constrain front-end implementation choices
- [[concepts/web-security-and-devops|Web Security & DevOps]] — STRIDE's threat model and HCI's threat surface analysis share an approach: enumerate threats by category before designing mitigations
