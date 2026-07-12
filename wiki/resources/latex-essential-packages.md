---
type: resource
address: c-000108
title: "LaTeX Essential Packages"
domain: academic-writing
created: 2026-07-12
updated: 2026-07-12
tags: [resource, latex, packages, typesetting, ctan, overleaf]
related:
  - concepts/latex-formatting
  - synthesis/research-latex-formatting
---

# LaTeX Essential Packages

Curated catalogue of packages used in almost every serious LaTeX document. All are available on CTAN and included in TeX Live / MiKTeX distributions.

---

## Mathematics

| Package | Purpose | Key Commands |
|---|---|---|
| **amsmath** | Multi-line equations, operators, spacing | `align`, `equation*`, `\DeclareMathOperator`, `\eqref` |
| **amssymb** | Extended math symbol set | `\mathbb`, `\mathfrak`, `\lesssim` |
| **mathtools** | Extension of `amsmath` | `\DeclarePairedDelimiter`, `\coloneqq`, aligned matrices |
| **physics** | Quantum notation, derivatives | `\ket`, `\bra`, `\dv`, `\pdv`, `\mqty` |
| **siunitx** | Numbers and SI units | `\SI{9.81}{\metre\per\second\squared}`, `\num{1.2e6}` |

```latex
\usepackage{amsmath, amssymb, mathtools}
\usepackage{siunitx}
% Usage:
\SI{3.14}{\kilo\gram\metre\per\second}
\num{1234567.89}   % → 1 234 567.89 (locale-aware)
```

---

## Graphics and Figures

| Package | Purpose | Key Commands |
|---|---|---|
| **graphicx** | Include raster and vector images | `\includegraphics[width=\textwidth]{file}` |
| **float** | Force float placement | `[H]` placement specifier |
| **subcaption** | Sub-figures with individual captions | `subfigure` environment |
| **tikz** | Programmable vector graphics | `\begin{tikzpicture}` |
| **pgfplots** | Function and data plots | `\begin{axis}`, `\addplot` |

```latex
\usepackage{graphicx}
\graphicspath{{figures/}}
\includegraphics[width=0.6\textwidth, trim=10 10 10 10, clip]{diagram.pdf}
```

---

## Tables

| Package | Purpose | Key Commands |
|---|---|---|
| **booktabs** | Professional horizontal rules | `\toprule`, `\midrule`, `\bottomrule` |
| **tabularx** | Auto-width `X` columns | `tabularx` environment |
| **multirow** | Cells spanning multiple rows | `\multirow{n}{width}{text}` |
| **longtable** | Tables spanning multiple pages | `longtable` environment |
| **array** | Extended column specifiers | `>{cmd}c`, `m{width}` |

```latex
\usepackage{booktabs}
\begin{tabular}{lrr}
  \toprule
  Method & F1 & AUC \\
  \midrule
  Baseline & 0.71 & 0.82 \\
  \bottomrule
\end{tabular}
```

---

## Layout and Typography

| Package | Purpose | Key Commands / Options |
|---|---|---|
| **geometry** | Page size and margins | `\usepackage[a4paper, margin=2cm]{geometry}` |
| **fontenc** | Output font encoding | `\usepackage[T1]{fontenc}` |
| **inputenc** | Input encoding (pdflatex only) | `\usepackage[utf8]{inputenc}` |
| **microtype** | Micro-typographic improvements | Load after font packages; no commands needed |
| **parskip** | Paragraph spacing (no indent) | `\usepackage{parskip}` |
| **setspace** | Line spacing | `\doublespacing`, `\onehalfspacing` |
| **fancyhdr** | Custom headers and footers | `\pagestyle{fancy}`, `\lhead{}`, `\rhead{}` |

```latex
\usepackage[a4paper, top=2.5cm, bottom=2.5cm, left=3cm, right=2.5cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{microtype}   % improves justification automatically
```

---

## Cross-Referencing and Links

| Package | Purpose | Key Commands |
|---|---|---|
| **hyperref** | Clickable links and PDF metadata | `\href{url}{text}`, `\url{url}` |
| **cleveref** | Auto-inserts label type | `\cref{key}`, `\Cref{key}`, `\crefrange{a}{b}` |
| **varioref** | Page-aware references | `\vref{key}` → "Figure 1 on page 4" |

**Load order is mandatory:**
```latex
\usepackage{varioref}    % 1st
\usepackage{hyperref}    % 2nd
\usepackage{cleveref}    % 3rd (always last)
```

```latex
\usepackage[colorlinks=true, linkcolor=blue, citecolor=teal, urlcolor=cyan]{hyperref}
\usepackage[capitalise, noabbrev]{cleveref}
```

---

## Bibliography

| Package | Purpose | Backend |
|---|---|---|
| **biblatex** | Modern bibliography management | `biber` (recommended) or `bibtex` |
| **natbib** | Author-year and numeric styles | works with BibTeX |

```latex
% BibLaTeX (recommended)
\usepackage[backend=biber, style=authoryear-comp, sorting=nyt]{biblatex}
\addbibresource{references.bib}
% ...
\printbibliography[heading=bibintoc]
```

**Common biblatex styles:**

| Style | Output format |
|---|---|
| `authoryear` | Smith (2024) |
| `numeric` | [1] |
| `alphabetic` | [Smi24] |
| `ieee` | IEEE-style |
| `apa` | APA 7th edition |

---

## Utilities

| Package | Purpose | Key Commands |
|---|---|---|
| **xcolor** | Colour support | `\textcolor{red}{text}`, `\colorbox` |
| **listings** | Source code typesetting | `lstlisting` environment |
| **minted** | Syntax-highlighted code (requires Python `Pygments`) | `minted` environment |
| **algorithm2e** | Algorithm pseudocode | `algorithm` environment |
| **todonotes** | Inline review annotations | `\todo{Fix this}` |
| **csquotes** | Context-aware quotation marks | `\enquote{text}` |
| **glossaries** | Glossary and acronym management | `\gls{key}`, `\Gls{key}` |

---

## Recommended Minimal Preamble

```latex
\documentclass[12pt, a4paper]{article}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}          % pdflatex only; omit for LuaLaTeX/XeLaTeX
\usepackage{microtype}

\usepackage[a4paper, margin=2.5cm]{geometry}
\usepackage{graphicx}
\usepackage{amsmath, amssymb, mathtools}
\usepackage{booktabs}
\usepackage{siunitx}
\usepackage{csquotes}                % required by biblatex
\usepackage[backend=biber, style=authoryear]{biblatex}
\addbibresource{references.bib}

\usepackage{hyperref}
\usepackage{cleveref}
```

---

## Tools and Editors

| Tool | Type | Notes |
|---|---|---|
| **Overleaf** | Cloud editor | Collaborative; no local install; auto-compiles |
| **TeX Live** | Local distribution (Linux/Mac/Windows) | Full; updated annually |
| **MiKTeX** | Local distribution (Windows) | On-demand package download |
| **TeXShop** | macOS editor | Tightly integrated with TeX Live |
| **VS Code + LaTeX Workshop** | Editor + extension | Live preview, auto-complete, linting |
| **CTAN** | Package archive | https://ctan.org — documentation for every package |

---

## See Also

- [[concepts/latex-formatting]] — comprehensive command reference and anti-patterns
- [[synthesis/research-latex-formatting]] — research summary
