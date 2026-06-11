---
type: example
title: "ICT2216 Lab 3 — Microsoft Threat Modeling Tool"
domain: secure-software-development
tags: [ICT2216, threat-modeling, STRIDE, DFD, microsoft-threat-modeling-tool]
updated: 2026-05-16
---

# ICT2216 Lab 3 — Microsoft Threat Modelling Tool

**Goal:** Use the Microsoft Threat Modelling Tool to draw a DFD for a project application, then analyse and document threats using STRIDE.

---

## Steps in Sequence

### Step 1 — Install
- Download and install from `https://aka.ms/threatmodelingtool`
- Requires: Windows, .NET 4.7.1+, internet connection (for template updates)

### Step 2 — Build a Model (DFD)
1. Open tool → **Create A Model**
2. Select template: **Azure Threat Model Template** (default — uses STRIDE)
3. Drag stencils onto the canvas to represent your system:
   - External entity (square) — e.g. Human User
   - Process (circle) — e.g. Web Server
   - Data store (two parallel lines) — e.g. Generic Data Store
4. Connect elements with labelled data flow arrows (e.g. Commands, Responses, Configuration, Results)
5. Draw **trust boundaries** (red dotted lines) wherever privilege or control changes

Sample minimal diagram from the lab:
```
[Human User] --Commands--> (Web Server) --Configuration--> [Generic Data Store]
             <-Responses--              <--Results----------
```

### Step 3 — Analyze Threats
1. Click the **analysis view** icon (file with magnifying glass)
2. The Threat List is auto-generated — each row = one STRIDE threat against a DFD interaction
3. Click a threat row to:
   - Highlight the involved stencils in the diagram
   - Open the **Threat Properties** panel (ID, Title, Category, Description, Justification, Priority)
4. For each threat:
   - Read the Description (includes a mitigation hint)
   - Fill in **Justification** with your team's notes / countermeasure decisions
   - Adjust **Priority** if needed
   - Set **Status**: `Not Started` → `Needs Investigation` → `Mitigated` or `Not Applicable`

### Step 4 — Reports & Sharing
1. **Reports → Create Full Report → Save Report**
2. Review the HTML report with your team
3. Confirm that every threat has a status and justification filled in

### Step 5 — Team Tasks (Deliverable)
1. Draw the DFD for **your project application** in the tool
2. Discuss and document how the design addresses each STRIDE category:
   - **S** — Spoofing: authentication mechanism?
   - **T** — Tampering: input validation, TLS?
   - **R** — Repudiation: audit logging?
   - **I** — Info Disclosure: access control, encryption?
   - **D** — Denial of Service: rate limiting, WAF?
   - **E** — Elevation of Privilege: least privilege, RBAC?

---

## Key Concepts Reinforced

- DFDs use four stencils: external entity / process / data store / data flow
- Trust boundaries demarcate attack surface — every crossing is a threat candidate
- STRIDE auto-generation is per-interaction, not per-element; same data flow can generate multiple threat categories
- Threat statuses (`Not Applicable`, `Needs Investigation`, `Mitigated`) are the primary triage mechanism
- The generated report is the shareable artifact for design review

---

## Related

- [[resources/microsoft-threat-modeling-tool]] — tool reference (install, full workflow, status system)
- [[concepts/threat-modeling]] — theory: trust boundaries, DFDs, STRIDE, attack trees, mis-actor model
- [[concepts/secure-software-requirements]] — upstream step: CIA+AAA requirements feed into threat modeling
- [[sources/ICT2216-secure-software-development]] — source course
