---
type: resource
address: c-000120
title: "Ollama — Local LLM Inference"
domain: ai-engineering
created: 2026-07-19
updated: 2026-07-19
tags: [resource, ollama, local-llm, inference, open-weight, DeepSeek, ai-agents, self-hosted]
related:
  - entities/deepseek
  - concepts/ai-agent-architecture
  - resources/ai-agent-frameworks
---

# Ollama — Local LLM Inference

Ollama is the standard tool for running open-weight LLMs on your own hardware. It downloads, manages, and serves models through an **OpenAI-compatible REST API** on `localhost:11434`, making it a drop-in backend for any LLM framework or client.

- **Website:** https://ollama.com
- **GitHub:** https://github.com/ollama/ollama
- **Licence:** MIT
- **Platforms:** macOS, Linux, Windows
- **API format:** OpenAI-compatible (`/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`)

---

## Installation

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows
# Download installer from https://ollama.com/download

# Verify
ollama --version
```

---

## Running a Model

```bash
# Pull and run (interactive)
ollama run deepseek-r1:7b

# Pull only
ollama pull deepseek-r1:14b

# List installed models
ollama list

# Remove a model
ollama rm deepseek-r1:7b

# Serve (background daemon — starts automatically on install)
ollama serve
```

The daemon listens on `http://localhost:11434` by default.

---

## Key Models for AI Agents

| Model | Pull command | VRAM | Notes |
|---|---|---|---|
| **DeepSeek-R1 7B** | `ollama pull deepseek-r1:7b` | 8 GB | Good reasoning; fits most laptops |
| **DeepSeek-R1 14B** | `ollama pull deepseek-r1:14b` | 16 GB | Better instruction following |
| **DeepSeek-R1 32B** | `ollama pull deepseek-r1:32b` | 32 GB | Near-frontier quality |
| **Llama 3.3 70B** | `ollama pull llama3.3` | 48 GB | Strong general-purpose |
| **Mistral 7B** | `ollama pull mistral` | 8 GB | Fast, good tool calling |
| **Qwen 2.5 7B** | `ollama pull qwen2.5` | 8 GB | Strong at code and structured output |
| **nomic-embed-text** | `ollama pull nomic-embed-text` | Low | Embeddings for RAG pipelines |

Full model library: https://ollama.com/library

---

## Framework Integration

All major agent frameworks support Ollama via the OpenAI-compatible endpoint.

### LangGraph / LangChain

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-r1:7b",
    base_url="http://localhost:11434/v1",
    api_key="ollama"          # any non-empty string; Ollama ignores it
)
```

### CrewAI

```python
import os
os.environ["OPENAI_API_BASE"]   = "http://localhost:11434/v1"
os.environ["OPENAI_API_KEY"]    = "ollama"
os.environ["OPENAI_MODEL_NAME"] = "deepseek-r1:7b"
```

### Plain OpenAI SDK

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="deepseek-r1:7b",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### LlamaIndex

```python
from llama_index.llms.ollama import Ollama

llm = Ollama(model="deepseek-r1:7b", request_timeout=120.0)
```

---

## Tool Calling with Ollama

Not all models served via Ollama support tool calling. Models that do (as of 2026):

| Model | Tool calling |
|---|---|
| DeepSeek-R1 (7B, 14B, 32B) | ✅ |
| Llama 3.x | ✅ |
| Mistral | ✅ |
| Qwen 2.5 | ✅ |
| Gemma 3 | ✅ |

If tool calling fails, check that the Ollama model manifest includes `tools` in its capabilities:
```bash
ollama show deepseek-r1:7b --modelfile
```

---

## Local Agent Stack (Full Example)

```
Hardware (your machine)
├── Ollama daemon         → serves model at localhost:11434
└── Agent script (Python)
    ├── LangGraph (or CrewAI) — orchestrates the agent loop
    ├── Tool definitions      — functions the agent can call
    └── ChatOpenAI pointing at http://localhost:11434/v1
```

```python
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# 1. Point to local Ollama
llm = ChatOpenAI(
    model="deepseek-r1:7b",
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

# 2. Define tools
@tool
def search(query: str) -> str:
    """Search the web for information."""
    # ... your implementation
    return "results"

# 3. Create ReAct agent
agent = create_react_agent(llm, tools=[search])

# 4. Run
result = agent.invoke({"messages": [("user", "What is the weather in Singapore?")]})
```

---

## Performance Tips

- **GPU acceleration:** Ollama uses Metal (macOS), CUDA (NVIDIA), or ROCm (AMD) automatically if available — no configuration needed.
- **CPU fallback:** Models run on CPU if no GPU is detected, but are much slower. 7B models are usable; 14B+ become impractical.
- **Context size:** Set with `OLLAMA_MAX_LOADED_MODELS` env var or in the model `Modelfile`. Defaults to model's trained context.
- **Concurrency:** Ollama queues requests by default. Set `OLLAMA_NUM_PARALLEL=4` to allow parallel inference (requires proportionally more VRAM).

---

## Alternative Local Inference Tools

| Tool | Key difference |
|---|---|
| **LM Studio** | GUI-first; good for non-technical users; same OpenAI-compatible API |
| **vLLM** | Production-grade; batching, continuous batching, high throughput — server deployments |
| **llama.cpp** | The underlying engine Ollama uses; lower-level, more control |
| **Jan** | Desktop app similar to LM Studio |

---

## See Also

- [[entities/deepseek]] — DeepSeek model lineup and agent-specific usage
- [[concepts/ai-agent-architecture]] — agent control loop; how a local LLM fits into the stack
- [[resources/ai-agent-frameworks]] — LangGraph, CrewAI, etc. — all work with Ollama as the backend
