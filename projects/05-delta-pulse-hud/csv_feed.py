"""Replay a CSV feed through the same configurable filter."""
import csv
from simulate_options_tape import Tick

def read_ticks(path):
    with open(path, newline='', encoding='utf-8') as file:
        for row in csv.DictReader(file):
            yield Tick(row['ticker'], row['contract'], float(row['vol_oi']), float(row['delta']), float(row['ask']), int(row['ivr']), float(row['time']))

def filter_ticks(ticks, engine): return [tick for tick in ticks if engine.accept(tick)]
