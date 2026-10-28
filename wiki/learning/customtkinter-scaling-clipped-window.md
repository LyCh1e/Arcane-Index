---
type: learning
status: established
created: 2026-10-28
updated: 2026-10-28
name: customtkinter-scaling-clipped-window
description: Bug lesson — a fixed CTk window size clips content and mis-centres once the UI-size setting or OS DPI scaling is not 100%; size from widget vs window scaling and scroll on overflow.
metadata:
  type: feedback
---

# CustomTkinter: fixed window size clips content under scaling (Learnix sign-in)

**Symptom:** the sign-in window (`geometry("480x620")`) cut off its card on small / scaled screens and looked off-centre. A too-small hit box (`CTkButton(width=20, height=20)`) on "Forgot password?" made the click area smaller than its label.

**Root cause:** CTk has two scale factors. `set_widget_scaling` (used by Learnix's Settings → UI size, on top of OS DPI) scales widget contents; `geometry()` only multiplies width/height by *window* scaling (DPI only) and leaves x/y alone. `winfo_screenwidth/height` are physical pixels. A hard-coded logical size therefore under-sizes the window whenever UI size > 100%, and centring with `(screen - 480)//2` ignores DPI.

**Fix pattern** (`src/ui/auth_ui.py` `_fit_window`):
- Read `ctk.ScalingTracker.get_widget_scaling(root)` and `get_window_scaling(root)`.
- Work in physical px: width = `base * widget_scale`, height = `card.winfo_reqheight() + padding`, capped at ~90% of screen height; centre in physical px.
- Convert to logical only for `root.geometry(f"{px/win_scale}x{px/win_scale}+x+y")`.
- Put screens in ONE persistent `CTkScrollableFrame` and `grid_remove()` its `_scrollbar` unless the card overflows. Don't recreate the scrollable per screen — it adds app-wide `bind_all("<MouseWheel>")` handlers each time.
- Size buttons from text (`CTkFont.measure(text) + padding`), not a tiny fixed width.

Related: [[learning/customtkinter-after-teardown]].
