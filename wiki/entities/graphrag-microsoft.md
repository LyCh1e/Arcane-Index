---
type: entity
status: established
title: "GraphRAG (Microsoft Research)"
category: tool
created: 2026-06-23
updated: 2026-06-23
tags:
  - ai-engineering
  - rag
  - knowledge-graph
  - microsoft
url: "https://microsoft.github.io/graphrag/"
github: "https://github.com/microsoft/graphrag"
related:
  - "[[concepts/rag-architectures]]"
  - "[[concepts/retrieval-augmented-generation]]"
  - "[[synthesis/research-rag]]"
---

# GraphRAG (Microsoft Research)

## What It Is

**GraphRAG** is a modular, graph-based Retrieval-Augmented Generation system developed by Microsoft Research. It extends standard vector RAG by constructing a **knowledge graph** from the source corpus and using hierarchical community summaries for retrieval — enabling holistic, relationship-aware answers that flat vector search cannot produce.

Published as a research paper (arXiv:2404.16130, April 2024) and released as open-source on GitHub.

## Key Metrics

- **72–83% comprehensiveness** improvement over naive RAG on global sensemaking queries (Microsoft Research, 2024).
- **3.4× accuracy improvement** in enterprise scenarios (Diffbot KG-LM Benchmark).

## Core Algorithm

1. Extract entities and relationships from all documents using an LLM.
2. Construct a knowledge graph.
3. Apply **Leiden community detection** to cluster nodes hierarchically.
4. Summarise each community with an LLM.
5. At query time: retrieve relevant community summaries and traverse the graph for local context.

## LazyGraphRAG (June 2025)

A cost-optimised variant that defers full graph construction, reducing indexing cost to **0.1% of the original GraphRAG cost** while maintaining comparable quality. Enables GraphRAG to be practical for larger or more frequently updated corpora.

## Deployment

Now available through **Microsoft Discovery**, an agentic platform for scientific research built on Azure.

## When to Use

Holistic or relational queries over large corpora — "What are the main themes?", "How are concept A and entity B related?" Standard vector RAG outperforms GraphRAG on simple fact lookups, and GraphRAG's indexing cost makes it unsuitable for frequently updated document sets without LazyGraphRAG.
