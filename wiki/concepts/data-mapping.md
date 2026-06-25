---
type: concept
status: established
address: c-000069
created: 2026-06-25
updated: 2026-06-25
tags: [data-mapping, etl, data-integration, schema-mapping, transformation, data-engineering, dto]
related:
  - "[[synthesis/data-mapper-repository-room-retrofit]]"
  - "[[concepts/database-indexing-transactions]]"
  - "[[concepts/nosql-and-data-warehousing]]"
---

# Data Mapping

Data mapping is the process of defining how data fields in one system correspond to data fields in another. It sits at the core of every data integration, migration, ETL pipeline, and API transformation — any time data crosses a boundary between systems, a mapping defines what goes where and how it should be transformed.

> [!info] Not the same as the Data Mapper pattern
> The **Data Mapper design pattern** (Fowler, *Patterns of Enterprise Application Architecture*) is a class-level OOP pattern for separating domain objects from persistence logic. See [[synthesis/data-mapper-repository-room-retrofit]] for that topic. This page covers **data mapping as an engineering practice**.

---

## Why Data Mapping Matters

- **Data integrity**: prevents field mismatches (e.g. "John Smith" vs "John Smiths" counted as two records in analytics)
- **Data quality**: profiling and validation rules catch anomalies before they reach the target system
- **Governance and lineage**: mapping documents record the full path data travels — essential for GDPR/HIPAA compliance audits
- **System decoupling**: each system evolves its schema independently; the mapping layer absorbs the difference

---

## Types of Data Mapping (by automation level)

| Type | Description | Best for |
|------|-------------|----------|
| **Manual** | Developers hand-code field connections, usually in SQL or a scripting language | One-off migrations; highly custom data types |
| **Spreadsheet-based** | Mapping rules documented in a spreadsheet; developers implement manually | Small projects; stakeholder review before implementation |
| **Semi-automated** | Visual drag-and-drop tool; IT reviews auto-suggested links before committing | Mid-size projects with moderate complexity |
| **Automated (rule-based)** | Tool applies naming-convention rules and data-type matching without human review per field | Well-structured, consistent source schemas |
| **AI/Semantic mapping** | ML infers semantic relationships (e.g. links `ShipCountry` → `ShipNation` automatically) | Complex schemas with inconsistent naming; legacy system migration |

---

## Mapping Techniques

| Technique | What it does |
|-----------|-------------|
| **Direct mapping** | One source field → one target field, no transformation |
| **Transformation mapping** | Applies a rule or conversion (date format, unit conversion, concatenation) |
| **Lookup mapping** | References an external table to resolve or enrich a value (e.g. country code → country name) |
| **Conditional mapping** | Routes data to different target fields based on a condition (`IF status = 'active' THEN ...`) |
| **Schema mapping** | Aligns the structure of source schema to target schema (table/column relationships) |
| **Semantic mapping** | Uses domain knowledge to match fields by meaning, not just name or type |
| **Template-based mapping** | Applies a reusable mapping template across multiple similar sources |
| **Metadata-driven mapping** | Rules stored in a metadata repository; changed centrally without modifying pipeline code |
| **Code-based mapping** | SQL `SELECT` / `INSERT`, Python `pandas`, or custom scripts — full programmatic control |

---

## Transformation Types

During mapping, data may need to be transformed before loading into the target:

| Transform | Example |
|-----------|---------|
| **Format conversion** | `YYYY-MM-DD` → `DD/MM/YYYY`; JSON → CSV |
| **Type casting** | String `"42"` → integer `42` |
| **Aggregation** | Sum daily transactions into a monthly total |
| **Calculation / derivation** | `full_name = first_name + ' ' + last_name` |
| **Conditional logic** | `IF revenue > 10000 THEN tier = 'Gold'` |
| **Enrichment (lookup)** | Replace a postcode with a full address using a reference table |
| **Normalisation** | Strip whitespace, uppercase, remove special characters |
| **Splitting / merging** | Split `full_address` into street, city, postcode; merge two name fields into one |

---

## The Data Mapping Process

1. **Define scope and objectives** — what systems, what data, what business goal
2. **Identify source and target structures** — schema dumps, API contracts, data dictionaries
3. **Profile the source data** — assess quality, completeness, anomalies, nulls
4. **Document mapping rules** — create the mapping document (see below)
5. **Apply transformations** — write or configure the transform logic
6. **Test on a data subset** — verify target fields receive correct, quality data
7. **Iterate and refine** — adjust rules based on test failures
8. **Deploy and monitor** — run in production; alert on schema drift or job failures
9. **Maintain documentation** — update the mapping document whenever schemas evolve

---

## The Data Mapping Document

The mapping document is the specification that governs the entire pipeline. Required fields:

| Field | Purpose |
|-------|---------|
| Source table / field | Origin of the data |
| Target table / field | Destination in the target system |
| Data type (source → target) | Type casting requirements |
| Transformation rule | Logic applied during mapping |
| Validation rule | Criteria the mapped value must meet |
| Business rule | Domain logic governing the mapping |
| Trigger / schedule | What initiates the data transfer and how often |
| Data lineage note | Path the data has travelled |

---

## Context: ETL Pipelines

In ETL (Extract–Transform–Load), data mapping governs the **Transform** stage:

```
[Source System] → Extract → [Staging Area] → Transform (mapping + rules) → Load → [Target / Warehouse]
```

ELT (Extract–Load–Transform) — common on cloud warehouses — reverses this: raw data is loaded first, then transformed in-place using SQL (e.g. dbt). Mapping rules still apply; they are expressed as SQL models rather than pipeline configurations.

---

## Context: Object Mapping (Software Development)

In application code, "data mapping" often refers to converting between object representations:

- **Domain entity → DTO** (Data Transfer Object): strip internal fields before sending to API consumer
- **API response → domain model**: normalise external data into internal types
- **ORM mapping**: map database rows to domain objects (Hibernate, Room, SQLAlchemy)

Libraries: **AutoMapper** (.NET), **MapStruct** (Java), **AutoMap** (Python).

---

## Use Cases

- **Data migration**: moving data from a legacy system to a new platform
- **Data warehousing / BI**: consolidating data from multiple sources into a single warehouse
- **API integration**: transforming request/response payloads between systems
- **Master data management**: deduplicating and unifying records across systems
- **Compliance (GDPR/HIPAA)**: documenting what personal data exists, where it goes, and who can access it

---

## Common Tools

| Tool | Tier | Strengths |
|------|------|-----------|
| **Talend** | Enterprise | Visual pipeline designer; generates native Java; big data + governance |
| **Informatica** | Enterprise | Best-in-class MDM and governance; AI-powered metadata; acquired by Salesforce (May 2025) |
| **dbt** | Open-source / SaaS | SQL-first transformation; version control; testing built-in; merged with Fivetran (Oct 2025) |
| **MuleSoft Anypoint** | Enterprise | API-led connectivity; ESB + iPaaS |
| **Airbyte** | Open-source / SaaS | 600+ connectors; AI schema detection; strong for ingestion |
| **Altova MapForce** | Mid-market ($299+) | Visual schema-to-schema mapping; EDI; XML/JSON/CSV/DB |
| **Pentaho** | Open-source | ETL + analytics; Hitachi Vantara |

---

## Challenges

- **Schema evolution**: source or target schemas change without notice → use schema drift detection and metadata-driven rules
- **Semantic ambiguity**: two fields with different names mean the same thing; two fields with the same name mean different things → require domain expert review
- **Data quality debt**: mapping cannot fix upstream quality issues; profiling must happen before mapping
- **Documentation lag**: mapping documents go stale as systems evolve → version-control mapping specs alongside code

---

## Related Pages

- [[synthesis/data-mapper-repository-room-retrofit]] — Data Mapper OOP pattern (Room + Retrofit)
- [[concepts/database-indexing-transactions]] — source-side schema context
- [[concepts/nosql-and-data-warehousing]] — target system context
