---
type: synthesis
status: developing
address: c-000072
created: 2026-06-25
updated: 2026-06-25
title: "Research: Data Mapping"
tags: [research, data-mapping, etl, data-integration, schema-mapping, transformation, data-engineering]
related:
  - "[[concepts/data-mapping]]"
  - "[[sources/airbyte-data-mapping-guide]]"
  - "[[sources/atlan-data-mapping-guide]]"
  - "[[synthesis/data-mapper-repository-room-retrofit]]"
sources:
  - "[[sources/airbyte-data-mapping-guide]]"
  - "[[sources/atlan-data-mapping-guide]]"
---

# Research: Data Mapping

## Overview

Data mapping is the engineering discipline of defining how data fields in one system correspond to data fields in another, covering field-to-field correspondence, transformation rules, and validation logic. It is the central work product of any ETL pipeline, data migration, API integration, or compliance data inventory. Research was conducted across 2 rounds, drawing on 4 sources (Airbyte, Atlan, Astera, Integrate.io tool survey).

---

## Key Findings

- **Mapping is a specification, not just a configuration.** The mapping *document* is the governing spec; the pipeline tool merely executes it. Keeping the spec in version control alongside code prevents documentation drift. (Source: [[sources/atlan-data-mapping-guide]])
- **Automation level is the primary design decision.** Manual mapping is flexible but fragile; automated mapping is fast but can miss semantic nuance. AI/semantic mapping bridges the gap but requires validation by domain experts. (Source: [[sources/airbyte-data-mapping-guide]])
- **Schema matching ≠ schema mapping.** Matching identifies that two fields are equivalent (semantic question); mapping defines the transformation to convert one to the other (engineering question). Conflating them is a source of integration bugs. (Source: [[sources/atlan-data-mapping-guide]])
- **The transformation stage is where quality is made or broken.** Profiling upstream data before writing mapping rules catches anomalies before they propagate into the target. Mapping cannot fix upstream quality issues. (Source: [[sources/airbyte-data-mapping-guide]], [[sources/atlan-data-mapping-guide]])
- **ETL vs ELT affects where mapping rules live**, not whether they exist. In ETL, rules run in the pipeline (Talend, Informatica); in ELT, rules run as SQL models in the warehouse (dbt). The mapping document applies to both. (Source: tool comparison search)
- **Compliance (GDPR/HIPAA) data mapping is a distinct use case** — cataloguing what personal data exists, where it flows, who accesses it — not a transformation exercise. Tools: Transcend, DataGrail, OneTrust. Concept overlap with data lineage.
- **The market is consolidating**: Salesforce acquired Informatica (May 2025); Fivetran and dbt merged (Oct 2025). Enterprise data integration is converging toward metadata-intelligence + cloud-native ELT.

---

## Key Entities

- **Airbyte** — open-source/SaaS data integration; 600+ connectors; AI-powered schema drift detection
- **Atlan** — data catalogue and active metadata platform; strong governance and lineage tooling
- **Talend** — enterprise ETL/ESB; visual pipeline designer generating native Java
- **Informatica** — enterprise MDM + governance; acquired by Salesforce (May 2025)
- **dbt (data build tool)** — SQL-first transformation; version-controlled models; merged with Fivetran (Oct 2025)
- **Altova MapForce** — mid-market visual schema-to-schema mapper; EDI and XML/JSON/DB support
- **Martin Fowler** — coined the Data Mapper OOP pattern in *Patterns of Enterprise Application Architecture*; conceptually related but distinct from the data mapping practice

---

## Key Concepts

- [[concepts/data-mapping]] — full concept page: techniques, process, transformation types, document structure, tools

---

## Contradictions

- Sources disagree on the number of distinct "types" of data mapping: Airbyte lists 5 techniques; Atlan lists 10; Astera lists 4 automation tiers. These are complementary taxonomies, not contradictions — Atlan's 10 include both automation level and technique type in a single flat list, while others separate the two dimensions.

---

## Open Questions

- **Metadata-driven mapping in practice** — how are metadata repositories structured and maintained as schemas evolve? Tools (e.g. Atlan) support this, but the implementation pattern is not well documented in free sources.
- **Semantic mapping accuracy** — what is the false-positive rate of AI-powered semantic mapping on real-world schemas? Sources make qualitative claims but no benchmarks found.
- **Compliance data mapping standards** — GDPR Article 30 (records of processing) requires data mapping but does not prescribe a format. Industry standards (ISO 29101, NIST Privacy Framework) overlap — not fully researched.
- **dbt + Fivetran post-merger tooling** — how the merged product surfaces data mapping is not yet documented (merger announced Oct 2025).

---

## Sources

- [[sources/airbyte-data-mapping-guide]] — Airbyte, 2024. Comprehensive technique and process guide.
- [[sources/atlan-data-mapping-guide]] — Atlan, 2024. Deepest process taxonomy; 12-step workflow; 10 technique types.
