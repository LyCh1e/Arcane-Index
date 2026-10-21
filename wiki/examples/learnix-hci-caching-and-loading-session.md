---
type: example
status: established
created: 2026-10-21
name: learnix-hci-caching-and-loading-session
description: Learnix (SE-24) — one session of UI work: chat shortcuts, stop-generation and copy, selectable messages, WCAG contrast and tooltips, a view-menu scaling bug, a stale-while-revalidate cache for the web frontend, a faster token-usage query, and one shared loading indicator (including the startup splash).
metadata:
  type: example
---

# Learnix: HCI pass, client caching and loading improvements

Done on `develop` (uncommitted at the time of writing). Full log in the repo's `cy-documentation.md`. Verified headlessly (real Tk event loop, a screenshot of the splash, Node tests, 448 desktop tests), **not** by clicking through the running app.

## 1. Chat controls (desktop, `ui/panels/chat_panel.py`)

- **Shortcuts**: Ctrl+N new chat, Ctrl+L focus input, Esc stop, Ctrl+Shift+C copy latest reply; ignored when a dialog has focus.
- **Stop generation**: the send button becomes a red **■** while a reply is generating. The LLM call cannot be cancelled, so a request counter (`_gen_id`) makes the worker discard a late reply; a "(Response stopped.)" turn is stored so user/assistant turns keep alternating.
- **Copy**: a "⧉ Copy" button per message; messages became read-only `CTkTextbox`es so text can be highlighted (Ctrl+C, Ctrl+A, right-click Copy). Textbox height is computed by word-wrapping with the same font instead of forcing a layout pass per message, which keeps long histories fast.

## 2. Accessibility (WCAG 2.1 AA)

- Computed contrast per text/background pair in both themes; muted text was as low as **2.2:1**. Adjusted values with a script until each reached 4.5:1; white on the dark-theme blue was **2.1:1**, so a new `ON_BLUE` colour was added for text on blue fills.
- 10–11 px fonts → 12 px; a reusable `Tooltip` / `with_tip` for icon-only buttons.
- Not addressed: Tab navigation of CTk buttons (they don't take focus), screen readers (Tk exposes nothing).

## 3. View-menu misalignment

At any UI size other than 100 % the drop-down was clipped. Cause: placement used CTk **window** scaling but `place()` multiplies by **widget** scaling, and the font-size setting changes only the latter. See [[concepts/customtkinter-widget-scaling]] (new gotcha). Verified headless at 0.8×–1.43×.

## 4. Web cache (React frontend)

[[concepts/stale-while-revalidate-client-cache]]: Map + IndexedDB, per-user scope set synchronously with auth state, wipe on logout, invalidation on mutations; Node-tested with [[resources/fake-indexeddb]].

## 5. Loading: thought process

1. **Measure before deciding** (faster, or an indicator?). Timing the real call showed 13.8 s for 583 records, so the cost was round trips.
2. **Fix the cause**: [[learning/n-plus-one-remote-queries-token-usage]] — 13.8 s → 3.4 s cold, ≈1.5 s warm, identical output.
3. **Also fix the perception**: the token page shows the last data at once with a small "Refreshing…" and repaints only if the data changed; the first visit shows a full indicator. A request counter makes the newest refresh win.
4. **One shared widget** (`ui/loading_indicator.py`): label + indeterminate `CTkProgressBar`; replaced ad-hoc "Loading…" labels on My Dashboard and the admin pages. `destroy()` stops the bar's animation first.
5. **Startup splash**: the canvas-drawn pulsing bar was replaced by the same indeterminate bar hosted on the canvas (fixed blue on navy, so it works in both themes). Status text still updates; progress fractions are no longer drawn.

Testing note: background-thread results reach Tk only while the real `mainloop` runs, so a test using `update()` in a loop never sees them — drive the test with `after()` callbacks inside `mainloop()`.

## 6. Type-checker clean-up

[[learning/mixin-type-checking-pylance]].

## Left open

Login/register screens still show only text while waiting; FAQ and some small admin status labels too; the font bump may crowd fixed-width layouts; an admin-dashboard screenshot showed overlapping repeated text that was not investigated.
