# moto-hud-copilot

The replay demonstrates a dark idle display, turn pre-alert and a higher-priority low-pressure warning. Thresholds and route data are illustrative; a separate GPX waypoint parser is included, but no vehicle, GPS navigation, voice, or hardware connection exists. This is not a validated riding aid and must not be relied on while riding.

Run from the repository root after installing the core:

```sh
python projects/02-moto-hud-copilot/simulate_ride.py
```

Example frame from the replay:

```text
+----------------------------------+
|                                  |
|                                  |
|                                  |
+----------------------------------+
```

`obd_watchdog.py` checks caller-supplied values against illustrative thresholds. Missing readings are not treated as proof of vehicle health.

`obd_adapter.py` can read supported standard PIDs through python-OBD. TPMS is not a standard PID and is not implemented. `nav_distance.py` computes straight-line distance, not driving directions.
