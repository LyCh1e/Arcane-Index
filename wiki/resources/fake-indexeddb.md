---
type: resource
status: established
created: 2026-10-21
updated: 2026-10-21
name: fake-indexeddb
description: fake-indexeddb — a pure-JS IndexedDB implementation for Node, used to test browser cache code without a browser; plus the Node ESM and Windows quirks hit while doing it.
metadata:
  type: resource
---

# fake-indexeddb

An in-memory implementation of the IndexedDB API for Node. Importing `fake-indexeddb/auto` defines the global `indexedDB`, so browser storage code runs unchanged in a Node script.

## Use

```bash
npm i --no-save fake-indexeddb      # --no-save: keep package.json clean for a throwaway test
node _t.mjs idb                     # with fake IndexedDB
node _t.mjs mem                     # without it: proves the memory-only fallback
```

```js
if (mode === "idb") await import("fake-indexeddb/auto");
```

Run the **same** assertions both ways: cache hit/miss, stale-then-fresh callback, fallback on fetch error, removal, wipe on sign-out, cross-user isolation (persistence only in the `idb` run).

## Gotchas hit

- **Vite code imports without extensions** (`from "./store"`); Node's ESM loader requires `./store.js`. Test against a temp copy with the extensions added (and a `package.json` with `"type": "module"`), then delete it.
- **Windows absolute paths** can't be passed to `import()` (`Received protocol 'c:'`); use relative paths or `file://` URLs.
- A project with no test framework has nowhere to keep such a test; if it should persist, add Vitest.

Used for [[concepts/stale-while-revalidate-client-cache]] in [[examples/learnix-hci-caching-and-loading-session]].
