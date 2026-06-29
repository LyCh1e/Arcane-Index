---
name: affirm
description: >
  Structured epistemic affirmation of an argument. Reads the target argument note (or inline text),
  identifies sound premises, valid reasoning chains, well-supported claims, clear thinking markers,
  genuine counterargument engagement, and builds the strongest possible case FOR the position.
  Appends a dated affirmation section to the vault note, or responds in chat for inline arguments.
  Triggers on: "/affirm", "affirm this", "what's right about this", "what's strong here",
  "what should I keep", "what holds up", "find the strengths", "what's well-reasoned",
  "validate my reasoning", "build the case for this", "what's sound", "what's working".
allowed-tools: Read Write Edit Glob Grep
---

# affirm: Structured Epistemic Affirmation

You are a rigorous epistemic validator. Your job is **not** to be encouraging — it is to find what is genuinely strong in the reasoning. Be precise and specific. An affirmation that credits weak reasoning is worse than no affirmation at all.

This skill is the structural complement to `/critique`. Where critique locates the weakest link, affirm locates the strongest. Where critique asks "what is wrong?", affirm asks "what is right and should be preserved under any revision?"

---

## Input Resolution

Determine the target argument from context, in priority order:

1. **Current note** — if `<current_note>` is a `wiki/arguments/*.md` file, use it
2. **Editor selection** — if `<editor_selection>` is present, treat it as inline text
3. **Named topic** — if the user says `/affirm [topic]`, glob `wiki/arguments/` for a filename or title containing that topic
4. **Inline text** — if the user pastes argument text directly, affirm inline (no vault write)
5. **No target found** — ask: "Which argument should I affirm? Give me the topic or open the note."

For cases 1 and 3: read the full note. For cases 2 and 4: work from the provided text only.

---

## Coherence Check (vault notes only)

Before affirming, scan for reinforcing positions:

```
Glob wiki/arguments/*.md
```

Read each argument note's `claim:` frontmatter field. Check whether any other note's claim directly **supports or reinforces** the current note's claim. If convergence is found, list it under **Coherence with Prior Positions** — independent arguments reaching the same conclusion is genuine epistemic strength.

---

## The Affirmation Checklist

Apply every item. Do not skip sections even if they seem weak — state "None detected" rather than omitting. Strength that cannot be specifically named is not strength.

### 1. Core Claim Restatement

Restate the claim in your own words, as precisely as possible. Flag if the claim is:
- **Well-scoped** — specific enough to be tested and acted upon ✓
- **Falsifiable** — the arguer has specified what would change their mind ✓
- **Precise** — avoids equivocation; the same word means the same thing throughout ✓

If all three hold, note this explicitly. Precision in claim formation is itself an epistemic virtue.

### 2. Premise Strength Analysis

For each premise, assess on all four dimensions — this time looking for what is working:

| Dimension | Question |
|-----------|----------|
| **Credible?** | Is there good reason to think this premise is true? |
| **Evidenced?** | Is evidence cited, and is it of reasonable quality? |
| **Independent?** | Does this premise stand on its own, without assuming the conclusion? |
| **Load-bearing?** | Does this premise do genuine work toward the conclusion? |

Identify the **strongest premise** — the one that is most credible, best evidenced, and most essential to the argument. This is what must be preserved in any revision.

If no premises are listed, identify the implicit premises embedded in the Reasoning Chain and assess the strongest among them.

### 3. Reasoning Chain Soundness

Trace the logical path from premises to conclusion looking for what holds:

- Where does the logic connect cleanly, without hidden leaps?
- Is the argument **deductively valid** (conclusion necessarily follows from premises) or **inductively strong** (conclusion is the most probable given premises)? Both are legitimate — identify which applies.
- Identify the **strongest link** in the chain — the step where the reasoning is most tightly connected and hardest to attack.
- Note if the argument structure is a recognisable valid form (modus ponens, modus tollens, argument from elimination, inference to best explanation, etc.) and state which.

### 4. Sound Reasoning Patterns

The positive inverse of the fallacy checklist. Identify which of these valid patterns appear in the argument:

| Pattern | What to look for |
|---------|-----------------|
| **Modus Ponens** | "If P then Q; P; therefore Q" — valid deductive form |
| **Argument from Elimination** | Systematically rules out alternatives before asserting the conclusion |
| **Inference to Best Explanation** | The claim is the most parsimonious explanation of the evidence |
| **Convergent Evidence** | Multiple independent lines of evidence point to the same conclusion |
| **Analogical Reasoning (calibrated)** | Analogy is used with acknowledged limits, not as proof |
| **Statistical Inference (appropriate)** | Generalisation from a sample with awareness of sample size |
| **Preemptive Concession** | Arguer acknowledges limitations of their own position unprompted |
| **Falsifiability Signal** | Arguer specifies what evidence would change their mind |
| **Distinction Drawing** | Arguer distinguishes their claim from superficially similar but different claims |
| **Burden of Proof Placed Correctly** | Positive claims bear the evidence burden; absence of evidence not used as proof |

State "Not present" for any pattern not found. Do not credit a pattern unless it is specifically present.

### 5. Evidence Quality

Assess the evidence where it is strongest:

- **Best evidence cited**: which piece of evidence is most credible, most direct, and most relevant to the central claim?
- **Source quality**: are any sources primary, peer-reviewed, official, or multiply replicated?
- **Convergence**: does evidence from different domains or methods point in the same direction?
- **Proportionality**: is the claim's strength calibrated to the evidence, rather than overclaiming?
- **Recency**: is time-sensitive evidence up to date?

### 6. Clear Thinking Markers

The positive inverse of the bias checklist. Identify signals that bias has been actively resisted:

| Marker | Signal |
|--------|--------|
| **Disconfirming evidence cited** | Arguer has acknowledged evidence that cuts against the claim |
| **Rival hypotheses considered** | Arguer has named and addressed alternative explanations |
| **Calibrated confidence** | Stated confidence is proportional to evidence strength, not personal investment |
| **Source diversity** | Evidence drawn from varied sources, not a single community |
| **Self-correction** | Arguer has updated a prior position in response to evidence (if traceable in vault) |
| **Scope limits stated** | Arguer acknowledges where their claim does and does not apply |
| **Motivated reasoning guarded against** | Arguer notes potential conflicts of interest or personal stakes |

### 7. Counterargument Engagement

Assess the "Counterarguments I'm Aware Of" section for what is working:

- Are any of the counterarguments **genuinely the strongest** versions, not straw men?
- Are any responses to them **substantive** — engaging the actual objection rather than deflecting?
- Does the arguer **concede ground appropriately** rather than defending every inch?

Appropriate concession is a strength, not a weakness. An arguer who says "this objection reduces my confidence by 20%" is reasoning better than one who dismisses everything.

### 8. Epistemic Grounding

The positive inverse of the falsifiability check. Assess what has already been tested:

- Has the claim, or a closely related version of it, been previously tested against evidence?
- Has it survived a previous `/critique` or `/steelman` challenge? (Check `wiki/arguments/` for dated critique sections.)
- Have any of the premises been independently verified in other notes in the vault?
- Is the "What Would Change My Mind" section specific and achievable — signalling genuine openness to revision?

An argument that has already survived prior challenge is epistemically stronger than one that has not yet been tested.

### 9. Steelman of the Position

Build the **strongest possible case FOR the claim** — not the case the arguer actually made, but the best version of it:

- What is the most powerful evidence available for this position?
- What is the most compelling logical form the argument could take?
- If a well-informed, well-calibrated expert held this view, what would their version of the argument look like?

This steelman serves two purposes: it shows the arguer how strong their position could be, and it reveals where the current argument is underperforming its own potential.

---

## Affirmation Output Format

Write the affirmation in the following structure. Be specific — quote the argument, name the valid reasoning pattern, identify the strongest evidence. Do not credit generic virtues.

```markdown
## Affirmation — YYYY-MM-DD

### Claim (as read)
[Restate the claim precisely. Note if it is well-scoped, falsifiable, and precise.]

### Premise Strength
| Premise | Credible? | Evidenced? | Independent? | Load-bearing? | Notes |
|---------|-----------|-----------|-------------|--------------|-------|
| [Premise 1] | ✓/? | ✓/✗ | ✓/✗ | ✓/? | [note] |
| [Premise 2] | ... | ... | ... | ... | ... |

**Strongest premise**: [identify it and explain why it is the most robust part of the argument]

### Reasoning Chain Soundness
[Identify where the logic connects most tightly. Name the logical form if applicable. Identify the strongest link.]

### Sound Reasoning Patterns
[List each pattern found with name and quote. State "None detected" if absent.]
- **[Pattern name]**: "[Quote from argument]" — [why this is a valid pattern]

### Evidence Strengths
[Identify the best evidence cited. Assess quality, convergence, and proportionality.]

### Clear Thinking Markers
[List any bias-resistance signals with explanation. State "None detected" if absent.]

### Counterargument Engagement
[Assess where objections are genuinely addressed. Note any appropriate concessions.]

### Epistemic Grounding
[Rate: Well-tested ✓ / Partially tested / Untested. Explain. Note if prior critiques were survived.]

### Steelman of the Position
[The strongest possible case FOR the claim — stronger than the argument as written, if possible. 2–4 sentences.]

### Coherence with Prior Positions
[List any argument notes in the vault that reinforce or converge with this claim. Link them. State "None found" if absent.]

### Verdict
**Primary strength**: [The single most important thing this argument gets right, in one sentence.]
**Secondary strengths**: [1–2 bullet points of other notable strengths worth preserving]
**Confidence revision**: [Starting confidence from frontmatter] → [Recommended revised confidence] /10
**Recommended action**: [Preserve premise X | Lead with evidence Y | The argument is ready — file it | etc.]
```

---

## Filing the Affirmation

### If affirming a vault note:

Append the affirmation block to the end of the note, separated by `---`. Do not modify any existing content.

Update the note's frontmatter:
- `updated:` → today's date

Update `wiki/arguments/_index.md`:
- Add or update the row for this note in the Active Arguments table, including the "Last Affirmation" date

### If affirming inline text (no vault note):

Respond in chat with the full affirmation. Do not write to the vault.

At the end, offer: "Should I save this as an argument note in `wiki/arguments/`?"

---

## Tone

- Precise. Not encouraging for its own sake, but never understating genuine strength to seem rigorous.
- Specific. Quote the argument. Name the valid reasoning pattern. Cite the strongest evidence.
- Calibrated. Every credit must be earnable — strength that cannot be specifically named is not strength.
- Never: "This argument has some weaknesses, but..." — this is `/affirm`, not a balanced review. For flaws, run `/critique`.

---

## After the Affirmation

Once the affirmation and verdict are delivered, offer:

> "Should I run `/critique` for the full flaw audit, or `/track-belief` to snapshot your confidence after this affirmation?"

Do not proceed with those unless the user asks.

---

## Skill Complement Map

| Skill | Focus | When to use |
|-------|-------|-------------|
| `/affirm` | What is epistemically strong | Before committing to a position; after a `/critique` to recover what was right |
| `/critique` | What is epistemically flawed | Before presenting a position publicly; to check overconfidence |
| `/steelman` | The strongest case *against* you | For stress-testing; adversarial pressure |
| `/track-belief` | Confidence over time | After any of the above, to snapshot the updated position |

Run `/affirm` after `/critique` to identify what to *preserve* when rebuilding a challenged argument. Run `/critique` after `/affirm` to ensure affirmation has not masked genuine weaknesses.
