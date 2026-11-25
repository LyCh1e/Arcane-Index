---
type: learning
status: established
created: 2026-05-22
updated: 2026-05-22
name: customtkinter-after-teardown
description: Bug lesson — CustomTkinter 5.x fires 'invalid command name' Tcl errors on window destroy because internal after() callbacks aren't cancelled; three-layer fix.
metadata:
  type: feedback
---

# CustomTkinter: `invalid command name` on Window Teardown

**Project context**: Learnix (ICT2114 ITP), `src/ui/auth_ui.py` and `src/ui/chat_ui.py`.
**CustomTkinter version**: 5.2.2.

## The Symptom

Console noise on every app close:

```
invalid command name "2065148414784check_dpi_scaling"
    while executing "2065148414784check_dpi_scaling" ("after" script)
invalid command name "2065148359488update"
    while executing "2065148359488update" ("after" script)
invalid command name "1734416686912<lambda>"
    Error in bgerror: can't invoke "tk" command: application has been destroyed
```

## Root Cause

CustomTkinter's `CTk.__init__` registers two recurring Tcl `after` timers: `check_dpi_scaling` (DPI monitor) and `update` (widget repaint). These timer IDs are stored internally as Tcl command names formatted as `{id(func)}{func_name}`.

When `CTk.destroy()` is called directly, Tkinter deletes all registered Python-callable Tcl commands **before** the pending `after` events fire. When those events eventually fire, Tcl can't find the command and raises `invalid command name`. The final `bgerror` line happens because the Tk error handler itself also can't run — the interpreter is already being torn down.

The `<lambda>` variant is a race condition: a background thread (e.g. the RAG/LLM `_query` thread) may call `self.after(0, lambda: ...)` **after** `destroy()` has already cancelled the currently-queued IDs but before the interpreter is fully gone.

## The Three-Layer Fix

### Layer 1 — Use `quit()` not `destroy()` in callbacks

`quit()` stops the mainloop but leaves the window alive. `destroy()` is then called **after** `mainloop()` returns, so there's no re-entrant teardown.

```python
# auth_ui.py — wrong
def _on_login_result(self, result):
    if result["ok"]:
        self._root.destroy()          # destroys mid-mainloop → timers still pending

# auth_ui.py — correct
def _on_login_result(self, result):
    if result["ok"]:
        self._user = result["user"]
        self._root.quit()             # stops mainloop; window still alive
```

```python
def run(self) -> dict | None:
    self._root.mainloop()             # returns after quit()
    # … now safe to cancel and destroy
```

### Layer 2 — Cancel all pending `after` IDs before `destroy()`

`after info` (no argument) returns all Tcl-level pending after IDs. Cancel them before the widget tree is torn down.

```python
def run(self) -> dict | None:
    self._root.mainloop()
    try:
        for after_id in self._root.tk.call("after", "info").split():
            try:
                self._root.after_cancel(after_id)
            except Exception:
                pass
    except Exception:
        pass
    try:
        self._root.destroy()
    except Exception:
        pass
    return self._user
```

For a `CTk` subclass (`LearnixApp extends ctk.CTk`), override `destroy()`:

```python
def destroy(self):
    try:
        for after_id in self.tk.call("after", "info").split():
            try:
                self.after_cancel(after_id)
            except Exception:
                pass
    except Exception:
        pass
    super().destroy()
```

### Layer 3 — Override Tcl `bgerror` for residual race noise

Background threads can schedule `after(0, lambda...)` **after** the cancel loop has already run. Redefine Tcl's `bgerror` procedure to silently drop these harmless teardown errors while still surfacing real errors:

```python
# In CTk __init__ (or AuthWindow.__init__)
try:
    self._root.tk.eval("""
        proc bgerror {msg} {
            if {[string match "*invalid command name*" $msg] ||
                [string match "*application has been destroyed*" $msg]} { return }
            puts stderr "Tcl background error: $msg"
        }
    """)
except Exception:
    pass
```

## Key Facts

- `after info` returns Tcl-native IDs (`after#N`), NOT the Tkinter command name strings like `2065...check_dpi_scaling`.
- `after_cancel(after_id)` cancels the Tcl event; this also prevents the associated Python command from being invoked.
- `bgerror` is Tcl's global background-error handler — redefining it is the standard Tcl idiom for suppressing noisy-but-harmless async errors.
- This pattern applies to **any** CTk window, not just auth flows.

## Why: `application has been destroyed`

This specific message means the Tk **interpreter** is gone. It appears when a background thread calls `widget.after(...)` on a widget whose root has been fully destroyed. The `bgerror` override in Layer 3 handles this because even the Tk error machinery has been torn down by then.

## File Refactor Note (same session)

When moving Python files into subdirectories (`src/auth_ui.py` → `src/ui/auth_ui.py`):

1. `sys.path.insert(0, str(Path(__file__).resolve().parent))` must become `.parent.parent` so it still points to `src/`.
2. `load_dotenv(Path(__file__).resolve().parent / ".env")` must similarly become `.parent.parent / ".env"`.
3. Any lazy `from auth_ui import X` inside methods must be updated to `from ui.auth_ui import X`.

**Why:** `Path(__file__).resolve().parent` resolves to the *directory containing the file*, which changes when the file moves. Always trace every `Path(__file__)` reference after a move.
