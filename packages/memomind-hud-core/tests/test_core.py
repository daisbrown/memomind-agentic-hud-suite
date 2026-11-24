import asyncio
import pytest
from memomind_core import Frame, HUDFormatter, Priority, PriorityQueueManager
from memomind_core.transport.batching import FrameBatcher


def test_frame_budget_and_whole_tokens():
    frame = HUDFormatter().format(["please the " + "WORD " * 20, "26 PSI", "↗ EXIT 42", "ignored"])
    assert len(frame.lines) == 3
    assert all(len(line) <= 32 for line in frame.lines)
    assert frame.lines[0].endswith("…")
    assert "26 PSI" in frame.lines
    with pytest.raises(ValueError):
        Frame(("x" * 33,))


def test_priority_expiry_and_resume():
    now = [0.0]
    q = PriorityQueueManager(clock=lambda: now[0])
    ambient, critical = Frame(("status",)), Frame(("alert",))
    q.push(ambient, Priority.P2_AMBIENT, 10)
    q.push(critical, Priority.P0_CRITICAL, 2)
    assert q.current() == critical
    now[0] = 3
    assert q.current() == ambient
    now[0] = 11
    assert q.current().blank


def test_batch_coalescing_and_critical_bypass():
    class Transport:
        def __init__(self): self.sent = []
        async def send(self, frame): self.sent.append(frame)
    async def run():
        now = [0.0]
        t = Transport()
        b = FrameBatcher(t, clock=lambda: now[0])
        a, c = Frame(("A",)), Frame(("C",))
        await b.submit(a)
        await b.submit(c)
        await b.flush()
        assert t.sent == []
        now[0] = .25
        await b.flush()
        await b.submit(c, Priority.P0_CRITICAL)
        assert t.sent == [c]
        await b.submit(a)
        await b.submit(c, Priority.P0_CRITICAL)
        await b.flush(force=True)
        assert t.sent == [c]
    asyncio.run(run())
