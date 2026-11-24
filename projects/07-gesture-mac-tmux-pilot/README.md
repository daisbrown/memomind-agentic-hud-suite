# gesture-mac-tmux-pilot

Mock pane cycling and an allowlist of proposed macros. The replay is mocked; separate local tmux inspection and explicitly confirmed macro dispatch are available. Gesture hardware is not connected.

Run from the repository root after installing the core:

```sh
python projects/07-gesture-mac-tmux-pilot/simulate_tmux_cluster.py
```

Example frame from the replay:

```text
+----------------------------------+
| [TMUX 1/4] claude [OK]           |
| Waiting                          |
| TAP: Next | HOLD: Confirm        |
+----------------------------------+
```

`pane_watcher.py` reads local tmux panes. `gesture_macro_router.py` accepts only allowlisted commands and requires explicit caller confirmation. It sends text and Enter to the selected pane, so inspect any existing input first.

`tmux_cli.py` lists panes or asks for explicit typed confirmation before dispatching an allowlisted macro.
