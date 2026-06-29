---
description: Run a structured epistemic affirmation on an argument — identifies sound premises, valid reasoning patterns, strong evidence, clear thinking markers, and builds the strongest possible case for the position. Appends a dated affirmation section to the argument note.
---

Read the `affirm` skill. Then run the affirmation workflow for the target argument.

## Usage

| Command | What it does |
|---------|-------------|
| `/affirm` | Affirm the currently open argument note |
| `/affirm [topic]` | Locate the argument note for that topic and affirm it |
| `/affirm [inline text]` | Affirm pasted argument text in chat — no vault write |

## When to Use

- You have just run `/critique` and want to identify what to **preserve** before rebuilding the argument
- You have a position you are confident in and want to know what its **genuine epistemic strengths** actually are, not just that it feels right
- You are about to commit to a position and want to confirm the **strongest premises and evidence** are load-bearing before doing so
- You have survived a `/steelman` challenge and want to catalogue *why* the argument held up
- You want to distinguish **warranted confidence** from motivated reasoning — affirm tells you whether confidence is earned

## What It Produces

An `## Affirmation — YYYY-MM-DD` section appended to the argument note, covering:

1. **Claim restatement** — flags if the claim is well-scoped, falsifiable, and precise
2. **Premise strength** — rates each premise on credibility, evidence, independence, and load-bearing weight; identifies the strongest premise
3. **Reasoning chain soundness** — identifies the strongest logical link and names the valid reasoning form used
4. **Sound reasoning patterns** — checks 10 named valid patterns (modus ponens, convergent evidence, inference to best explanation, etc.)
5. **Evidence strengths** — identifies the best evidence cited and assesses its quality and convergence
6. **Clear thinking markers** — checks 7 bias-resistance signals (disconfirming evidence cited, rival hypotheses considered, calibrated confidence, etc.)
7. **Counterargument engagement** — notes where the strongest objections are genuinely addressed and appropriate concessions are made
8. **Epistemic grounding** — assesses whether the claim has been previously tested and survived challenge
9. **Steelman of the position** — the strongest possible case *for* the claim, potentially stronger than the argument as written
10. **Coherence with prior positions** — cross-checks other notes in `wiki/arguments/` for convergent support
11. **Verdict** — primary strength, secondary strengths, recommended confidence revision upward

## Complement Map

| Skill | Use after `/affirm` when... |
|-------|---------------------------|
| `/critique` | You want the full flaw audit to balance the affirmation |
| `/steelman` | You want adversarial stress-testing after knowing what is strong |
| `/track-belief` | You want to snapshot your updated confidence level |

## Notes

- Affirming a vault note writes back to that note and updates `wiki/arguments/_index.md`
- Affirming inline text responds in chat only; you will be offered the option to save as a new argument note
- The skill credits only what can be specifically named and quoted — it does not generate generic encouragement
- `/affirm` and `/critique` are designed to be run together: critique finds the weakest link, affirm finds the strongest; run both to know what to discard and what to keep
- The steelman of the position produced here is the *pro* version; `/steelman` produces the *contra* version
