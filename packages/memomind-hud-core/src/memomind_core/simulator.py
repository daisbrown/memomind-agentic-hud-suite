"""Portable terminal renderer; no hardware or external dependencies required."""
from .formatter import MAX_CHARS_PER_LINE, MAX_LINES

def render(frame):
    lines = list(frame.lines) + [""] * (MAX_LINES - len(frame.lines))
    border = "+" + "-" * (MAX_CHARS_PER_LINE + 2) + "+"
    return "\n".join([border, *("| " + line.ljust(MAX_CHARS_PER_LINE) + " |" for line in lines), border])
