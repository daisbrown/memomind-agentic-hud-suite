# moa-sentinel-hud

A deterministic replay for quiet operation, heartbeat timeout and batch completion. A synchronous execution-observer decorator is included. Live heartbeat ingestion, async tracking, throughput tracking and the FastAPI bridge remain future work.

Run from the repository root after installing the core:

```sh
python projects/03-moa-sentinel-hud/simulate_moa_batch.py
```

Example frame from the replay:

```text
+----------------------------------+
|                                  |
|                                  |
|                                  |
+----------------------------------+
```

`stall_detector.py` evaluates supplied heartbeat timestamps and pass counts.
