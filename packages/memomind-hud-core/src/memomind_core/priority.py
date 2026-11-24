"""Priority and expiry handling with an injectable monotonic clock."""
from dataclasses import dataclass
from enum import IntEnum
import time
from .formatter import CLEAR_FRAME, Frame

class Priority(IntEnum):
    P0_CRITICAL = 0
    P1_ACTIONABLE = 1
    P2_AMBIENT = 2

@dataclass
class _Entry:
    frame: Frame
    priority: Priority
    expires: float
    sequence: int

class PriorityQueueManager:
    def __init__(self, clock=time.monotonic):
        self.clock = clock
        self._entries = []
        self._sequence = 0

    def push(self, frame, priority, ttl=6.0):
        if ttl <= 0:
            raise ValueError("ttl must be positive")
        self._sequence += 1
        self._entries.append(_Entry(frame, Priority(priority), self.clock() + ttl, self._sequence))

    def current(self):
        now = self.clock()
        self._entries = [entry for entry in self._entries if entry.expires > now]
        return min(self._entries, key=lambda e: (e.priority, -e.sequence)).frame if self._entries else CLEAR_FRAME

    def dismiss(self, frame):
        self._entries = [entry for entry in self._entries if entry.frame != frame]
