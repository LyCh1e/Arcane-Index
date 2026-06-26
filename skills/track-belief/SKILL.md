---
name: track-belief
description: >
  Snapshots the current state of a belief or argument into its Belief History table,
  with a date and confidence score. Creates a new argument note from the template if
  none exists. Enables tracking how positions evolve over time across sessions.
  Triggers on: "/track-belief", "track my belief", "track this belief",
  "snapshot my position", "record this belief", "log my confidence",
  "how has my thinking changed", "show belief history", "update my confidence",
  "track my thinking on [topic]", "I've changed my mind on".
allowed-tools: Read Write Edit Glob Grep
---

# track-belief: Belief Snapshot and Evolution Tracker

Beliefs and positions change. This skill makes that change visible. Every time you run it, a dated snapshot is added to the argument note's Belief History table. Over time this produces a record of how your thinking evolved on any subject.

---

## Mode Detection

Detect which operation the user wants:

| User intent | Mode |
|-------------|------|
| "Track my belief that X" / "Snapshot my position on X" | **Snapshot** (create or update) |
| "I've changed my mind on X" | **Revision** (update + note the change) |
| "How has my thinking changed on X?" / "Show belief history" | **Review** |
| "I no longer believe X" / "I'm abandoning this position" | **Abandon** |

If unclear, default to **Snapshot** mode.

---

## Step 1 — Locate or Create the Argument Note

### If a note already exists:

Check `<current_note>` first. If it is a `wiki/arguments/*.md` note, use it.

Otherwise, glob `wiki/arguments/` and search for a filename or `topic:` frontmatter field matching the user's stated topic.

### If no note exists:

1. Ask the user for:
   - **Claim**: the position in one sentence
   - **Confidence**: a number 1–10 (optional; default 5 if not given)

2. Create `wiki/arguments/[topic-slug].md` using the argument template structure:

```markdown
---
type: argument
title: "[Topic Title]"
topic: "[topic]"
claim: "[User's claim]"
confidence: [N]
created: [TODAY]
updated: [TODAY]
status: active
tags:
  - argument
  - [topic-tag]
related: []
---

# [Topic Title]

## Claim

[User's stated claim]

## Premises

[To be filled in — use /critique or /steelman to develop this]

## Evidence

[To be filled in]

## Counterarguments I'm Aware Of

[To be filled in]

## What Would Change My Mind

[To be filled in]

## Reasoning Chain

[To be filled in]

---

## Belief History

| Date | Confidence | Summary of position |
|------|-----------|-------------------|
| [TODAY] | [N]/10 | [User's claim, condensed to 15 words] |
```

3. Add the note to `wiki/arguments/_index.md` Active Arguments table.

---

## Step 2 — Snapshot Mode

Read the current state of the note:
- `claim:` from frontmatter
- `confidence:` from frontmatter
- The most recent row in the Belief History table (if any)

Ask the user (if not already provided):
- **Current confidence**: "What's your confidence in this position right now? (1–10)"
- **Position summary**: "Any shift in how you'd state the claim compared to before?" (Optional — if no change, reuse the existing claim)

Compare current state to the **last Belief History row**:
- Has confidence changed? By how much?
- Has the claim wording changed?
- Were there new premises, evidence, or counterarguments added to the note since the last snapshot?

### Append to Belief History table:

Add a new row at the **bottom** of the table:

```
| [TODAY] | [N]/10 | [Brief summary — one sentence, ≤15 words] |
```

The summary should capture the **essence of the current position**, not just restate the original claim if it has evolved.

### Update frontmatter:

- `confidence:` → new value
- `updated:` → today's date

### If confidence changed significantly (≥2 points):

Add an inline note in the table row:

```
| [TODAY] | [N]/10 | [Summary] *(↑ from X — [brief reason])* |
```

or

```
| [TODAY] | [N]/10 | [Summary] *(↓ from X — [brief reason])* |
```

---

## Step 3 — Revision Mode ("I've changed my mind on X")

Used when the user's core position has shifted, not just their confidence.

1. Read the existing note
2. Ask: "How has your position changed? What's your new claim?"
3. Update the note:
   - **Do not overwrite** the original Claim section — add a new `## Revised Claim (YYYY-MM-DD)` section below the original
   - Update `claim:` in frontmatter to the new claim
   - Update `status:` to `revised` if the change is substantial
4. Append to Belief History with a note on what changed:

```
| [TODAY] | [N]/10 | [New position summary] *(revised — [what changed in one phrase])* |
```

5. Update `wiki/arguments/_index.md` — move the note to the **Revised Arguments** table.

---

## Step 4 — Review Mode ("How has my thinking changed?")

Display a summary of the belief's evolution:

```
## Belief History: [Topic]

Tracking since: [Date of first entry]
Entries: [N snapshots]

| Date | Confidence | Position |
|------|-----------|----------|
[All rows from the Belief History table]

**Trajectory**: [One sentence describing the trend — e.g., "Confidence increased steadily after critique on YYYY-MM-DD. Core claim narrowed from X to Y."]

**Biggest shift**: [Identify the largest confidence change or claim revision and when it happened]

**Current status**: [active / revised / abandoned]
```

If there is only one entry, note that there is not enough history to show a trajectory yet.

---

## Step 5 — Abandon Mode

Used when the user no longer holds the position.

1. Ask: "Why are you abandoning this position? What changed?" (Optional — they may just say "it's wrong")
2. Update the note:
   - `status:` → `abandoned`
   - `updated:` → today
3. Append final Belief History row:

```
| [TODAY] | [N]/10 | *(abandoned — [brief reason])* |
```

4. Update `wiki/arguments/_index.md`:
   - Remove from Active table
   - Add to Abandoned table with the reason

---

## Updating the Arguments Index

After any snapshot, revision, or abandonment, update `wiki/arguments/_index.md`:

**Active Arguments table** — columns: Page | Topic | Claim (summary) | Confidence | Last Critique

Update the row for this note. If the note is new, add it. If the status changed to revised or abandoned, move it to the appropriate table.

---

## Confirm to User

After completing the snapshot:

```
Snapshot recorded: [[wiki/arguments/[note-name]]]
Topic: [topic]
Confidence: [old] → [new] /10
Entries in history: [N]
```

If confidence changed significantly, note it:
```
⚠ Confidence shifted [+/-N] points since last snapshot ([date]).
```

Offer follow-up options:
> "Run `/critique` to identify what's driving that confidence shift, or `/steelman` to stress-test the current position."
