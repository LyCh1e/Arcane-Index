---
type: concept
title: "HCI Fundamentals"
domain: hci
course: INF2002
complexity: medium
tags: [hci, ucd, ux, ui, history, wimp, ubiquitous-computing, personas, prototyping, usability]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000012
---

# HCI Fundamentals

Human-Computer Interaction is the study of how people interact with computational systems and how to design systems that are effective, efficient, and satisfying. It is inherently interdisciplinary: it draws on cognitive psychology, ethnography, graphic design, and engineering. The unifying commitment is that **users are not optional** — they must be involved throughout design, not consulted at the end.

## Definitions

**HCI**: The discipline concerned with the design, evaluation, and implementation of interactive computing systems for human use and with the study of major phenomena surrounding them (ACM SIGCHI).

**UI (User Interface)**: The technical layer through which a user interacts with a system — screens, buttons, forms, gestures, voice commands.

**UX (User Experience)**: The full experience of using a product — encompassing utility, usability, accessibility, and emotion. UX includes and extends UI: a beautifully designed UI can produce terrible UX if the underlying task model is wrong.

A common mistake: optimising the UI while ignoring the UX. Air traffic control interfaces can be aesthetically minimal and functionally catastrophic.

## History of HCI

### Pre-1960s: Theoretical Foundations

- **1945** — Vannevar Bush, "As We May Think": described the Memex, a hypothetical device for navigating linked information. First articulation of hypertext and associative memory as a computer model.
- **1950s** — Human Factors / Ergonomics: designing physical equipment to fit human capabilities (aircraft cockpits, nuclear control panels). Direct ancestor of HCI.

### 1960s: Pivotal Inventions

- **1963** — Ivan Sutherland, **Sketchpad** (MIT): first interactive graphical computer program. Introduced direct manipulation — the user acts on objects on screen, not punch cards. Foundation of all GUI computing.
- **1968** — Doug Engelbart, **"The Mother of All Demos"** (Stanford Research Institute): live demonstration of the computer mouse, windows, hypertext links, collaborative real-time editing, and video conferencing. All of these features took 20+ years to become mainstream.

### 1970s–1980s: WIMP Goes Commercial

- **Xerox PARC** (1970s): Alto computer — first machine with a modern GUI (WIMP: Windows, Icons, Menus, Pointer). Researchers invented overlapping windows, the desktop metaphor, and the first WYSIWYG word processor.
- **Apple Lisa (1983) / Macintosh (1984)**: first commercial WIMP computers. Brought Xerox's research to consumers.
- **Direct manipulation** (Ben Shneiderman, 1983): coined the term; defined principles: visible objects, incremental actions, rapid reversible operations, immediate feedback.

### 1990s–2000s: Web and Mobile Emergence

- **World Wide Web (1991)**: transformed HCI from desktop GUIs to information architecture, web usability, and hypertext navigation.
- **Jakob Nielsen's usability heuristics (1994)**: 10 principles became the industry standard for usability evaluation.

### 1991: Ubiquitous Computing

Mark Weiser (Xerox PARC) coined **ubiquitous computing**: computation embedded in the environment, invisible to the user. Tabs (cm-scale), pads (dm-scale), boards (m-scale). Vision: "the most profound technologies are those that disappear" — they weave themselves into everyday life until indistinguishable from it. Precursor to IoT, smart homes, wearables.

### 2007–Present: Touch, Voice, AR/VR

- **iPhone (2007)**: multitouch paradigm replaced stylus and resistive touch. Triggered the touchscreen era.
- **Voice interfaces** (Siri 2011, Alexa 2014): natural language as interaction modality; no visual UI required.
- **Wearables**: smartwatches, fitness trackers — extremely constrained screen real estate, glanceable UI.
- **AR/VR**: spatial computing — interaction in 3D space, new paradigms (gaze, gesture, controller).

## Real-World Design Failures

HCI uses disasters to make the stakes concrete:

### Air Inter Flight 148 (1992)
A French Airbus A320 crashed into a mountain, killing 87 people. The crew entered **3.3** into the Flight Control Unit intending a 3.3° flight path angle, but the mode was set to **vertical speed** — the system interpreted it as a 3,300 ft/min descent. The two modes used the same display format with no differentiation. **Mode confusion** caused by poor interface design.

### Anton Yelchin (2016)
The actor was killed by his own Jeep Grand Cherokee, which had a monostable gear selector — a joystick-like control that returns to centre regardless of gear. Unlike traditional selectors with distinct positions, this provided no tactile or positional feedback that the car was in "Park" vs "Reverse." He exited on a slope believing it was in Park. **Affordance failure**: the interface didn't communicate its state.

### Hawaii Missile Alert (2018)
An employee at the Hawaii Emergency Management Agency accidentally sent a real ballistic missile alert to 1.4 million people. The interface was a **dropdown list** containing both test options and real alerts, with no confirmation dialog. **Irreversible action** with no safeguard. The error was not corrected for 38 minutes because there was no built-in way to send a retraction.

These three failures share a pattern: the interface did not match the user's mental model, provided insufficient feedback, or made catastrophic actions too easy.

## User-Centered Design (UCD)

UCD is the design process framework mandated by ISO 9241-210. Its premise: design cannot be correct without real users involved throughout.

### Three Core Principles

1. **Early focus on users and tasks**: understand users through research before designing; design to real tasks, not imagined ones
2. **Empirical measurement**: test prototypes with real users; collect behavioural data; do not rely on designer intuition
3. **Iterative design**: design → prototype → test → redesign; expect and plan for multiple cycles

### UCD Process (Iterative Cycle)

```
Understand context → Specify requirements → Design solution → Evaluate
         ↑_______________________________________________|
```

Each iteration produces a more refined design validated by real users.

### Personas

A **persona** is a fictional, archetypal user created from real research data. It is not a stereotype — it is a synthesis of observed behaviours, goals, frustrations, and context.

A persona includes:
- Name, photo, demographic sketch (makes it feel real)
- Goals (what they're trying to accomplish, not features they want)
- Tasks (what they actually do)
- Pain points (where current systems fail them)
- Context of use (device, environment, time pressure)

Personas keep the design team aligned: instead of "users might want X," discussions become "Alice would find this confusing because her goal is Y."

### Paper Prototyping

Low-fidelity prototyping with pen, paper, and scissors. Advantages:
- **Fast**: hours, not days
- **Cheap**: anyone can modify it
- **Non-precious**: users give honest feedback when they know it's just paper
- **Collaborative**: stakeholders can participate directly

A facilitator operates the "computer" (swaps paper screens), a user thinks aloud while attempting tasks, an observer notes errors and hesitations. This technique catches 80% of major usability problems before any code is written.

### Usability Testing

A controlled session where users attempt realistic tasks while the team observes. The test measures:
- **Effectiveness**: can users complete tasks?
- **Efficiency**: how long does completion take?
- **Satisfaction**: how do users feel about it? (System Usability Scale / Likert)

Nielsen's rule: **5 users** will reveal ~85% of usability problems. Beyond 5, you're mostly re-finding the same issues.

## Usability Principles (Nielsen's 10 Heuristics)

1. **Visibility of system status** — always keep users informed
2. **Match between system and real world** — speak users' language
3. **User control and freedom** — support undo/redo
4. **Consistency and standards** — follow platform conventions
5. **Error prevention** — design to prevent problems before they occur
6. **Recognition over recall** — minimise the user's memory load
7. **Flexibility and efficiency of use** — accelerators for expert users
8. **Aesthetic and minimalist design** — no irrelevant information
9. **Help users recognize, diagnose, and recover from errors** — plain-language error messages
10. **Help and documentation** — provide searchable, task-focused documentation

## See Also

- [[needfinding-and-task-analysis]] — data gathering and task decomposition methods
- [[requirements-engineering]] — needfinding outputs feed RE elicitation
- [[INF2002-human-computer-interaction]] — source course
- [[INF2007-mobile-app-development]] — HCI principles applied to mobile UI/UX
