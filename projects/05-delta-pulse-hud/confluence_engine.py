"""Load optional YAML thresholds for the replay filter."""
from pathlib import Path
from simulate_options_tape import ConfluenceEngine

def from_yaml(path):
    try: import yaml
    except ImportError as exc: raise RuntimeError('Install PyYAML to load rules') from exc
    data = yaml.safe_load(Path(path).read_text())
    if not isinstance(data, dict): raise ValueError('rules must be a mapping')
    ratio = float(data.get('min_vol_oi_ratio', 3.0))
    bounds = data.get('delta_range', [.30, .45])
    cooldown = float(data.get('per_ticker_cooldown_sec', 300))
    if len(bounds) != 2 or not 0 <= float(bounds[0]) <= float(bounds[1]) <= 1 or ratio < 0 or cooldown < 0: raise ValueError('invalid rules')
    return ConfluenceEngine(ratio, tuple(map(float, bounds)), cooldown)
