---
type: entity
entity_type: company
address: c-000119
title: "DeepSeek"
created: 2026-07-19
updated: 2026-07-19
tags: [entity, deepseek, llm, open-weight, ai-agents, china, ollama]
status: active
related:
  - concepts/ai-agent-architecture
  - resources/ai-agent-frameworks
  - resources/ollama-local-inference
---

# DeepSeek

## Overview

DeepSeek is a Chinese AI research lab that has released open-weight frontier models competitive with GPT-4o and Claude Sonnet at significantly lower cost. Their models are notable for being open-weight (MIT licence for R1) and for having an OpenAI-compatible API, making them straightforward to integrate into existing LLM toolchains.

- **Website:** https://www.deepseek.com
- **API:** https://api.deepseek.com
- **GitHub:** https://github.com/deepseek-ai
- **Headquarters:** China (Hangzhou)
- **Licence:** MIT (R1 open weights); proprietary (hosted API)

---

## Model Lineup

| Model | Type | Context | Open weights | Best for |
|---|---|---|---|---|
| **DeepSeek-V3** | General-purpose MoE | 128K | No (API only) | Fast, cheap production use; tool calling; RAG |
| **DeepSeek-R1** | Chain-of-thought reasoning | 128K | ✅ MIT | Multi-step planning, complex reasoning, research |
| **DeepSeek-R1 Distil (7B–70B)** | Distilled R1 reasoning | 128K | ✅ MIT | Local deployment at various hardware tiers |

---

## Suitability for AI Agents

DeepSeek-V3 and R1 both support the capabilities required by the [[concepts/ai-agent-architecture]] control loop:

| Requirement | Support |
|---|---|
| Tool / function calling | ✅ Native JSON function definitions |
| Structured output / JSON mode | ✅ |
| Multi-turn instruction following | ✅ |
| Large context window | ✅ 128K tokens |
| OpenAI-compatible API | ✅ Drop-in for LangGraph, CrewAI, LlamaIndex, plain OpenAI SDK |

**Which model for agents:**

| Agent type | Recommended |
|---|---|
| General-purpose (search, write, execute) | DeepSeek-V3 (`deepseek-chat`) |
| Complex planning / reasoning | DeepSeek-R1 (`deepseek-reasoner`) |
| Cost-sensitive / high-volume | DeepSeek-V3 (cheapest capable option in 2026) |
| Air-gapped / self-hosted | DeepSeek-R1 distilled variants via [[resources/ollama-local-inference]] |

---

## API Integration (OpenAI-compatible)

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-deepseek-key",
    base_url="https://api.deepseek.com"
)

# LangChain / LangGraph:
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="deepseek-chat",          # or "deepseek-reasoner" for R1
    api_key="your-deepseek-key",
    base_url="https://api.deepseek.com"
)
```

---

## Local Deployment (Open Weights)

R1 distilled variants run locally via **Ollama**:

```bash
ollama pull deepseek-r1:7b     # ~8 GB VRAM — most laptops
ollama pull deepseek-r1:14b    # ~16 GB VRAM
ollama pull deepseek-r1:32b    # ~32 GB VRAM
```

Then point any OpenAI-compatible client to `http://localhost:11434/v1`. See [[resources/ollama-local-inference]].

**Hardware guide:**

| Variant | VRAM | RAM | Notes |
|---|---|---|---|
| R1 7B | 8 GB | 16 GB | Runs on most gaming laptops |
| R1 14B | 16 GB | 32 GB | Good quality/cost balance |
| R1 32B | 32 GB | 64 GB | Near-frontier quality locally |
| V3 (full 671B MoE) | ~400 GB | Server-grade | Not practical on consumer hardware |

---

## Caveats

| Concern | Detail |
|---|---|
| **Data sovereignty** | Hosted API routes through Chinese servers. Not suitable for regulated industries, enterprise data, or PII without self-hosting. |
| **R1 reasoning verbosity** | R1 exposes `<think>...</think>` blocks in its response. These count toward token cost and slow agent loops — strip them if not needed. |
| **Tool call reliability** | V3 is solid; R1 can occasionally malform tool call JSON on complex schemas. Always validate tool call outputs. |
| **API availability** | Subject to rate limits and demand spikes. Self-hosting or using a provider mirror (e.g., Fireworks, Together AI) mitigates this. |

---

## See Also

- [[resources/ollama-local-inference]] — serve DeepSeek (and other open-weight models) locally
- [[concepts/ai-agent-architecture]] — agent control loop, memory, tools, evals, guardrails
- [[resources/ai-agent-frameworks]] — framework comparison (LangGraph, CrewAI, etc. — all work with DeepSeek)
