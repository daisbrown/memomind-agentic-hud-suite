import pytest
from simulate_rack_debug import Runbook, STEPS, health_frame

def test_runbook_boundaries():
    with pytest.raises(ValueError): Runbook([])
    b = Runbook(STEPS); b.previous(); assert b.index == 0
    for _ in range(10): b.advance()
    assert b.index == 2
    b.previous(); assert b.index == 1
    assert len(health_frame().lines) == 3
