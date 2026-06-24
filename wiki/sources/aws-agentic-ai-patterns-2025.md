---
type: source
title: "Agentic AI Patterns and Workflows on AWS — AWS Prescriptive Guidance"
source_type: reference
author: Aaron Sempf and Andrew Hooker, Amazon Web Services
date_published: 2025-07-01
url: "https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html"
confidence: high
ingested: 2026-06-23
tags:
  - ai-engineering
  - agents
  - workflows
  - cloud
  - aws
key_claims:
  - Defines three guide layers: agent patterns, LLM workflows, and agentic workflow patterns
  - Agent patterns cover reasoning agents, retrieval-augmented agents, coding agents, voice interfaces, orchestrators, collaborative multi-agent systems
  - Workflow patterns cover task orchestration, sub-agent delegation, event-based coordination, observability, and control
  - Maps each pattern to AWS services for production cloud deployment
related:
  - "[[concepts/ai-workflows]]"
  - "[[concepts/ai-workflow-orchestration]]"
  - "[[synthesis/research-ai-workflows]]"
---

# Agentic AI Patterns and Workflows on AWS — AWS Prescriptive Guidance

## Summary

AWS Prescriptive Guidance document (July 2025) providing a design framework and implementation approach for production-grade AI agent systems. Connects event-driven architectural patterns with agentic alternatives and maps each pattern to AWS services.

## Three-Layer Framework

1. **Agent patterns**: Reusable design templates for individual agents — reasoning agents, RAG agents, coding agents, voice interfaces, workflow orchestrators, multi-agent collaboration. Each pattern describes how agents perceive, reason, act, and learn.

2. **LLM workflows**: How agents use LLMs for reasoning. Prompting strategies, planning mechanisms, and how LLMs drive structured, interpretable, reliable behaviours within an agent loop.

3. **Agentic workflow patterns**: How multiple agents, tools, and environments interact. Task orchestration, sub-agent delegation, event-based coordination, observability, and control. Promotes scalable, composable, and auditable AI architectures.

## Target Audience

Architects, developers, and product leaders building intelligent applications that go beyond static or deterministic automation.

## Confidence Notes

High confidence — authoritative cloud architecture reference from AWS. Reflects production patterns validated across large-scale enterprise deployments.
