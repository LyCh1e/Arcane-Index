---
type: concept
status: established
created: 2026-07-24
updated: 2026-10-21
name: customtkinter-widget-scaling
description: CTk's built-in set_widget_scaling() live-rescales every constructed CTkFont and widget dimension without a rebuild — the cheap alternative to the colour-rebind-and-rebuild pattern, useful for user-facing font-size / accessibility-zoom settings.
metadata:
  type: concept
---

# CustomTkinter Widget Scaling

## The Problem

CustomTkinter widgets hard-code font sizes at construction time
(`ctk.CTkFont(family="Segoe UI", size=14)`), scattered across every panel. A
"font size" or accessibility-zoom setting that needs to touch **all** of them
looks, at first glance, like it needs the same architecture as colour theming:
push a new value into every module's frozen constants, then rebuild the whole
window from scratch (see [[customtkinter-window-lifecycle]] for why colour
theming needs that).

Font size doesn't need that heavy machinery — CTk already ships a mechanism
built for exactly this.

## The Fix: `set_widget_scaling`

CustomTkinter's `ScalingTracker` registers every `CTkFont` and every widget
instance as it's constructed. Calling `ctk.set_widget_scaling(factor)`
iterates that registry and rescales each one **live**, in place — no
destroy/rebuild, no per-module rebinding:

```python
import customtkinter as ctk

DEFAULT_FONT_SIZE = 14   # baseline the app's font sizes were authored against

def apply_font_size(size: int) -> None:
    ctk.set_widget_scaling(size / DEFAULT_FONT_SIZE)
```

Call it once and every already-on-screen label, button, and entry resizes its
text immediately — including widgets built before the call. A `1.0` factor is
a no-op; `size / DEFAULT_FONT_SIZE` gives a scale relative to whatever base
size the UI was designed around (not necessarily 1.0 if most labels use a
non-default size).

## Contrast with Colour Theming

| | Colour theme | Font size |
|---|---|---|
| Storage | frozen module constants, bound by value at import | nothing to freeze — CTk tracks widgets itself |
| Change mechanism | rebind every module's constants, **then rebuild the window** | call `set_widget_scaling()` |
| Needs a window rebuild? | Yes — see [[customtkinter-window-lifecycle]] | No — live |
| Persistence pattern | still identical: save the raw preference, re-apply on next login/relaunch | same |

Both still need re-applying on every fresh window (login, re-login as a
different user, or any relaunch) because scaling is a **process-global** CTk
setting, not attached to the destroyed/rebuilt window — but that's a single
function call at each entry point, not a colour-style rebuild.

## Gotchas

- **Range matters for readability.** Don't let scaling run unbounded — clamp
  to a sane min/max (e.g. the app's default size up to a hard cap) so text
  doesn't overflow fixed-width containers.
- **`set_widget_scaling` is global, not per-window.** If the app ever opens
  two `CTk` roots at once, both will scale together — there is no per-window
  override.
- **`place(x=, y=)` coordinates scale with *widget* scaling, not window scaling.**
  `ctk.ScalingTracker.get_widget_scaling(widget)` is what CTk applies to `place()`
  positions and widget sizes (DPI × the UI-size setting). `get_window_scaling`
  stays at 1.0 when only `set_widget_scaling` is used. A pop-up menu positioned
  from `winfo_rootx()/winfo_width()` divided by the *window* factor lands in the
  wrong spot (and clips at the right edge) at any size other than 100 % — divide
  by the widget factor instead. Learnix's view-menu bug; see
  [[examples/learnix-hci-caching-and-loading-session]].
- **Fixed-width controls crowd shared rows.** Widget scaling multiplies every
  hard-coded `width=`/`height=` too, but the window (and `minsize`) does not
  grow with it. A row mixing an expanding `CTkTextbox` with fixed-width
  pickers/buttons has the textbox absorb all the loss: Learnix's chat input went
  518px -> 186px at 1300px wide / font 20, and 37px (send/attach pushed off the
  window, unclickable) at the 960x640 minimum. Put the fixed-width controls on
  their own row, and re-stack them from a deferred (`after_idle`) `<Configure>`
  handler when `winfo_reqwidth()` sums exceed the bar width — measuring inside
  the event reads pre-rescale widths.
- Test method that worked: launch the real window headless-ish, loop over
  window sizes x font sizes, and flag clickable widgets whose rect leaves the
  toplevel/parent or whose input width collapses. Geometry only — `ImageGrab`
  captures the user's whole desktop, not just the app.
- Distinguish from `ctk.set_window_scaling()`, which scales window geometry
  (DPI), not font/widget size — the two are independent knobs.

## When to Reach for This

Any user-facing "text size" / accessibility zoom preference in a CustomTkinter
app. Don't reinvent the colour-theme rebuild pattern for something CTk already
solved natively.

**See also**: [[customtkinter-window-lifecycle]] for the *other* live-update
problem (colour theming) that genuinely does need a rebuild, and why.
