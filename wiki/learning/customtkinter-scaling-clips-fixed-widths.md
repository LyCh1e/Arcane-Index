---
type: learning
status: established
created: 2026-11-10
updated: 2026-11-10
name: customtkinter-scaling-clips-fixed-widths
description: Bug lesson — CTk multiplies every width and wraplength by the widget scale, so fixed 680-unit text blocks and one-row button groups run off the window at large font sizes; cap them to the container's real width.
metadata:
  type: feedback
---

# CustomTkinter: fixed widths and wraplengths clip under a large font size (Learnix)

**Symptom.** With Learnix's Font Size setting at 20 (widget scaling 1.43), text was cut off at the right edge on the chat, FAQ and scenario pages; the role chips lost their last button; the user avatar and "Sign Out" were pushed off-screen. Buttons themselves scaled fine.

**Root cause.** `ctk.set_widget_scaling()` multiplies *every* size given in CTk units: fonts, button sizes, and also `wraplength=680` and `CTkTextbox(width=680)`. 680 units is 970 px at 1.43, wider than the 870 px chat area. The content was written for scale 1.0, and nothing shrinks it when the scale grows or the window narrows.

**Fix (in `src/ui/utils.py`).**
- `fit_width(container, max_width, margin, share)` returns `min(max_width, container_px / scale - margin)`.
- `wrap_to_width(label, container, max_wrap, margin)` re-applies that as the label's wraplength.
- `flow_layout(frame, widgets, container)` re-grids a row of buttons onto more rows when they do not fit.
- Chat messages are hand-sized textboxes, so `_refit_messages()` recomputes their width and height.
- The top bar drops the account name, then the "Switch view:" lead-in, before it lets a button be clipped.

**Gotchas.**
- The `container` must be a widget whose width follows the window, not its contents. A card with `sticky="ew"` grows to fit an over-wide label, so measuring it never shrinks anything. A `CTkScrollableFrame` works: its inner frame is forced to the canvas width.
- A font-size change does not resize the window, so the container gets no `<Configure>`. Bind the label's (or button row's) own `<Configure>` as well: its size changes on a rescale. Hand-sized widgets need an explicit call after `apply_font_size`.
- Requested sizes only settle after the rescale has laid out, so measure in `after_idle`, not inside the event.
- Divide pixel widths by `ScalingTracker.get_widget_scaling(widget)` (DPI x font setting), not window scaling.

**How to apply.** Any new wrapping label or fixed-width block in a resizable CTk view should go through `wrap_to_width` / `fit_width`. Check new screens at the largest font size and the minimum window size before calling them done.

**Still open (2026-11-10).** The admin Class Overview tiles clip at the smallest window with the largest font. `token_usage_panel.py` binds `<TouchpadScroll>` without a guard, which raises on Tk 8.6.

Related: [[concepts/customtkinter-widget-scaling]], [[learning/customtkinter-scaling-clipped-window]], [[learning/customtkinter-fast-theme-rebuild]].
