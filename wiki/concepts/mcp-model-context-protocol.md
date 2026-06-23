---
type: concept
title: "Model Context Protocol (MCP)"
created: 2026-06-23
updated: 2026-06-23
tags:
  - ai-engineering
  - protocols
  - tool-use
  - agents
  - mcp
domain: ai-engineering
complexity: high
related:
  - "[[concepts/mcp-security]]"
  - "[[entities/agentic-ai-foundation-aaif]]"
  - "[[questions/research-mcp-servers]]"
sources:
  - "[[sources/anthropic-mcp-launch-2024]]"
  - "[[sources/mcp-spec-2025-11-25]]"
  - "[[sources/mcp-first-year-2025]]"
---

# Model Context Protocol (MCP)

## Definition

The **Model Context Protocol (MCP)** is an open standard and open-source protocol introduced by Anthropic on 25 November 2024. It standardises how AI systems — particularly large language models — connect to external tools, data sources, and systems. MCP replaces fragmented, one-off integrations with a single, provider-agnostic protocol analogous to USB-C for AI applications. (Source: [[sources/anthropic-mcp-launch-2024]])

## Origin

**Created by**: David Soria Parra and Justin Spahr-Summers at Anthropic.
**Launched**: 25 November 2024.
**Donated to**: The Agentic AI Foundation (AAIF) under the Linux Foundation, December 2025.

The core problem MCP addresses is the "information silo" problem: AI models that could not reach live data or take action in external systems without bespoke integrations built for every pairing of model and tool.

## Architecture

MCP follows a three-layer client–server model built on JSON-RPC 2.0.

```
┌──────────────────────────────┐
│           HOST               │  e.g. Claude Desktop, Cursor, custom agent
│  ┌───────────┐               │
│  │  MCP Client│──────────────┼──► MCP Server A (filesystem)
│  └───────────┘               │
│  ┌───────────┐               │
│  │  MCP Client│──────────────┼──► MCP Server B (GitHub)
│  └───────────┘               │
└──────────────────────────────┘
```

| Layer | Role |
|---|---|
| **Host** | The LLM application that orchestrates the interaction (e.g. Claude Desktop). |
| **Client** | Lives inside the Host; maintains one stateful session with one MCP Server. Handles protocol negotiation, capability exchange, and bidirectional message routing. |
| **Server** | Exposes capabilities (tools, resources, prompts) to the LLM. Connects to APIs, databases, file systems, or any external service. |

One Host may run many Clients simultaneously, each connected to a different Server.

## The Three Primitives

### Tools
Callable functions the LLM may invoke (with user approval). Examples: querying a database, calling an API, running a shell command, searching the web.

### Resources
Static or semi-static data exposed to the LLM as context. Analogous to file reads — FAQ documents, configuration files, API response snapshots.

### Prompts
Pre-written templates that scaffold common interactions. The Server provides the prompt; the LLM uses it as structured guidance.

## Transport Mechanisms

| Transport | Use Case | Added |
|---|---|---|
| **Stdio** | Local servers, same-machine IPC, high-performance | Nov 2024 (v1) |
| **HTTP + SSE** | Remote servers, streaming events | Nov 2024 (v1) |
| **Streamable HTTP** | Modern remote transport; POST requests with optional SSE streaming | March 2025 spec |

Streamable HTTP became the default for vendor-hosted remote servers by mid-2025. Most public servers (Sentry, Linear, Figma, Supabase, Notion) now ship as `--transport http` URLs with browser-based OAuth.

## SDK and Language Support

Official and community SDKs exist for:
Python, TypeScript, Java, Kotlin, C#, Go, Ruby, Rust, Swift, PHP, Perl.

TypeScript is the primary language of the reference implementation. The Python SDK includes `FastMCP`, which uses decorators and type hints to auto-generate tool schemas. Testing is done via `npx @modelcontextprotocol/inspector`.

## The Specification Timeline

| Date | Milestone |
|---|---|
| 25 Nov 2024 | Protocol launched by Anthropic; Stdio + HTTP/SSE transports. |
| Mar 2025 | OpenAI adopts MCP; Streamable HTTP transport introduced. |
| Sep 2025 | MCP Registry launched (~500 entries). |
| Nov 2025 | v2025-11-25 spec: async Tasks, CIMD OAuth, M2M OAuth, Cross App Access, extensions framework. |
| Dec 2025 | Donated to AAIF / Linux Foundation. |
| Apr 2026 | MCP Dev Summit North America (~1,200 attendees). Registry grows to ~2,000 entries. |

## November 2025 Specification Highlights

The 2025-11-25 release is the most significant update since launch. (Source: [[sources/mcp-spec-2025-11-25]])

**Async Tasks primitive**: Any request can return a task handle instead of a blocking response. Clients poll or subscribe for status transitions (`working` → `input_required` → `completed` / `failed`). Enables long-running agent workflows.

**Client ID Metadata Documents (CIMD)**: Replaces Dynamic Client Registration. Clients self-host a metadata URL as identity, anchored in DNS and HTTPS. Eliminates per-server registration friction.

**Machine-to-Machine OAuth** (`client_credentials`): Headless agents and background automation no longer require user consent flows.

**Cross App Access (XAA)**: Enterprise identity providers regain visibility and control when users connect MCP clients to downstream tools.

**Extensions framework**: Composable optional extensions allow ecosystem innovation without bloating the core spec.

## Ecosystem

The MCP ecosystem grew from a few dozen servers at launch to over 500 public servers by April 2026, catalogued on the MCP Registry. The official reference servers split in May 2025:
- **Active**: `modelcontextprotocol/servers` — filesystem, git, fetch, memory, sequential-thinking, time, everything.
- **Archived**: `modelcontextprotocol/servers-archived` — GitHub, Postgres, Slack, Brave, Sentry, Puppeteer (moved to vendor-maintained repos).

The recommended starter set for Claude Code or Cursor: **Filesystem, GitHub, Context7, Playwright, Sequential Thinking**.

## MCP vs Function Calling

| Dimension | MCP | Function Calling |
|---|---|---|
| Scope | Provider-agnostic protocol; tools reusable across clients and models | Vendor-specific (OpenAI, Anthropic, etc.) |
| Setup | Separate server process; more infrastructure | Inline in API request; simpler for small use |
| Reuse | Any MCP client can use a given server | Tools are application-specific |
| State | Stateful sessions | Stateless per-request |
| Best for | Shared infrastructure, multi-client, production agents | Lightweight prototypes, single-app tools |

The recommended production pattern is both: function calling for application-specific tools, MCP for shared infrastructure.

## Governance

MCP is governed by the [[entities/agentic-ai-foundation-aaif]] (AAIF), a Linux Foundation project. Co-founders: Anthropic, OpenAI, Block. Supporting members include AWS, Google DeepMind, Microsoft, Cloudflare, GitHub, and Bloomberg. The maintainer group has 9 core leaders and 58 maintainers as of November 2025.

## Security

See [[concepts/mcp-security]] for a dedicated treatment of the known vulnerability classes (prompt injection, tool poisoning, rug pull attacks, supply chain risks).

## Open Questions

- How will the async Tasks primitive evolve as multi-agent orchestration matures?
- Will CIMD-based OAuth become the universal standard, or will competing identity patterns fragment the ecosystem?
- How will the OWASP MCP Top 10 shape security tooling and compliance requirements in enterprises?
