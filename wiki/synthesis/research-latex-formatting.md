---
type: synthesis
address: c-000111
title: "Research: LaTeX Formatting"
created: 2026-07-12
updated: 2026-07-12
tags: [research, latex, typesetting, academic-writing]
status: complete
related:
  - concepts/latex-formatting
  - resources/latex-essential-packages
  - sources/overleaf-learn-latex-30min
  - sources/emonts-latex-best-practices
sources:
  - "[[sources/overleaf-learn-latex-30min]]"
  - "[[sources/emonts-latex-best-practices]]"
---

# Research: LaTeX Formatting

## Overview

LaTeX is a document preparation system in which the author writes semantic mark-up and LaTeX compiles it into typeset output (PDF). It is the standard for academic and scientific writing because it handles complex mathematics, automatic numbering, cross-referencing, and bibliography management far better than word processors. Two research rounds (5 searches, 5 fetches) produced a comprehensive concept page and package catalogue.

---

## Key Findings

- **Document anatomy** — Every document has a preamble (class declaration, package loading, settings) and a body (`\begin{document}` … `\end{document}`). Forgetting either is the most common beginner error. (Source: [[sources/overleaf-learn-latex-30min]])
- **Math mode pitfalls** — `$$...$$` and `eqnarray` are legacy constructs that conflict with `amsmath` and should never be used in new documents. `align` is the correct multi-line environment. (Source: [[sources/emonts-latex-best-practices]])
- **Float ordering** — `\caption` must appear before `\label` inside figure and table environments; reversing the order breaks `\ref` resolution. (Source: [[sources/overleaf-learn-latex-30min]])
- **Bibliography** — BibLaTeX with `biber` backend is the modern standard, replacing legacy BibTeX + `natbib`. Compile order: `pdflatex → biber → pdflatex → pdflatex`.
- **Cross-referencing** — `\eqref` (from `amsmath`) wraps equation numbers in parentheses automatically; `\cref` (from `cleveref`) inserts the correct object label name ("Figure", "Table", "Eq.") automatically. Package load order: `hyperref` then `cleveref` (always last).
- **Typography** — `booktabs` rules (`\toprule`/`\midrule`/`\bottomrule`) produce significantly better table output than `\hline`; `microtype` improves justification with no configuration; `siunitx` is mandatory for correctly spaced units.
- **Source formatting** — One sentence per source line enables proper version-control diffs; `~` (non-breaking space) before `\ref` and `\cite` prevents awkward line breaks.

---

## Key Entities

- **Overleaf** — Cloud LaTeX editor and primary learning platform; hosts the definitive beginner tutorial
- **CTAN** (Comprehensive TeX Archive Network) — Central repository for all LaTeX packages; https://ctan.org
- **Donald Knuth** — Creator of TeX (the underlying engine); TeX is the foundation on which LaTeX is built
- **Patrick Emonts** — Physics researcher and author of the LaTeX Best Practices blog post

---

## Key Concepts

- [[concepts/latex-formatting]] — Core reference: document structure, math, tables, figures, bibliography, custom commands, page layout, anti-patterns
- [[resources/latex-essential-packages]] — Curated package catalogue: maths, graphics, tables, layout, referencing, bibliography, utilities

---

## Contradictions

None found between sources. Minor difference in framing: Overleaf's tutorial permits `$...$` for inline math (widely used); Emonts recommends `\(...\)` for stricter LaTeX convention. Both are functionally identical. Consensus is that `$...$` is acceptable inline; `$$...$$` for display is the problematic form.

---

## Open Questions

- Which LaTeX compiler is best? `pdflatex` is simplest; `LuaLaTeX` or `XeLaTeX` are required for custom fonts (OpenType); research into compiler differences would be worth a separate page
- What is the state of LaTeX-to-HTML/CSS converters (e.g. `lwarp`, `LaTeXML`, `Pandoc`)? Relevant for web publishing of academic content
- How does `tabularray` compare to `tabularx` + `booktabs` for complex table layouts? It is a newer unified table package worth investigating

---

## Sources

- [[sources/overleaf-learn-latex-30min]]: Overleaf Team, 2024 — primary tutorial
- [[sources/emonts-latex-best-practices]]: Patrick Emonts, 2023 — practitioner best practices
- Overleaf mathematical expressions guide: https://www.overleaf.com/learn/latex/Mathematical_expressions
- Overleaf bibliography management: https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX
- Fan Pu Zeng LaTeX tips: https://fanpu.io/blog/2023/latex-tips/
