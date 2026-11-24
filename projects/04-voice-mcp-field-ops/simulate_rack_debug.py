"""Replay of a rack health query and checklist."""
from memomind_core import HUDFormatter
from memomind_core.simulator import render

PINOUTS = {"RJ45": "1 TX+ | 2 TX- | 3 RX+ | 6 RX-", "OBD-II": "4 GND | 6 CAN-H | 14 CAN-L | 16 +12V"}
STEPS = ["CHECK NODE REACHABILITY", "INSPECT POD STATUS", "REVIEW POD LOGS"]

class Runbook:
    def __init__(self, steps):
        if not steps: raise ValueError("runbook needs steps")
        self.steps, self.index = tuple(steps), 0
    def advance(self): self.index = min(self.index + 1, len(self.steps)-1)
    def previous(self): self.index = max(self.index - 1, 0)
    def frame(self): return HUDFormatter().format([f"RUNBOOK {self.index+1}/{len(self.steps)}", self.steps[self.index], "TAP: NEXT | DOUBLE: BACK"])

def health_frame():
    return HUDFormatter().format(["[RACK-02] k3s-worker-01", "CPU: 78% | MEM: 29.4/32G", "PODS: 41/42 (1 CrashLoop)"])

def main():
    print(render(health_frame()))
    book = Runbook(STEPS)
    for _ in STEPS:
        print(render(book.frame())); book.advance()

if __name__ == '__main__': main()
