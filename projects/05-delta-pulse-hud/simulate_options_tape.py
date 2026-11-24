"""Deterministic options filter replay; illustrative data only."""
from dataclasses import dataclass
from memomind_core import HUDFormatter
from memomind_core.simulator import render

@dataclass(frozen=True)
class Tick:
    ticker: str
    contract: str
    vol_oi: float
    delta: float
    ask: float
    ivr: int
    time: float

class ConfluenceEngine:
    def __init__(self, min_ratio=3.0, delta_range=(.30,.45), cooldown=300):
        self.min_ratio, self.delta_range, self.cooldown = min_ratio, delta_range, cooldown
        self.last = {}
    def accept(self, tick):
        if not (tick.vol_oi >= self.min_ratio and self.delta_range[0] <= tick.delta <= self.delta_range[1]): return False
        last = self.last.get(tick.ticker)
        if last is not None and tick.time - last < self.cooldown: return False
        self.last[tick.ticker] = tick.time
        return True

def card(t):
    return HUDFormatter().format([f"{t.ticker} {t.contract} [SWEEP]", f"VOL/OI: {t.vol_oi:.1f}x | DELTA: {t.delta:.2f}", f"ASK: ${t.ask:.2f} | IVR: {t.ivr}%"])

def tape():
    return [Tick('NVDA' if i == 10 else 'AMD' if i == 30 else 'NOISE', '145C 11/28', 4.8 if i in (10,30) else 1.2, .38, 2.45, 42, i) for i in range(50)]

def main():
    engine = ConfluenceEngine()
    matches = [t for t in tape() if engine.accept(t)]
    for tick in matches: print(render(card(tick)))
    print(f"{len(matches)} alerts from 50 ticks")

if __name__ == '__main__': main()
