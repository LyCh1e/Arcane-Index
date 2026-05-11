---
type: source-index
title: "INF1009 Object-Oriented Programming"
course: INF1009
institution: SIT
raw: "raw/INF1009 Object Orientated Programming Notes.md"
domain: software-engineering
topics: [oop, java, design-patterns, solid-principles, uml]
ingested: 2026-05-11
---

# INF1009 — Object-Oriented Programming

OOP teaches the dominant paradigm in enterprise and mobile software. The course covers both theory (the four pillars, SOLID principles, design patterns) and practice (Java primary, C++ comparison, UML class diagrams). Students leave able to design flexible, maintainable class hierarchies and recognise common structural patterns.

## Course Overview

The course starts from primitive classes and objects, builds up through the four pillars, then applies SOLID as a quality filter, and concludes with the Gang-of-Four (GoF) Creational patterns as practical instantiations of good OOP design.

## Key Topics

### The Four Pillars

Every OOP course in every language centres on the same four ideas:

1. **Encapsulation** — bundle data with the methods that act on it; control visibility via access modifiers (`private`, `protected`, `public`, package-private in Java)
2. **Inheritance** — a subclass acquires the fields and methods of its superclass; enables code reuse and IS-A relationships
3. **Polymorphism** — one interface, many implementations; overloading (compile-time) vs overriding (runtime / dynamic binding)
4. **Abstraction** — hide implementation details behind contracts (abstract classes, interfaces)

See [[oop-four-pillars]] for deep coverage including the Interface vs Abstract Class comparison table and OOP relationship types (Association, Aggregation, Composition).

### Access Modifiers & Constructors

Java access modifier scope: `private` (class only) → package-private (default) → `protected` (package + subclasses) → `public` (everywhere). Constructors can be chained with `this()` and `super()`. Default constructor is inserted by the compiler if none is defined.

### Cloning

**Shallow copy** copies the object but not referenced objects (aliases shared). **Deep copy** recursively copies all referenced objects (fully independent). Java's `Object.clone()` is shallow by default; deep copy requires manual implementation or serialisation.

### Generics

Generics parameterise classes and methods by type (`List<T>`, `Map<K,V>`), enabling type-safe reuse without casting. Bounded wildcards (`extends`, `super`) add flexibility.

### Exception Handling

Checked vs unchecked exceptions. `try-catch-finally`, multi-catch, custom exception classes. The course emphasises failing fast and providing meaningful error messages — a form of defensive programming.

### SOLID Principles & Design Patterns

The five SOLID principles are the bridge between raw OOP and professional-grade design. GoF patterns implement these principles in reusable templates. See [[solid-and-design-patterns]] for all five principles with examples plus Singleton, Factory, and Abstract Factory deep dives.

### Java vs C++

| Feature | Java | C++ |
|---------|------|-----|
| Memory | Garbage collected | Manual (new/delete) |
| Pointers | References only | Raw pointers + references |
| Multiple inheritance | Via interfaces | Yes (with diamond problem) |
| Platform | JVM (bytecode) | Native compiled |
| Default access | Package-private | private (class), public (struct) |

### UML Class Diagrams

Class diagrams show classes (name/attributes/methods compartments), visibility modifiers (+/-/#/~), and relationships:
- **Association** — a uses b (plain arrow)
- **Aggregation** — whole/part, loosely coupled (open diamond)
- **Composition** — whole/part, tightly coupled (filled diamond)
- **Inheritance** — IS-A (open triangle arrow)
- **Realization** — implements interface (dashed open triangle)

## Concept Pages

| Concept | Description |
|---------|-------------|
| [[oop-four-pillars]] | Encapsulation, Inheritance, Polymorphism, Abstraction |
| [[solid-and-design-patterns]] | SOLID principles, Singleton, Factory, Abstract Factory |

## Related Courses

- [[ICT2113-software-modelling]] — UML is shared vocabulary
- [[INF1008-data-structures-algorithms]] — DSA data structures are implemented using OOP
- [[INF2007-mobile-app-development]] — Android is OOP at scale (Kotlin)
