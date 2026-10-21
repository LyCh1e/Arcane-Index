---
type: concept
status: established
created: 2026-10-21
updated: 2026-10-21
name: stale-while-revalidate-client-cache
description: Stale-while-revalidate client cache — show the last known data instantly, refresh behind it, and fall back to it on failure; built as an in-memory Map in front of IndexedDB, scoped per user and wiped on logout (Learnix React frontend).
metadata:
  type: concept
---

# Stale-While-Revalidate Client Cache

## The problem

A page that fetches on every visit shows nothing until the network answers. For data the user has already seen (a chat list, past messages, a usage dashboard) the wait is mostly wasted: the old copy is almost always still right.

## The pattern

1. Look in the cache. If there is a copy, **show it immediately**.
2. **Always fetch** in the background.
3. On success, store the fresh result and replace what is on screen.
4. On failure, **if a cached copy was shown, keep it** (return it, don't throw). With nothing cached, surface the error as usual.

```js
export async function cachedFetch(key, fetcher, { onCached } = {}) {
  const cached = await getEntry(key);
  if (cached) onCached?.(cached.data, cached.ts);
  try {
    const fresh = await fetcher();
    await setEntry(key, fresh);
    return fresh;
  } catch (err) {
    if (cached) return cached.data;
    throw err;
  }
}
```

The caller passes `onCached: setState` for the instant paint and `.then(setState)` for the refresh.

## Two tiers

| Tier | Role |
|------|------|
| In-memory `Map` | Instant reads within a page session |
| IndexedDB | Survives reloads; read once, then hydrated into the Map |

IndexedDB can be missing or blocked (private windows, storage disabled, old browsers), so **every IDB call must degrade silently to memory-only**: wrap the open, each transaction, and resolve to `undefined` on any error. The page must work with the cache absent.

## Rules that are easy to get wrong

- **Scope by user.** Key every entry `"<userId>|<key>"`. On a shared browser a cache without scope shows one learner another's chats. Set the scope **synchronously** with the auth-state change, not in a `useEffect`: child components mounting in the same render run their effects *before* the parent's, so an effect-based scope is still `null` when the child first reads the cache.
- **Wipe on sign-out, expiry, or a different user.** Privacy beats offline convenience; this also wipes after a transient failure of the startup auth check.
- **Invalidate on mutation.** Creating, deleting, sending a message or uploading a file removes the entries it makes stale (`removeEntry`); the refetch that follows repopulates them.
- **Guard against out-of-order results.** A cached paint for chat A can arrive after the user clicked chat B. Keep an "active id" ref and ignore results for any other id.
- **Expire.** Store a timestamp; drop entries older than a fixed age (7 days in Learnix) on read and with a startup prune.
- **Cross-tab:** a plain Map + IDB does not sync tabs; each tab shows its own copy until its next refresh. Accepted trade-off.

## Applying the same idea in a desktop GUI

The same shape works without a browser: keep the last result in a dict keyed by account, render it at once on page entry, fetch in a worker thread, and **repaint only if the new data differs**. A request counter makes the newest refresh win so overlapping refreshes cannot overwrite newer data. See [[examples/learnix-hci-caching-and-loading-session]] (token usage page).

## Testing without a browser

Node has no IndexedDB. `fake-indexeddb` supplies one for a throwaway test (see [[resources/fake-indexeddb]]); also run the same test with no IndexedDB at all to prove the memory-only fallback.

**See also**: [[learning/n-plus-one-remote-queries-token-usage]] (making the fetch itself faster).
