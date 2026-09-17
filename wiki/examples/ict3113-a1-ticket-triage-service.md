---
type: example
title: "ICT3113 Assignment 1 — Ticket Triage Service (FastAPI + Ollama + Docker)"
domain: performance-engineering
course: ICT3113
created: 2026-09-17
updated: 2026-09-17
tags: [ict3113, fastapi, ollama, docker-compose, sqlite, synchronous-baseline, llm-classification, performance-testing]
related:
  - resources/ollama-local-inference
  - concepts/docker-compose
  - concepts/performance-metrics
  - concepts/workload-identification
---

# ICT3113 Assignment 1 — Ticket Triage Service

Built the coding portion of Assignment 1 (Performance Requirements &
Testing) for team P1-6: a synchronous ticket classification service that
is deliberately naive, so that Assignment 1's testing can measure an
honest baseline before Assignment 2's optimisation pass. Repo:
`ICT3113-Performance-Testing-and-Optimisation-Project` (local, not yet
pushed to a team GitHub remote at time of writing).

## The scenario shape

Client wants complaint tickets auto-routed into 7 fixed categories.
Hard constraint: no public model API — all inference must run on
commodity CPU hardware via Ollama, GPU inference explicitly disallowed.
The brief is structured so **Step 1 (build the golden test set) must
finish before any model exists** — labels come first, then code, so a
model's output can never leak into the ground truth.

## What "baseline" means here, precisely

The brief is unusually explicit that the service should be "the
straightforward thing an agent writes: sequential calls, no caching, no
queuing" and that pre-optimising it defeats the assignment's purpose —
Assignment 2 is where optimisation is scored. This reframes what would
normally look like corner-cutting into the correct choice:

- `POST /tickets` blocks on the Ollama call — no background task, no
  async fire-and-forget.
- SQLite via a **fresh `sqlite3.connect()` per request**, opened and
  closed inside the same thread that handles it — no connection pool,
  no ORM. This is deliberate, not just simple: FastAPI runs sync `def`
  endpoints in a threadpool, and [[examples/ict3113-lab2-jmeter-testing|
  Lab 2's own root-caused bug]] already showed that a **shared** cursor
  across threads (Flask-profiler's sqlite backend) causes `Recursive use
  of cursors` crashes under load. Per-request connections sidestep that
  bug by construction, while still leaving realistic lock contention
  (`sqlite3.connect(..., timeout=30)` just raises the busy-timeout so it
  doesn't fail instantly) as a legitimate, diagnosable bottleneck for the
  Step 5 stress test to find.
- No prompt-following enforcement beyond a plain substring match against
  the 7 category names — CPU-bound small models (1-3B class) frequently
  ignore "respond with only X" instructions. Rather than retrying or
  constraining generation (both are a shape of pre-optimisation and add
  latency variance that would contaminate the load-test numbers), the
  classifier does exact-match then substring-match then a fixed fallback
  category, and **logs `fallback_used: true`** whenever the fallback
  fired. That single boolean field turns "the model was wrong" and "the
  model didn't follow the output format" into two separately measurable
  failure modes for the Step 6 accuracy write-up, for free.

## Model backend as a pure env var

`OLLAMA_MODEL` is read at process start and threaded through one
`OllamaClient` instance — nothing in the service code names a specific
model. Swapping candidates for Step 5's per-model benchmark runs is
`docker compose exec ollama ollama pull <tag>` + restart with a new env
var, never a code change. This matters because the assignment requires
3-5 pinned candidates spanning ≥2 size classes tested under an identical
harness — any model-specific branching in the service would make that
comparison unfair by construction.

## Instrumentation

Every HTTP request and every classification call is one JSON line
(custom `logging.Formatter` subclass, not a dict logged as a string) to
both a file (kept in the repo, per the brief's "every number must
reconcile with a log entry" requirement) and stdout. Fields on a
`ticket_classified` event: `ticket_id`, `narrative_chars`, `model`,
`category`, `classify_latency_ms`, `fallback_used`. This is the minimum
needed to later cross-check JMeter's own latency numbers against the
service's self-reported per-call latency, and to separate Ollama latency
from FastAPI/SQLite overhead if the two ever diverge.

## Supporting scripts (stdlib-only, no deps)

Three scripts do the part of Step 1 that's mechanical rather than
judgment-based:

- `extract_team_rows.py` — filters the full ~146K-row CSV on its `row`
  column (not line position) for `team*1000..team*1000+999`. Using
  `csv.DictReader` instead of line-splitting matters here: many
  narratives contain literal embedded newlines inside quoted CSV fields,
  so `wc -l` on the source file overcounts massively (146,216 lines for
  what is actually far fewer records) and naive line-based slicing would
  corrupt multi-line narratives.
- `sample_golden_set.py` — seeded random sample (default n=180, refuses
  outside 150-200 per the brief) from the team's 1000 rows, **writes out
  only `row` + `narrative`, dropping the noisy source label** so
  labellers can't be anchored to it while building ground truth.
- `agreement.py` — Cohen's kappa for exactly 2 raters, Fleiss' kappa for
  3+, both implemented from the closed-form definitions (no scipy/sklearn
  dependency, since this is meant to run anywhere Python 3.10+ runs).
  Verified against synthetic data: 50 items, ~80% engineered raw
  agreement over 3 categories → kappa 0.7595 ("substantial" on the
  Landis & Koch scale, which is the expected shape: kappa sits below raw
  agreement because it subtracts out chance agreement, more so with
  fewer categories). Also emits a disagreements CSV with an empty
  `resolution` column, ready for the team's discussion step.

## Verification approach without Docker Desktop running

Docker wasn't running in the dev session, so the service logic was
verified directly: a throwaway venv + FastAPI's `TestClient` (used as a
context manager — `with TestClient(app) as client:` — which is required
to actually fire Starlette's startup/shutdown lifespan events; a bare
`TestClient(app)` silently skips them, which surfaced as `_DB_PATH` being
`None` on first attempt). With `app.main.ollama_client.classify` mocked
via `unittest.mock.patch`, the full `POST /tickets` → `GET /search` →
`GET /stats` path was exercised end-to-end, confirming categories
persist, search matches on substring, and `/stats` always reports all 7
categories (zero-filled) even against an empty database. `docker compose
config` validated the compose file's structure separately, since it
doesn't need the daemon running.

## See also

- [[resources/ollama-local-inference]] — the OpenAI-compatible
  `/api/generate` endpoint used here instead of the `/v1/chat/completions`
  shim, since the raw Ollama API gives direct access to `options.temperature`.
- [[concepts/docker-compose]] — the two-service pattern (app + local
  inference backend) used here follows the same build-context and
  bind-mount conventions documented there.
- [[concepts/workload-identification]] and [[concepts/performance-metrics]]
  — the concepts this assignment's Steps 3-4 (not yet built) will apply to
  size the load tests against.
