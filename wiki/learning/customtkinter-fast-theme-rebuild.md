---
type: learning
status: established
created: 2026-11-03
updated: 2026-11-03
name: customtkinter-fast-theme-rebuild
description: Lesson — a slow CustomTkinter theme switch was repeated startup, not recolouring. Rebuild widgets inside the open window, destroy subtrees top-down (list children first or widgets leak), suppress nested layout flushes, and measure before optimising.
metadata:
  type: feedback
---

# CustomTkinter: fast theme switch by rebuilding widgets in place (Learnix)

**Symptom:** UAT reported that changing theme took too long. Measured at about 16.5s; now about 1.6s from Settings.

**Root cause:** the theme change destroyed the window and built a new `LearnixApp`, which repeated all startup work behind the splash (14s). Building the widgets took only about 0.8s. Measure first: the obvious suspect, recolouring, was not the cost.

**Fix pattern** (`src/ui/chat_ui.py`, `_rebuild_widgets_for_theme`):
- Keep the root window and long-lived state (retriever, sessions, threads). Destroy the children, push the palette into the panel modules, build again, restore the page.
- Threads calling `self.after(...)` keep working because the root survives, so in-flight replies still arrive.
- Reset every attribute panels test with `hasattr`, or they will touch dead widgets.
- `unbind_all` the five sequences `CTkScrollableFrame` adds, or they pile up per rebuild.

**Speed-ups, by measured cost:**
- `self.tk.call("destroy", body)` removes a subtree top-down in one call. Tkinter's `destroy()` goes bottom-up, and each removal re-lays out the parent (2.75s down to 0.35s for about 3,000 widgets).
- Run the first `update()` inside the flush suppression. CTk's redraws otherwise force nested window-wide layouts.
- Hide that first layout behind a plain `tk.Frame`, because it paints piece by piece.
- Hold back CTk's Windows title bar hide/show with `_deactivate_windows_window_header_manipulation`, and run it once at the end.

**Trap:** take `winfo_children()` *before* the Tk-level destroy. Afterwards Tk no longer lists the subtree, so its Python `destroy()` never runs. Widgets stay in CTk's trackers, their timers keep firing, and the timings look better than they really are. Check the tracker for dead widgets.

**Testing trap:** worker threads need a running `mainloop`, so a probe that polls with `update()` breaks them. Drive the probe with a generator stepped by `after()`. `update()` during a rebuild also re-enters the event loop, so a probe can read state mid-rebuild.

Related: [[learning/customtkinter-subclass-method-collision]], [[learning/customtkinter-scaling-clipped-window]], [[learning/customtkinter-after-teardown]].
