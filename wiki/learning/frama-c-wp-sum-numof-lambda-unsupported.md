---
type: learning
title: "Frama-C WP does not define \sum / \numof with lambdas"
domain: formal-verification
status: resolved
created: 2026-11-23
tags: [frama-c, wp, acsl, ai-verification-loop]
---

# Frama-C WP does not define \sum / \numof with lambdas

Context: ICT3112 Assignment 2 (AI verification loop). See [[resources/frama-c]].

**Symptom.** Goals mentioning `\sum(a,b,\lambda ...)` or `\numof(a,b,\lambda ...)` stay unproved whatever the loop invariants say, even the empty-sum goal `w = 0`. WP warns `Builtin \sum(int,int,_) not defined` and `Lambda-functions not yet implemented`, then treats each occurrence as an opaque term.

**Impact in the assignment.** 146 of 177 unproved goals (m3_frequencies, L2_gradebook) came from this, not from the iteration budget. Repair agents cannot fix it with annotations; logic functions and axioms were forbidden.

**Workaround.** State counts and sums without lambdas: explicit loop-carried facts, or bounds such as `0 <= \result <= n`, `\result == 0 <==> no match`. The bounds form is weaker than an exact count, so a `fix_contract` that does this weakens the specification and must be disclosed.

**Lesson.** Tell the Annotator prompt up front to avoid `\sum`/`\numof` lambdas. Also, the contract-integrity guard checked approval, not strength, so weakened contracts passed under `--auto-approve`.
