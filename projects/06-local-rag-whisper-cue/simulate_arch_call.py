"""Small deterministic local keyword retrieval demonstration."""
import re
from memomind_core import HUDFormatter
from memomind_core.formatter import CLEAR_FRAME
from memomind_core.simulator import render

DOCS = {"ADR-014": ("BLE GATT MTU", "MAX PAYLOAD: EXAMPLE ONLY", "RETRY: 3x BACKOFF")}

def cue(transcript):
    match = re.search(r"\bADR-\d{3}\b", transcript, re.I)
    if not match: return CLEAR_FRAME
    key = match.group().upper()
    if key not in DOCS: return CLEAR_FRAME
    title, metric, constraint = DOCS[key]
    return HUDFormatter().format([f"[{key}] {title}", metric, constraint])

def main():
    for segment in ["Good morning everyone", "What does ADR-014 say about BLE?", "Let's move on"]:
        frame = cue(segment)
        print(f"TRANSCRIPT: {segment}")
        print(render(frame))

if __name__ == '__main__': main()
