---
type: meta
status: established
title: "Examples Index"
updated: 2026-05-13
tags: [meta, index, examples]
---

# Examples Index

This folder contains two categories of grounded, applied content that sit alongside the abstract concept pages in `wiki/concepts/`:

| Category | Description |
|----------|-------------|
| **Real-world examples** | Concrete instances of concepts observed in industry, news, or practice (e.g. a software failure illustrating poor RE, a real app's MVVM implementation) |
| **Lab sessions** | Ingested practical exercises, code walkthroughs, and worksheet solutions from university lab work |

## How to Use This Folder

- Each page links back to its parent concept page (e.g. an HCI lab links to [[concepts/needfinding-and-task-analysis]]).
- Pages are tagged with both `example` or `lab` and the relevant course code (e.g. `inf2002`, `inf1008`).
- When ingesting a lab session, use the naming convention: `[COURSE]-lab-[week]-[topic].md` (e.g. `inf1008-lab-03-sorting.md`).
- When adding a real-world example, use: `example-[topic]-[short-descriptor].md` (e.g. `example-hci-hawaii-missile-alert.md`).

## Pages

| Page | Type | Course / Domain | Concept |
|------|------|-----------------|---------|
| [[ict2216-lab1-docker-compose\|ICT2216 Lab 1 — Multi-Container Docker Compose Stack]] | lab | ICT2216 | [[concepts/docker-compose\|Docker Compose]] |
| [[ict2216-lab2-securityrat\|ICT2216 Lab 2 — SecurityRAT: Defining Secure Software Requirements]] | lab | ICT2216 | [[concepts/secure-software-requirements\|Secure Software Requirements]] |
| [[ict2216-lab3-threat-modeling-tool\|ICT2216 Lab 3 — Microsoft Threat Modeling Tool]] | lab | ICT2216 | [[concepts/threat-modeling\|Threat Modeling]] |
| [[ict2216-lab4-owasp-threat-dragon\|ICT2216 Lab 4 — OWASP Threat Dragon]] | lab | ICT2216 | [[concepts/threat-modeling\|Threat Modeling]] |
| [[ict2216-lab5-github-actions\|ICT2216 Lab 5 — Web Proxy and GitHub Actions with Docker]] | lab | ICT2216 | [[concepts/nginx-reverse-proxy-and-tls\|Nginx TLS]], [[concepts/github-actions-cicd\|GitHub Actions]] |
| [[ict2216-project-phase4-auth\|ICT2216 Project — Phase 4 Authentication & Docker Stack]] | project | ICT2216 | [[concepts/secure-design-implementation\|Secure Design]] |
| [[ict2216-project-deployment-phases-9-12\|ICT2216 Project — Deployment Phases 9–12 (EC2)]] | project | ICT2216 | [[concepts/docker-compose\|Docker Compose]] |
| [[ict3112-lab1-nunit-tdd-calculator\|ICT3112 SVV Lab 1 — NUnit + TDD Calculator]] | lab | ICT3112 | [[concepts/test-driven-development\|Test-Driven Development]] |
| [[stock-prediction-neural-network\|Stock Prediction Neural Network — SOLID ML App with Tkinter GUI]] | project | machine-learning | [[concepts/neural-networks-linear-models\|Neural Networks & Linear Models]] |
| [[ict2216-project-vite-refactor\|ICT2216 Project — UMD Prototype to Vite + React SPA Refactor]] | project | ICT2216 / web-development | [[resources/vite\|Vite]], [[concepts/javascript-fundamentals\|JavaScript]] |

---

*Drop a lab file into `raw/` and say "ingest [filename] as a lab session" to populate this folder.*
