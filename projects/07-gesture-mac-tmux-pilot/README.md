# gesture-mac-tmux-pilot

Mock pane cycling and an allowlist of proposed macros. No tmux inspection, gesture hardware, confirmation mechanism or command dispatch is connected.

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
