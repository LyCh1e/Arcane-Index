---
name: <% tp.file.title.toLowerCase().replace(/\s+/g, '-') %>
description: >
  [One sentence describing what this skill does and when to use it.]
  Triggers on: "/<% tp.file.title.toLowerCase() %>", "[trigger phrase 2]", "[trigger phrase 3]",
  "[trigger phrase 4]", "[trigger phrase 5]".
allowed-tools: Read Write Edit Glob Grep
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
version: 1.0.0
---

# <% tp.file.title %>: [One-line role description]

> **Role statement.** You are a [role]. Your job is [what you do]. [Why precision matters — state the failure mode of doing this badly.]

---

## Input Resolution

Determine the target from context, in priority order:

1. **Named argument** — user says `/<% tp.file.title.toLowerCase() %> [argument]`, use it directly
2. **Editor selection** — `<editor_selection>` is present, use it as the working text
3. **Current note** — `<current_note>` is an appropriate file type, read it fully
4. **Inline text** — user has provided content in the message body, use it directly
5. **No target found** — ask: "[Specific question to ask if no input is detected]"

> Remove any resolution paths that don't apply to this skill. Order matters — the first match wins.

---

## Pre-Flight Checks

> Run before the core protocol. Checks that protect against common failure modes.

```
[e.g. Glob wiki/[relevant-dir]/*.md to load context]
[e.g. Read wiki/index.md to check for duplicates before creating]
[e.g. Read <current_note> if resolution path 3 was used]
```

Conditions that should halt execution and ask the user:
- [ ] [Condition 1 — e.g. "Input is empty or ambiguous"]
- [ ] [Condition 2 — e.g. "Target file does not exist"]
- [ ] [Condition 3 — e.g. "Required context file missing"]

---

## Core Protocol

> The numbered steps of the skill. Each step should be atomic and verifiable.

### Step 1 — [Name]

[What happens in this step. Be specific about inputs and outputs.]

### Step 2 — [Name]

[What happens in this step.]

### Step 3 — [Name]

[What happens in this step.]

> Add or remove steps as needed. Do not leave placeholders unpopulated in the final SKILL.md.

---

## Checklist / Analysis Framework

> If this skill has a structured analytical component (like /critique's fallacy checklist or /affirm's reasoning patterns), define it here. If the skill is purely procedural, remove this section.

Apply every item. State "[Not applicable / None detected / Clean]" rather than omitting a section.

| Item | What to look for | Finding |
|------|-----------------|---------|
| [Item 1] | [Signal or criterion] | [Positive / Negative / N/A] |
| [Item 2] | [Signal or criterion] | |
| [Item 3] | [Signal or criterion] | |

---

## Output Format

> Exactly what the skill produces. Use a fenced code block with a markdown template if the output has a fixed structure.

```markdown
## [Skill Name] — YYYY-MM-DD

### [Section 1]
[Description of what goes here]

### [Section 2]
[Description of what goes here]

### Verdict
**Primary [finding/output]**: [One sentence — the single most important result]
**Secondary points**: [1–2 bullet points]
**Recommended action**: [What the user should do next]
```

---

## Filing

> Where output goes. Be explicit — one rule per case.

### If operating on a vault note:

1. [e.g. Append the output block to the end of the note, separated by `---`]
2. [e.g. Update frontmatter: `updated:` → today's date]
3. [e.g. Update `wiki/[index-file].md` — add or update the relevant row]

Do not modify any existing content. Only append.

### If operating on inline / chat input (no vault note):

Respond in chat with the full output. Do not write to the vault.

At the end, offer: "Should I save this as a note in `wiki/[relevant-dir]/`?"

---

## After the Skill Runs

Once the output is delivered, offer (select which apply):

> "Should I run `/[complement-skill-1]` to [what it does], or `/[complement-skill-2]` to [what it does]?"

Do not proceed with those unless the user asks.

---

## Tone

- **[Quality 1]** — [brief rule, e.g. "Direct — name the issue, don't soften it"]
- **[Quality 2]** — [brief rule, e.g. "Specific — quote the source, name the pattern"]
- **[Quality 3]** — [brief rule, e.g. "Constructive — every finding should point to an action"]
- **Never**: "[The failure mode to avoid, e.g. 'Praise without specific evidence']"

---

## Skill Complement Map

| Skill | Focus | When to use together |
|-------|-------|---------------------|
| `/<% tp.file.title.toLowerCase() %>` | [This skill's focus] | — |
| `/[complement-1]` | [Complement focus] | [When to run this after or before] |
| `/[complement-2]` | [Complement focus] | [When to run this after or before] |

---

> **Filing note:** Save this file at `skills/<% tp.file.title.toLowerCase().replace(/\s+/g, '-') %>/SKILL.md`. Register the trigger in `CLAUDE.md` under the Plugin Skills table.
