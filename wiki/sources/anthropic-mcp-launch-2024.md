---
type: source
title: "Introducing the Model Context Protocol — Anthropic"
source_type: article
author: Anthropic
date_published: 2024-11-25
url: "https://www.anthropic.com/news/model-context-protocol"
confidence: high
ingested: 2026-06-23
tags:
  - mcp
  - ai-engineering
  - anthropic
  - protocol
key_claims:
  - MCP is an open standard for two-way connections between data sources and AI tools
  - Created by David Soria Parra and Justin Spahr-Summers
  - Launched 25 November 2024
  - Includes SDKs, Claude Desktop support, and a pre-built server repository
related:
  - "[[concepts/mcp-model-context-protocol]]"
  - "[[questions/research-mcp-servers]]"
---

# Introducing the Model Context Protocol — Anthropic

## Summary

The official Anthropic announcement of the Model Context Protocol. Published on the same day as the initial release: 25 November 2024.

## What the Source Says

MCP is described as "an open standard that enables developers to build secure, two-way connections between their data sources and AI-powered tools." It was created to solve the information silo problem: AI models were isolated from live data and external systems, requiring custom one-off integrations for each pairing.

The launch shipped three components:
1. The protocol specification and SDKs
2. Local MCP server support in Claude Desktop
3. An open-source repository of pre-built servers (Google Drive, Slack, GitHub, Postgres, and others)

**Creators**: David Soria Parra and Justin Spahr-Summers at Anthropic.

**Early adopters**: Block and Apollo integrated MCP; Zed, Replit, and Sourcegraph adopted it for AI coding assistants. Claude 3.5 Sonnet was highlighted as capable of rapidly building MCP server implementations.

## Contribution to the Topic

This is the primary source for MCP's origin, stated purpose, and initial feature set. All subsequent protocol evolution builds on this foundation.

## Confidence Notes

High confidence — primary source from the creating organisation, official announcement with no attribution chain required.
