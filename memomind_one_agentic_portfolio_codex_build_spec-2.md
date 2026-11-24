# MemoMind One — Agentic AI & HUD Portfolio Blueprint (Codex Spec)

## 🏆 EXPLICIT WIN CONDITION & GOAL FOR CHATGPT CODEX (READ FIRST)

**Primary Mission Objective:** You are acting as a Staff Systems & AI Architect. Your goal is to build a flagship, zero-fluff Python monorepo (`memomind-agentic-hud-suite`) for the developer's public GitHub (`https://github.com/daisbrown`) engineered specifically to **WIN approval for MemoMind's $100 Developer Discount ($399 target price) and Developer Workbench hardware allocation**.

**What "WINNING" Looks Like (Reviewer Psychology):**
MemoMind's Developer Relations and SDK engineering team manually reviews applications and only awards the $100 developer discount + Workbench hardware access to builders who will ship real ecosystem value—not casual tinkerers. When a MemoMind engineer opens `https://github.com/daisbrown/memomind-agentic-hud-suite`, every file must scream:
1. **"Ship this person hardware immediately."** The repo already implements a clean, isolated BLE GATT / `PhoneSDK` adapter layer (`# TODO(memomind-sdk)`) ready to drop in official SDK bindings on Day 1.
2. **"They mastered monochrome waveguide physics."** Zero bloated web dashboards or wall-of-text LLM dumps—every single project strictly respects `3 lines × 32 characters`, battery-saving BLE duty-cycle batching, and dark-by-default peripheral safety.
3. **"7 distinct, real-world agentic apps out of the box."** From autonomous CLI coding gates (`claude-hud-gate`) and safety-critical motorcycle telemetry (`moto-hud-copilot`) to edge-RAG live meeting cues (`local-rag-whisper-cue`) and multi-pane `tmux` voice/gesture control (`gesture-mac-tmux-pilot`).

**Non-Negotiable Engineering Standards:**
* **Zero Vaporware:** Every single one of the 7 projects must include an executable CLI simulator, deterministic replay datasets, an ASCII render of the `3×32` green HUD in its `README.md`, and passing `pytest` unit/integration tests.
* **Clean SDK Boundaries:** Isolate all hardware-specific bindings inside `packages/memomind-hud-core/src/memomind_core/transport/` so swapping from simulated terminal output to physical MemoMind One glasses requires changing a single transport config flag.

---

## 🛠️ Recommended Open-Source Frameworks & Tooling Stack

Codex must build on top of these proven open-source repositories and libraries:

| Layer | Recommended Framework / Repo | Package / URL | Purpose in This Suite |
| :--- | :--- | :--- | :--- |
| **Agent Tool Protocol** | **Model Context Protocol (Python SDK)** | `modelcontextprotocol/python-sdk` (`pip install mcp`) | Exposes deterministic tools (`stdio` & `SSE`) so Claude Code, local LLMs, or voice routers trigger HUD frames and receive temple-tap approvals. |
| **BLE Transport Layer** | **Bleak (Cross-Platform BLE)** | `hbldh/bleak` (`pip install bleak`) | Async Bluetooth Low Energy client abstraction for PhoneSDK-to-Glass GATT characteristic simulation and packet chunking. |
| **API & Event Streaming** | **FastAPI + SSE-Starlette** | `fastapi/fastapi` (`pip install fastapi uvicorn sse-starlette`) | Local companion bridge receiving webhooks from CLI agents, OBD-II adapters, and market feeds. |
| **Data Validation & Config** | **Pydantic v2 + PyYAML** | `pydantic/pydantic` (`pip install pydantic pyyaml`) | Enforces strict schema validation on HUD payloads, risk rules, and YAML alert thresholds. |
| **Automotive / Moto Telemetry** | **python-OBD + gpxpy** | `brendan-w/python-OBD`, `tkrajina/gpxpy` (`pip install obd gpxpy`) | Parses real/simulated ELM327 OBD-II PIDs (coolant temp, battery voltage, TPMS, RPM) and GPX motorcycle route waypoints. |
| **Local Edge RAG & Embeddings** | **LanceDB + Sentence-Transformers** | `lancedb/lancedb` (`pip install lancedb`) | Sub-15ms local vector retrieval for real-time conversational/technical cues without cloud roundtrips. |
| **Local Voice / Intent Routing** | **Faster-Whisper + Instructor** | `SYSTRAN/faster-whisper`, `jxnl/instructor` | Low-latency onboard-mic speech-to-text paired with structured Pydantic tool-call extraction (zero verbose LLM prose). |
| **Terminal Multiplexing** | **libtmux** | `tmux-python/libtmux` (`pip install libtmux`) | Programmatic inspection and control of active `tmux` sessions, build panes, and SSH agent windows. |
| **CLI & Terminal Simulation** | **Rich + Typer** | `Textualize/rich`, `fastapi/typer` (`pip install rich typer pytest pytest-asyncio`) | Renders an authentic green-on-black (`#00FF66`) monochrome waveguide HUD preview box directly in the developer's terminal. |

---

## 📁 Target Monorepo Directory Structure

Codex must scaffold the repository using this exact 7-project layout:

```text
memomind-agentic-hud-suite/
├── README.md                          # Master showcase, architecture diagram, quickstart
├── pyproject.toml                     # Workspace config, ruff, mypy, pytest settings
├── packages/
│   └── memomind-hud-core/             # Shared Waveguide Engine & Mock BLE Transport
│       ├── pyproject.toml
│       ├── src/memomind_core/
│       │   ├── formatter.py           # 3x32 semantic truncator & glyph budgeter
│       │   ├── priority.py            # P0/P1/P2 preemption queue & TTL auto-dismiss
│       │   ├── gestures.py            # Temple tap / long-press / voice-ack state machine
│       │   ├── simulator.py           # Rich green-monochrome terminal HUD renderer
│       │   └── transport/
│       │       ├── base.py            # Abstract MemoMindTransport interface
│       │       ├── bleak_stub.py      # Bleak GATT stub with TODO(memomind-sdk) hooks
│       │       └── ws_bridge.py       # Local WebSocket transport for desktop testing
│       └── tests/
│           └── test_formatter_and_queue.py
└── projects/
    ├── 01-claude-hud-gate/            # Project 1: Claude Code & CLI Diff Approval Gate
    ├── 02-moto-hud-copilot/           # Project 2: Motorcycle Telemetry & Rider Copilot
    ├── 03-moa-sentinel-hud/           # Project 3: Async Multi-Agent & Ollama Watchdog
    ├── 04-voice-mcp-field-ops/        # Project 4: Hands-Free Lab & Hardware MCP Copilot
    ├── 05-delta-pulse-hud/            # Project 5: Event-Driven Options Flow Ticker
    ├── 06-local-rag-whisper-cue/      # Project 6: Sub-Second Edge-RAG & Live Meeting Cue
    └── 07-gesture-mac-tmux-pilot/     # Project 7: Multi-Pane Tmux & Dev-Cluster HUD Pilot
```

---

## 🧱 Shared Core Library Specification (`memomind-hud-core`)

All 7 projects must import `memomind-hud-core`. Reviewers look closely at how developers handle small waveguide displays.

### Core Technical Requirements
1. **Strict Waveguide Frame Budgeter (`HUDFormatter`):**
   * Enforces hard hardware bounds: `MAX_LINES = 3`, `MAX_CHARS_PER_LINE = 32`.
   * Implements **semantic token preservation**: strips filler words first, preserves numbers, exit codes, ticker symbols, file extensions, and directional arrows (`↗`, `↰`, `⚠`) so critical telemetry is never clipped mid-number.
2. **Priority Preemption & Auto-Blanking (`PriorityQueueManager`):**
   * `P0_CRITICAL`: Immediate interrupt (e.g., motorcycle TPMS drop, destructive `rm -rf` gate). Bypasses cooldowns.
   * `P1_ACTIONABLE`: Interactive prompt awaiting temple tap (`SINGLE_TAP`, `DOUBLE_TAP`, `LONG_PRESS`) or voice confirmation with configurable timeout.
   * `P2_AMBIENT`: Low-priority status update with automatic TTL fade-to-black (default `6.0s`) so the waveguide stays dark when idle.
3. **BLE Duty-Cycle Optimizer:**
   * Deduplicates identical frames and batches rapid updates within a `250ms` window to preserve smart-glasses battery life.

---

## 🚀 Project 1: `claude-hud-gate` — Headless CLI & Claude Code Approval Bridge

### Problem & Value Proposition
When running autonomous coding agents (Claude Code, Codex CLI) in the background, developers lose flow state every time the agent blocks on a destructive shell command, database migration, or git push. `claude-hud-gate` exposes an **MCP server** and CLI hook wrapper that pipes **only blocking permission gates and 1-line risk summaries** to the MemoMind One HUD, letting you approve or reject via temple gestures without switching windows.

### Implementation Spec for Codex
* **Dependencies:** `mcp`, `fastapi`, `pydantic`, `memomind-hud-core`.
* **Key Modules:**
  * `mcp_server.py`: Exposes `request_hud_approval(command: str, target_files: list[str], diff_summary: str) -> ApprovalResult`.
  * `risk_analyzer.py`: Regex + AST heuristic classifier tagging commands as `LOW`, `MED`, or `HIGH` (flags `DROP`, `rm -rf`, `--force`, `.env` edits, production deploy scripts).
  * `cli_wrapper.py`: Executable wrapper (`hud-exec -- <command>`) that intercepts `stdin` confirmation prompts and routes them through the HUD simulator.
* **Exact 3×32 HUD Output Target:**
  ```text
  [GATE: HIGH] db/migrate_04.sql
  DROP idx_users_email (LOCK)
  TAP: Approve | HOLD: Reject
  ```
* **Simulation & Tests:** Include `demo_claude_session.py` simulating 3 sequential agent actions (safe lint check auto-approved, medium package install, high-risk SQL drop) + `pytest` suite verifying exit codes on tap vs. long-press.

---

## 🏍️ Project 2: `moto-hud-copilot` — Motorcycle Telemetry, Navigation & Mesh Rider HUD

### Problem & Value Proposition
Glancing down at a handlebar-mounted phone or dash cluster at 65+ mph takes eyes off the road during critical cornering or traffic merges. Built specifically for **MemoMind One worn inside a motorcycle helmet**, `moto-hud-copilot` acts as a zero-clutter, peripheral-vision **Motorcycle Copilot** combining vector turn pre-alerts, real-time OBD-II/CAN-bus bike health monitoring, and hands-free helmet-mic MCP queries.

### Safety-First Motorcycle UX Rules (Must Enforce in Code)
1. **Zero-Idle Clutter (Dark-By-Default):** During steady-state cruising with no upcoming turns or faults, the HUD transmits a `CLEAR_FRAME` command so the display remains **100% transparent/dark**.
2. **High-Contrast Vector Glyphs:** Uses crisp monochrome arrows (`↗`, `↰`, `↱`, `⚠`) and high-legibility uppercase telemetry (`PSI`, `TEMP`, `MI`, `OCT`).
3. **100% Glove-Free Operation:** Zero touch-temple gestures required while riding; driven strictly by speed/GPS triggers, OBD-II fault thresholds, and helmet-mic push-to-talk voice intents.

### Implementation Spec for Codex
* **Dependencies:** `obd`, `gpxpy`, `mcp`, `pydantic`, `memomind-hud-core`.
* **Key Modules:**
  * `nav_prealert.py`: Parses GPX routes and wakes the HUD `0.5 miles` prior to a turn, exit, or sharp advisory curve, auto-dismissing 5 seconds after completing the maneuver:
    ```text
    ↗ EXIT 42B  |  0.4 MI
    I-85 N -> US-74 W (MERGE)
    SPD LIM: 65  |  CURVE: MOD
    ```
  * `obd_watchdog.py`: Polls ELM327 / CAN-bus PIDs (coolant temp, battery voltage, front/rear TPMS, estimated fuel range). Fires a `P0_CRITICAL` interrupt only when a parameter crosses safe thresholds:
    ```text
    ⚠ ALERT: REAR TPMS LOW
    26 PSI (TARGET: 36 PSI)
    NEXT FUEL/AIR: 3.2 MI ↗
    ```
  * `rider_voice_mcp.py`: Maps short helmet-mic voice utterances (`"Find 93 octane"`, `"Check weather ahead"`, `"Send ETA text"`) to deterministic MCP tools returning a 3-line answer that auto-blanks after `6 seconds`:
    ```text
    [FUEL 93] SHELL - 1.8 MI ↗
    EXIT 44 (RIGHT AT LIGHT)
    EST RANGE LEFT: 24 MI
    ```
* **Simulation & Tests:** Include a realistic GPX ride simulator (`simulate_ride.py` modeled on a North Carolina highway/mountain loop with injected low-TPMS and low-fuel events) + full `pytest` coverage.

---

## 🧠 Project 3: `moa-sentinel-hud` — Async Multi-Agent & Local LLM Watchdog

### Problem & Value Proposition
Engineers running overnight evaluation suites, local Ollama/MLX batch jobs, or Mixture-of-Agents (MoA) pipelines shouldn't have to babysit terminal logs. `moa-sentinel-hud` provides a drop-in Python decorator and FastAPI telemetry bridge that keeps the HUD silent while agents run normally, surfacing a crisp green card only when a worker stalls, hits a governance guardrail, or finishes a run.

### Implementation Spec for Codex
* **Dependencies:** `fastapi`, `uvicorn`, `pydantic`, `memomind-hud-core`.
* **Key Modules:**
  * `decorator.py`: `@hud_watch(pipeline_name="moa-grader")` context manager/decorator tracking execution time, token throughput, and exception states.
  * `stall_detector.py`: Detects heartbeat timeouts, repetitive token loops, or pass-rate drops below threshold.
* **Exact 3×32 HUD Output Target:**
  ```text
  [MOA-EVAL] 100% COMPLETE
  PASS: 94.2% | TOKENS: 1.4M
  AVG LATENCY: 410ms [OK]
  ```
* **Simulation & Tests:** Include `simulate_moa_batch.py` demonstrating both a clean batch completion card and a stalled-worker `P1` alert.

---

## 🔧 Project 4: `voice-mcp-field-ops` — Hands-Free Hardware & Server Room Copilot

### Problem & Value Proposition
When working inside a server rack, wiring a home lab, or probing a circuit with a multimeter, both hands are occupied. `voice-mcp-field-ops` connects MemoMind One's onboard microphone to an MCP client host backed by local system diagnostics, hardware pinout databases, and step-by-step runbooks—rendering structured key-value tables directly in your line of sight.

### Implementation Spec for Codex
* **Dependencies:** `mcp`, `pydantic`, `memomind-hud-core`.
* **Key Modules:**
  * `mcp_providers/docker_health.py`: Queries container/node health and formats compact resource metrics.
  * `mcp_providers/pinout_lookup.py`: Deterministic lookup for GPIO, OBD-II, RJ45, and automotive relay pinouts.
  * `runbook_stepper.py`: Interactive checklist controller where `SINGLE_TAP` advances to the next step and `DOUBLE_TAP` repeats the previous step.
* **Exact 3×32 HUD Output Target:**
  ```text
  [RACK-02] k3s-worker-01
  CPU: 78% | MEM: 29.4/32G
  PODS: 41/42 (1 CrashLoop)
  ```
* **Simulation & Tests:** Include `simulate_rack_debug.py` walking through a voice query + 3-step runbook traversal.

---

## 📈 Project 5: `delta-pulse-hud` — Event-Driven Market & Options Flow Ticker

### Problem & Value Proposition
Traders monitoring unusual options activity or automated strategy triggers suffer from multi-monitor fatigue and alert noise. `delta-pulse-hud` applies a strict multi-factor Pydantic rule engine and cooldown deduplicator so the MemoMind One HUD surfaces only high-conviction setups in a glanceable 3-line card.

### Implementation Spec for Codex
* **Dependencies:** `pydantic`, `pyyaml`, `memomind-hud-core`.
* **Key Modules:**
  * `confluence_engine.py`: Filters incoming option sweeps against YAML rules (`min_vol_oi_ratio: 3.0`, `delta_range: [0.30, 0.45]`, `per_ticker_cooldown_sec: 300`).
  * `ticker_formatter.py`: Formats passing contracts into aligned monochrome cards.
* **Exact 3×32 HUD Output Target:**
  ```text
  NVDA 145C 11/28 [SWEEP]
  VOL/OI: 4.8x | DELTA: 0.38
  ASK: $2.45 | IVR: 42%
  ```
* **Simulation & Tests:** Include `simulate_options_tape.py` feeding 50 noisy ticks and proving only the 2 high-conviction sweeps reach the HUD.

---

## ⚡ Project 6: `local-rag-whisper-cue` — Sub-Second Edge-RAG & Live Architecture Cue

### Problem & Value Proposition
During live architecture reviews, technical briefings, or incident bridges, looking down at notes or searching docs breaks eye contact and momentum. `local-rag-whisper-cue` listens via the glasses' microphone, detects technical entities or architecture questions in real time, queries a local **LanceDB** vector store of your markdown docs/ADRs in `<20ms`, and flashes a 3-line micro-fact card in your peripheral vision—with zero cloud latency.

### Implementation Spec for Codex
* **Dependencies:** `lancedb`, `pydantic`, `memomind-hud-core`.
* **Key Modules:**
  * `entity_trigger.py`: Lightweight keyword + semantic trigger gate that fires *only* when a technical term, SLA metric, or ADR ID is spoken (prevents constant HUD noise during normal conversation).
  * `rag_micro_summarizer.py`: Compresses retrieved vector chunks into a 3-line key-value fact card (`METRIC`, `CONSTRAINT`, `ADR REF`).
* **Exact 3×32 HUD Output Target:**
  ```text
  [ADR-014] BLE GATT MTU
  MAX PAYLOAD: 244B @ 15ms
  RETRY: 3x EXP BACKOFF (50ms)
  ```
* **Simulation & Tests:** Include `simulate_arch_call.py` indexing sample Architecture Decision Records into an ephemeral LanceDB table, feeding simulated transcript segments, and asserting sub-50ms retrieval + HUD card formatting.

---

## 🖥️ Project 7: `gesture-mac-tmux-pilot` — Multi-Pane `tmux` & Local Agent Cluster Pilot

### Problem & Value Proposition
Developers running 4–6 parallel `tmux` panes on a Mac Studio or Linux workstation (e.g., Claude Code in pane 1, Docker build in pane 2, pytest watcher in pane 3, Ollama server in pane 4) need a heads-up command switcher while grabbing coffee or pacing the office. `gesture-mac-tmux-pilot` monitors `tmux` pane exit statuses and lets you cycle panes via `SINGLE_TAP`, send pre-bound recovery macros (`pytest -lf`, `git status`, `docker compose restart`) via `LONG_PRESS`, and inspect tail logs hands-free.

### Implementation Spec for Codex
* **Dependencies:** `libtmux`, `pydantic`, `memomind-hud-core`.
* **Key Modules:**
  * `pane_watcher.py`: Polls `libtmux` session panes (with a clean mock fallback when `tmux` isn't running in CI) to detect non-zero exit codes or build completions.
  * `gesture_macro_router.py`: Maps temple tap gestures to safe, allowlisted `tmux send-keys` macros with confirmation guardrails.
* **Exact 3×32 HUD Output Target:**
  ```text
  [TMUX 2/4] pytest-watch [FAIL]
  E AssertionError: test_ble.py
  TAP: Next Pane | HOLD: Re-run
  ```
* **Simulation & Tests:** Include `simulate_tmux_cluster.py` demonstrating multi-pane status cycling and macro dispatch using mock `tmux` sessions + full `pytest` coverage.

---

## 📋 Master Copy-Paste Prompt for ChatGPT Codex

Copy and paste the block below directly into ChatGPT Codex inside your empty `memomind-agentic-hud-suite` repository:

```text
Read `memomind_codex_blueprint.md` carefully—especially the "EXPLICIT WIN CONDITION & GOAL FOR CHATGPT CODEX" section at the top.

Your mission is to build a flagship, zero-fluff Python monorepo (`memomind-agentic-hud-suite`) ready to push to `https://github.com/daisbrown` that WINS MemoMind's SDK team review for the $100 Developer Discount and Workbench hardware allocation.

Execute in this exact order:
1. Scaffold the monorepo directory layout and root `pyproject.toml`.
2. Build `packages/memomind-hud-core` first:
   - Implement `HUDFormatter` enforcing strict 3-line x 32-character waveguide bounds with semantic token preservation.
   - Implement `PriorityQueueManager` (`P0_CRITICAL`, `P1_ACTIONABLE`, `P2_AMBIENT`) with auto-blanking TTLs and BLE duty-cycle batching.
   - Implement `Rich` terminal simulator (`simulator.py`) that renders an authentic green-on-black monochrome HUD box so anyone running the demos sees the exact glasses UX.
   - Implement `Bleak` transport stubs (`bleak_stub.py`) with clear `# TODO(memomind-sdk)` integration points.
3. Build all 7 projects under `projects/`:
   - `01-claude-hud-gate` (MCP approval server + risk analyzer + CLI gate demo)
   - `02-moto-hud-copilot` (Dark-by-default motorcycle HUD + GPX turn pre-alerts + OBD-II/TPMS fault watchdog + hands-free helmet-mic MCP queries + full ride simulation)
   - `03-moa-sentinel-hud` (`@hud_watch` decorator + FastAPI telemetry bridge + batch simulation)
   - `04-voice-mcp-field-ops` (MCP providers for node health, pinouts, and temple-tap runbook stepping)
   - `05-delta-pulse-hud` (YAML multi-factor options flow filter + cooldown deduplicator + tape replay)
   - `06-local-rag-whisper-cue` (Sub-20ms LanceDB local edge-RAG + entity trigger gate + live architecture cue simulation)
   - `07-gesture-mac-tmux-pilot` (`libtmux` multi-pane watcher + temple-tap macro router + cluster simulation)
4. Write clean, high-impact `README.md` files at the root and inside every project folder featuring ASCII renders of the 3x32 green HUD output, architecture diagrams, and exact CLI commands to run each simulation.
5. Run `pytest` across the entire workspace and fix any linting, typing, or test failures until 100% of tests pass.
```

---

## 🎯 Bonus: Winning Pitch for Your MemoMind Developer Discount Form

Once Codex pushes `memomind-agentic-hud-suite` to `https://github.com/daisbrown`, paste this into the **"What do you plan to build?"** field on [MemoMind's Developer Discount page](https://www.memo-mind.com/pages/developer-discount):

> I am an AI Systems Architect building **Agentic HUD Bridges** designed specifically around MemoMind One's monochrome waveguide constraints (`3×32` character semantic budgeting, priority preemption, and dark-by-default peripheral safety). I have already built and open-sourced a 7-project MCP + BLE transport suite (`github.com/daisbrown/memomind-agentic-hud-suite`) with ready-to-bind `PhoneSDK` adapter hooks—including **Claude-HUD-Gate** (hands-free CLI/agent permission approvals via temple tap), **Moto-HUD-Copilot** (zero-clutter motorcycle GPX turn pre-alerts, OBD-II/TPMS fault interrupts, and helmet-mic MCP queries), **Local-RAG-Whisper-Cue** (sub-20ms LanceDB architectural recall), and **Tmux-Pilot**. Getting MemoMind One hardware in hand will let me immediately swap my Bleak GATT stubs for native `PhoneSDK`/`GlassSDK` bindings and publish production-ready MCP plugins for the MemoMind developer community.