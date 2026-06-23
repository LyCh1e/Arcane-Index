---
type: concept
title: "Retrieval-Augmented Generation (RAG)"
created: 2026-06-23
updated: 2026-06-23
tags:
  - ai-engineering
  - rag
  - llm
  - vector-databases
  - embeddings
domain: ai-engineering
complexity: high
related:
  - "[[concepts/rag-architectures]]"
  - "[[concepts/context-compression-llm]]"
  - "[[concepts/mcp-model-context-protocol]]"
  - "[[concepts/prompt-compression]]"
  - "[[entities/graphrag-microsoft]]"
  - "[[questions/research-rag]]"
sources:
  - "[[sources/humanloop-rag-architectures-2025]]"
  - "[[sources/pinecone-rag-guide]]"
---

# Retrieval-Augmented Generation (RAG)

## Definition

**Retrieval-Augmented Generation (RAG)** is a framework that combines a retrieval mechanism with a generative language model to produce factually grounded, up-to-date responses. Instead of relying solely on knowledge encoded in the model's parameters at training time, RAG fetches relevant external documents at inference time and injects them into the prompt before generation.

Introduced by Lewis et al. (Meta AI Research, 2020) and now the dominant pattern for knowledge-intensive LLM applications.

---

## The Core Problem RAG Solves

| Problem | Consequence | RAG's Solution |
|---|---|---|
| Knowledge cutoff | Model cannot answer about recent events | Retrieve from live or updated document stores |
| Hallucination | Model invents plausible-sounding but false facts | Ground generation in retrieved evidence |
| Private data | Model has never seen internal documents | Index and retrieve from proprietary knowledge bases |
| Context window limits | Cannot load an entire knowledge base into context | Retrieve only the top-k most relevant chunks |

---

## The Four-Stage Pipeline

```
USER QUERY
    │
    ▼
┌─────────────────────────────┐
│  1. INDEX (offline)         │  Source docs → chunks → embeddings → vector store
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  2. RETRIEVE (online)       │  Query → embed → similarity search → top-k chunks
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  3. AUGMENT                 │  Inject chunks into prompt: "Context: [...] Question: [query]"
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  4. GENERATE                │  LLM produces a grounded answer
└─────────────────────────────┘
```

---

## Stage 1 — Indexing (Offline)

### Chunking

Documents are split into retrievable units before embedding. Chunk size and overlap are the most influential tuning parameters.

| Strategy | How it works | Best for |
|---|---|---|
| **Fixed-size** | Split at N tokens, optional overlap | Simple text; surprisingly competitive |
| **Sliding window** | Adjacent chunks share 5–10% overlap | Preserving continuity across boundaries |
| **Recursive** | Split on paragraph → sentence → word as needed | General purpose; default recommendation |
| **Semantic** | Group by topic/meaning boundary | Domain-specific documents with clear sections |
| **Parent-child** | Small child chunks for retrieval; parent chunk for context injection | Balancing precision and context |

> **Production guidance** (2026): use recursive chunking by default; reserve semantic chunking for document types where evaluation demonstrates improvement. Semantic chunking is not universally better — benchmarks show mixed results.

### Embedding

Each chunk is passed through an embedding model to produce a dense vector representing its semantic meaning.

- Common models: `text-embedding-3-small` / `text-embedding-3-large` (OpenAI), BGE, `all-MiniLM-L6-v2`, `nomic-embed-text`
- Output: a high-dimensional float vector (typically 384–3072 dimensions)

### Vector Database Storage

Embeddings are stored in a vector database with indexing structures that enable fast approximate nearest-neighbour (ANN) search.

| Index type | Mechanism | Best for |
|---|---|---|
| **HNSW** (Hierarchical Navigable Small World) | Graph-based; logarithmic query time | High-accuracy production workloads |
| **IVF** (Inverted File) | Cluster-then-search; faster at scale | Very large corpora |
| **Flat** | Brute-force exact search | Small datasets or gold-standard evaluation |

**Common vector databases**: Pinecone, Chroma, Weaviate, Qdrant, pgvector (Postgres extension), Milvus, LanceDB.

---

## Stage 2 — Retrieval (Online)

The user's query is embedded using the same model as the index. The database returns the top-k chunks by similarity.

### Similarity Metrics

| Metric | Formula | Notes |
|---|---|---|
| **Cosine similarity** | `cos(q, d) = q·d / (|q||d|)` | Most common; direction not magnitude |
| **Dot product** | `q · d` | Faster; assumes normalised vectors |
| **Euclidean distance** | `||q - d||₂` | Less common for dense embeddings |

### Retrieval Methods

**Semantic search** (dense vectors): Finds meaning-based matches. Handles synonyms and paraphrasing well. Can miss exact keyword matches.

**Lexical / keyword search** (sparse vectors, BM25): Matches exact terms. Good for domain jargon and specific identifiers.

**Hybrid search**: Combines dense + sparse retrieval, then re-ranks. Best overall performance; default for production systems.

---

## Stage 3 — Augmentation

Retrieved chunks are injected into the prompt. The standard pattern:

```
System: You are a helpful assistant. Answer only using the provided context.
         If the context does not contain the answer, say "I don't know."

Context:
[Chunk 1 text]
[Chunk 2 text]
...

Question: [user query]
Answer:
```

---

## Stage 4 — Generation

The LLM generates a response grounded in the injected context. Crucially: the model is not inventing facts from parametric memory — it is synthesising the retrieved evidence.

---

## Evaluation — RAGAS Framework

RAGAS (Retrieval-Augmented Generation Assessment) is the standard evaluation framework for RAG systems. It measures both the retriever and the generator independently.

| Metric | What it measures | Formula (conceptual) |
|---|---|---|
| **Faithfulness** | Are all claims in the answer supported by retrieved chunks? | `supported_claims / total_claims` |
| **Context Precision** | Are retrieved chunks actually relevant to the question? | `relevant_chunks / retrieved_chunks` |
| **Context Recall** | Does the retrieved context contain everything needed to answer? | `covered_information / required_information` |
| **Answer Relevancy** | Does the answer actually address the question? | Semantic similarity of answer to question |
| **Noise Sensitivity** | Does adding irrelevant chunks degrade answer quality? | Answer stability under noise injection |

A faithfulness score of 0.5 means half the answer's claims are unsupported — the model is hallucinating the other half.

---

## RAG vs Fine-Tuning

| Dimension | RAG | Fine-Tuning |
|---|---|---|
| **What it changes** | External context injected at inference | Model weights updated at training |
| **Knowledge freshness** | Instant — add/update documents in the store | Requires expensive re-training |
| **Cost** | Low — no GPU training | High — GPU compute, days to weeks |
| **Latency** | +retrieval overhead at inference | Zero overhead — knowledge is in weights |
| **Source attribution** | Can cite specific retrieved chunks | Cannot trace which training example caused an output |
| **Hallucination** | Reduced (grounded in context) | Not inherently reduced |
| **Best for** | Dynamic knowledge, QA over documents | Task-specific behaviour, style, format |

**2025 consensus**: the two are complementary, not competing. Fine-tune for behaviour and format; use RAG for knowledge. Most production systems combine both.

---

## RAG and Related Concepts

- **MCP Resources primitive**: The [[concepts/mcp-model-context-protocol]] Resources primitive is MCP's standardised way of exposing retrievable data to an LLM host — effectively RAG built into the protocol layer.
- **Context compression**: When retrieved chunks are too long for the context window, [[concepts/context-compression-llm]] techniques (prompt compression, summarisation) can reduce their token footprint before injection.
- **Agentic RAG**: See [[concepts/rag-architectures]] for the full architecture taxonomy, including agentic patterns where the LLM controls when and what to retrieve.

---

## Key Entities and Tools

- [[entities/graphrag-microsoft]]: Microsoft's graph-based RAG variant using knowledge graphs and community summaries.
- **RAGAS**: Python library for RAG evaluation (`pip install ragas`).
- **LangChain / LlamaIndex**: The two dominant RAG orchestration frameworks.
- **Pinecone, Chroma, Weaviate, Qdrant, pgvector**: Popular vector databases.

---

## Open Questions

- Will hybrid search + re-ranking become the universal default, or will dense-only retrieval catch up with better embedding models?
- Can end-to-end trainable RAG systems (retriever + generator jointly optimised) outperform modular pipelines in production?
- How will multimodal RAG (retrieving images, tables, audio) mature?
- What is the right chunking strategy for code, structured data (JSON/CSV), and mixed-media documents?
