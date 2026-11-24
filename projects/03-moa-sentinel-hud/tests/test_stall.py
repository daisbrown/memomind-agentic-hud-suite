import pytest
from stall_detector import StallDetector

def test_heartbeats_and_rate():
    d = StallDetector(timeout=10); d.heartbeat('a', 0); d.heartbeat('b', 8)
    assert d.stalled(11) == ['a']
    assert d.low_pass_rate(7, 10)
    assert not d.low_pass_rate(8, 10)
    with pytest.raises(ValueError): d.low_pass_rate(0, 0)
