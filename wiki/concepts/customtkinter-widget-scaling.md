---
type: concept
status: established
created: 2026-07-24
updated: 2026-07-24
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
- Distinguish from `ctk.set_window_scaling()`, which scales window geometry
  (DPI), not font/widget size — the two are independent knobs.

## When to Reach for This

Any user-facing "text size" / accessibility zoom preference in a CustomTkinter
app. Don't reinvent the colour-theme rebuild pattern for something CTk already
solved natively.

**See also**: [[customtkinter-window-lifecycle]] for the *other* live-update
problem (colour theming) that genuinely does need a rebuild, and why.
