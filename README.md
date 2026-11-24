# MemoMind Agentic HUD Suite

A simulation-first exploration of compact heads-up displays for agent workflows. The first milestone provides a shared 3-line, 32-character frame budget, priority and expiry handling, a terminal renderer, a coalescing transport wrapper, and a coding-gate replay.

**Status:** early prototype. The 3 × 32 layout, gesture semantics and display capabilities are design assumptions, not verified MemoMind specifications. No glasses, BLE protocol, SDK integration, microphone, real approvals, or claimed latency have been tested. The BLE transport intentionally fails until official integration details are available. This repository does not establish eligibility for any hardware or discount.

```text
Agent replay → formatter → priority / batching → simulator
                                             ↘ SDK adapter (future)
```

## Run

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python projects/01-claude-hud-gate/demo_claude_session.py
pytest
```

The batcher requires its caller to invoke `flush()` after the batching window; it is not an autonomous scheduler. Frames are measured in Python code points, which does not guarantee physical glyph width. The formatter avoids partial tokens but may omit critical content; callers must supply concise, prioritized lines.

## Roadmap

- Implement and validate a genuine approval integration with explicit authorization and fail-closed behavior.
- Develop the six additional projects in the included blueprint, beginning with simulation and safety boundaries.
- Verify display capabilities and SDK transport against official documentation and hardware before claiming compatibility.

The original design brief is included for context; it describes aspirations, not completed functionality.
