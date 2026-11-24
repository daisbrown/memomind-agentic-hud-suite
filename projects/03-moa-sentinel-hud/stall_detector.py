"""Caller driven heartbeat and quality checks using monotonic time."""
class StallDetector:
    def __init__(self, timeout=30, minimum_pass_rate=0.8):
        if timeout <= 0 or not 0 <= minimum_pass_rate <= 1: raise ValueError('invalid thresholds')
        self.timeout, self.minimum_pass_rate, self.heartbeats = timeout, minimum_pass_rate, {}
    def heartbeat(self, worker, now): self.heartbeats[worker] = now
    def stalled(self, now): return sorted(worker for worker, stamp in self.heartbeats.items() if now - stamp > self.timeout)
    def low_pass_rate(self, passed, total):
        if total <= 0 or passed < 0 or passed > total: raise ValueError('invalid counts')
        return passed / total < self.minimum_pass_rate
