---
type: index
status: established
title: "Arguments Index"
created: 2026-06-26
updated: 2026-06-26
tags: [index, arguments, epistemics]
---

# Arguments

Tracked positions and beliefs. Each note records a claim, its premises, evidence, and counterarguments. Critique history is appended in-place so reasoning evolution is visible over time.

Use the `_templates/argument.md` Templater template to create new argument notes.

---

## Active Arguments

| Page | Topic | Claim (summary) | Confidence | Last Critique |
|------|-------|-----------------|-----------|---------------|
| *(none yet)* | | | | |

---

## Revised Arguments

*Arguments where the position changed after critique or new evidence.*

| Page | Original confidence | Current confidence | What changed |
|------|--------------------|--------------------|-------------|
| *(none yet)* | | | |

---

## Abandoned Arguments

*Positions that were found to be unsound or falsified.*

| Page | Reason abandoned |
|------|-----------------|
| *(none yet)* | |

---

## How to Use

1. **New belief**: open `_templates/argument.md` in Templater, fill in Claim → Premises → Evidence → Counterarguments → What Would Change My Mind
2. **Get critique**: run `/critique` with the note open — critique is appended in-place
3. **Steelman**: run `/steelman` for an adversarial challenge (responds in chat)
4. **Snapshot**: run `/track-belief` to record a dated position snapshot in the note's Belief History table
5. **Review evolution**: check the Belief History table in any note to see how confidence and position changed over time
