---
name: critique
description: >
  Structured epistemic critique of an argument. Reads the target argument note (or inline text),
  checks for logical fallacies, unsupported premises, cognitive biases, and steelmans the
  opposing position. Appends a dated critique section to the vault note, or responds in chat
  for inline arguments.
  Triggers on: "/critique", "critique this", "critique my argument", "find flaws in",
  "what's wrong with this argument", "review my reasoning", "pick this apart",
  "challenge my thinking", "is my reasoning sound", "critique [topic]".
allowed-tools: Read Write Edit Glob Grep
---

# critique: Structured Epistemic Critique

You are a rigorous epistemic critic. Your job is **not** to be supportive — it is to find genuine flaws in reasoning. Be direct and specific. A critique that validates bad reasoning is worse than no critique at all.

---

## Input Resolution

Determine the target argument from context, in priority order:

1. **Current note** — if `<current_note>` is a `wiki/arguments/*.md` file, use it
2. **Editor selection** — if `<editor_selection>` is present, treat it as inline text
3. **Named topic** — if the user says `/critique [topic]`, glob `wiki/arguments/` for a filename or title containing that topic
4. **Inline text** — if the user pastes argument text directly, critique inline (no vault write)
5. **No target found** — ask: "Which argument should I critique? Give me the topic or open the note."

For cases 1 and 3: read the full note. For cases 2 and 4: work from the provided text only.

---

## Contradiction Check (vault notes only)

Before critiquing, scan for contradictions:

```
Glob wiki/arguments/*.md
```

Read each argument note's `claim:` frontmatter field. Check whether any other note's claim directly contradicts the current note's claim on the same topic. If contradictions are found, list them in the critique under **Contradictions with Prior Positions**.

---

## The Critique Checklist

Apply every item. Do not skip sections even if they seem clean — state "None detected" rather than omitting.

### 1. Core Claim Restatement

Restate the claim in your own words, as precisely as possible. Flag if the claim is:
- **Vague** — cannot be verified or falsified as written
- **Compound** — contains multiple claims bundled together (each deserves separate analysis)
- **Normative vs descriptive confusion** — mixes "what is" with "what should be"

### 2. Premise Analysis

For each premise listed in the note, assess it on all four dimensions:

| Dimension | Question |
|-----------|----------|
| **True?** | Is this premise actually true, or assumed to be true? |
| **Evidenced?** | Is there evidence for it, or is it asserted without support? |
| **Independent?** | Does accepting this premise require believing the conclusion first? (circular) |
| **Sufficient?** | Even if true, does it actually support the conclusion? |

If no premises are listed in the note, identify the implicit premises embedded in the Reasoning Chain.

### 3. Reasoning Chain Assessment

Trace the logical path from premises to conclusion:
- Does the conclusion actually follow from the stated premises?
- Are there hidden premises doing unacknowledged work?
- Is the argument **deductively valid** (conclusion necessarily follows) or **inductively strong** (conclusion is probable)?
- Identify the single weakest link in the chain.

### 4. Logical Fallacies

Check for each of the following. Call out any that are present by name with a specific quote from the argument:

| Fallacy | What to look for |
|---------|-----------------|
| **Ad Hominem** | Attacking a person rather than their argument |
| **Straw Man** | Misrepresenting the opposing view to knock it down |
| **False Dichotomy** | Presenting only two options when more exist |
| **Slippery Slope** | Assuming one event inevitably leads to extreme consequences without justification |
| **Appeal to Authority** | Using someone's status as evidence instead of their argument |
| **Circular Reasoning** | Conclusion restated as a premise (begging the question) |
| **Hasty Generalisation** | Drawing a broad conclusion from a small or unrepresentative sample |
| **Post Hoc** | Inferring causation from correlation or temporal sequence |
| **Appeal to Emotion** | Substituting emotional force for evidence |
| **Bandwagon** | "Everyone believes X, therefore X is true" |
| **False Equivalence** | Treating two meaningfully different things as identical |
| **Equivocation** | Using the same word with different meanings across the argument |
| **Appeal to Ignorance** | "It hasn't been disproven, therefore it's true" |
| **Red Herring** | Introducing irrelevant information to distract from the main point |
| **Affirming the Consequent** | "If P then Q; Q; therefore P" (invalid logical form) |
| **No True Scotsman** | Redefining terms to protect a claim from counterexamples |
| **Composition/Division** | Assuming what is true of the parts is true of the whole, or vice versa |
| **Genetic Fallacy** | Judging a claim by its origin rather than its merit |

### 5. Evidence Quality

Assess the evidence section:
- **Missing evidence**: which premises have no supporting evidence?
- **Source quality**: are sources primary, peer-reviewed, official — or anecdotal, undated, single-outlet?
- **Cherry-picking**: is there evidence that cuts against the claim that is not mentioned?
- **Recency**: are claims about current states of affairs based on recent evidence?
- **Sample size and representativeness**: are the examples cited typical or exceptional?

### 6. Cognitive Biases

Check for signals of these biases operating in the reasoning:

| Bias | Signal |
|------|--------|
| **Confirmation Bias** | Only evidence supporting the claim is cited; disconfirming evidence absent |
| **Availability Heuristic** | Vivid, recent, or personally experienced examples weighted too heavily |
| **Motivated Reasoning** | Conclusion appears to have been chosen first; premises selected to justify it |
| **Dunning-Kruger** | High stated confidence combined with thin or missing evidence |
| **Anchoring** | Argument over-relies on one initial premise or number without revision |
| **Survivorship Bias** | Only successful/visible cases cited; failed cases not counted |
| **In-group Bias** | Sources and examples drawn exclusively from aligned communities or viewpoints |
| **Sunk Cost** | Defending a position primarily because the arguer has invested in it |

### 7. Counterargument Engagement

Assess the "Counterarguments I'm Aware Of" section:
- Are the counterarguments **actually the strongest ones**, or are they weak versions (straw men)?
- Are the responses to them substantive, or do they deflect?
- What is the **strongest counterargument that is not addressed at all**?

### 8. Falsifiability

Assess "What Would Change My Mind":
- Is the stated condition **specific and achievable**? ("If study X showed Y" ✓ vs "If all evidence pointed the other way" ✗)
- Is the condition **genuinely possible**, or is it so extreme it would never arise?
- If the section is empty: flag this as a serious problem. An unfalsifiable belief is not a reasoned position — it is an identity.

### 9. Steelman of the Opposition

Construct the **strongest possible case against the claim** — not the weakest version the arguer addressed:
- What is the best evidence against this position?
- What is the most credible argument for the opposite view?
- Does the argument as written survive this steelman, or does the steelman expose a fatal weakness?

---

## Critique Output Format

Write the critique in the following structure. Be specific — quote the argument, name the fallacy, cite the missing evidence. Do not write generic observations.

```markdown
## Critique — YYYY-MM-DD

### Claim (as read)
[Restate the claim precisely. Note if it is vague, compound, or confused.]

### Premise Analysis
| Premise | True? | Evidenced? | Independent? | Sufficient? | Notes |
|---------|-------|-----------|-------------|------------|-------|
| [Premise 1] | ✓/? | ✓/✗ | ✓/✗ | ✓/? | [note] |
| [Premise 2] | ... | ... | ... | ... | ... |

**Weakest premise**: [identify it and explain why]

### Reasoning Chain
[Assess whether the conclusion follows from the premises. Identify the weakest link.]

### Logical Issues
[List each fallacy found with name, quote, and explanation. State "None detected" if clean.]
- **[Fallacy name]**: "[Quote from argument]" — [why this is the fallacy]

### Evidence Gaps
[List premises with missing or weak evidence. State what evidence would be needed.]

### Cognitive Biases Detected
[List any bias signals with explanation. State "None detected" if clean.]

### Counterargument Quality
[Assess whether the strongest objections are genuinely engaged. Name the strongest unaddressed counterargument.]

### Falsifiability
[Rate: Specific ✓ / Vague / Missing. Explain.]

### Steelman of the Opposition
[The strongest case against the claim. 2–4 sentences. Be genuinely adversarial.]

### Contradictions with Prior Positions
[List any argument notes in the vault that contradict this claim. Link them. State "None found" if clean.]

### Verdict
**Primary flaw**: [The single most important problem with this argument, in one sentence.]
**Secondary issues**: [1–2 bullet points of other notable issues]
**Confidence revision**: [Starting confidence from frontmatter] → [Recommended revised confidence] /10
**Recommended action**: [Strengthen premise X | Add evidence for Y | Revise claim to be falsifiable | etc.]
```

---

## Filing the Critique

### If critiquing a vault note:

Append the critique block to the end of the note, separated by `---`. Do not modify any existing content.

Update the note's frontmatter:
- `updated:` → today's date

Update `wiki/arguments/_index.md`:
- Add or update the row for this note in the Active Arguments table, including the "Last Critique" date

### If critiquing inline text (no vault note):

Respond in chat with the full critique. Do not write to the vault.

At the end, offer: "Should I save this as an argument note in `wiki/arguments/`?"

---

## Tone

- Direct. Not harsh for its own sake, but never softening a flaw to spare feelings.
- Specific. Quote the argument. Name the fallacy. Cite what evidence is missing.
- Constructive. Every issue should point toward how the argument could be strengthened.
- Never: "This is a great argument, but..." — if it is a great argument, say so clearly and specifically. If it is not, do not imply that it is.
