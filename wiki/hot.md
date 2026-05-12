---
type: meta
title: "Hot Cache"
updated: 2026-05-12T00:00:00
tags: [meta, hot-cache]
---

# Recent Context

## Last Updated

2026-05-12. Sessions: (1) ICT2112 Software Design fully ingested — design process pipeline, GoF patterns (all 23), architectural/layer patterns, SOA, ATAM, design smells. (2) Stock Prediction Neural Network project ingested — custom NumPy two-layer NN, SOLID/DIP architecture, 12-feature yfinance pipeline, composite accuracy scoring, band calibration, background threading.

## Key Recent Facts

- **ICT2112 Design Process**: Architecture → Detailed → Construction. Architecture serves 4 roles (Structural, Communication, Quality, Foundation). Detailed design = Interface Design + Component Design. Construction design produces pseudocode/flowcharts (flow-based) and decision/state-transition tables (table-based).
- **Quality attributes** (Microsoft model): Usability; Availability, Performance, Reliability, Scalability, Security (run-time); Conceptual Integrity, Maintainability, Reusability, Testability (design).
- **Coupling scale (tight → loose)**: Content → Common → Control → Stamp → Data. **Cohesion scale (high → low)**: Informational → Functional → Communicational → Procedural → Temporal → Logical → Coincidental.
- **Architectural/Layer patterns**: Layered 3-Tier (Presentation / Domain / Data Source). Domain layer: Transaction Script (simple), Table Module (medium), Domain Model (complex). Data Source: Table Data Gateway, Row Data Gateway, Active Record, Data Mapper (cleanest separation). Presentation: MVC, MVP (passive view, testable Presenter), MVVM (two-way binding).
- **SOA patterns**: Gateway (single entry point), Service Registry/Discovery (Consul/Eureka), Circuit Breaker (Closed → Open → Half-Open), Adapter (bridge incompatible interfaces).
- **GoF Patterns — all 23**: Creational (Singleton, Factory Method, Abstract Factory, Builder, Prototype); Structural (Adapter, Decorator, Facade, Composite, Proxy, Bridge, Flyweight); Behavioural (Observer, Strategy, Command, Iterator, Template Method, State, CoR, Mediator, Memento, Visitor).
- **Design Evaluation — ATAM**: 9-step process; outputs sensitivity points, tradeoffs, risks, non-risks. **Design Smells**: Rigidity, Fragility, Immobility, Viscosity, Needless Complexity, Needless Repetition, Opacity.

## Domain Summaries

**Software Design** (ICT2112): Full design pipeline from architecture to construction. Coupling/cohesion are the two key internal quality metrics. The 3-Tier layered architecture separates Presentation, Domain, and Data Source concerns; each layer has specific patterns (MVC, Domain Model, Data Mapper). SOLID + GoF patterns are applied at the detailed design level. ATAM evaluates architecture against quality attributes. Design smells (Rigidity, Fragility …) signal SOLID violations.

**Secure Software Development** (ICT2216): Security requirements derived from CIA + AAA pillars. OWASP ASVS provides tiered verification (Level 1–3). SecurityRAT automates requirement selection. Docker Compose is the primary deployment tool across all labs. Windows Docker deployments require CRLF-to-LF conversion for shell scripts; use PowerShell for `docker exec` with Linux paths.

**Software Engineering** (ICT2113 + INF1009): Requirements Engineering covers the full RE lifecycle — BCIC analysis, PS/SRS documents, McCall's quality model (3 perspectives, 11 features), iRTM for traceability. Lightweight RCM covers User Stories (3C's, INVEST, Connextra) and UseCase 2.0 (parent-UC, Stories, Slices, 8-step process). OOP covers the 4 pillars with Java/C++ comparison, OOP relationships (Association/Aggregation/Composition), and UML class diagrams.

**Computer Science** (INF1008): Algorithm complexity from Big-Oh through Master Theorem. Data structures from arrays to B-Trees with a full complexity comparison table. Sorting (Bubble/Selection/Insertion/Merge/Quick) and string algorithms (Brute Force/KMP/Boyer-Moore) with when-to-use guidance. Graph algorithms: DFS/BFS/Topological Sort, MST (Prim's vs Kruskal's), shortest paths (Dijkstra vs Bellman-Ford).

**Mobile Development** (INF2007): Android OS stack, 4 app components, Activity lifecycle. Jetpack Compose declarative UI with recomposition and state hoisting. Full MVVM architecture (UI → ViewModel → Repository → Room/Retrofit). Kotlin coroutines (launch/async, Dispatchers, Structured Concurrency), Flow/StateFlow, Hilt DI, Retrofit, WorkManager.

**HCI** (INF2002): Definition, UI vs UX distinction. History from Memex (1945) to ubiquitous computing (Weiser 1991) to touchscreens. Real-world design failures (Air Inter 148, Anton Yelchin, Hawaii missile alert). UCD principles, personas, paper prototyping. Needfinding methods (observation, ethnography, surveys/Likert/Semantic Differential, interviews, focus groups). Task analysis (HTA, TDH with XOR/AND/OR, knowledge-based / declarative vs procedural).

## Recent Changes

- Created: `wiki/examples/stock-prediction-neural-network.md` (custom NN project — SOLID ML + Tkinter GUI)
- Created: `wiki/sources/ICT2112-software-design.md`
- Created: `wiki/concepts/software-design-process.md` (design pipeline, quality attributes, coupling/cohesion, ATAM, design smells, construction design)
- Created: `wiki/concepts/software-architecture-patterns.md` (layered, domain/data-source/presentation patterns, SOA)
- Updated: `wiki/concepts/solid-and-design-patterns.md` (added Builder, Prototype + all structural and behavioural GoF patterns; now covers all 23)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

## Active Threads

- ICT2216 Lab 2 Steps 5–7 (browser UI / artifact exploration) — user to complete independently
- Next: create learning/study notes (flashcard-style summaries for exam prep)
- Gap: no synthesis page connecting ICT2113 RE elicitation ↔ ICT2216 CIA+AAA (McCall's Integrity maps directly to CIA Integrity)
- Gap: no synthesis page connecting ICT2113 RE elicitation ↔ INF2002 HCI needfinding
- ✓ Resolved: [[synthesis/dip-hilt-dependency-injection]] — DIP → Hilt mapping written
- ✓ Resolved: [[synthesis/data-mapper-repository-room-retrofit]] — Data Mapper → Repository/Room/Retrofit mapping written
