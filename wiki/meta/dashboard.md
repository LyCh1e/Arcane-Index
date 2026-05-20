---
type: meta
title: "Dashboard"
updated: 2026-05-21
tags: [meta, dashboard]
---

# Wiki Dashboard

## Recent Activity

```dataview
TABLE type, status, updated FROM "wiki" SORT updated DESC LIMIT 15
```

## Seed Pages (Need Development)

```dataview
LIST FROM "wiki" WHERE status = "seed" SORT updated ASC
```

## Entities Missing Sources

```dataview
LIST FROM "wiki/entities" WHERE !sources OR length(sources) = 0
```

## Open Questions

```dataview
LIST FROM "wiki/questions" WHERE answer_quality = "draft" SORT created DESC
```

## Active Learning Notes

```dataview
TABLE module, skill, status FROM "wiki/learning" WHERE status = "active" SORT updated DESC
```

## Concepts by Domain

```dataview
TABLE domain, complexity FROM "wiki/concepts" SORT domain ASC
```
