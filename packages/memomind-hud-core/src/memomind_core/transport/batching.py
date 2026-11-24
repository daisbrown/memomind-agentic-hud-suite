"""Explicitly flushed coalescing; P0 frames bypass the batch window."""
import time
from ..priority import Priority

class FrameBatcher:
    def __init__(self, transport, window=0.25, clock=time.monotonic):
        self.transport, self.window, self.clock = transport, window, clock
        self.pending = None
        self.deadline = None
        self.last = None

    async def submit(self, frame, priority=Priority.P2_AMBIENT):
        if priority == Priority.P0_CRITICAL:
            self.pending = self.deadline = None
            await self._send(frame)
            return
        if self.pending is None:
            self.deadline = self.clock() + self.window
        self.pending = frame

    async def flush(self, force=False):
        if self.pending is not None and (force or self.clock() >= self.deadline):
            frame = self.pending
            self.pending = self.deadline = None
            await self._send(frame)

    async def _send(self, frame):
        if frame != self.last:
            await self.transport.send(frame)
            self.last = frame
