---
type: learning
status: established
created: 2026-09-21
updated: 2026-09-21
name: learnix-srl-keyword-detection-pitfalls
description: Lesson — keyword-substring detection of LLM-tutor progress (Learnix SRL steps) inflates when it scans the bot's own replies, misfires on substrings, and goes silent on plain language; measured findings and the fix order.
metadata:
  type: feedback
---

# Learnix: pitfalls of keyword-based SRL step detection

**Project context**: Learnix (ICT2114 ITP), branch `feature/better-srl-detection`. Full write-up in the repo at `cy-documentation.md`.

## The non-obvious root cause

The tracker ran the same substring detector on the learner's messages **and the bot's replies** (`chat_panel.py:822`), while the system prompt told the bot to steer toward the next uncompleted step. That is a feedback loop: the bot asks about step N+1 using step N+1 vocabulary, which ticks N+1, so the bot moves on. One "hi" from the learner plus one plausible bot reply completed Self-Monitoring.

## Other measured problems

- Substring matching, no word boundaries: `roi` fires on *android*/*heroic*, `level 1` on *level 10/12*. Word-boundary regex fixes those but **not** generic words (`coaching`, `classroom`, `productivity`).
- Silent on plain language: the prompt forbids jargon, so learners mirror it. 7/9 genuine plain-language progress statements fired nothing; 27/45 (60%) of the project's own eval-set questions fired nothing.
- A definition question ("What is ROI?") and a negation ("we haven't done a questionnaire") count as evidence.
- The model already emits `<step_note>` tags for step transitions but the app only strips them for display. Wasted signal. Use JSON inside the existing tag so the strip regexes still work, and corroborate to avoid sycophancy.
- The web backend never updates `srl_steps`, so the LLM prompt says "Completed 0/12" forever there.

## Generalisable lessons

1. Never derive **learner** progress from **model** output without corroboration; if the model is also steered by that progress, the metric becomes self-fulfilling.
2. Build a small labelled gold set before tuning any lexicon; otherwise every keyword edit is a guess. Record the baseline (here: 60% silent).
3. Zero-shot embedding similarity (all-MiniLM-L6-v2, one description per step) got 6/9 top-1 but score ranges for on-topic (0.11–0.51) and off-topic (0.07–0.28) overlapped; use it as a recall booster only.
4. Keep one UI-free taxonomy module shared by desktop, backend and analytics instead of synchronised copies guarded by a test.

Related: [[learning/customtkinter-after-teardown]] (same project).

## Implemented (2026-09-21): R1-R3

Learner-only detection, whole-word matching with plurals and explicit `*` stems, and longest-match resolution now live in `src/srl/matcher.py` in the Learnix repo (uncommitted at time of writing).

**Lessons from doing it:**
- Switching substring to whole-word matching silently drops inflections the old code accepted by accident (`triggered`, `benchmarking`, `environmental scanning`). Diff the old and new detector over a real corpus (course chapters + eval questions) before trusting the change; that caught a missed stem.
- "Longest match wins" must suppress only matches **nested inside** a longer one, not any **overlap**. `formal learning solutions` holds two concepts that share a word; rejecting overlaps erased one of them.
- A keyword-redundancy list computed under substring semantics is wrong under whole-word semantics (`planned need` no longer sits inside `unplanned need`). Recompute it.
- A regression test is only worth keeping if it fails on the old code: verify by stashing the fix and rerunning.
