---
name: customtkinter-window-lifecycle
description: Correct CTk window teardown pattern — quit()+cancel_afters()+destroy() with bgerror override; covers sequential multi-window flows and CTk subclass overrides.
metadata:
  type: concept
---

# CustomTkinter Window Lifecycle

## The Problem with `destroy()`

`CTk.__init__` registers Tcl `after` timers for DPI scaling (`check_dpi_scaling`) and widget repaints (`update`). These fire periodically for the lifetime of the window. Calling `destroy()` directly deletes the associated Tcl command objects **before** the pending timer events fire, producing `invalid command name` errors.

## Correct Teardown: Three Steps

```
mainloop() → quit() → cancel_all_afters() → destroy()
```

### Step 1 — Stop the event loop with `quit()`

Call `quit()` from inside the running mainloop (e.g. on successful login). This exits `mainloop()` cleanly without touching the widget tree.

```python
# Correct: stop the loop without destroying
self._root.quit()

# Wrong: destroys mid-mainloop while timers are still pending
self._root.destroy()
```

### Step 2 — Cancel all pending `after` IDs

After `mainloop()` returns, the Tcl event queue still holds pending timer events. Cancel them all before destroying:

```python
try:
    for after_id in self._root.tk.call("after", "info").split():
        try:
            self._root.after_cancel(after_id)
        except Exception:
            pass
except Exception:
    pass
```

`after info` (Tcl command, no argument) returns all pending after IDs. `after_cancel` takes a Tcl-native ID (`after#N`).

### Step 3 — Destroy after the queue is clean

```python
try:
    self._root.destroy()
except Exception:
    pass
```

## Suppress Race-Condition Residuals with `bgerror`

Background threads (e.g. an LLM query thread) may schedule `after(0, lambda...)` **after** the cancel loop runs. Override Tcl's global error handler to silently swallow these harmless teardown errors:

```python
self._root.tk.eval("""
    proc bgerror {msg} {
        if {[string match "*invalid command name*" $msg] ||
            [string match "*application has been destroyed*" $msg]} { return }
        puts stderr "Tcl background error: $msg"
    }
""")
```

Install this in `__init__` before `mainloop()` is ever called.

## Complete Pattern: Plain `CTk()` (e.g. AuthWindow)

```python
class AuthWindow:
    def __init__(self):
        self._root = ctk.CTk()
        # Suppress teardown noise
        self._root.tk.eval("""
            proc bgerror {msg} {
                if {[string match "*invalid command name*" $msg] ||
                    [string match "*application has been destroyed*" $msg]} { return }
                puts stderr "Tcl background error: $msg"
            }
        """)
        self._root.protocol("WM_DELETE_WINDOW", self._on_close)

    def run(self) -> dict | None:
        self._root.mainloop()
        # Cancel remaining after IDs
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
        return self._result

    def _on_success(self):
        self._result = ...
        self._root.quit()          # stops loop; run() will clean up

    def _on_close(self):
        self._result = None
        self._root.quit()
```

## Complete Pattern: `CTk` Subclass (e.g. Main App)

Override `destroy()` to cancel before calling super:

```python
class LearnixApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tk.eval("""
            proc bgerror {msg} {
                if {[string match "*invalid command name*" $msg] ||
                    [string match "*application has been destroyed*" $msg]} { return }
                puts stderr "Tcl background error: $msg"
            }
        """)

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

## Sequential Multi-Window Flows

When an auth window is followed by a main app window (two sequential `CTk` roots), the auth window must be **fully destroyed** before the next root is created:

```python
# main.py
auth = AuthWindow()
user = auth.run()        # internally: mainloop → quit → cancel_afters → destroy
if user is None:
    sys.exit(0)
app = LearnixApp(user=user)   # fresh Tcl interpreter; no cross-contamination
app.mainloop()
```

Do NOT share a root between windows or create the second window before the first is destroyed.

## `after info` vs Tkinter after IDs

| Thing | Format | Example |
|-------|--------|---------|
| Tcl after ID (from `after info`) | `after#N` | `after#42` |
| Tkinter command name (from `_register`) | `{id(func)}{func.__name__}` | `2065148414784check_dpi_scalingcallit` |

`after_cancel` takes the Tcl after ID, not the command name. The command name appears in error messages; the after ID is what you cancel.

## When This Matters

- Any `ctk.CTk()` or `ctk.CTkToplevel()` window that is destroyed while timers are still running.
- Especially common in flows where the window is closed programmatically (login success, logout, navigation).
- The `bgerror` layer is specifically needed when background threads (network, LLM, file I/O) may schedule `after()` callbacks during or after teardown.

**See also**: [[learning/customtkinter-after-teardown]] for the bug discovery context on the Learnix project.
