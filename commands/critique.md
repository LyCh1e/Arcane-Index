---
description: Run a structured epistemic critique on an argument — checks for logical fallacies, unsupported premises, cognitive biases, and constructs a steelman of the opposition. Appends a dated critique section to the argument note.
---

Read the `critique` skill. Then run the critique workflow for the target argument.

## Usage

| Command | What it does |
|---------|-------------|
| `/critique` | Critique the currently open argument note |
| `/critique [topic]` | Locate the argument note for that topic and critique it |
| `/critique [inline text]` | Critique pasted argument text in chat — no vault write |

## When to Use

- You have written (or are reading) an argument in `wiki/arguments/` and want a rigorous audit before committing to the position
- You want to find the weakest link in your reasoning chain before presenting it
- You have just run `/track-belief` and your confidence is high — a critique keeps overconfidence in check
- You want an independent check on whether your counterargument engagement is genuine or a straw man
- You want a **steelman of the opposition** embedded in the output alongside the full logical audit

## What It Produces

A `## Critique — YYYY-MM-DD` section appended to the argument note, covering:

1. **Claim restatement** — flags vague, compound, or normative-vs-descriptive confusion
2. **Premise analysis** — rates each premise on truth, evidence, independence, and sufficiency
3. **Reasoning chain** — identifies the weakest logical link
4. **Logical fallacies** — checks 17 named fallacies with quotes and explanations
5. **Evidence gaps** — identifies which premises have no supporting evidence
6. **Cognitive biases** — checks 8 biases including confirmation bias and motivated reasoning
7. **Counterargument quality** — names the strongest unaddressed objection
8. **Falsifiability** — flags if "What Would Change My Mind" is missing or too vague
9. **Steelman of the opposition** — the best case against the claim
10. **Contradictions with prior positions** — cross-checks other notes in `wiki/arguments/`
11. **Verdict** — primary flaw, secondary issues, recommended confidence revision

## Notes

- Critiquing a vault note writes back to that note and updates `wiki/arguments/_index.md`
- Critiquing inline text responds in chat only; you will be offered the option to save as a new argument note
- The skill is deliberately direct — it will not soften a genuine flaw
- For adversarial stress-testing only (no full audit), prefer `/steelman`
- For recording your confidence after a critique, use `/track-belief`
