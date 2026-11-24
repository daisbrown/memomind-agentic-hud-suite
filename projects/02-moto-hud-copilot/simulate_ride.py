"""Deterministic telemetry replay; no live vehicle or navigation connection."""
from memomind_core import HUDFormatter
from memomind_core.formatter import CLEAR_FRAME
from memomind_core.simulator import render

RIDE = [
    {"mile": 0.0, "distance": 1.2, "rear_psi": 36},
    {"mile": 0.8, "distance": 0.4, "rear_psi": 36},
    {"mile": 1.0, "distance": 0.2, "rear_psi": 26},
    {"mile": 1.3, "distance": None, "rear_psi": 36},
]

def ride_frame(sample):
    fmt = HUDFormatter()
    if sample["rear_psi"] < 30:
        return fmt.format(["⚠ ALERT: REAR TPMS LOW", f"{sample['rear_psi']} PSI (TARGET: 36 PSI)", "STOP WHEN SAFE"])
    distance = sample.get("distance")
    if distance is not None and 0 <= distance <= .5:
        return fmt.format([f"↗ EXIT 42B | {distance:.1f} MI", "I-85 N -> US-74 W (MERGE)", "SPD LIM: 65 | CURVE: MOD"])
    return CLEAR_FRAME

def main():
    for sample in RIDE:
        print(f"MILE {sample['mile']}: {'DARK' if ride_frame(sample).blank else 'ALERT'}")
        print(render(ride_frame(sample)))

if __name__ == '__main__': main()
