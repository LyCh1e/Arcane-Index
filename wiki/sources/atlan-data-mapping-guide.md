---
type: source
status: established
address: c-000071
created: 2026-06-25
updated: 2026-06-25
title: "What is Data Mapping? Steps, Techniques & More — Atlan"
source_type: guide
author: Atlan
date_published: 2024-01-01
url: https://atlan.com/what-is-data-mapping/
confidence: high
tags: [data-mapping, schema-mapping, semantic-mapping, data-governance, etl, data-lineage]
related:
  - "[[concepts/data-mapping]]"
  - "[[synthesis/research-data-mapping]]"
---

# What is Data Mapping? Steps, Techniques & More — Atlan

## Summary

Detailed practitioner guide from Atlan (a data catalogue and active metadata platform). Covers 10 distinct mapping techniques, a 12-step process, the data mapping document structure, and the distinction between schema matching and semantic mapping. Strongest source for process depth and technique taxonomy.

## Key Claims

- Schema matching answers "do these fields mean the same thing?" using algorithms; schema mapping goes further by defining the actual transformation from one to the other
- Semantic mapping uses domain knowledge and business rules to preserve intended meaning — essential when naming conventions differ across systems
- A mapping document must include: source-to-target rules, transformation rules, validation rules, business rules, data lineage, and metadata
- 12-step process from objective definition through deployment and ongoing documentation maintenance

## Ten Mapping Techniques (Atlan taxonomy)

Manual · Spreadsheet-based · ETL/data mapping tools · Code-based (SQL, Python) · Metadata-driven · Schema matching and profiling · Rule-based (conditional logic) · Template-based · Semantic · Data mapping visualisation

## Process (12 Steps)

Define objectives → identify sources and targets → gather requirements → profile data → create mapping document → perform mapping → test and validate → iterate → document maintenance → deploy → monitor → update documentation

## Concepts Generated

| Concept | Action |
|---------|--------|
| [[concepts/data-mapping]] | Created |
