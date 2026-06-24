---
type: example
status: established
title: "ICT2216 Lab 4 — OWASP Threat Dragon"
domain: secure-software-development
course: ICT2216
tags: [ict2216, owasp, threat-dragon, threat-modeling, dfd, stride, lab]
created: 2026-05-30
updated: 2026-05-30
---

# ICT2216 Lab 4 — OWASP Threat Dragon

**Lab file:** `Lab4/Lab04 - OWASP Threat Dragon-2025.pdf`

## Outcomes

- Draw a threat model diagram using OWASP Threat Dragon
- Determine and rank threats per DFD element
- Enter mitigations and countermeasures
- Apply the threat model diagram to the team project

## Section 1: Installation

Two variants available:

| Variant | Steps |
|---------|-------|
| **Desktop** | Download installer from github.com/OWASP/threat-dragon/releases; run installer |
| **Web (self-hosted)** | Clone github.com/owasp/threat-dragon; follow README |
| **Docker** | `docker pull appsecco/owasp-threat-dragon` |

## Section 2: Create a Model

### Load the Demo Model First

On the Threat Dragon welcome page, click the **download (↓) icon** to load the bundled sample threat model. This shows a real worked example with data flows, trust boundaries, and pre-generated threats — a useful reference before building your own.

### Create a New Model

1. Click **New Model** on the welcome screen
2. Give it a title and description
3. Click **Add a new diagram** → name it (e.g. "Main Request Data Flow")
4. The diagram editor opens with the stencil panel on the left

## Section 3: Generate Threats

### Step 1 — Add Processes, Stores, and Actors

From the **stencil panel** (left side):

| Click this | To add |
|------------|--------|
| Process (circle) | An application component, server, function |
| Store (rectangle) | A database, config file, cache |
| Actor (rectangle with label) | A human user or external system |

- Click to add → element appears on canvas
- Drag to reposition
- Click element to open **Properties** and **Threats** panels at the bottom
- Delete: select element → click the **red ✕** icon at top-left of the element

### Step 2 — Add Data Flows and Trust Boundaries

**Data flows** represent data moving between elements:

**Method A (drag):**
- Click Data Flow in stencil → appears on canvas
- Drag each end to snap onto source and destination elements

**Method B (link tool — faster):**
1. Click source element to select it
2. Click the **grey link icon** (top-right of element, next to red ✕) → turns **green**
3. Click the destination element → data flow auto-created between them

**Editing flows:**
- Click anywhere on the flow line to add a routing vertex
- Hover near a flow → red remove tool appears → click to delete

**Trust boundaries:**
- Add from stencil panel; drag corners to resize
- Represents a privilege or control zone change
- Every data flow crossing a trust boundary generates STRIDE threats automatically

### Step 3 — Mark Out-of-Scope Elements

Elements needed for diagram context but not being threat-modelled:

1. Select the element
2. In Properties panel → check **Out of Scope**
3. Enter a **Reason** (shown to reviewers)

Effect:
- Element renders with **dashed border/line**
- Threat generation is **disabled** for that element

### Step 4 — Review and Triage Generated Threats

Select any in-scope element → the **Threats panel** (bottom) shows auto-generated STRIDE threats.

Elements with **unmitigated (open) threats are highlighted red** on the diagram — scan the canvas for red elements to find outstanding issues.

For each threat:
1. Read the generated title and description
2. Set status: **Open** / **Mitigated** / **Not Applicable**
3. Add mitigation notes explaining what control addresses the threat

Work through all red elements until none remain (or all are triaged as Not Applicable).

### Step 5 — Generate the Report

From the **Threat Model details view** (one level above the diagram editor):

1. Click **"Report"** (bottom-right of page)
2. Customise visibility:
   - Show/hide out-of-scope elements
   - Show/hide mitigated threats
   - Show/hide diagram images
3. Review the report: all diagrams + per-element threat list + mitigation notes

## Section 4: Supplementary — Passwordless Design

The lab includes reading links on passwordless authentication (relevant to [[concepts/secure-design-implementation]] — passwordless auth design):
- Microsoft Azure AD passwordless phone sign-in
- Apple AuthenticationServices (passkeys / Face ID)
- Google's password-free future

These tie to the course theme: authentication design decisions should use modern passwordless patterns where possible.

## Key Differences from Lab 3 (Microsoft TMT)

| Aspect | Lab 3 — Microsoft TMT | Lab 4 — OWASP Threat Dragon |
|--------|----------------------|------------------------------|
| Platform | Windows only | Cross-platform (web + desktop) |
| Out-of-scope | Not supported | Explicit dashed marking + reason |
| Open threat visibility | List-only | **Red highlighting on diagram** |
| Report | Fixed HTML | Customisable (toggle sections) |
| Threat status | Not Started / Mitigated / Not Applicable / Needs Investigation | Open / Mitigated / Not Applicable |
| Docker support | No | Yes |

## Gotchas

- **Grey link tool vs. red ✕**: They are side-by-side on the selected element. Grey (right) = link tool; Red (left) = delete. Don't confuse them.
- **Trust boundary crossing = threats**: A data flow that does NOT cross a trust boundary generates fewer auto-threats. Place trust boundaries deliberately to surface the right threats.
- **Out-of-scope ≠ delete**: Mark out-of-scope when you need the element for diagram readability but don't want threats generated. Delete only elements that don't belong at all.
- **Save frequently**: Desktop app saves to local JSON; web app may not auto-save.

## Related

- [[resources/owasp-threat-dragon]] — tool reference (stencil, UI, comparison table)
- [[concepts/threat-modeling]] — underlying theory: STRIDE, DFDs, trust boundaries, 5-step process
- [[examples/ict2216-lab3-threat-modeling-tool]] — Lab 3 using Microsoft TMT (compare workflow)
