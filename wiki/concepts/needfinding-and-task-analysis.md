---
type: concept
title: "Needfinding and Task Analysis"
domain: hci
course: INF2002
complexity: medium
tags: [needfinding, observation, ethnography, surveys, interviews, focus-groups, task-analysis, hta, tdh]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000013
---

# Needfinding and Task Analysis

Needfinding is the research phase of User-Centered Design: systematically discovering what users actually need (as opposed to what they say they want, or what designers assume they need). Task analysis then decomposes what users do into structured representations that drive interface design. Together, they are the empirical foundation of HCI.

## The Core Needfinding Questions

Before choosing a method, define what you need to learn:

1. **Who are the users?** — demographics, experience levels, roles
2. **What are their goals?** — ultimate outcomes, not just tasks
3. **What tasks do they perform?** — current workflows, workarounds
4. **What are their pain points?** — where current solutions fail
5. **What is the context of use?** — environment, devices, time pressure, interruptions

These questions determine which needfinding method is appropriate.

## Needfinding Methods

### Observation

Watch users in their **natural environment** performing real tasks. Does not rely on what users say — captures what they actually do.

**Direct observation**: researcher is present, may ask clarifying questions. Risk: **Hawthorne Effect** — users alter behaviour when they know they're being watched. Mitigation: observe multiple sessions until behaviour normalises; frame observation as studying the work, not the person.

**Indirect observation**: video recording, log analysis, eye tracking. User is unaware during the session; no Hawthorne effect. Requires ethical consent obtained beforehand.

What to capture:
- Actions performed (sequence, duration)
- Errors and recoveries
- Workarounds and hacks (high-value signal: these reveal where the system fails)
- Environmental factors (interruptions, lighting, noise)
- Artefacts used (sticky notes, paper checklists alongside digital tools)

### Ethnography

**Ethnography** is extended, immersive observation within a community or workplace. The researcher embeds in the user's world for days or weeks to understand culture, social dynamics, and tacit knowledge that brief observation misses.

Originated in anthropology; brought into HCI and CSCW research in the 1990s.

When to use: understanding complex, context-dependent work practices; discovering unarticulated needs; studying expert workers (their expertise is often invisible to them).

**Contextual Inquiry** (Beyer & Holtzblatt) is a structured ethnographic method: observe users at work, then ask them to explain what they're doing and why. Combines observation and interview in context.

### Surveys

Surveys collect **self-reported data** from many users efficiently. Useful for measuring attitudes, satisfaction, preferences, and quantifying how widespread a behaviour is.

**Types of questions**:
- **Closed**: multiple choice, rating scales — easy to analyse, loses nuance
- **Open**: free text — rich data, harder to analyse
- **Likert scale**: agree/disagree on a 5 or 7-point scale — industry standard for attitude measurement
- **Semantic Differential scale**: bipolar adjectives (fast ←——→ slow, simple ←——→ complex); captures connotative meaning

**Likert vs Semantic Differential**:

| Feature | Likert | Semantic Differential |
|---------|--------|----------------------|
| Structure | Agreement with a statement | Rating between two opposite adjectives |
| Measures | Attitude toward a subject | Connotative perception of a concept |
| Example | "The interface is easy to use" [1-5] | Easy [1-2-3-4-5] Difficult |

**Survey best practices**:
- One question per item — avoid double-barrelled questions ("Is the system fast and easy to use?")
- Avoid leading questions ("Don't you agree that X is better?")
- Balance scales — equal positive and negative options
- Pilot test before distribution
- Response bias: users tend toward agreement (acquiescence bias) and socially desirable answers
- Random sampling or quota sampling for generalisable results

### Interviews

Interviews yield **rich, qualitative data** about individual experience, mental models, and rationale. More flexible than surveys; the researcher can probe unexpected answers.

**Types**:
- **Structured**: fixed questions, same order — comparable across participants; less flexible
- **Unstructured**: conversational, no fixed script — rich but hard to analyse
- **Semi-structured**: prepared questions as guides, with freedom to probe — the standard in HCI research

**5-Step Interview Process**:
1. **Introduction**: explain purpose, obtain consent, assure confidentiality, build rapport
2. **Warm-up**: easy, non-threatening questions (role, experience)
3. **Main body**: core questions; use probing follow-ups ("Can you tell me more about...?", "What happened when...?")
4. **Cooling down**: wrap up main topics, ask for anything the participant wants to add
5. **Closing**: summarise key points, thank participant, explain next steps

**Probing techniques**:
- **Silence**: wait after an answer — participants often add important information
- **Clarification**: "What do you mean by 'slow'?"
- **Critical incident**: "Tell me about the last time this caused a problem"
- **Think-aloud**: ask participants to verbalise their thoughts during a task

### Focus Groups

A moderated discussion with 6–10 users simultaneously. Efficient for collecting diverse perspectives and observing how users respond to each other's ideas.

**Strengths**: generates a wide range of opinions quickly; social interaction can surface ideas that individual interviews miss; good for early ideation and concept testing.

**Weaknesses**: groupthink (dominant voices suppress minority views); lack of depth on any individual's experience; not suitable for sensitive topics; Hawthorne effect amplified by social pressure.

**Moderator role**: keep discussion on track, ensure all voices are heard, prevent domination by one participant, remain neutral.

## Task Analysis

Task analysis decomposes what users do into structured representations. It transforms raw observation and interview data into design-ready artefacts.

### HTA — Hierarchical Task Analysis

HTA represents tasks as a **tree hierarchy** of goals and sub-goals, connected by **plans** that specify the ordering and conditions.

Structure:
- **Goal** (root): the overall objective
- **Sub-goals**: decomposed steps to achieve the goal
- **Operations**: atomic actions at the leaf level (no further decomposition needed)
- **Plans**: describe the order and conditions (plan 0: do 1, then 2; plan 1: if condition, do 3 or 4)

Example — "Send an email":
```
0. Send email
  Plan 0: do 1, then 2, then 3, then 4
  1. Open email client
  2. Compose message
     Plan 2: do 2.1, then 2.2, then 2.3
     2.1 Enter recipient
     2.2 Enter subject
     2.3 Type body
  3. Attach file (if needed)
  4. Send
```

HTA is used to identify where users might make errors, what information they need at each step, and where the system should provide feedback or support.

### TDH — Task Decomposition Hierarchy

TDH extends HTA with logical operators to handle branching:

| Operator | Meaning |
|----------|---------|
| **AND** | All sub-tasks must be performed |
| **XOR** | Exactly one sub-task is performed (mutually exclusive) |
| **OR** | One or more sub-tasks may be performed |

TDH is particularly useful for documenting alternative paths (XOR) and parallel activities (AND).

### Knowledge-Based Analysis

Distinguishes two types of knowledge that affect task performance:

**Declarative knowledge (knowing that)**:
- Facts, concepts, relationships
- "The submit button is in the top-right corner"
- Can be communicated explicitly; stored in manuals, help text
- Beginners rely heavily on declarative knowledge

**Procedural knowledge (knowing how)**:
- Skills, sequences of actions, patterns
- "Muscle memory" for keyboard shortcuts
- Acquired through practice; difficult to articulate
- Experts operate primarily through procedural knowledge

**Design implication**: beginners need explicit cues (labels, tooltips, wizards) that support declarative learning. Experts need shortcuts and accelerators that leverage procedural knowledge. Good interfaces serve both (Nielsen Heuristic 7: flexibility and efficiency of use).

The gap between expert and novice mental models is a major source of usability problems: designers (experts) underestimate how much declarative support beginners need.

## Choosing the Right Method

| Method | Data type | Scale | When to use |
|--------|-----------|-------|-------------|
| Direct observation | Qualitative | Small | Understand current behaviour in context |
| Ethnography | Qualitative | Very small | Deep understanding of complex work practice |
| Survey | Quantitative | Large | Measure attitudes, validate hypotheses |
| Interview | Qualitative | Small–medium | Rich individual perspectives, mental models |
| Focus group | Qualitative | Medium | Broad ideation, concept testing |
| HTA | Structural | N/A | Document task hierarchy for design |
| TDH | Structural | N/A | Document branching and parallel tasks |

In practice, **triangulation** — using multiple methods — produces more reliable insights than any single method.

## See Also

- [[hci-fundamentals]] — UCD framework, personas, prototyping, usability principles
- [[requirements-engineering]] — elicitation methods overlap significantly with needfinding
- [[INF2002-human-computer-interaction]] — source course
