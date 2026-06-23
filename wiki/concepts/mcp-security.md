---
type: concept
title: "MCP Security"
created: 2026-06-23
updated: 2026-06-23
tags:
  - ai-engineering
  - security
  - mcp
  - prompt-injection
  - agents
domain: ai-engineering
complexity: high
related:
  - "[[concepts/mcp-model-context-protocol]]"
  - "[[concepts/owasp-top-10]]"
  - "[[concepts/threat-modeling]]"
  - "[[synthesis/research-mcp-servers]]"
sources:
  - "[[sources/mcp-spec-2025-11-25]]"
---

# MCP Security

## Overview

MCP's design — where LLMs read tool descriptions and invoke them with ambient authority — introduces a class of vulnerabilities distinct from traditional web security. The attack surface is the model's context window itself. An adversary who can influence what the LLM reads can influence what it does.

Security researchers identified these vulnerability classes starting in April 2025. The OWASP MCP Top 10 project subsequently formalised them.

---

## Vulnerability Classes

### 1. Prompt Injection

**What it is**: An attacker embeds adversarial instructions inside content the LLM will read — a file, a database record, a tool response — and the model follows them as if they were from the user or developer.

**MCP-specific risk**: Because MCP tools return data directly into the model's context, any tool response from a compromised or malicious server is a potential injection vector. The model has no native provenance check on where instructions originate.

**Severity**: High. Ranked #1 in OWASP Top 10 for LLM Applications 2025.

---

### 2. Tool Poisoning

**What it is**: An attacker who controls an MCP server writes adversarial directives directly into tool *descriptions* (the metadata the LLM reads before deciding to call a tool). The model ingests these without sanitisation and may execute unauthorised actions.

**CVE reference**: CVE-2025-54136 covers a structural tool poisoning vulnerability.

**Key research**: The MCPTox benchmark (2025) showed that tool poisoning attacks pass seamlessly into AI agent contexts at an alarmingly high rate, resulting in data leakage or unauthorised execution.

---

### 3. Rug Pull Attacks

**What it is**: An MCP server exposes a safe-looking tool at installation time. After the user approves it, the server silently mutates the tool's definition — redirecting API key targets, exfiltrating data, or executing new commands.

**Why it is possible**: The MCP specification (pre-Nov 2025) did not require tool definitions to be immutable after negotiation. The Nov 2025 spec adds capability declarations and CIMD-anchored identity, which partially mitigate this.

**Confidence**: High — documented in multiple security analyses (2025).

---

### 4. Supply Chain Vulnerabilities

**What it is**: Malicious code injected into third-party MCP server packages or dependencies.

**CVE reference**: CVE-2025-6514 — a critical OS command injection in `mcp-remote` (an OAuth proxy with 437,000+ downloads) affecting integrations from Cloudflare, Hugging Face, and Auth0.

**Pattern**: Follows the same supply chain attack surface as npm/PyPI packages; MCP servers are code, and any dependency in that code is an attack vector.

---

### 5. Over-Privileged Access

**What it is**: An MCP server (or the agent using it) is granted broader access than necessary. When one agent carries the credentials of a database administrator, a single successful attack against that agent exposes the entire database.

**OWASP MCP Top 10**: Identifies over-privileged access as a foundational structural risk. The blast radius of any compromise scales directly with the access level granted.

---

### 6. Session Hijacking

**CVE reference**: CVE-2025-6515 — prompt hijacking via session manipulation in MCP ecosystems. An attacker intercepts or forges MCP session tokens to inject instructions.

---

## Mitigations

| Risk | Mitigation |
|---|---|
| Prompt injection | Treat all tool responses as untrusted data; never allow them to override system instructions. Use separate context layers. |
| Tool poisoning | Pin tool definitions at connection time; verify against a known-good registry hash. |
| Rug pull | Use CIMD-anchored OAuth (Nov 2025 spec) to tie server identity to DNS; re-verify tool schemas on reconnect. |
| Supply chain | Audit MCP server dependencies; prefer official or well-audited servers; scan with MCPGuard. |
| Over-privileged access | Apply the principle of least privilege; scope each agent's credentials to the minimum required. |
| Session hijacking | Use Streamable HTTP over TLS; validate session tokens server-side on every request. |

---

## The Nov 2025 Spec Response

The 2025-11-25 specification addressed several of these risks:
- **CIMD**: Anchors client identity in DNS/HTTPS, making server impersonation harder.
- **Client security requirements** (SEP-1024): Mandatory security behaviours for local MCP installations.
- **Default scopes** (SEP-835): Limits the OAuth permissions an MCP server can request by default.
- **Extensions gating**: Capability negotiation ensures servers cannot silently add capabilities.

> [!gap] The OWASP MCP Top 10 project was still evolving as of mid-2026. Check `owasp.org` for the latest finalised list.

---

## Open Questions

- Will MCPGuard (automatic vulnerability detection for MCP servers) become a standard part of CI/CD pipelines for agent developers?
- How will enterprise IdP controls via Cross App Access (XAA) affect the practical attack surface in large organisations?
- Can tool-definition pinning be standardised in the core spec to prevent rug pull attacks at the protocol level?
