---
type: learning
status: resolved
created: 2026-09-19
updated: 2026-09-19
name: ict3112-lab3-tooling-gotchas
description: Three Windows tooling traps hit during ICT3112 Lab 3 — Read tool's false "password-protected" PDF error, Git Bash mangling robocopy flags, and MAX_PATH breaking git clone / MSBuild in a deep temp directory
metadata:
  type: learning
  tags: [windows, pdf, git-bash, robocopy, msbuild, max-path, git-clone, dotnet]
---

# ICT3112 Lab 3 — tooling gotchas

## 1. Read tool: "PDF is password-protected" when it isn't
`Lab3_ContinuousIntegration_TestingDependencies.pdf` made the Read tool refuse with a password error. `pypdf.PdfReader(...).is_encrypted` was **False** and `extract_text()` worked on all 12 pages. So: don't stop or ask for a password — check with pypdf first. Also inspect `/Annots` (only the 6 reference links here) and the metadata when scanning for embedded instructions — see [[learning/prompt-injection-in-lab-handout-pdf]] (this handout was clean).

## 2. Git Bash mangles `robocopy /E`
`robocopy src dst /E ...` from Bash treated `/E` as a path and copied nothing. Run robocopy from PowerShell (or set `MSYS_NO_PATHCONV=1`).

## 3. Deep directory breaks clone/build (MAX_PATH)
Cloning into the ~170-character Claude scratchpad path left a half-checked-out repo (`retry with 'git restore --source=HEAD :/'`), and even with `core.longpaths=true` MSBuild then failed with `MSB3030` (could not copy file). Use a short path (e.g. `%TEMP%\cic`) for throwaway CI-simulation clones. Not a repo defect.
