"""Conservative formatting for the assumed 3 x 32 display budget."""
from dataclasses import dataclass
import re

MAX_LINES = 3
MAX_CHARS_PER_LINE = 32
_FILLER = {"the", "a", "an", "please", "currently", "is", "are"}

@dataclass(frozen=True)
class Frame:
    lines: tuple[str, ...]

    def __post_init__(self):
        if len(self.lines) > MAX_LINES or any(len(line) > MAX_CHARS_PER_LINE or "\n" in line or "\r" in line for line in self.lines):
            raise ValueError("frame exceeds 3 x 32 budget")

    @property
    def blank(self):
        return not any(self.lines)

class HUDFormatter:
    def format(self, lines):
        result = []
        for line in list(lines)[:MAX_LINES]:
            words = str(line).split()
            text = " ".join(words)
            if len(text) > MAX_CHARS_PER_LINE:
                words = [word for word in words if word.lower() not in _FILLER]
                text = " ".join(words)
            if len(text) > MAX_CHARS_PER_LINE:
                # Never emit a partial token: omitted content is signaled with an ellipsis.
                kept = []
                for word in words:
                    candidate = " ".join(kept + [word])
                    if len(candidate) > MAX_CHARS_PER_LINE - 2:
                        break
                    kept.append(word)
                text = (" ".join(kept) + " …").strip()
            result.append(text)
        return Frame(tuple(result))

CLEAR_FRAME = Frame(())
