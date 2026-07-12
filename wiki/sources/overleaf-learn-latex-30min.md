---
type: source
address: c-000109
title: "Overleaf — Learn LaTeX in 30 Minutes"
source_type: web-article
author: Overleaf Team
date_published: 2024-01-01
url: https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes
confidence: high
domain: academic-writing
created: 2026-07-12
updated: 2026-07-12
tags: [source, latex, typesetting, overleaf, tutorial]
related:
  - concepts/latex-formatting
  - resources/latex-essential-packages
---

# Overleaf — Learn LaTeX in 30 Minutes

**URL:** https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes  
**Author:** Overleaf Team  
**Type:** Official tutorial  
**Confidence:** High — Overleaf is the leading LaTeX platform; content is peer-reviewed by the TeX community

---

## What This Source Contributes

The authoritative beginner-to-intermediate LaTeX tutorial maintained by Overleaf. Covers the full document lifecycle from a minimal working example through to tables, figures, maths, and bibliography. Used as the primary reference for the vault's [[concepts/latex-formatting]] page.

---

## Key Claims

- A LaTeX document must have `\begin{document}` and `\end{document}`; content in between constitutes the body; everything before is the preamble
- Document class (`\documentclass{article}`) controls default layout and available commands
- `\maketitle` renders `\title`, `\author`, and `\date` metadata in the body
- The `equation*` environment (unnumbered equation) requires `amsmath`
- Inline math uses `$...$` or `\(...\)`; display math uses `\[...\]` or `equation`
- `\caption` then `\label` is the required order in float environments
- `\ref{label}` cross-references; use with `~` to prevent line-break before number

---

## Concepts Linked

- [[concepts/latex-formatting]] — primary concept page built from this source

---

## Key Takeaways

1. Separate preamble from body; load all packages in the preamble
2. Use `\maketitle` for automatic title rendering
3. Always label floats after their caption
4. `amsmath` extends the math environment significantly — load it by default
5. Find packages via CTAN (https://ctan.org); Overleaf bundles TeX Live
