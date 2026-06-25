---
type: source
status: established
address: c-000070
created: 2026-06-25
updated: 2026-06-25
title: "What is Data Mapping? — Airbyte Data Engineering Resources"
source_type: documentation / guide
author: Airbyte
date_published: 2024-01-01
url: https://airbyte.com/data-engineering-resources/data-mapping
confidence: high
tags: [data-mapping, etl, data-integration, schema-mapping, transformation, airbyte]
related:
  - "[[concepts/data-mapping]]"
  - "[[synthesis/research-data-mapping]]"
---

# What is Data Mapping? — Airbyte

## Summary

Comprehensive practitioner guide covering the definition, purpose, techniques, process, and best practices for data mapping in data engineering contexts. Published by Airbyte, an open-source data integration platform; content is tool-agnostic and broadly applicable.

## Key Claims

- Data mapping establishes connections between data elements across sources and systems to ensure accurate data movement whilst maintaining integrity
- Three core purposes: understanding data flow, ensuring data quality, supporting data governance
- Five primary techniques: direct mapping, transformation mapping, lookup mapping, schema mapping, automated mapping
- Modern platforms add schema drift detection (real-time structural change monitoring) and AI-powered mapping adaptation (ML-suggested field correlations)
- Step-by-step process: define scope → identify sources → profile data → match fields → standardise format → test and automate

## Techniques Documented

| Technique | Key characteristic |
|-----------|--------------------|
| Direct mapping | One-to-one, no manipulation |
| Transformation mapping | Rules/conversions applied |
| Lookup mapping | External reference tables for enrichment |
| Schema mapping | Structural alignment of tables/columns |
| Automated mapping | Software/ML handles matching |

## Concepts Generated

| Concept | Action |
|---------|--------|
| [[concepts/data-mapping]] | Created |
