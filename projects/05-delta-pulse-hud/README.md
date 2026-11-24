# delta-pulse-hud

Replay filters 50 fictional ticks to two alerts and applies a per-ticker cooldown. No live market feed, YAML configuration or trading functionality is connected. Output is illustrative, not investment advice.

Run from the repository root after installing the core:

```sh
python projects/05-delta-pulse-hud/simulate_options_tape.py
```

Example frame from the replay:

```text
+----------------------------------+
| NVDA 145C 11/28 [SWEEP]          |
| VOL/OI: 4.8x | DELTA: 0.38       |
| ASK: $2.45 | IVR: 42%            |
+----------------------------------+
```
