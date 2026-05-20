---
type: meta
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
| [[stock-prediction-neural-network\|Stock Prediction Neural Network — SOLID ML App with Tkinter GUI]] | project | machine-learning | [[concepts/neural-networks-linear-models\|Neural Networks & Linear Models]] |

---

*Drop a lab file into `raw/` and say "ingest [filename] as a lab session" to populate this folder.*
