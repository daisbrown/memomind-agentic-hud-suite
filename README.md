# MemoMind Agentic HUD Suite

A simulation-first exploration of compact heads-up displays for agent workflows. The suite provides a shared 3-line, 32-character frame budget, priority and expiry handling, a terminal renderer, a coalescing transport wrapper, and seven deterministic project replays. Each project README describes what is simulated and what remains to be integrated.

**Status:** early prototype. The 3 × 32 layout, gesture semantics and display capabilities are design assumptions, not verified MemoMind specifications. No glasses, BLE protocol, MemoMind SDK integration, microphone, gesture approval, or claimed latency have been tested. The local CLI gate supports explicit terminal confirmation only. The BLE transport intentionally fails until official integration details are available. This repository does not establish eligibility for any hardware or discount.

```text
Local sources → formatter → priority / batching → simulator
                                           ↘ MemoMind plugin bridge (future)
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

## MemoMind platform direction

The [official platform overview](https://open-platform.memo-mind.com/docs/get-started/overview/?lang=en) describes GlassSDK plugins in C and PhoneSDK web plugins. A future adapter needs to follow that platform and its supported bridge; the BLE stub is exploratory and does not implement the official SDK. The three-line display is a simulator convention, not an established hardware limit. Device and App validation require compatible hardware and software.

## Project capabilities

| Project | Working local components | Remaining integration |
| --- | --- | --- |
| Claude gate | Replay, risk heuristic, terminal confirmation, MCP risk tool | Device approval |
| Moto | Replay, GPX parser, distance calculation, OBD adapter, threshold checker | Real GPS and OBD validation, voice and rider safety validation |
| MoA sentinel | Replay, synchronous observer, heartbeat detector and local HTTP bridge | Async instrumentation and deployment security |
| Field ops | Checklist, local Docker listing, reference pinouts and stdio MCP tools | Voice integration |
| Delta pulse | Replay, CSV feed, cooldown filter, YAML rules | Live market feed |
| Local cue | ADR trigger, local lexical index and CLI | Speech and vector retrieval |
| Tmux pilot | Replay, pane listing, interactive confirmed allowlisted macros | Device gestures and real-session validation |

The terminal gate is not a security sandbox or a Claude Code permission hook. The tmux macro router sends text and Enter to an existing pane only after caller confirmation; existing pane contents can change what executes. Review the pane before use.

## Optional local integrations

Install `python -m pip install -e '.[integrations]'`. Start the gate MCP server with `python projects/01-claude-hud-gate/mcp_server.py` and field ops with `python projects/04-voice-mcp-field-ops/mcp_server.py` as stdio MCP server commands. The gate returns `approved: false` and `unavailable`; it does not provide real approvals.

For the local telemetry bridge, from `projects/03-moa-sentinel-hud`, run `python -m uvicorn telemetry_bridge:app --host 127.0.0.1`. It has no authentication or persistence and must remain on a trusted loopback interface. `projects/06-local-rag-whisper-cue/cli.py` searches local Markdown. The optional OBD adapter requires `.[obd]` and a compatible device.

## Roadmap

- Implement and validate a genuine approval integration with explicit authorization and fail-closed behavior.
- Expand the six additional project replays into the integrations described in the blueprint, with tests and safety boundaries.
- Verify display capabilities and SDK transport against official documentation and hardware before claiming compatibility.

The original design brief is included for context; it describes aspirations, not completed functionality.
