---
type: reference
title: Tutor Agent — Published Quiz Artifact Links
tags: [tutor, artifacts, links]
---

# Tutor Agent — Published Quiz Artefact Links

These are the three permanent, hosted quiz pages (published via the Artifact tool on claude.ai) that the tutor agent rebuilds and republishes in place every time it runs. They are the **only** place the daily reading + quiz content lives — no Markdown or HTML file is written to the vault for it any more.

Each link is a persistent URL: republishing to the same URL updates the page's content without creating a new artifact or changing the link. Bookmark these three on your phone's home screen for one-tap access — the bookmarks never need to change, only the content behind them does.

| Module | Artefact URL |
|---|---|
| ICT3112 | https://claude.ai/artifact/8CuL27NdrZqYRu1qBG9rJV |
| ICT3113 | https://claude.ai/artifact/VC19BXRWz158dszEdJ79G1 |
| INF2005 | https://claude.ai/artifact/Ar7Qj3yH2fua71nW2rXuUv |

## How the tutor agent uses this file

Each run, for each module, the tutor agent builds the day's reading + 20-question quiz content fresh (see `agents/tutor.md`) and republishes it to the matching URL above, passing `url=<the link above for that module>` so the same link is updated rather than a new artifact being created. `icon` and `title` are omitted on every republish (only set on first publish) so the artefact keeps its identity.

If a publish ever returns a different URL than the one listed here (for example, if an artefact was deleted), replace the affected row above with the new URL so future runs update the correct page.

See also `agents/tutor-topic-history.md`, which tracks recently-covered subtopics per module so the rotation logic still works without local daily files to scan.

Last published: 2026-09-27.
