---
type: learning
status: established
created: 2026-11-03
updated: 2026-11-03
name: customtkinter-subclass-method-collision
description: Bug lesson — subclassing a CTk widget and naming a method _draw overrides CTk's internal _draw and crashes the constructor; pure-logic tests miss it, so render the widget. Includes the pattern for a tk.Canvas that follows CTk scaling.
metadata:
  type: feedback
---

# CustomTkinter: a subclass method named `_draw` crashes the constructor (Learnix usage graph)

**Symptom:** `TypeError: UsageChart._draw() got an unexpected keyword argument 'no_color_updates'`, raised from inside `CTkFrame.__init__`. All unit tests and ruff had passed, because they only covered the chart's pure data helpers and never built the widget.

**Root cause:** CTk widgets call their own private methods from `__init__`, and `CTkFrame.__init__` ends with `self._draw(no_color_updates=True)`. Python resolves that to the subclass, so a chart's own `_draw(self)` silently replaces CTk's. Attributes are at risk too: `CTkFrame` already uses `self._canvas`.

**Fix:** use specific names in CTk subclasses (`_draw_plot`, `_plot`, `_axis_font`), and render a new widget at least once before calling it done.

## Pattern: a tk.Canvas that follows CTk scaling

A bare `tk.Canvas` ignores `ctk.set_widget_scaling` (Learnix's font size setting). Host it in a `CTkFrame` subclass instead (`src/ui/usage_chart.py`):

- Size everything through `self._apply_widget_scaling(n)`, including the canvas height.
- Build fonts as `("Segoe UI", -round(self._apply_widget_scaling(12)))`. A negative size means pixels, which is what CTk's own fonts use.
- Override `_set_scaling(self, new_widget_scaling, new_window_scaling)`: call `super()`, reconfigure the canvas height, then redraw.
- Redraw on `<Configure>`, and return early while `winfo_width()` is still 1 (the widget has not been laid out yet).

Related: [[learning/customtkinter-scaling-clipped-window]], [[learning/customtkinter-after-teardown]].
