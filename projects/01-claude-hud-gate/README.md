# Claude HUD Gate — first simulation

A deterministic replay of a coding-agent approval display. It never executes commands or grants permissions. Risk classification is a heuristic, not a security boundary. Real device approval and an agent permission hook remain to be built.

```text
+----------------------------------+
| [GATE: HIGH] db/migrate_04.sql   |
| DROP idx_users_email (LOCK)      |
| TAP: Approve | HOLD: Reject      |
+----------------------------------+
```

From the repository root: `python projects/01-claude-hud-gate/demo_claude_session.py` after installing the package as described in the root README.

The optional local wrapper runs a command only after explicit terminal confirmation: `python projects/01-claude-hud-gate/cli_wrapper.py -- echo hello`. This is not an agent permission hook or a security sandbox.

`mcp_server.py` provides a stdio risk review tool. It never approves commands; the result explicitly reports approval unavailable.
