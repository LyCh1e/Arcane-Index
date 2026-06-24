---
type: source
status: established
title: "8 RAG Architectures You Should Know — Humanloop"
source_type: article
author: Humanloop
date_published: 2025-01-01
url: "https://humanloop.com/blog/rag-architectures"
confidence: high
ingested: 2026-06-23
tags:
  - rag
  - ai-engineering
  - architecture
key_claims:
  - Defines 8 distinct RAG architecture patterns from Simple RAG to Agentic RAG
  - HyDE uses hypothetical answer embeddings for vague query retrieval
  - Adaptive RAG adjusts retrieval strategy based on query complexity
  - Corrective RAG grades retrieved chunks and triggers web search as fallback
  - Self-RAG uses reflection tokens to self-critique and guide generation
  - Agentic RAG uses Document Agents per document coordinated by a Meta-Agent
related:
  - "[[concepts/rag-architectures]]"
  - "[[concepts/retrieval-augmented-generation]]"
  - "[[synthesis/research-rag]]"
---

# 8 RAG Architectures You Should Know — Humanloop

## Summary

Humanloop's 2025 architectural taxonomy of RAG systems. The article defines eight distinct patterns, each addressing specific limitations of the prior generation. The taxonomy progresses from simple fixed-pipeline RAG through query transformation, self-reflection, and fully agentic architectures.

## Eight Patterns Covered

1. **Simple RAG**: Fixed query → search → inject → generate. For bounded, static knowledge bases.
2. **Simple RAG with Memory**: Adds stored past interactions for conversational continuity.
3. **Branched RAG**: Routes queries to the most relevant source from multiple specialised corpora.
4. **HyDE**: Generates a hypothetical ideal document, embeds it, and searches with that embedding.
5. **Adaptive RAG**: Dynamically selects retrieval depth and source count based on query complexity.
6. **Corrective RAG (CRAG)**: Grades retrieved chunks; triggers supplementary web search when relevance is below threshold.
7. **Self-RAG**: Generates reflection tokens during output to self-critique retrieval and generation quality.
8. **Agentic RAG**: Multi-agent architecture — Document Agents per document, coordinated by a Meta-Agent.

## Confidence Notes

High confidence — Humanloop is a well-regarded LLM evaluation and deployment platform; the taxonomy is consistent with academic literature and other 2025 sources.
