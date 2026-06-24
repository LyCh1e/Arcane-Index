---
type: concept
status: established
title: "RAG Architectures"
created: 2026-06-23
updated: 2026-06-23
tags:
  - ai-engineering
  - rag
  - llm
  - agents
  - architecture
domain: ai-engineering
complexity: high
related:
  - "[[concepts/retrieval-augmented-generation]]"
  - "[[entities/graphrag-microsoft]]"
  - "[[concepts/mcp-model-context-protocol]]"
  - "[[synthesis/research-rag]]"
sources:
  - "[[sources/humanloop-rag-architectures-2025]]"
---

# RAG Architectures

## Overview

RAG has evolved through four generations since the original Lewis et al. (2020) paper. Each generation added complexity to address specific failure modes of the prior approach. The right architecture depends on query complexity, latency budget, and accuracy requirements.

```
Naive RAG (2020–2022)
    └── Advanced RAG (2022–2023)
            └── Modular / Agentic RAG (2023–2024)
                    └── GraphRAG (2024–present)
```

---

## Generation 1 — Naive RAG

**Pattern**: Fixed query → vector search → inject top-k → generate.

**Failure modes**:
- Low context precision: retrieved chunks are often irrelevant
- Low context recall: missing relevant information scattered across documents
- Hallucination persists when retrieved context is insufficient
- Cannot handle multi-hop questions requiring information from multiple sources

**Best for**: Simple FAQ systems, customer support bots with a bounded, stable document set.

---

## Generation 2 — Advanced RAG

Addresses Naive RAG's failure modes with pre-retrieval and post-retrieval enhancements.

### Pre-retrieval Techniques (improve the query)

**Query Transformation**
Transform the user's raw question into a better retrieval query before searching.
- **Query rewriting**: Rephrase the question for better embedding similarity
- **Query expansion**: Generate multiple sub-queries to cover different facets
- **Step-back prompting**: Ask a more abstract question to retrieve broader context first

**HyDE (Hypothetical Document Embeddings)**
Generate a hypothetical ideal answer first, embed *that*, then retrieve documents similar to the hypothetical answer rather than to the bare question. Handles vague or abstract queries where the question embedding is far from the answer's embedding space.

### Post-retrieval Techniques (improve the context)

**Re-ranking**
Retrieve a large candidate set (top-50), then score each candidate against the query using a cross-encoder. Return only top-k (e.g., top-5) after re-ranking. Cross-encoders process query and document jointly, giving more accurate relevance scores than the embedding-based retriever.
- Common re-rankers: Cohere Rerank, ColBERT, BGE-Reranker, Jina Reranker

**Contextual Compression**
Compress retrieved documents to extract only the query-relevant passages. Reduces noise and saves context window tokens before injection.

**Parent-Child Chunking**
Index small child chunks for high-precision retrieval; when a child chunk is retrieved, return its larger parent chunk as context. Balances retrieval precision with contextual completeness.

---

## Generation 3 — Modular and Adaptive RAG

### Modular RAG
Decomposes the pipeline into independent, swappable components — query router, retriever, reranker, compressor, generator — each tunable independently. Enables domain-specific optimisation per stage.

### Branched RAG
Evaluates multiple retrieval sources in parallel and selects the most relevant one based on the query. Avoids querying all sources every time (cost) while preserving access to specialised corpora.

### Adaptive RAG
Dynamically chooses the retrieval strategy based on query complexity. Simple factual queries go to a single-source fast path; complex analytical queries trigger multi-source retrieval with re-ranking.

### Corrective RAG (CRAG)
Grades each retrieved chunk for relevance. If no chunk meets the relevance threshold, CRAG automatically triggers a web search for supplementary information. Provides automatic fallback for knowledge gaps.

### Self-RAG
The model generates special **reflection tokens** inline during generation to:
1. Decide *whether* retrieval is needed (avoids unnecessary calls)
2. Critique retrieved passages for relevance and support
3. Evaluate the quality of its own generated segments

Reduces hallucination on long-form tasks but is slower due to iterative self-assessment.

### FLARE (Forward-Looking Active Retrieval)
Triggers retrieval dynamically during generation whenever the model's next-token confidence falls below a threshold. The model pauses, retrieves, and re-generates the uncertain span with new context. Effective for long documents where information needs evolve mid-generation.

---

## Generation 4 — Agentic RAG

An LLM agent autonomously decides when, what, and how to retrieve. Retrieval is one tool in a broader tool-use loop rather than a fixed pre-generation step.

### Architecture

```
User Query
    │
    ▼
┌─────────────┐
│   AGENT     │◄── Orchestrates: plan → retrieve → reason → retrieve again → generate
└─────┬───────┘
      │  Uses tools:
      ├── Vector search (dense retrieval)
      ├── Web search (external knowledge)
      ├── Calculator / code executor
      ├── Structured DB query
      └── Document Agent (sub-agent per document)
```

**Document Agents**: Each major document has a dedicated sub-agent. A Meta-Agent coordinates between Document Agents, routing queries to the relevant specialist. Effective for large, multi-source research tasks.

**Multi-hop retrieval**: The agent iteratively refines its queries based on what it learns from each retrieval step, enabling answers that require chaining information across multiple documents.

**Best for**: Automated research, executive decision support, scientific literature review, enterprise multi-source QA.

**Trade-off**: Most capable but highest latency and most complex to evaluate and debug.

---

## GraphRAG (Microsoft, 2024)

GraphRAG replaces the flat vector store with a **knowledge graph** built from the document corpus.

### How it works

1. **Entity extraction**: LLM reads all documents and extracts entities (people, places, concepts, events) and their relationships.
2. **Graph construction**: Entities become nodes; relationships become edges.
3. **Community detection**: The Leiden algorithm clusters densely-connected nodes into "communities" at multiple hierarchical levels (high-level themes → low-level topics).
4. **Community summarisation**: An LLM summarises each community, producing a hierarchical summary of the entire corpus.
5. **Retrieval**: Queries search the community summaries and traverse the graph to retrieve multi-hop relational context.

### Strengths vs Weaknesses

| | GraphRAG | Naive/Vector RAG |
|---|---|---|
| **Global questions** (themes, summaries) | Excellent — 72–83% comprehensiveness vs vector RAG | Poor |
| **Local questions** (specific facts) | Comparable | Good |
| **Multi-hop reasoning** | Native — graph traversal follows relationships | Requires agentic patterns |
| **Index cost** | High — LLM reads every document twice | Low — just embedding |
| **Query cost** | Can be high (community summaries are long) | Low |

**LazyGraphRAG** (June 2025): reduced GraphRAG indexing cost to 0.1% of original by deferring full graph construction.

**Best for**: Large corpora where users ask holistic questions ("What are the main themes?", "How does X relate to Y?") rather than specific fact lookups.

See [[entities/graphrag-microsoft]] for full entity page.

---

## Choosing an Architecture

| Scenario | Recommended Architecture |
|---|---|
| Small, static FAQ / support bot | Naive RAG |
| Production QA over internal documents | Advanced RAG (hybrid search + re-ranking) |
| Multi-domain enterprise search | Modular / Adaptive RAG |
| High-accuracy critical applications | Corrective RAG or Self-RAG |
| Long-form research and writing | FLARE or Agentic RAG |
| Thematic / relationship questions over large corpora | GraphRAG |
| Autonomous research agent | Agentic RAG with Document Agents |

---

## Open Questions

- Is self-RAG's quality gain worth the latency and complexity cost in production?
- Can LazyGraphRAG match full GraphRAG accuracy while keeping costs low enough for typical enterprise corpora?
- Will multimodal RAG (images, tables, audio) follow the same generational pattern?
