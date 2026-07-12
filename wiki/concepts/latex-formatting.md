---
type: concept
address: c-000107
title: "LaTeX Formatting"
domain: academic-writing
complexity: medium
created: 2026-07-12
updated: 2026-07-12
tags: [concept, latex, typesetting, academic-writing, math, bibliography, formatting, tex]
related:
  - resources/latex-essential-packages
  - synthesis/research-latex-formatting
---

# LaTeX Formatting

LaTeX is a document preparation system built atop Donald Knuth's TeX engine. The author marks up structure with semantic commands; LaTeX handles layout, numbering, cross-referencing, and bibliography management automatically. Central philosophy: separate *content* from *presentation*.

---

## Document Anatomy

Every LaTeX document has a **preamble** (setup) and a **body** (content):

```latex
\documentclass[12pt, a4paper]{article}  % class + options
\usepackage{amsmath}                     % preamble: load packages
\usepackage{graphicx}

\title{My Document}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle

Content goes here.

\end{document}
```

**Document classes:**

| Class | Use |
|---|---|
| `article` | Papers, short reports, journal submissions |
| `report` | Longer reports with chapters |
| `book` | Books (chapters, front/back matter) |
| `beamer` | Slide presentations |
| `IEEEtran` | IEEE conference/journal format |

---

## Text Formatting

| Effect | Command |
|---|---|
| **Bold** | `\textbf{text}` |
| *Italic* | `\textit{text}` |
| Underline | `\underline{text}` |
| Emphasis (context-aware) | `\emph{text}` |
| Small caps | `\textsc{text}` |
| Monospace/code | `\texttt{text}` |

**Quotation marks:** Use `` ``text'' `` (double backticks + double single-quotes), not `"text"`.

**Non-breaking space:** `~` prevents a line break between logically linked tokens:
```latex
Figure~\ref{fig:results}    Section~\ref{sec:method}    Ref.~\cite{key}
```

**Comments:** `%` makes the rest of the line invisible in output.

---

## Structure and Sectioning

```latex
\chapter{Chapter}          % report / book classes only
\section{Section}
\subsection{Subsection}
\subsubsection{Subsubsection}
\paragraph{Inline heading}
```

Append `*` to suppress auto-numbering: `\section*{Preface}`  
Manually add unnumbered sections to the TOC:
```latex
\addcontentsline{toc}{section}{Preface}
```

Generate table of contents: `\tableofcontents`

---

## Lists

```latex
\begin{itemize}            % bullet list
  \item First point
  \item Second point
\end{itemize}

\begin{enumerate}          % numbered list
  \item First
  \item Second
\end{enumerate}

\begin{description}        % definition list
  \item[Term] Definition text.
\end{description}
```

Lists nest by adding another environment inside an `\item`.

---

## Mathematics Typesetting

### Modes and Environments

| Mode | Syntax | Use |
|---|---|---|
| Inline | `\(...\)` or `$...$` | Formula within a sentence |
| Display, unnumbered | `\[...\]` | Standalone equation |
| Display, numbered | `\begin{equation}...\end{equation}` | Standalone, auto-numbered |
| Multi-line, aligned | `\begin{align}...\end{align}` | Multiple equations aligned at `&` |
| Multi-line, unnumbered | `\begin{align*}...\end{align*}` | Same, no numbers |

> **Avoid** `$$...$$` (old TeX — breaks `amsmath` spacing) and `eqnarray` (deprecated, poor spacing).

### Core Syntax

```latex
x^2 + y^2 = z^2              % superscript ^ / subscript _
\frac{a}{b}                   % fraction
\sqrt[n]{x}                   % nth root
\int_0^\infty f(x)\,dx        % integral (thin space \, before dx)
\sum_{i=1}^{n} x_i            % summation
\prod_{k=1}^{n} k             % product
\begin{pmatrix} a & b \\ c & d \end{pmatrix}  % matrix
```

### Alignment

```latex
\begin{align}
  f(x) &= x^2 + 2x + 1 \\
       &= (x + 1)^2 \label{eq:factored}
\end{align}
```

Place `&` **before** the alignment symbol. `\nonumber` suppresses a single line's number.  
Reference: `\eqref{eq:factored}` → "(2)" (parentheses included automatically).

### Symbol Best Practices

| Prefer | Avoid | Reason |
|---|---|---|
| `\varepsilon` | `\epsilon` | Conventional in analysis |
| `\mid` | `\|` | Correct spacing in `p(x \mid y)` |
| `\cdot` or `\times` | `*` | Proper multiplication symbol |
| `\langle`, `\rangle` | `<`, `>` | Correct mathematical brackets |
| `\dots` | `...` | Correct contextual spacing |
| `\sin`, `\log`, `\exp` | `sin`, `log` (plain text) | Upright (not italic) operators |

Define custom operators in the preamble:
```latex
\DeclareMathOperator*{\E}{\mathbb{E}}
\DeclareMathOperator*{\Var}{\mathrm{Var}}
\DeclarePairedDelimiter\abs{\lvert}{\rvert}   % auto-sizing: \abs*{x}
```

Add spacing around differentials: `\int f(x)\,dx` (thin space `\,`).

---

## Tables

```latex
\begin{table}[htbp]
  \centering
  \caption{Comparison of methods.}
  \label{tab:comparison}
  \begin{tabular}{lrr}
    \toprule
    Method    & Precision & Recall \\
    \midrule
    Baseline  & 0.72      & 0.68   \\
    Proposed  & 0.89      & 0.91   \\
    \bottomrule
  \end{tabular}
\end{table}
```

**Column specifiers:** `l` left, `c` centre, `r` right, `p{3cm}` fixed-width paragraph, `|` vertical rule.  
**Cell separator:** `&` | **Row end:** `\\` | **Horizontal rules:** `\toprule`, `\midrule`, `\bottomrule` (from `booktabs`).

> `\caption` must come **before** `\label`. Use `booktabs` rules (`\toprule` etc.) instead of `\hline` for professional output.

---

## Figures and Floats

```latex
\usepackage{graphicx}
\graphicspath{{images/}}           % image search directory

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.75\textwidth]{diagram.pdf}
  \caption{System architecture overview.}
  \label{fig:arch}
\end{figure}

See Figure~\ref{fig:arch}.
```

**Float placement specifiers:**

| Specifier | Meaning |
|---|---|
| `h` | Approximately here |
| `t` | Top of page |
| `b` | Bottom of page |
| `p` | Dedicated float page |
| `H` | Force here exactly (`float` package required) |

LaTeX may override `h` and `t` to optimise layout. `[htbp]` is the sensible default.

---

## Bibliography Management

### BibLaTeX (recommended for new documents)

```latex
\usepackage[backend=biber, style=authoryear, sorting=nyt]{biblatex}
\addbibresource{references.bib}
...
\printbibliography
```

Compile order: `pdflatex → biber → pdflatex → pdflatex`

### .bib Entry Format

```bibtex
@article{einstein1905,
    author  = {Albert Einstein},
    title   = {Zur Elektrodynamik bewegter Körper},
    journal = {Annalen der Physik},
    year    = {1905},
    volume  = {17},
    pages   = {891--921},
    doi     = {10.1002/andp.19053221004}
}
```

Common types: `@article`, `@book`, `@inproceedings`, `@thesis`, `@online`, `@misc`

### Citation Commands (BibLaTeX)

| Command | Output style |
|---|---|
| `\cite{key}` | Author, Year |
| `\parencite{key}` | (Author, Year) |
| `\textcite{key}` | Author (Year) — inline prose |

**BibTeX (legacy):** `\bibliographystyle{plain}` + `\bibliography{refs}`. Compile: `latex → bibtex → latex → latex`.

---

## Custom Commands

```latex
% Preamble
\newcommand{\reals}{\mathbb{R}}               % no arguments
\newcommand{\norm}[1]{\left\| #1 \right\|}    % one argument
\renewcommand{\vec}[1]{\boldsymbol{#1}}       % redefine existing
```

- `\newcommand` — errors if the name already exists
- `\renewcommand` — errors if the name does *not* exist
- `[n]` — declares *n* arguments (referenced as `#1`, `#2`, …)
- Wrap in `\ensuremath{}` for commands that must work in both text and math mode

---

## Cross-Referencing

Prefix-by-convention for clarity:

```latex
\label{sec:method}   \label{fig:arch}   \label{tab:results}   \label{eq:energy}
\ref{sec:method}     \ref{fig:arch}     \ref{tab:results}      \eqref{eq:energy}
```

`\eqref` (from `amsmath`) automatically wraps the number in parentheses — use it for equations.

**cleveref** (load after `hyperref`) inserts the object name automatically:

```latex
\cref{fig:arch}           % → "Figure 1"
\Cref{eq:energy}          % → "Equation 3" (capitalised, for sentence start)
\crefrange{eq:1}{eq:5}   % → "Eqs. (1)–(5)"
```

---

## Page Layout

```latex
\usepackage[a4paper, margin=2.5cm]{geometry}
% Fine-grained:
\usepackage[top=2.5cm, bottom=2.5cm, left=3cm, right=2.5cm]{geometry}
```

**hyperref** (must load late — after most packages, before `cleveref`):
```latex
\usepackage[colorlinks=true, linkcolor=blue, citecolor=green, urlcolor=cyan]{hyperref}
```
Makes all internal links, citations, and URLs clickable in the output PDF.

**Recommended load order:** `geometry` → `siunitx` → `hyperref` → `cleveref`

---

## Common Anti-Patterns

| Anti-pattern | Correct practice |
|---|---|
| `$$...$$` for display math | `\[...\]` or `equation` environment |
| `eqnarray` environment | `align` or `align*` |
| Hardcoded "Equation 3" | `\label` + `\eqref` |
| `"quoted text"` | `` ``quoted text'' `` |
| `...` ellipsis | `\dots` |
| `*` for multiplication | `\cdot` or `\times` |
| `<`, `>` for angle brackets | `\langle`, `\rangle` |
| `|` in conditional probability | `\mid` |
| `\\\\` to add vertical space | Blank line between paragraphs; `parskip` package |
| `\label` before `\caption` | `\caption` first, then `\label` |
| `\hline` in tables | `\toprule`/`\midrule`/`\bottomrule` from `booktabs` |

---

## See Also

- [[resources/latex-essential-packages]] — curated package catalogue with usage snippets
- [[synthesis/research-latex-formatting]] — research summary and open questions
