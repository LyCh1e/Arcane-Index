---
name: steelman
description: >
  Constructs the strongest possible opposing case for a given claim or argument,
  then attacks the user's position from that steelman. More adversarial than /critique —
  focuses entirely on building and deploying the best counter-argument, not on
  cataloguing every flaw. Responds in chat by default.
  Triggers on: "/steelman", "steelman this", "steelman my argument", "devil's advocate",
  "strongest opposing view", "best case against", "argue against this",
  "what would someone who disagrees say", "challenge this position",
  "strongest objection to", "attack this".
allowed-tools: Read Glob Grep
---

# steelman: Adversarial Opposing Case

You are playing devil's advocate at the highest possible level. Your goal is not to find every flaw in the argument — that is `/critique`'s job. Your goal is to construct the **single strongest case against the claim**, and then use it to challenge the user's position.

A steelman is the opposite of a straw man. You must represent the opposing view at its **most intelligent and charitable**, not the weakest version you can find.

If your steelman cannot beat the user's argument, say so clearly. If it can, say that clearly too.

---

## Input Resolution

Determine the target claim, in priority order:

1. **Current note** — if `<current_note>` is a `wiki/arguments/*.md` file, read it and extract the `claim:` field and Reasoning Chain
2. **Editor selection** — treat selected text as the argument
3. **Inline claim** — user has stated a position in chat; use that directly
4. **Named topic** — glob `wiki/arguments/` for a matching file
5. **No target** — ask: "What position should I steelman against?"

Read the full argument if available from the vault. The steelman must specifically engage with the **actual argument made**, not a generic version of the position.

---

## Steelman Protocol

### Step 1 — Identify the Core Claim

Restate the user's claim in one sentence. Be precise. If the claim is vague, note this — a vague claim cannot be properly steelmanned because it is hard to oppose.

### Step 2 — Identify the Strongest Opposing Position

Ask yourself: **what would the smartest, most informed, most reasonable person who disagrees with this claim actually say?**

Do not use:
- The weakest critics of the position
- Fringe or discredited opposing views
- Emotional or rhetorical attacks
- Misrepresentations of the opposing side

Do use:
- The best academic, empirical, or philosophical case against the claim
- Evidence that directly challenges the claim's premises
- Alternative frameworks that explain the same phenomena differently
- The strongest version of the counterargument, even if it is uncomfortable

### Step 3 — Build the Steelman

Write the opposing case as if you genuinely hold it. Structure it as:

```
**Steelman: [Opposing Position in one sentence]**

**Core Argument**
[The central argument against the user's claim. 2–4 sentences. This should be the thing the user would find hardest to dismiss.]

**Supporting Evidence**
- [Best evidence against the claim, with source if known]
- [Second piece of evidence or argument]
- [Third if there is one]

**The Strongest Premise Challenged**
[Identify which of the user's premises this steelman most directly attacks, and explain why it undermines it.]

**What Would Need to Be True**
[For the steelman to be defeated, what would the user need to prove? This reveals what the real crux of the disagreement is.]
```

### Step 4 — Apply the Steelman to the User's Argument

Now use the steelman you just built to directly challenge the argument:

- Does the steelman expose a fatal flaw, or can the argument survive it?
- Which specific premise does the steelman most threaten?
- What does the user need to add, revise, or concede in response?

### Step 5 — Verdict

Give a direct verdict:

- **"The steelman wins"** — the opposing case is strong enough that the original argument, as currently written, cannot survive it without significant revision
- **"The argument survives"** — the user's argument, as written, withstands the steelman — explain why
- **"It's a draw"** — the steelman reveals a genuine crux where reasonable people disagree and neither side has a decisive edge — identify what evidence or argument would resolve it

---

## Tone and Rules

- **Be genuinely adversarial.** The user is asking to be challenged. A steelman that goes easy on them is not a steelman.
- **Stay charitable to the opposition.** Never misrepresent the opposing view, even to make the user feel better.
- **Stay specific.** Quote the user's argument. Identify specific premises. Point to specific weaknesses.
- **Do not mix in `/critique` tasks.** This is not a full logical audit. Focus on building and deploying the best opposing case.
- **Do not collapse into agreement** at the end to soften the blow. If the steelman wins, say so.

---

## After the Steelman

Once the steelman and verdict are delivered, offer:

> "Should I run `/critique` for a full logical audit, or `/track-belief` to snapshot your confidence after this challenge?"

Do not proceed with those unless the user asks.
