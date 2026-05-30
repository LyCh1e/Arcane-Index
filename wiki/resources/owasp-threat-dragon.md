---
name: owasp-threat-dragon
description: OWASP Threat Dragon — free open-source threat modeling tool with DFD diagramming and STRIDE rule engine; web and desktop variants
metadata:
  type: reference
domain: secure-software-development
tags: [owasp, threat-dragon, threat-modeling, dfd, stride, tool]
created: 2026-05-30
---

# OWASP Threat Dragon

Free, open-source, cross-platform threat modeling application. Combines system DFD diagramming with a rule engine that auto-generates threats and mitigations per element. OWASP Incubator Project. Current version: **v2.3.0**.

## Two Variants

| Variant | Description | Where to get |
|---------|-------------|-------------|
| **Desktop** | Electron app, runs offline | github.com/OWASP/threat-dragon/releases |
| **Web app** | Self-hosted, runs in browser | github.com/owasp/threat-dragon (clone + run) |
| **Docker** | Web app containerised | `docker pull appsecco/owasp-threat-dragon` |

## UI Overview

The editor has three main zones:

```
┌─────────────┬────────────────────────────────┬────────────────┐
│  Stencil    │        Diagram Canvas          │  Properties /  │
│  Panel      │                                │  Threats Panel │
│  (left)     │                                │  (bottom)      │
└─────────────┴────────────────────────────────┴────────────────┘
```

## DFD Stencil Elements

| Element | Shape | Purpose |
|---------|-------|---------|
| **Process** | Circle (solid border) | Application component, service, function |
| **Store** | Rectangle | Database, config file, message queue |
| **Actor** | Rectangle | External entity — human user, third-party API |
| **Data Flow** | Labelled arrow | Data moving between elements |
| **Trust Boundary** | Dashed border / line | Privilege/control zone change |

## Creating Elements and Data Flows

**Adding elements:**
1. Click a shape in the stencil panel → it appears on the canvas
2. Drag to position; click to select and view Properties/Threats
3. Delete: select element → click red ✕ icon at top-left of element

**Adding data flows (two methods):**
- Drag from stencil panel → drag ends onto source and destination elements
- **Faster**: select source element → click the grey link tool (top-right, next to red ✕) → it turns green → click the destination element → data flow auto-created

**Editing data flows:**
- Click anywhere on a line to add a vertex (for routing)
- Delete: hover over flow → red remove tool appears → click

**Trust boundaries:**
- Add from stencil; resize/reposition by dragging corners
- Any data flow crossing a trust boundary is a candidate for auto-generated threats

## Out-of-Scope Elements

Any element (process, store, actor, data flow) can be marked **Out of Scope** in its Properties panel. Use this for context elements not being threat-modelled.

- Provide a **reason** in the Properties panel (for reviewers)
- Out-of-scope elements render with **dashed borders**
- Threat generation is **disabled** for these elements

## Threat Generation and Status

Threat Dragon's rule engine auto-generates threats per STRIDE for each in-scope element. Threats appear in the **Threats panel** (bottom) when an element is selected.

| Visual indicator | Meaning |
|-----------------|---------|
| Element highlighted **red** | Has at least one open (unmitigated) threat |
| Element normal colour | All threats mitigated or no threats |
| Element **dashed** | Out of scope |

For each generated threat you can:
- Add a **title** and **description**
- Set **status**: open / mitigated / not applicable
- Add **mitigation notes**

## Threat Model Report

From the Threat Model details view → click **"Report"** (bottom-right).

Report is customisable — toggle visibility of:
- Out-of-scope model elements
- Mitigated threats
- Threat model diagrams

Output includes: all diagrams, per-element threat list, mitigation notes.

## Comparison: Threat Dragon vs Microsoft TMT

| Feature | OWASP Threat Dragon | Microsoft TMT |
|---------|---------------------|---------------|
| Platform | Web + Desktop (cross-platform) | Windows only |
| Cost | Free, open-source | Free |
| DFD drawing | Yes | Yes |
| STRIDE auto-generation | Yes (rule engine) | Yes (template-based) |
| Trust boundaries | Yes | Yes |
| Out-of-scope marking | Yes (dashed, with reason) | No |
| Open threat highlighting | Red colour on element | Not visual on diagram |
| Report format | Customisable web report | Full HTML report |
| Docker support | Yes (appsecco image) | No |
| Integration | OWASP lifecycle tools | Azure DevOps |

## Related

- [[concepts/threat-modeling]] — full theory: STRIDE, DFDs, attack trees, trust boundaries, 5-step process
- [[resources/microsoft-threat-modeling-tool]] — Microsoft's alternative for Windows
- [[examples/ict2216-lab4-owasp-threat-dragon]] — Lab 4 walkthrough
