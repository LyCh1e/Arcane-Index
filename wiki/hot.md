---
type: meta
title: "Hot Cache"
updated: 2026-05-13T00:00:00
tags: [meta, hot-cache]
---

# Recent Context

## Last Updated

2026-05-13. Sessions: (1) ICT2112 Software Design — design process, GoF patterns (all 23), architectural/layer patterns, SOA, ATAM. (2) INF2003 Database Systems — relational model, full SQL, BCNF normalisation, ER diagrams, B+ tree indexing, ACID transactions, NoSQL, data warehousing. (3) Synthesis gaps filled — RE×Security (McCall Integrity ↔ CIA-AAA) and RE×HCI (elicitation ↔ needfinding). (4) ICT1011 Computer Organisation and Architecture — Von Neumann, MSP430 ISA/assembly/modular programming, I/O interfacing, memory technologies, memory management.

## Key Recent Facts

- **ICT1011 Computer Architecture**: Von Neumann stored-program concept, common bus. Computer classes: supercomputer → mainframe → minicomputer → microcomputer → embedded/SoC. 3 basic operations: Store/Transform/Transfer.
- **ICT1011 Memory Hierarchy**: Registers (< 1 ns) → Cache (8–35 ns, SRAM) → Main Memory (20–100 ns, DRAM) → Secondary (5–20 ms). Volatile vs non-volatile.
- **ICT1011 MSP430 ISA**: 16-bit RISC MCU, 27 core instructions, 7 addressing modes, 16 registers. R0=PC, R1=SP (pre-decrement/post-increment), R2=SR (N/Z/C/V flags + GIE + power), R3=CG2 (constant generator), R4–R15 GPR. Little-endian. Memory map: 0x0000–0x01FF (8-bit peripherals), 0x2400 (RAM), 0x4400 (Flash), 0xFF80–0xFFFF (interrupt vectors).
- **ICT1011 Instruction Formats**: Format I (double operand), Format II (single operand), Format III (10-bit signed jump offset, ±512 words). 7 modes: Register, Indexed, Indirect, Indirect Auto-increment, Symbolic, Absolute, Immediate.
- **ICT1011 Assembly**: 4 columns (label/mnemonic/operand/comment). Directives: .text/.data/.bss/.byte/.word/.equ/.global. 2-pass assembly: Pass 1 → symbol table; Pass 2 → machine code. Emulated instructions map to core instructions (NOP=MOV R3,R3; CLR=MOV #0; RET=MOV @SP+,PC).
- **ICT1011 Modular Programming**: CALL = push PC+2 (SP−2) then jump; RET = MOV @SP+,PC. 3 parameter-passing strategies: registers (fast), memory block (not re-entrant), stack (general, supports recursion). Local variables via SUB #N,SP at entry; ADD #N,SP at exit.
- **ICT1011 I/O**: Parallel vs serial; simplex/half-duplex/full-duplex. Async serial: start(0) + 7/8 data bits (LSB first) + parity + stop(1); baud = 1/T. RS-232 for DTE↔DCE. Memory-mapped I/O (MSP430) vs isolated I/O (x86). Polled (busy-wait, CPU inefficient) vs interrupt-driven (ISR, efficient). Bluetooth: 2402–2480 MHz, FHSS 1600 hops/s, piconet (1 master + ≤7 slaves), BLE for IoT.
- **ICT1011 Secondary Memory**: HDD platters/tracks/cylinders/sectors. Access time = Ts + Tr + Tt. RAID 0 (stripe, performance), RAID 1 (mirror, fault-tolerance), RAID 10 (both).
- **ICT1011 Primary Memory**: Bus: data (width = bits/transfer), address (width = log₂ max memory), control. Synchronous bus (clocked, simple) vs asynchronous (handshake, flexible). SRAM (latch, fast, cache); DRAM (capacitor+refresh, high density, main memory). ROM→PROM→EPROM→EEPROM→Flash (block-erase, SSDs/phones).
- **ICT1011 Memory Management**: Uni-program (1 process) vs multi-program (concurrent). Swapping: long-term queue/intermediate queue ↔ main memory. Partitioning: fixed (internal fragmentation) vs dynamic (external fragmentation → coalesce/compact). Paging: process split into pages, memory into frames (same size); page table maps page# → frame#; logical address = page#+offset → physical = frame#+offset; eliminates external fragmentation.



- **INF2003 Relational Model**: DB/DBMS 3-level abstraction (view/logical/physical). Physical independence easier than logical. Relation = table of unordered tuples; keys: superkey → candidate key → primary key → foreign key. ACID (Atomicity/Consistency/Isolation/Durability). 6 design stages: Requirements → Conceptual (ER) → Logical → Refinement (BCNF) → Physical → Security.
- **INF2003 Relational Algebra**: 6 fundamental operators — σ (select rows), π (select columns), ∪, −, × (cartesian product), ρ (rename). Extended: ∩, ⋈ (natural join), outer joins (⟕⟖⟗), ÷ (division — "for all" queries), ← (assignment). Push σ/π before joins for efficiency.
- **INF2003 SQL**: DDL (`CREATE TABLE`, `ALTER`, `DROP`). DML: `SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY`. Aggregate: SUM/COUNT/AVG/MIN/MAX. NULL semantics: use `IS NULL` not `= NULL`. Set ops: `UNION`/`INTERSECT`/`EXCEPT` (+ ALL variants). Subqueries: `IN`, `EXISTS`, `ANY`, `ALL`. Optimisation: `EXISTS` > `COUNT(*)>0`; JOINs > correlated subqueries; avoid leading wildcards.
- **INF2003 Normalisation**: Anomalies: insertion/update/deletion/redundancy. FD: X→Y. Armstrong's axioms: Reflexivity, Augmentation, Transitivity (+ Union/Decomposition/PseudoTransitivity). Closure X⁺: iteratively add attributes. BCNF: every non-trivial FD X→Y must have X as superkey. Decomposition: lossless (BCNF guarantees) ✓; dependency-preserving (BCNF does NOT guarantee) ✗.
- **INF2003 ER Diagrams**: Entity (rectangle), relationship (diamond), attribute (oval). Attribute types: key/composite/multivalued/derived. Participation: total (double line) vs partial (single). Cardinality: 1:1/M:1/1:N/M:N. Weak entity = depends on owner for identity. ISA = subclass with overlap/covering constraints. ER→schema: entity→table, composite→flatten, multivalued→separate table, M:N relationship→table with composite PK, weak entity→merged with identifying relationship.
- **INF2003 Indexing**: Heap/sorted/indexed file organisations. Hash index: O(1) equality only. B+ tree: all data in leaves (linked list); internal nodes route; min 50% occupancy; O(log n) search/insert/delete; supports range queries; insert splits leaves upward; delete borrows from sibling or merges.
- **INF2003 Transactions**: ACID deep-dive. Serial schedule = safest. Serializable = equivalent to some serial. Interleaving → dirty reads/lost updates. TCL: COMMIT/ROLLBACK/SAVEPOINT. Lock granularity: DB→table→page→row→field. Deadlock: prevent by ordering; detect by timeout. Optimistic 3-phase: read (private copy) → validate → write. Recovery: write-ahead transaction log on separate device; checkpoint + redo/undo.
- **INF2003 NoSQL**: Key-value (Redis, O(1) get/set/del); Document (MongoDB, schema-less JSON/BSON, no joins); Columnar (Cassandra, column-wise storage, compression, fast aggregation); Graph (Neo4j, node+edge+property, traversal). Use NoSQL when ACID not needed, data is large/diverse, or high availability required.
- **INF2003 Data Warehouse**: ETL (Extract→Transform→Load). Star schema: 1 fact table + N dimension tables (denormalised, simple queries). Snowflake: normalised dimensions (storage savings, slower queries). OLAP cube operations: Slice (fix dimension), Dice (sub-cube), Drill Down (summary→detail), Roll Up (detail→summary), Pivot (rotate). OLTP vs OLAP: OLTP normalised+fast writes; OLAP denormalised+complex reads.

- **ICT2112 Design Process**: Architecture → Detailed → Construction. Architecture serves 4 roles (Structural, Communication, Quality, Foundation). Detailed design = Interface Design + Component Design. Construction design produces pseudocode/flowcharts (flow-based) and decision/state-transition tables (table-based).
- **Quality attributes** (Microsoft model): Usability; Availability, Performance, Reliability, Scalability, Security (run-time); Conceptual Integrity, Maintainability, Reusability, Testability (design).
- **Coupling scale (tight → loose)**: Content → Common → Control → Stamp → Data. **Cohesion scale (high → low)**: Informational → Functional → Communicational → Procedural → Temporal → Logical → Coincidental.
- **Architectural/Layer patterns**: Layered 3-Tier (Presentation / Domain / Data Source). Domain layer: Transaction Script (simple), Table Module (medium), Domain Model (complex). Data Source: Table Data Gateway, Row Data Gateway, Active Record, Data Mapper (cleanest separation). Presentation: MVC, MVP (passive view, testable Presenter), MVVM (two-way binding).
- **SOA patterns**: Gateway (single entry point), Service Registry/Discovery (Consul/Eureka), Circuit Breaker (Closed → Open → Half-Open), Adapter (bridge incompatible interfaces).
- **GoF Patterns — all 23**: Creational (Singleton, Factory Method, Abstract Factory, Builder, Prototype); Structural (Adapter, Decorator, Facade, Composite, Proxy, Bridge, Flyweight); Behavioural (Observer, Strategy, Command, Iterator, Template Method, State, CoR, Mediator, Memento, Visitor).
- **Design Evaluation — ATAM**: 9-step process; outputs sensitivity points, tradeoffs, risks, non-risks. **Design Smells**: Rigidity, Fragility, Immobility, Viscosity, Needless Complexity, Needless Repetition, Opacity.

## Domain Summaries

**Database Systems** (INF2003): Full relational model from ACID to normalisation. The 6-stage design process runs: requirements → ER diagram → relational schema → BCNF refinement → physical design (B+ tree indexes) → security. SQL is the declarative layer over relational algebra; every SELECT maps to σ/π/⋈. Normalisation uses FD closure and BCNF to eliminate all anomalies while guaranteeing lossless decomposition (but not always dependency preservation). B+ tree is the universal index: O(log n) equality and range, dynamic insert/delete. ACID transactions are enforced via write-ahead logging + locking (or optimistic 3-phase). NoSQL trades ACID for scale and flexibility; choose the model (KV/document/columnar/graph) based on query patterns. Data warehouses deliberately de-normalise into star/snowflake schemas for OLAP analytics.

**Software Design** (ICT2112): Full design pipeline from architecture to construction. Coupling/cohesion are the two key internal quality metrics. The 3-Tier layered architecture separates Presentation, Domain, and Data Source concerns; each layer has specific patterns (MVC, Domain Model, Data Mapper). SOLID + GoF patterns are applied at the detailed design level. ATAM evaluates architecture against quality attributes. Design smells (Rigidity, Fragility …) signal SOLID violations.

**Secure Software Development** (ICT2216): Security requirements derived from CIA + AAA pillars. OWASP ASVS provides tiered verification (Level 1–3). SecurityRAT automates requirement selection. Docker Compose is the primary deployment tool across all labs. Windows Docker deployments require CRLF-to-LF conversion for shell scripts; use PowerShell for `docker exec` with Linux paths.

**Software Engineering** (ICT2113 + INF1009): Requirements Engineering covers the full RE lifecycle — BCIC analysis, PS/SRS documents, McCall's quality model (3 perspectives, 11 features), iRTM for traceability. Lightweight RCM covers User Stories (3C's, INVEST, Connextra) and UseCase 2.0 (parent-UC, Stories, Slices, 8-step process). OOP covers the 4 pillars with Java/C++ comparison, OOP relationships (Association/Aggregation/Composition), and UML class diagrams.

**Computer Architecture** (ICT1011): Full hardware stack from Von Neumann fundamentals through MSP430 assembly to memory management. The MSP430 RISC MCU is the teaching platform throughout: 16-bit, 27 instructions, 7 addressing modes, 16 registers (R0=PC, R1=SP, R2=SR, R3=CG2). I/O chapter covers serial communications (async framing, RS-232), polled vs interrupt-driven I/O, and Bluetooth (FHSS piconet). Memory chapters cover SRAM (cache) vs DRAM (main memory), ROM/Flash (non-volatile), and memory management (swapping → partitioning → paging). Paging is the capstone concept bridging into OS (ICT1007).

**Computer Science** (INF1008): Algorithm complexity from Big-Oh through Master Theorem. Data structures from arrays to B-Trees with a full complexity comparison table. Sorting (Bubble/Selection/Insertion/Merge/Quick) and string algorithms (Brute Force/KMP/Boyer-Moore) with when-to-use guidance. Graph algorithms: DFS/BFS/Topological Sort, MST (Prim's vs Kruskal's), shortest paths (Dijkstra vs Bellman-Ford).

**Mobile Development** (INF2007): Android OS stack, 4 app components, Activity lifecycle. Jetpack Compose declarative UI with recomposition and state hoisting. Full MVVM architecture (UI → ViewModel → Repository → Room/Retrofit). Kotlin coroutines (launch/async, Dispatchers, Structured Concurrency), Flow/StateFlow, Hilt DI, Retrofit, WorkManager.

**HCI** (INF2002): Definition, UI vs UX distinction. History from Memex (1945) to ubiquitous computing (Weiser 1991) to touchscreens. Real-world design failures (Air Inter 148, Anton Yelchin, Hawaii missile alert). UCD principles, personas, paper prototyping. Needfinding methods (observation, ethnography, surveys/Likert/Semantic Differential, interviews, focus groups). Task analysis (HTA, TDH with XOR/AND/OR, knowledge-based / declarative vs procedural).

## Recent Changes

- Created: `wiki/sources/ICT1011-computer-organisation-architecture.md`
- Created: `wiki/concepts/computer-architecture-fundamentals.md` (Von Neumann, computer classes, memory hierarchy, MSP430 registers/memory map/ISA formats/addressing modes)
- Created: `wiki/concepts/assembly-programming-msp430.md` (syntax, directives, 2-pass assembly, executable instructions, emulated instructions, CALL/RET, parameter passing, stack frames)
- Created: `wiki/concepts/io-and-memory-systems.md` (serial/parallel I/O, async framing, polled vs interrupt, Bluetooth, HDD, RAID, bus interconnect, SRAM vs DRAM, ROM/Flash, memory management: swapping/partitioning/paging)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`



- Created: `wiki/synthesis/re-elicitation-cia-aaa-security-requirements.md` (McCall Integrity ↔ CIA-AAA; RE lifecycle ↔ SSDLC; BCIC for security; Mag7 on security requirements)
- Created: `wiki/synthesis/re-elicitation-hci-needfinding.md` (method mapping table; HTA/TDH → requirements pipeline; personas → stakeholder profiles; pain points → BCIC Interpret)
- Updated: `wiki/synthesis/_index.md`, `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

- Created: `wiki/examples/stock-prediction-neural-network.md` (custom NN project — SOLID ML + Tkinter GUI)
- Created: `wiki/sources/INF2003-database-systems.md`
- Created: 6 concept pages — `relational-database-fundamentals`, `relational-algebra-and-sql`, `database-normalisation`, `er-diagrams`, `database-indexing-transactions`, `nosql-and-data-warehousing`
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

- Created: `wiki/sources/ICT2112-software-design.md`
- Created: `wiki/concepts/software-design-process.md` (design pipeline, quality attributes, coupling/cohesion, ATAM, design smells, construction design)
- Created: `wiki/concepts/software-architecture-patterns.md` (layered, domain/data-source/presentation patterns, SOA)
- Updated: `wiki/concepts/solid-and-design-patterns.md` (added Builder, Prototype + all structural and behavioural GoF patterns; now covers all 23)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

## Active Threads

- ICT2216 Lab 2 Steps 5–7 (browser UI / artifact exploration) — user to complete independently
- Next: create learning/study notes (flashcard-style summaries for exam prep)
- ✓ Resolved: [[synthesis/dip-hilt-dependency-injection]] — DIP → Hilt mapping written
- ✓ Resolved: [[synthesis/data-mapper-repository-room-retrofit]] — Data Mapper → Repository/Room/Retrofit mapping written
- ✓ Resolved: [[synthesis/re-elicitation-cia-aaa-security-requirements]] — McCall Integrity ↔ CIA+AAA; RE lifecycle ↔ SSDLC requirements phases; BCIC applied to security requirements
- ✓ Resolved: [[synthesis/re-elicitation-hci-needfinding]] — Needfinding methods ↔ RE elicitation; HTA/TDH → use cases → SRS; personas → stakeholder profiles; pain points → BCIC Interpret → hidden requirements
