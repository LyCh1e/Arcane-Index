---
type: area
title: "Software Engineering"
domain: software-engineering
sources: [[[sources/ICT2113-software-modelling]], [[sources/INF1009-object-oriented-programming]], [[sources/ICT2112-software-design]]]
updated: 2026-05-14
tags: [area, software-engineering]
---

# Software Engineering

**Sources**: ICT2113 (Requirements Engineering), INF1009 (OOP), ICT2112 (Software Design), SIT.

---

## What I Know

Three modules cover the full software engineering pipeline: from eliciting and specifying requirements (ICT2113) through designing solutions (ICT2112) to implementing them in object-oriented code (INF1009). The pipeline runs: requirements → architecture → detailed design → construction.

---

## Concept Pages

| Page | Source | What It Covers |
|------|--------|---------------|
| [[concepts/requirements-engineering\|Requirements Engineering]] | ICT2113 | BCIC analysis, SRS, PS, McCall's quality model, iRTM traceability |
| [[concepts/lightweight-rcm\|Lightweight RCM]] | ICT2113 | User Stories (INVEST, Connextra), UseCase 2.0 (UC Slices, 8-step) |
| [[concepts/oop-four-pillars\|OOP Four Pillars]] | INF1009 | Encapsulation, inheritance, polymorphism, abstraction; Java/C++ comparison |
| [[concepts/solid-and-design-patterns\|SOLID & Design Patterns]] | INF1009/ICT2112 | All 5 SOLID principles + all 23 GoF patterns (Creational/Structural/Behavioural) |
| [[concepts/software-design-process\|Software Design Process]] | ICT2112 | Architecture vs detailed design, quality attributes, coupling/cohesion, ATAM, design smells |
| [[concepts/software-architecture-patterns\|Software Architecture Patterns]] | ICT2112 | 3-Tier layered, Domain Model/Data Mapper/Active Record, MVC/MVP/MVVM, SOA, Circuit Breaker |

---

## Key Ideas

- **The pipeline**: BCIC analysis → Problem Statement → SRS → Architecture → Detailed Design (Interface + Component) → Construction
- **Coupling/cohesion**: lowest coupling + highest cohesion = most maintainable. Content coupling is worst; data coupling is best. Informational cohesion is highest
- **GoF patterns by intent**: Creational (how objects are made), Structural (how objects are composed), Behavioural (how objects communicate)
- **ATAM outputs**: sensitivity points, trade-offs, risks, and non-risks — evaluates architecture against quality attributes before building
- **Design smells** signal SOLID violations: Rigidity (OCP), Fragility (SRP), Immobility (DIP), Viscosity, Needless Complexity

---

## Cross-Domain Connections

- [[synthesis/dip-hilt-dependency-injection|DIP → Hilt]] — SOLID DIP principle implemented in Android via Hilt
- [[synthesis/data-mapper-repository-room-retrofit|Data Mapper → Room + Retrofit]] — ICT2112 patterns applied to Android data layer
- [[synthesis/re-elicitation-cia-aaa-security-requirements|RE × Security]] — McCall's Integrity ↔ CIA+AAA; RE lifecycle ↔ SSDLC
- [[synthesis/re-elicitation-hci-needfinding|RE × HCI]] — elicitation methods ↔ needfinding methods

---

## Study Notes

*(none yet — ICT2113 and ICT2112 study-notes pages not yet created)*
