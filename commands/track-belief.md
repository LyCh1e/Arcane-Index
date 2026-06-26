---
description: Snapshot the current state of a belief or argument into its Belief History table. Creates a new argument note if none exists. Tracks how positions and confidence evolve across sessions over time.
---

Read the `track-belief` skill. Then run the appropriate mode for the user's intent.

## Usage

| Command | What it does |
|---------|-------------|
| `/track-belief [topic]` | Snapshot current confidence and position for that topic |
| `/track-belief` | Snapshot the currently open argument note |
| `I've changed my mind on [topic]` | Open revision mode — records a position change |
| `How has my thinking changed on [topic]?` | Review mode — displays the full belief history |
| `I'm abandoning [topic]` | Abandon mode — marks the position as retired |

## When to Use

- **After any `/critique` or `/steelman` run** — record how your confidence shifted in response to the challenge
- **When starting a new position** — create an argument note and log the initial confidence score
- **When you notice your views have changed** — capture the revision before the old framing fades
- **Periodically on important beliefs** — build a longitudinal record of how your thinking evolves
- **Before a major decision** — snapshot the beliefs underlying the decision so you can review them later

## The Four Modes

### Snapshot
Records the current date, confidence (1–10), and a one-sentence position summary in the Belief History table. Updates the `confidence:` and `updated:` frontmatter fields. Flags with ⚠ if confidence has shifted ±2 or more points since the last entry.

### Revision
Used when the core claim has changed, not just the confidence. Adds a `## Revised Claim (YYYY-MM-DD)` section below the original claim — the original is never overwritten. Moves the note to the Revised table in `wiki/arguments/_index.md`.

### Review
Displays all rows of the Belief History table with a trajectory summary: overall trend, biggest single shift, and current status. Useful for periodic epistemic housekeeping.

### Abandon
Marks a position as no longer held. Updates the note status, appends a final history row with the reason, and moves the entry to the Abandoned table in `_index.md`.

## What It Produces

- A new row appended to the `## Belief History` table in the argument note
- Updated `confidence:` and `updated:` frontmatter
- Updated `wiki/arguments/_index.md` (Active, Revised, or Abandoned table)
- A confirmation summary in chat:

```
Snapshot recorded: [[wiki/arguments/[note-name]]]
Topic: [topic]
Confidence: [old] → [new] /10
Entries in history: [N]
```

## Notes

- If no argument note exists for the topic, the skill will create one from the argument template and prompt for the initial claim and confidence score
- The Belief History table is append-only — existing rows are never modified
- Works best as part of a loop: `/steelman` or `/critique` → `/track-belief` → repeat over weeks and months
- The `wiki/arguments/_index.md` file is the master register of all tracked beliefs; it is updated automatically
