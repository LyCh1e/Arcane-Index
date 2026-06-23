---
type: synthesis
title: "Research: Retrieval-Augmented Generation (RAG)"
created: 2026-06-23
updated: 2026-06-23
tags:
  - research
  - rag
  - ai-engineering
  - llm
  - vector-databases
  - agents
status: developing
related:
  - "[[concepts/retrieval-augmented-generation]]"
  - "[[concepts/rag-architectures]]"
  - "[[entities/graphrag-microsoft]]"
  - "[[concepts/context-compression-llm]]"
  - "[[concepts/mcp-model-context-protocol]]"
sources:
  - "[[sources/humanloop-rag-architectures-2025]]"
  - "[[sources/pinecone-rag-guide]]"
---

# Research: Retrieval-Augmented Generation (RAG)

## Overview

Retrieval-Augmented Generation (RAG) is the dominant pattern for knowledge-intensive LLM applications. Introduced by Lewis et al. (Meta AI Research, 2020), it solves three core problems: LLM knowledge cutoffs, hallucination on factual questions, and the impossibility of loading entire private corpora into context. RAG fetches relevant document chunks at inference time and injects them into the prompt before generation. Since 2022 the architecture has evolved through four generations, from a simple fixed pipeline to fully agentic multi-source retrieval systems and graph-structured knowledge bases (GraphRAG).

---

## Key Findings

- **RAG is a four-stage pipeline.** Indexing (offline): chunk → embed → store in vector database. Retrieval (online): embed query → ANN search → top-k chunks. Augmentation: inject chunks into prompt. Generation: LLM produces grounded answer. (Source: [[sources/pinecone-rag-guide]])

- **Chunking strategy is the most overlooked tuning parameter.** Recursive chunking is the safe default. Semantic chunking outperforms fixed-size on some domain-specific document types but underperforms on others — 87% vs 13% in one clinical study, but 54% vs 69% for recursive splitting in a 2026 general benchmark. Always evaluate on your specific corpus before committing to a strategy.

- **Hybrid search (dense + sparse) outperforms either alone.** Dense (semantic) vectors handle synonyms and paraphrasing; sparse (BM25/keyword) vectors handle exact terms and domain jargon. Combining both with re-ranking is the current production default. (Source: [[sources/pinecone-rag-guide]])

- **RAG has evolved through four generations.** Naive RAG (2020) → Advanced RAG with query transformation, HyDE, re-ranking, contextual compression (2022) → Modular/Adaptive/Self-RAG/Corrective RAG (2023) → Agentic RAG and GraphRAG (2024–present). (Source: [[sources/humanloop-rag-architectures-2025]])

- **Re-ranking is the highest-ROI single improvement to a naive RAG pipeline.** Retrieve top-50, score with a cross-encoder, return top-5. Adds ~50–100ms latency but substantially improves context precision.

- **HyDE bridges query-document embedding gaps for abstract queries.** Generate a hypothetical ideal answer first, embed that, retrieve against the hypothetical. Handles vague queries where the bare question's embedding is distant from relevant document embeddings. More expensive (one extra LLM call) but often worth it for research-style queries.

- **GraphRAG dominates on global/relational questions; vector RAG wins on specific lookups.** Microsoft's GraphRAG achieves 72–83% comprehensiveness over naive RAG on holistic queries. LazyGraphRAG (June 2025) reduces indexing cost to 0.1% of original, making it practical for real-world corpora. (Source: [[entities/graphrag-microsoft]])

- **RAG and fine-tuning are complementary.** Fine-tuning teaches the model *how to behave* (format, style, task-specific skill); RAG gives it *what to know* (current, specific facts). The 2025 consensus is to use both. Neither alone is optimal for most production applications.

- **RAGAS is the standard evaluation framework.** Key metrics: Faithfulness (claims supported by context), Context Precision (retrieved chunks that are relevant), Context Recall (coverage of needed information), Answer Relevancy (answer matches the question). Faithfulness below 0.8 in production indicates active hallucination from insufficient or ignored context.

- **RAG connects directly to MCP.** The [[concepts/mcp-model-context-protocol]] Resources primitive is a standardised protocol-level implementation of RAG — MCP servers expose retrievable data to LLM hosts via a consistent interface. Agentic RAG and MCP-based agents are converging.

- **RAG connects to context compression.** When retrieved chunks overflow the context window, [[concepts/context-compression-llm]] techniques (summarisation, prompt compression) can reduce their footprint before injection. See [[concepts/prompt-compression]] for token-level compression approaches.

---

## Key Entities

- [[entities/graphrag-microsoft]]: Microsoft Research's graph-based RAG system; open-source on GitHub; 72–83% comprehensiveness improvement on global queries.
- **Lewis et al. (Meta AI Research, 2020)**: Original RAG paper authors.
- **RAGAS**: Python evaluation framework for RAG pipelines.
- **LangChain / LlamaIndex**: Dominant RAG orchestration frameworks.
- **Pinecone, Chroma, Weaviate, Qdrant, pgvector**: Leading vector databases.

---

## Key Concepts

- [[concepts/retrieval-augmented-generation]]: Full pipeline, chunking, embedding, similarity metrics, RAGAS evaluation, RAG vs fine-tuning.
- [[concepts/rag-architectures]]: Full taxonomy — Naive → Advanced (HyDE, re-ranking, CRAG, Self-RAG, FLARE) → Modular/Adaptive → Agentic → GraphRAG.

---

## Contradictions

- **Semantic vs recursive chunking**: Two 2025–2026 benchmarks contradict each other. Adaptive/semantic chunking hit 87% accuracy in a clinical study vs 13% for fixed-size; but a general benchmark placed recursive 512-token splitting first at 69% vs semantic at 54%. Conclusion: chunking performance is corpus-dependent — evaluate on your own data, do not generalise.

- **GraphRAG cost vs quality**: Microsoft's own paper claims 72–83% comprehensiveness improvement; LazyGraphRAG dramatically cuts cost but with some quality trade-off. Real-world deployments need to benchmark both on their specific corpus.

---

## Open Questions

- Will end-to-end jointly trained RAG (retriever + generator optimised together) outperform modular pipelines?
- How will multimodal RAG (images, tables, code, audio) standardise its chunking, embedding, and retrieval?
- Will agentic RAG and MCP fully converge — i.e., will MCP servers become the universal retrieval layer for agents?
- What is the right evaluation metric for agentic RAG where the "retrieval" is distributed across multiple dynamic steps?
- Can LazyGraphRAG reach full GraphRAG quality while maintaining 0.1% indexing cost?

---

## Sources

- [[sources/humanloop-rag-architectures-2025]]: Humanloop — 8 RAG architecture taxonomy.
- [[sources/pinecone-rag-guide]]: Pinecone — four-stage pipeline and hybrid search.

---

## Research Metadata

| Field | Value |
|---|---|
| Rounds | 3 |
| Web searches | 6 |
| Sources fetched | 3 |
| Pages created | 6 |
| Date | 2026-06-23 |
