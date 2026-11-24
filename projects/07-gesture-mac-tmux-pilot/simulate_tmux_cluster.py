"""Mock tmux pane navigation; no commands are dispatched."""
from dataclasses import dataclass
from memomind_core import HUDFormatter
from memomind_core.simulator import render

@dataclass(frozen=True)
class Pane:
    name: str
    status: str
    detail: str

class Pilot:
    ALLOWED = {"pytest": "pytest -lf", "status": "git status"}
    def __init__(self, panes):
        if not panes: raise ValueError("at least one pane required")
        self.panes, self.index = tuple(panes), 0
    def next(self): self.index = (self.index + 1) % len(self.panes)
    def frame(self):
        p = self.panes[self.index]
        return HUDFormatter().format([f"[TMUX {self.index+1}/{len(self.panes)}] {p.name} [{p.status}]", p.detail, "TAP: Next | HOLD: Confirm"])
    def proposed_macro(self, key):
        if key not in self.ALLOWED: raise ValueError("macro is not allowlisted")
        return self.ALLOWED[key]

def main():
    pilot = Pilot([Pane('claude','OK','Waiting'), Pane('pytest','FAIL','AssertionError: test_ble.py'), Pane('build','OK','Complete'), Pane('ollama','OK','Serving')])
    for _ in pilot.panes:
        print(render(pilot.frame())); pilot.next()
    print('PROPOSED ONLY:', pilot.proposed_macro('pytest'))

if __name__ == '__main__': main()
