---
type: source
status: established
title: "ICT2112 Software Design"
domain: software-engineering
course: ICT2112
tags: [software-design, architecture, design-patterns, solid, gof, layers, mvc, soa, atam]
ingested: 2026-05-12
raw: "raw/ICT2112 Software Design Notes.md"
---

# Source: ICT2112 / ICT2106 — Software Design

**Institution:** Singapore Institute of Technology (SIT)  
**Academic Year:** AY2025/26  
**Module Lead:** Asst. Prof. Alex Q. Chen  
**Programming Stack:** C#, .NET Core, ASP.NET Core

---

## Coverage Summary

Full module notes covering software design from first principles through to construction. The module takes students from architecture style selection through to detailed component design and pattern application, using C# and ASP.NET Core as the implementation vehicle.

| Topic | Key Content |
|-------|-------------|
| Topic 1 — Introduction | Software design process, quality attributes, Microsoft quality model, design tactics |
| Topic 2 — Design Principles | Architecture drivers, modularisation, abstraction, encapsulation, coupling, cohesion |
| Topic 3 — Architecture Patterns | Layered architecture, MVC, SOA/Microservices, overview of styles |
| Topic 4 — Data Source & Presentation | Table/Row Data Gateway, Active Record, Data Mapper; MVC, MVP, MVVM |
| Topic 5 — SOA & Synthesis | Gateway pattern, Circuit Breaker, Service Registry; end-to-end design pipeline |
| Topic 6 — Detailed Design | SOLID principles, interface design, component design with UML |
| Topic 7 — Creational Patterns | Factory Method, Abstract Factory, Singleton, Builder, Prototype |
| Structural Patterns | Adapter, Decorator, Facade, Composite, Proxy, Bridge, Flyweight |
| Behavioural Patterns | Observer, Strategy, Command, Iterator, Template Method, State, CoR, Mediator, Memento, Visitor |
| Design Evaluation | ATAM, design smells (Rigidity, Fragility, Immobility, Viscosity, Opacity …) |
| Construction Design | Pseudocode, flowcharts, decision tables, state transition tables |

---

## Assessment

| Item | Weight |
|------|--------|
| In-class activities | 5% |
| Project (D1 + D2) | 40% |
| Quizzes (Week 6 + Week 12) | 25% |
| Final Exam | 30% |

---

## Key Concepts Generated

- [[concepts/software-design-process]] — Design process, quality attributes, drivers, coupling, cohesion, ATAM, design smells, construction design
- [[concepts/software-architecture-patterns]] — Layered architecture, domain/data-source/presentation layer patterns, SOA/Microservices patterns
- [[concepts/solid-and-design-patterns]] — SOLID principles and full GoF catalogue (updated to include all 23 patterns with C# examples)

---

## Main Textbooks

1. Martin Fowler, *Patterns of Enterprise Application Architecture*, Addison-Wesley, 2003
2. Carlos E. Otero, *Software Engineering Design: Theory and Practice*, CRC Press, 2012
3. Erich Gamma et al., *Design Patterns: Elements of Reusable Object-Oriented Software*, Addison-Wesley, 1994

---

## Case Studies

- **ElectronicDeals** — e-commerce system illustrating layered architecture and domain patterns
- **Library Books Management System** — full-stack ASP.NET system integrating Google Books API and weather API; demonstrates Layered + MVC + Data Mapper + Repository + SOA + Factory Method + Observer in a single coherent design
