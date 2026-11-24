"""Deterministic batch monitor replay."""
from memomind_core import HUDFormatter
from memomind_core.formatter import CLEAR_FRAME
from memomind_core.simulator import render

def status_frame(name, heartbeat_age, timeout, completed=False, pass_rate=0.0, tokens=0, latency_ms=0):
    f = HUDFormatter()
    if heartbeat_age > timeout and not completed:
        return f.format([f"[{name}] WORKER STALLED", f"NO HEARTBEAT: {heartbeat_age}s", "CHECK WORKER"])
    if completed:
        return f.format([f"[{name}] 100% COMPLETE", f"PASS: {pass_rate:.1f}% | TOKENS: {tokens}", f"AVG LATENCY: {latency_ms}ms"])
    return CLEAR_FRAME

def main():
    for event in [dict(name="MOA-EVAL", heartbeat_age=2, timeout=10), dict(name="MOA-EVAL", heartbeat_age=12, timeout=10), dict(name="MOA-EVAL", heartbeat_age=0, timeout=10, completed=True, pass_rate=94.2, tokens="1.4M", latency_ms=410)]:
        print(render(status_frame(**event)))

if __name__ == '__main__': main()
