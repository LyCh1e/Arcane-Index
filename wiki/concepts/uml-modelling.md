---
type: concept
status: established
title: "UML Modelling"
domain: software-engineering
complexity: high
source: "[[sources/INF2001-intro-software-engineering]]"
address: c-000050
created: 2026-05-23
updated: 2026-05-23
tags: [concept, software-engineering, uml, use-case, activity-diagram, class-diagram, sequence-diagram, component-diagram, INF2001]
---

# UML Modelling

The Unified Modelling Language (UML) provides a standardised set of diagrams for capturing requirements, structure, and behaviour at different levels of abstraction. All diagrams model the **same system** from different complementary perspectives.

---

## Why Model?

Before writing code, modelling serves four purposes:

1. **Communicate requirements** — stakeholders validate what the system should do
2. **Bridge the gap** — between problem domain (user world) and solution domain (machine world)
3. **Guide design** — decompose work, allocate responsibilities, spot missing details
4. **Enable team collaboration** — non-coders can review; teams can work in parallel

---

## Diagram Progression (Requirements → Architecture)

```
Requirements
     ↓
Use Case Diagram         ← what the system does (for whom)
     ↓
Activity Diagram         ← workflow / process flow
     ↓
Class Diagram            ← structure — entities, attributes, relationships
     ↓
Sequence Diagram         ← behaviour — interactions over time
     ↓
Component Diagram        ← higher-level modules and their interfaces
     ↓
Architecture Diagram     ← deployment, physical topology
```

All diagrams use the same underlying requirements. They do not contradict each other; each reveals a different aspect of the system.

---

## 1. Use Case Diagram

Captures what each **actor** can do with the system — not how the system does it.

### Core Notation

| Symbol | Meaning |
|---|---|
| Stick figure | Actor |
| Ellipse with label | Use Case |
| Rectangle boundary | System |
| Solid line | Actor ↔ Use Case association |
| `<<include>>` arrow | Mandatory sub-use case (always occurs) |
| `<<extend>>` arrow | Optional/conditional extension (sometimes occurs) |

### Actors

- **Primary actor**: initiates the interaction to achieve a goal
- **Supporting actor**: performs sub-goals (e.g., external payment system)
- Actors can be humans, hardware timers, or other systems
- Name actors after the **role** they play, not the person

### Goals and Levels

| Level | Example |
|---|---|
| Summary | Manage customer banking |
| User Goal | Withdraw money |
| Sub-function | Validate PIN |

### `<<include>>` Stereotype

Used when a use case **always** requires another use case to complete.  
Use it when the included use case is shared by two or more base use cases.

```
Withdraw Cash ──<<include>>──► Validate PIN
Check Balance ──<<include>>──► Validate PIN
```

### `<<extend>>` Stereotype

Used when a use case **optionally** adds behaviour to another based on a condition.  
Arrow points from the extension to the base use case.

```
Report Forgery ──<<extend>>──► Validate ID Card
```

### Use Case Description Template

| Field | Description |
|---|---|
| Use Case ID | Unique identifier (e.g., UC-6) |
| Name | Action phrase (e.g., "Register for Courses") |
| Description | One-sentence overview |
| Primary Actor | Who initiates this use case |
| Pre-conditions | What must be true before the use case starts |
| Main Success Scenario | Step-by-step flow (numbered), assuming everything works |
| Alternative Scenarios | Exceptions and deviations (e.g., `2a. No courses available`) |
| Post-conditions | What the system guarantees after completion |
| Priority | Low / Medium / High |
| Non-Functional Requirements | Any NFRs specific to this use case |

> Non-functional requirements (performance, security, availability) are **not** represented in use case diagrams — they appear in NFR documentation and are addressed in architecture.

---

## 2. Activity Diagram

Models the **workflow or process flow** of a system — particularly useful for understanding synchronous behaviours and business processes.

### Core Notation

| Symbol | Meaning |
|---|---|
| Filled circle | Start state (initial node) |
| Bullseye (circle with dot) | End state |
| Rounded rectangle | Activity (labelled with a verb phrase in present tense) |
| Diamond | Decision / Branch (one input, multiple guarded outputs) |
| Thick bar (horizontal or vertical) | **Fork** (split into parallel activities) / **Join** (synchronise parallel flows) |
| Arrow | Flow / Transition |

### Rules

- All branches (from a decision) must be matched by a **merge** to close the conditional.
- All parallel flows (from a fork) must be matched by a **join** before continuing.
- Activity labels should be verb phrases: *Validate Payment*, not *Payment Validation*.

### Use Cases

- Document existing processes for analysis
- Analyse new process concepts
- Identify reengineering opportunities

### Limitation

Activity diagrams do not explicitly show **which object** executes which activity or how messaging works between objects. Use sequence diagrams for that.

---

## 3. Class Diagram

Captures the **static structure** of the system: classes, their attributes, operations, and relationships.

### Class Notation

```
┌─────────────────────────┐
│        ClassName        │
├─────────────────────────┤
│ - privateAttr: Type     │
│ # protectedAttr: Type   │
│ + publicAttr: Type      │
├─────────────────────────┤
│ + operation(): RetType  │
│ # helperMethod()        │
└─────────────────────────┘
```

Visibility modifiers:

| Symbol | Visibility | Accessible by |
|---|---|---|
| `−` | private | Same class only |
| `#` | protected | Same class + subclasses in same package |
| `+` | public | Everywhere (forms the API) |

### Object Notation

```
objectName : ClassName
- attr1 : String = "value"
+ method1() : ReturnType
```

### Identifying Classes — Noun Extraction

1. Write a concise, natural-language description of the system
2. Extract all nouns from the description
3. Eliminate: nouns outside the problem boundary, abstract nouns (→ become attributes)
4. Remove duplicates; convert to singular
5. Confirm each candidate class: does it need **remembrance** (attributes), **services** (operations), and **multiple attributes**?

### Class Confirmation Criteria

A noun becomes a class if it has:
- **Needed Remembrance** — data that must persist
- **Needed Services** — operations the system invokes on it
- **Multiple Attributes** — more than one property

### OOP Principles Expressed in Class Diagrams

| Principle | Meaning |
|---|---|
| **Encapsulation** | Group data + operations; control access via visibility |
| **Information Hiding** | External clients see only the public interface, not internals |
| **Inheritance** | Sub-class inherits properties and behaviour from super-class (`is-a` relationship) |
| **Polymorphism** | Multiple sub-classes override the same method differently |

---

## 4. Sequence Diagram

Models a **single scenario** — interactions between objects over time.

### Axes

- **Horizontal axis**: which participant is acting
- **Vertical axis**: time (top = start, down = later)

### Core Notation

| Element | Notation |
|---|---|
| Participant (object/system) | Box at top with name (format: `objectName : ClassName` or `: ClassName`) |
| Lifeline | Dashed vertical line below participant box |
| Message call | Solid horizontal arrow with method name + args above |
| Return | Dashed horizontal arrow back |
| Activation | Thick rectangle on lifeline (method on the call stack) |
| Object creation | Arrow labelled `new` (recipient box appears lower) |
| Object destruction | `×` at bottom of lifeline |
| Self-call | Arrow curving back to the same lifeline |

### Frames (Combined Fragments)

| Frame keyword | Meaning |
|---|---|
| `opt [condition]` | Optional — executes only if condition is true |
| `alt [condition]` | Alternative — if/else branches, separated by dashed line |
| `loop [condition]` | Repeat while condition is true |
| `ref` | Reference to another sequence diagram |

### From Use Case to Sequence Diagram

Each step in a use case's main/alternative scenario typically corresponds to one or more messages in the sequence diagram. The sequence diagram adds the object-level detail of **who sends what to whom**.

---

## 5. Component Diagram

Captures **higher-level modules** (components) and their interfaces — above the class level.

### What Is a Component?

- An independent unit that encapsulates a semantically related collection of classes and data
- Collaborates with other components through **well-defined interfaces**
- Designed to be modular, portable, replaceable, and reusable
- Could be a package, a web service, a library, or a hardware resource

### Core Notation

| Element | Notation |
|---|---|
| Component | Box with component `⊞` widget stereotype |
| Provided interface | Lollipop (facet) attached to component — "I provide this" |
| Required interface | Socket (open arc) attached to component — "I need this" |
| Port | Shaded box on a component's boundary |
| `<<delegate>>` | Delegates a provided/required interface to a sub-component |

### Levels of Design (McConnell)

```
System → Sub-systems → Components → Classes → Routines
```

Class diagrams live at the class level; component diagrams live at the component level.

---

## Diagram Relationships Summary

| Diagram | Layer | Question answered |
|---|---|---|
| Use Case | Requirements | What can each actor do? |
| Activity | Requirements / Analysis | How does the workflow proceed? |
| Class | Analysis / Design | What are the entities, their data and relationships? |
| Sequence | Design | Which objects talk to which, in what order? |
| Component | Design / Architecture | What are the high-level modules and interfaces? |

---

## Related Pages

- [[concepts/sdlc-models|SDLC Models]] — where each diagram fits in the lifecycle
- [[concepts/requirements-engineering|Requirements Engineering]] — elicitation feeds into use cases
- [[concepts/software-design-process|Software Design Process]] — design activities use class/component/sequence diagrams
- [[concepts/software-architecture-patterns|Software Architecture Patterns]] — architectural diagrams (C4, 4+1)
- [[concepts/oop-four-pillars|OOP Four Pillars]] — principles behind class diagram design
- [[sources/INF2001-intro-software-engineering|INF2001 Source Index]]
