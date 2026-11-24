# voice-mcp-field-ops

A mocked rack health card and bounded checklist with a small static pinout lookup. The replay uses mock data; microphone input and electrical verification are not provided; verify pinouts against authoritative device documentation before use.

Run from the repository root after installing the core:

```sh
python projects/04-voice-mcp-field-ops/simulate_rack_debug.py
```

Example frame from the replay:

```text
+----------------------------------+
| [RACK-02] k3s-worker-01          |
| CPU: 78% | MEM: 29.4/32G         |
| PODS: 41/42 (1 CrashLoop)        |
+----------------------------------+
```

`mcp_providers/docker_health.py` can list local Docker containers using the Docker CLI. The pinout lookup is reference material requiring device-specific verification.

`mcp_server.py` exposes read-only pinout and local Docker listing through MCP stdio.
