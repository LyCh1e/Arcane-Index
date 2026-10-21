---
type: learning
status: resolved
created: 2026-10-21
updated: 2026-10-21
name: n-plus-one-remote-queries-token-usage
description: Lesson — a dashboard that took 13.8 s for 583 records was one serial remote query per user; measuring first, then parallelising, projecting fields and skipping empty collections cut it to 3.4 s (1.5 s warm) with identical output.
metadata:
  type: feedback
---

# N+1 serial queries against a remote database

**Project context**: Learnix token-usage page (admin view), MongoDB Atlas, `db/token_usage.py`. Write-up: `cy-documentation.md` in the repo.

## Symptom

The admin Token Usage page "took a while". The request offered two routes (faster, or add a loading indicator). Rather than guess, the real call was timed: `all_usage_summary()` took **13.8 s for 57 users and only 583 records**. That ratio says the cost is round trips, not data volume.

## Root cause

One collection per user, so the code did: list users, then for each user `find({})` **one after another**, each downloading every full document. About 0.18 s per round trip, times one per user, plus a one-off 2.8 s connection. 19 of 44 accounts had no usage collection at all, so those queries returned nothing.

## Fix, in the order it paid off

| Change | Why |
|--------|-----|
| Fetch `list_collection_names()` once; accounts with no collection get an empty summary **locally** | Removes ~45 % of the queries outright |
| Run the remaining reads in a `ThreadPoolExecutor` (cap 12) | `MongoClient` is thread-safe and pools connections; latency overlaps instead of adding |
| Projection: ask only for the six fields the summary reads (`_id: 0`) | Smaller payloads |

Result (real database): **13.8 s → 3.4 s first call, ≈1.5 s repeat**, output byte-for-byte equal to the old code (compared per user).

## Non-obvious details

- The warm run is **not** 12× faster: each new thread may open its own connection the first time, so the first parallel call still pays TLS handshakes. Time a repeat call too.
- The 3.4 s first call includes the one-off connection; the app already connects at startup, so normal use costs about the repeat figure.
- Compare outputs before and after (save the old result to a file) — a performance fix that silently changes numbers is a regression.
- A single aggregate would be faster still, but needs usage in **one** collection instead of one per user; a bigger schema change, left as a follow-up.

## Making waiting visible

Speed alone still leaves a blank page each visit, and some pages are network-bound regardless. So the page also shows the last data immediately and refreshes behind it ([[concepts/stale-while-revalidate-client-cache]]) and uses one shared loading indicator everywhere ([[examples/learnix-hci-caching-and-loading-session]]).
