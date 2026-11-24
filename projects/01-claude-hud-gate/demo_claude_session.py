"""Replay illustrative actions; no commands are executed."""
from memomind_core import HUDFormatter
from memomind_core.simulator import render
from risk_analyzer import classify

ACTIONS = [("ruff check .", [], "Lint check"), ("pip install example", [], "Package install"), ("DROP idx_users_email", ["db/migrate_04.sql"], "DROP idx_users_email (LOCK)")]

def main():
    formatter = HUDFormatter()
    for command, files, summary in ACTIONS:
        risk = classify(command, files)
        if risk == "LOW":
            print("[SIMULATED AUTO-APPROVE]", command)
            continue
        print(render(formatter.format([f"[GATE: {risk}] " + (files[0] if files else "agent action"), summary, "TAP: Approve | HOLD: Reject"])))
        print("[SIMULATION ONLY: no approval or command execution]")

if __name__ == "__main__":
    main()
