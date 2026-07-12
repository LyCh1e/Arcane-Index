---
type: source
address: c-000110
title: "Patrick Emonts — LaTeX Best Practices"
source_type: blog-post
author: Patrick Emonts
date_published: 2023-01-01
url: https://patrickemonts.com/post/latex_best_practice/
confidence: high
domain: academic-writing
created: 2026-07-12
updated: 2026-07-12
tags: [source, latex, typesetting, best-practices, academic-writing]
related:
  - concepts/latex-formatting
  - resources/latex-essential-packages
---

# Patrick Emonts — LaTeX Best Practices

**URL:** https://patrickemonts.com/post/latex_best_practice/  
**Author:** Patrick Emonts (physics researcher)  
**Type:** Technical blog post  
**Confidence:** High — specific, actionable advice consistent with TeX Stack Exchange community consensus

---

## What This Source Contributes

A practitioner's list of LaTeX best practices and anti-patterns focused on mathematical and scientific writing. Complements the Overleaf tutorial by addressing style decisions that beginners typically get wrong after learning the basics.

---

## Key Claims

- One sentence per source line enables line-by-line diffs (`meld`, `vimdiff`) to work correctly; LaTeX ignores single returns
- `eqnarray` is deprecated with "problematic typesetting"; always use `align`
- `\eqref` is the correct command for equation references (auto-parentheses); `\ref` is for tables and figures
- Label prefixes (`eq:`, `sec:`, `fig:`, `tab:`) are a consistency convention that makes source readable; `cleveref` enforces them
- `\varepsilon` is conventional in analysis, not `\epsilon`
- `\coloneqq` (from `mathtools`) is the correct definition symbol, not `:=`
- `siunitx` package is the correct way to typeset units; not inline math
- The `physics` package provides semantic quantum mechanics notation (`\ket`, `\bra`, `\mqty`)
- Auto-sizing delimiters via `\DeclarePairedDelimiter` (from `mathtools`) are safer than manual `\bigl`/`\bigr` sizing

---

## Notable Quotes

> "The amount of attention and care you put into the presentation is indicative of the amount of thought you put into the content."

---

## Concepts Linked

- [[concepts/latex-formatting]] — anti-patterns and best practices sections
- [[resources/latex-essential-packages]] — `physics`, `siunitx`, `mathtools`, `cleveref` entries

---

## Key Takeaways

1. One sentence per source line — enables better version control diffs
2. Never use `eqnarray`; use `align`
3. Use `\eqref` for equation references, not plain `\ref`
4. Prefix all labels: `eq:`, `fig:`, `tab:`, `sec:`
5. Define semantic macros for repeated notation to prevent typos
6. Use `siunitx` for all units — never write units in raw math mode
