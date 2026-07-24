---
type: example
status: established
created: 2026-07-24
name: learnix-fontsize-and-srl-pacing
description: Learnix (SE-24) — added a per-user font-size setting via CTk widget scaling, and slowed Forethought-phase SRL step ticking to require 3 distinct-message keyword mentions instead of 1.
metadata:
  type: example
---

# Learnix: Font-Size Setting + Slower Forethought SRL Pacing

Two small features added to Learnix in one session, on branch
`feature-fontsize-and-LNA-phase`.

## 1. Font-Size Setting (Settings → Appearance)

Added alongside the existing theme picker, following the same
preference-storage shape but a much lighter apply path — see
[[concepts/customtkinter-widget-scaling]] for why font size doesn't need the
colour-theme rebuild machinery.

**`ui/theme.py`** — new constants + the live-apply function:

```python
DEFAULT_FONT_SIZE = 14   # matches the most common body-text size across panels
MAX_FONT_SIZE = 20

def apply_font_size(size: int) -> None:
    import customtkinter as ctk
    ctk.set_widget_scaling(size / DEFAULT_FONT_SIZE)
```

**`ui/panels/settings_panel.py`** — a `CTkOptionMenu` (values `14`..`20`) in
the Appearance card, right under the theme dropdown. On pick: apply
immediately (`apply_font_size(size)`), then persist via the *existing*
generic preference writer:

```python
from db.auth_db import update_user_preference
update_user_preference(email, "font_size", size)   # same fn theme uses
```

`update_user_preference(email, key, value)` does a dot-path Mongo `$set` on
`preferences.<key>` — it's schema-less, so a brand-new preference key needed
zero DB changes.

**Reapplying on every fresh window.** Because `set_widget_scaling` is
process-global (see the concept page), it has to be called again wherever the
theme preference is re-applied: `main.py` (first login) and
`topbar_panel.run_app`'s relaunch loop (theme-change rebuild, or re-login as a
different user with a different saved size).

## 2. Slower Forethought-Phase SRL Ticking

**Problem**: `_detect_srl(text)` returns the *set* of SRL steps whose keyword
group appears anywhere in a message. The chat panel did
`sess["srl_steps"].update(_detect_srl(text))` on every message — so a single
passing mention of a Forethought keyword (e.g. "business need") instantly
ticked that step complete, which overstated how much real planning happened.

**Fix**: gate Forethought-phase steps behind 3 *distinct messages* mentioning
that step's keyword group, while leaving every other phase's steps ticking on
first mention (unchanged).

`ui/constants.py` — derive the gated step set from the existing phase table
instead of hardcoding it a second time:

```python
FORETHOUGHT_STEPS = frozenset(
    next(p["steps"] for p in SRL_PHASES if p["key"] == "forethought")
)
```

`ui/utils.py` — the counting lives in one small helper, called instead of the
old direct `.update()`:

```python
FORETHOUGHT_MENTIONS_REQUIRED = 3

def _register_srl_progress(sess: dict, detected: set[str]) -> set[str]:
    counts = sess.setdefault("srl_mention_counts", {})
    newly_completed = set()
    for step in detected:
        if step in sess["srl_steps"]:
            continue
        if step in FORETHOUGHT_STEPS:
            counts[step] = counts.get(step, 0) + 1
            if counts[step] < FORETHOUGHT_MENTIONS_REQUIRED:
                continue
        newly_completed.add(step)
    sess["srl_steps"].update(newly_completed)
    return newly_completed
```

**Why "once per message" needed no extra bookkeeping**: `_detect_srl` already
collapses a message's keyword hits down to *set membership* — a message that
says "business need" five times still only contributes `{"Task Analysis"}` to
`detected`. So counting `detected` membership per call already IS "once per
message"; no separate dedup was needed.

Call sites in `ui/panels/chat_panel.py` (both user message and assistant
response — steps can complete from either side of the conversation):

```python
_register_srl_progress(sess, _detect_srl(text))       # was: sess["srl_steps"].update(...)
...
_register_srl_progress(sess, _detect_srl(response))    # was: sess["srl_steps"].update(...)
```

**Note on persistence**: `srl_mention_counts` is session-local, not written to
Mongo (only the resulting `srl_steps` list is, unchanged). Reloading a session
from the DB resets counts to zero, but that's harmless — the `if step in
sess["srl_steps"]: continue` guard means already-completed steps never get
re-counted anyway.

## Takeaways

- When a "settings" feature needs to touch every widget app-wide, check
  whether the GUI toolkit already has a live mechanism (CTk's widget scaling)
  before reaching for the heavier rebuild pattern used elsewhere in the same
  codebase (colour theming) — they can look similar from the outside but have
  very different costs.
- A generic `update_user_preference(email, key, value)` (dot-path `$set` on a
  `preferences` sub-document) means new user-facing settings are free on the
  DB side — no migration, no schema change.
- When a "counted once per X" requirement shows up, check whether an existing
  function already collapses to the right granularity (here, `_detect_srl`
  returning a `set` per message) before adding new dedup logic.

**See also**: [[concepts/customtkinter-widget-scaling]],
[[concepts/customtkinter-window-lifecycle]]
