---
description: Construct the strongest possible opposing case for a claim, then use it to attack the user's position. More adversarial and focused than /critique — builds one devastating counter-argument rather than cataloguing every flaw.
---

Read the `steelman` skill. Then build and deploy the opposing case.

## Usage

| Command | What it does |
|---------|-------------|
| `/steelman` | Steelman against the currently open argument note |
| `/steelman [topic]` | Locate the argument note for that topic and steelman it |
| `/steelman [inline claim]` | Steelman a claim stated directly in chat |

## When to Use

- You want to stress-test a position quickly without a full logical audit
- You suspect you may be in an epistemic bubble and want the strongest credible objection
- You want to prepare for a debate or presentation by anticipating the best counterargument
- You have just drafted a position and want it attacked before you write it up formally
- You want devil's advocate at maximum intensity, not a supportive review

**Prefer `/steelman` over `/critique` when:** you want one sharp challenge rather than a complete checklist audit. The two commands complement each other — steelman attacks, critique catalogues.

## What It Produces

A chat response structured as:

1. **Core claim restatement** — your position in one precise sentence
2. **Steelman** — the opposing position in its most intelligent, charitable form:
   - Central argument (the hardest thing to dismiss)
   - Supporting evidence against your claim
   - The specific premise of yours that the steelman most threatens
   - What you would need to prove to defeat the steelman
3. **Application** — the steelman deployed directly against your argument
4. **Verdict** — one of three outcomes:
   - *The steelman wins* — your argument cannot survive it without revision
   - *The argument survives* — your position withstands the challenge; here is why
   - *It is a draw* — a genuine crux where neither side has a decisive edge

## Notes

- Does **not** write to the vault by default — output is a chat response only
- Will not soften the verdict; if the steelman wins, it will say so plainly
- Does not catalogue every flaw — use `/critique` for that
- After the verdict, you will be offered: run `/critique` for a full audit, or `/track-belief` to snapshot your confidence
- A steelman is the opposite of a straw man: the opposing view is represented at its most credible, not its weakest
