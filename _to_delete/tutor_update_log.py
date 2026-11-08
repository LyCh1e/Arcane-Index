# -*- coding: utf-8 -*-
path = "study-notes/log.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Last Published dates
content = content.replace(
    "| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV | 2026-11-03 |",
    "| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV | 2026-11-04 |"
)
content = content.replace(
    "| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 | 2026-11-03 |",
    "| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 | 2026-11-04 |"
)
content = content.replace(
    "| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv | 2026-11-03 |",
    "| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv | 2026-11-04 |"
)
assert "2026-11-04 |" in content and content.count("2026-11-04 |") == 3, "date replace failed"

# 2. Insert new run-57 note before "## Topic Rotation History"
marker = "## Topic Rotation History"
new_note = (
"> [!note] Run 57 on 2026-11-04 (first run today)\n"
"> Before selecting this run's topics, all three live Artefact pages were fully read via the Artifact tool's `read` action (the full saved source for each) and confirmed to match this file's \"run 56\" entries exactly for all three modules — no unlogged gap, file was in sync.\n"
">\n"
"> ICT3112 moved to V&V Fundamentals & Famous Failures, Control Flow Graphs (CFGs), and Hoare Logic — the Six Inference Rules & Weakest Precondition Calculus — none used in the last 5 runs; its lab moved to a fresh angle on `ict3112-lab2-reqnroll-bdd.md` (last used run 50's Gherkin-scenarios/Musa-calculation angle) — Reqnroll BDD mechanics (Cucumber Expressions, Scenario Outline vs data-table distinction, tags→NUnit categories, context injection, ambiguous bindings) plus the handout's adversarial section-7 prompt-injection-style trap and its `@ignore` handling. ICT3113 moved to Operational Laws (Forced Flow & Service Demand), Lost Work & the Erlang B Formula, and Workload Identification — the Decomposition Chain & Peak vs Average; its lab pool had been exhausted (all 5 lab source files used within the last 5 runs), so the pool-exhaustion rule applied — it revisited `ict3113-a1-ticket-triage-service.md` (least recently used, last seen run 52's golden-set/kappa-validation angle) with a genuinely different angle: the OLLAMA_MODEL env-var model-swap mechanism, per-event JSON latency instrumentation cross-checked against JMeter, and the exact→substring→fallback classifier design, distinct from both run 52's and run 47's prior angles on the same file. INF2005 moved to Foundations (the CIA Triad & Alice/Bob/Eve Threat Model), Password Security — Storage, Salting & Attacks, and RSA — Asymmetric Encryption in Practice; its lab pool was also exhausted (all 3 known lab files used within the last 5 runs), so it revisited `inf2005-acw3-mod-dav-fs-proppatch-dos.md` (least recently used, last seen run 54's defence-in-depth/detection/tooling angle) with the O(n²) memory-blowup mechanics (SIGSEGV vs OOM-kill, the 5GB/10.8GB figures) and the \"worker crash ≠ container down\" observability trap instead.\n"
">\n"
"> All three modules' 20 new questions per module were verified programmatically (not by eye) for stray HTML entities, option-length balance (`len(correct) - len(longest distractor) > 15`), and A/B/C/D answer-position distribution before publishing; INF2005 initially had 2 stray HTML entities caught and fixed in the RSA section's questions, with all three modules re-verified clean (5/5/5/5 position distribution, 0 length-tell failures, 0 entity leaks) across all 60 questions before publishing. All three pages' republish attempts needed the standard \"hadn't viewed the live version\" refusal followed by a full read of the live saved source, then one \"identical content already refused, resent unchanged\" refusal before an immediate retry succeeded — consistent with the established retry precedent. All three pages were republished to their existing Artefact URLs (no new URLs created). All three modules' estimated reading time remained at the generator's 10-minute floor.\n"
)
idx = content.index(marker)
assert idx > 0
content = content[:idx] + new_note + "\n\n" + content[idx:]

# 3. Update Topic Rotation History per module
lines = content.split("\n")

def update_module(lines, header, new_line):
    idx = lines.index(header)
    start = idx + 1
    i = start
    bullets = []
    while i < len(lines) and lines[i].startswith("- "):
        bullets.append(lines[i])
        i += 1
    assert len(bullets) == 5, f"{header}: expected 5 bullets, found {len(bullets)}"
    new_bullets = bullets[1:] + [new_line]
    lines[start:i] = new_bullets
    return lines

lines = update_module(lines, "### ICT3112",
    "- 2026-11-04 (run 57): V&V Fundamentals & Famous Failures; Control Flow Graphs (CFGs); Hoare Logic — the Six Inference Rules & Weakest Precondition Calculus; [Lab] Reqnroll BDD — Cucumber Expressions, Scenario Outlines vs Data Tables & the Section-7 Trap")
lines = update_module(lines, "### ICT3113",
    "- 2026-11-04 (run 57): Operational Laws — Forced Flow Law & Service Demand Law; Lost Work & the Erlang B Formula; Workload Identification — the Decomposition Chain & Peak vs Average; [Lab] Ticket Triage Service — Env-Var Model Swapping, Latency Instrumentation & the Fallback-Aware Classifier")
lines = update_module(lines, "### INF2005",
    "- 2026-11-04 (run 57): Foundations — the CIA Triad & the Alice/Bob/Eve Threat Model; Password Security — Storage, Salting & Attacks; RSA — Asymmetric Encryption in Practice; [Lab] mod_dav_fs PROPPATCH DoS — the Memory-Blowup Mechanics & Why the Container Looks Fine")

content = "\n".join(lines)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("UPDATE_OK")
