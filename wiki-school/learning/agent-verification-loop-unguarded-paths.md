---
type: learning
title: "Agent verification loop: unguarded paths and unchecked report claims"
updated: 2026-11-26
tags: [learning, ict3112, frama-c, llm-agents]
---

# Unguarded paths in an annotate-verify-repair loop

Found while checking the ICT3112 A2 report against the final programs, state files and logs.

- Code integrity checked only for the Annotator: repairs labelled `fix_annotation` or `fix_contract` changed executable code.
- All annotation attempts failing did not stop the run: review showed no contracts, `approved_contracts` stayed empty, and later contracts were never approved.
- Contract guard iterates only over old contracts, so new contracts pass under any decision.
- Re-annotation after a mid-loop parse error has no contract guard.
- Unannotated programs still give RTE goals, so a "first annotation proved N%" figure can describe no annotation at all.

**How to check:** strip comments and diff final code against the input per function; compare `approved_contracts` with the final contracts; count unproved goals per function before attributing a single cause. Claude Code transcripts under `~/.claude/projects/*Temp-tmp*` keep token usage per agent call.
- Console goal names (`ensures`, `loop_invariant`) never match CSV property kinds (`postcondition`, `loop invariant`); matching a formula on kind alone attaches the wrong formula to most goals.
