---
type: resource
status: established
created: 2026-05-15
updated: 2026-05-15
name: microsoft-threat-modeling-tool
description: Microsoft Threat Modeling Tool — install, workflow (Build→Analyze→Report), DFD stencils, STRIDE generation, and threat status system
metadata:
  type: reference
---

# Microsoft Threat Modeling Tool

A free Windows desktop tool that automates **Data Flow Diagram (DFD) creation** and **STRIDE threat generation**. Download from `https://aka.ms/threatmodelingtool`. Requires .NET 4.7.1+.

---

## The Four-Step Workflow

### 1. Build a Model
- Open tool → **Create A Model**
- Select a template (default: Azure Threat Model Template — uses STRIDE)
- Draw a DFD using the stencil panel:

| Stencil | Shape | Example |
|---------|-------|---------|
| External entity | Square | Human User, Third-party API |
| Process | Circle | Web Server, Auth Service |
| Data store | Two parallel lines | Database, Config Store |
| Data flow | Labelled arrow | Commands, Responses, Results |

- Add **trust boundaries** (red dotted lines) wherever control or privilege changes — every data flow crossing a trust boundary is a candidate threat.

### 2. Analyze Threats
- Click the **analysis view** icon (file + magnifying glass) to open the Threat List
- The tool auto-generates threats per DFD element using STRIDE:

| Category | Violated Property |
|----------|------------------|
| Spoofing | Authentication |
| Tampering | Integrity |
| Repudiation | Non-repudiation |
| Information Disclosure | Confidentiality |
| Denial of Service | Availability |
| Elevation of Privilege | Authorisation |

- Click a threat row → the relevant DFD interaction is highlighted + **Threat Properties** panel opens showing: Title, Category, Description (with mitigation hints), Justification (editable), Priority.

### 3. Triage Each Threat
Set the **Status** dropdown on each threat:

| Status | Meaning |
|--------|---------|
| Not Started | Default — unreviewed |
| Needs Investigation | Flagged for follow-up |
| Mitigated | Countermeasure implemented |
| Not Applicable | Covered by existing controls |

Fill in the **Justification** field with notes, assigned owner, or design decisions.

### 4. Report & Share
- **Reports → Create Full Report → Save Report**
- Output: HTML report with the DFD diagram, per-threat summary (Category, Description, Justification, Possible Mitigations, SDL Phase), and a threat count summary table.

---

## Threat Status Summary Table (Report)

| Status | Count |
|--------|-------|
| Not Started | N |
| Not Applicable | N |
| Needs Investigation | N |
| Mitigation Implemented | N |
| Total | N |

---

## Related

- [[concepts/threat-modeling]] — full theory: DFDs, STRIDE, attack trees, 5-step process, mis-actor categories
- [[examples/ict2216-lab3-threat-modeling-tool]] — Lab 03 walkthrough using this tool for a project DFD
