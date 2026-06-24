---
type: meta
title: "Dashboard"
updated: 2026-06-25
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

## Research Syntheses

```dataview
TABLE status, updated FROM "wiki/synthesis" WHERE contains(file.name, "research-") SORT updated DESC
```

## Pages Missing Address (DragonScale)

```dataview
LIST FROM "wiki" WHERE !address AND type != "meta" AND type != "index" SORT created DESC LIMIT 20
```

## Active Learning Notes

```dataview
TABLE module, skill, status FROM "wiki/learning" WHERE status = "active" SORT updated DESC
```

## Concepts by Domain

```dataview
TABLE domain, complexity FROM "wiki/concepts" SORT domain ASC
```
