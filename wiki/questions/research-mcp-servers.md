---
type: synthesis
title: "Research: MCP Servers (Model Context Protocol)"
created: 2026-06-23
updated: 2026-06-23
tags:
  - research
  - mcp
  - ai-engineering
  - agents
  - tool-use
  - protocols
status: developing
related:
  - "[[concepts/mcp-model-context-protocol]]"
  - "[[concepts/mcp-security]]"
  - "[[entities/agentic-ai-foundation-aaif]]"
sources:
  - "[[sources/anthropic-mcp-launch-2024]]"
  - "[[sources/mcp-spec-2025-11-25]]"
  - "[[sources/mcp-first-year-2025]]"
---

# Research: MCP Servers (Model Context Protocol)

## Overview

The Model Context Protocol (MCP) is an open standard launched by Anthropic on 25 November 2024 to solve the "information silo" problem: AI models could not reach live data or take external actions without bespoke integrations for every model-tool pair. MCP provides a single provider-agnostic protocol — modelled on JSON-RPC 2.0 — through which any LLM host can connect to any MCP server exposing tools, resources, or prompts. Within one year, MCP grew from a small Anthropic project to the industry-wide standard for AI tool integration, adopted by OpenAI, Google, Microsoft, and hundreds of community builders. It was donated to the Linux Foundation's Agentic AI Foundation (AAIF) in December 2025.

---

## Key Findings

- **MCP is a standardised tool layer, not a model feature.** Vendor-specific function calling (OpenAI, Anthropic, Google) requires per-provider integration; MCP is provider-agnostic. Any MCP client can call any MCP server without modification. (Source: [[sources/anthropic-mcp-launch-2024]])

- **Architecture is Host → Client → Server over JSON-RPC 2.0.** One host can run many clients in parallel, each connected to a different server. Servers expose three primitives: Tools (callable functions), Resources (data context), Prompts (templates). (Source: [[concepts/mcp-model-context-protocol]])

- **Transport evolved: Stdio → HTTP+SSE → Streamable HTTP.** Streamable HTTP (March 2025 spec) is the modern standard for remote servers. Most major vendor-hosted servers (Sentry, Linear, Figma, Supabase, Notion) now use HTTP transport with browser-based OAuth. (Source: [[sources/mcp-first-year-2025]])

- **The November 2025 spec is the biggest single update.** It adds async Tasks (call-now, fetch-later), CIMD-anchored OAuth (replacing Dynamic Client Registration), Machine-to-Machine OAuth for headless agents, Cross App Access for enterprise IdP control, and a composable extensions framework. (Source: [[sources/mcp-spec-2025-11-25]])

- **The ecosystem grew 407% in two months after the registry launched.** The MCP Registry launched in September 2025; by November 2025 it held ~2,000 server entries. As of April 2026, 500+ public servers exist. (Source: [[sources/mcp-first-year-2025]])

- **Security vulnerabilities are structural, not incidental.** Because the LLM reads tool descriptions and responses without provenance checking, adversaries can inject instructions via tool outputs (prompt injection), poisoned tool definitions (tool poisoning), or mutated post-install server definitions (rug pull attacks). The November 2025 spec partially mitigates these via CIMD identity and capability declarations. (Source: [[concepts/mcp-security]])

- **Both MCP and function calling have a place.** Function calling (vendor-specific) is simpler for lightweight single-app integrations. MCP is the right choice for shared infrastructure tools that multiple clients and agents need to access. Production architectures typically use both. (Source: multiple search results)

- **Governance is now multi-stakeholder.** MCP is owned by the AAIF (Anthropic + OpenAI + Block as co-founders; AWS, Google, Microsoft, Cloudflare, GitHub, Bloomberg as supporting members). This reduces vendor lock-in risk significantly. (Source: [[entities/agentic-ai-foundation-aaif]])

---

## Key Entities

- [[entities/agentic-ai-foundation-aaif]]: Linux Foundation body governing MCP; co-founded by Anthropic, OpenAI, Block.
- **David Soria Parra & Justin Spahr-Summers**: Anthropic engineers who created MCP.
- **Anthropic**: Original creator and primary steward until Dec 2025.
- **OpenAI**: Adopted MCP in March 2025; co-founder of AAIF.
- **MCP Registry**: Central discovery catalogue for MCP servers; launched Sep 2025.

---

## Key Concepts

- [[concepts/mcp-model-context-protocol]]: The full protocol — architecture, primitives, transports, timeline, ecosystem.
- [[concepts/mcp-security]]: Prompt injection, tool poisoning, rug pull, supply chain, over-privileged access.

---

## Contradictions

- **Function calling vs MCP**: Some sources position MCP as a replacement for function calling; authoritative sources clarify they are complementary. MCP standardises the *server* layer; function calling is the *model* layer mechanism by which the LLM decides to invoke a tool. They can and typically do coexist.

- **Async Tasks maturity**: The 2025-11-25 spec labels Tasks as "experimental". Some articles treat them as production-ready. Treat Tasks as medium confidence for production use until the spec removes the experimental label.

---

## Open Questions

- Will the async Tasks primitive stabilise into a non-experimental state in the 2026 specification?
- How will the OWASP MCP Top 10 evolve and what compliance requirements will it generate for enterprise MCP deployments?
- Can tool-definition pinning be standardised at the protocol level to close the rug pull attack surface permanently?
- How will competing MCP registries (community vs official) converge, or will ecosystem fragmentation emerge?
- What does the 2026-07-28 Release Candidate spec introduce? (A new RC was announced; content not yet researched.)

---

## Sources

- [[sources/anthropic-mcp-launch-2024]]: Anthropic, 25 Nov 2024 — original launch announcement.
- [[sources/mcp-spec-2025-11-25]]: WorkOS / MCP Blog, 25 Nov 2025 — November 2025 spec detailed breakdown.
- [[sources/mcp-first-year-2025]]: MCP Team, 25 Nov 2025 — first-year retrospective, ecosystem statistics.

---

## Research Metadata

| Field | Value |
|---|---|
| Rounds | 3 |
| Web searches | 5 |
| Sources fetched | 5 |
| Pages created | 7 |
| Date | 2026-06-23 |
