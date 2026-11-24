# Claude HUD Gate — first simulation

A deterministic replay of a coding-agent approval display. It never executes commands or grants permissions. Risk classification is a heuristic, not a security boundary. The MCP server, real approval flow and CLI hook remain to be built.

```text
+----------------------------------+
| [GATE: HIGH] db/migrate_04.sql   |
| DROP idx_users_email (LOCK)      |
| TAP: Approve | HOLD: Reject      |
+----------------------------------+
```

From the repository root: `python projects/01-claude-hud-gate/demo_claude_session.py` after installing the package as described in the root README.
