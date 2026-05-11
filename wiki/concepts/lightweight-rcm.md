---
type: concept
title: "Lightweight Requirements Change Management"
domain: software-engineering
course: ICT2113
complexity: medium
tags: [agile, user-stories, usecase-2.0, xp, invest, connextra, jacobson]
updated: 2026-05-11
---

# Lightweight Requirements Change Management

Lightweight RCM replaces heavy specification documents with **conversation-centred artefacts** — small, negotiable units of work that defer detail until it is needed. The two dominant forms are **XP User Stories** and **UseCase 2.0**. Both acknowledge that requirements are discovered through collaboration, not extracted in advance.

## User Stories (XP Origin)

User Stories were introduced by Kent Beck in **Extreme Programming (XP)** in the late 1990s as a reaction to heavyweight RE. The core insight: a story is a **promise of a conversation**, not a specification. Detail is intentionally deferred.

### The 3C's

Every User Story has three components:

| Component | Description |
|-----------|-------------|
| **Card** | A brief written description of the story — fits on a 3x5 index card. Serves as a reminder, not a spec. |
| **Conversation** | The ongoing dialogue between developer and stakeholder that fleshes out the detail. Most of the RE happens here. |
| **Confirmation** | Acceptance criteria — the conditions under which the story is considered done. Becomes the basis for acceptance tests. |

### Connextra Format

The standard User Story template, coined by Rachel Davies at Connextra:

> **As a** [role], **I want** [feature/goal], **so that** [benefit/reason].

Example:  
> As a registered user, I want to reset my password via email, so that I can regain access if I forget my credentials.

The "so that" clause is critical — it forces articulation of the business value, not just the feature.

### INVEST Criteria

Bill Wake's INVEST checklist defines a well-formed User Story:

| Letter | Criterion | Meaning |
|--------|-----------|---------|
| **I** | Independent | Stories should not depend on each other (enables flexible prioritisation) |
| **N** | Negotiable | Details are not fixed; they evolve through conversation |
| **V** | Valuable | Delivers business value — not a technical sub-task |
| **E** | Estimable | Developers can estimate the effort involved |
| **S** | Small | Completable within one iteration (sprint) |
| **T** | Testable | Acceptance criteria can be defined |

A story that fails INVEST should be split, clarified, or discarded.

### Story Splitting

Large stories (epics) must be split before implementation. Common splitting strategies:
- By user role (different actors have different needs)
- By data type (handle one type first)
- By workflow step (onboarding vs ongoing use)
- By CRUD operation (read before write)

## UseCase 2.0 (Jacobson)

UseCase 2.0 (Ivar Jacobson, 2011) is a scaled-up approach that bridges User Stories and traditional Use Cases. It introduces a three-level hierarchy:

### Three Levels

1. **Parent Use Case (UC)** — high-level goal shared by multiple users; roughly equivalent to an epic. Describes the full interaction from trigger to completion.
2. **Stories** — specific narrative paths through the UC (basic flow + alternative flows). Closer in granularity to User Stories.
3. **Slices** — the smallest schedulable unit; a slice of a UC that can be implemented, tested, and delivered independently.

The **Slice** is the key innovation. A slice must be:
- Independently testable
- Independently deliverable
- Traceable back to its parent UC and story

### The 8-Step UseCase 2.0 Process

1. Identify the system's actors
2. Identify the parent use cases for each actor
3. Write the basic flow for each UC (happy path)
4. Identify and write alternate/exception flows
5. Slice each UC into deliverable pieces
6. Prioritise slices into iterations
7. Implement and test each slice
8. Evolve the use cases as understanding grows

### Use Case Narrative Elements

Each UC contains:
- **Preconditions** — what must be true before the UC starts
- **Postconditions** — what is guaranteed after the UC completes
- **Basic flow** — the most common, successful path
- **Alternative flows** — variations of the basic flow
- **Exception flows** — error and failure paths
- **Stakeholders and interests** — whose needs does this UC serve?

## Heavyweight vs Lightweight Comparison

| Dimension | Heavyweight RE (SRS) | User Stories | UseCase 2.0 |
|-----------|---------------------|--------------|-------------|
| **Artefact** | Formal document | Card + acceptance criteria | UC narrative + slices |
| **Detail timing** | Upfront | Just-in-time | Progressive |
| **Change tolerance** | Low (change control needed) | High (negotiable) | Medium |
| **Team communication** | Document-mediated | Face-to-face | Mixed |
| **Traceability** | iRTM | Story → acceptance test | Slice → UC → test |
| **Best for** | Fixed contracts, regulated domains, large distributed teams | Small co-located agile teams | Medium teams, complex domains |
| **Ceremony** | High | Very low | Medium |

## Fragmentation Debt

A risk unique to story-based approaches: **fragmentation debt**. When a system grows via many small stories without a unifying architectural view, the stories may individually satisfy INVEST but collectively create an inconsistent, overlapping feature set.

Symptoms:
- Same feature reimplemented differently in two stories
- Acceptance criteria contradict each other across stories
- No clear owner of cross-cutting concerns (security, error handling)

UseCase 2.0 mitigates fragmentation debt by anchoring stories to parent UCs — the UC provides the unifying narrative. Periodic **story map reviews** are the standard remedy in pure XP.

## See Also

- [[requirements-engineering]] — heavyweight RE, BCIC, McCall, iRTM
- [[ICT2113-software-modelling]] — source course
- [[hci-fundamentals]] — personas and task analysis complement UC story writing
