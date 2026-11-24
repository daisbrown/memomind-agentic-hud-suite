import pytest
from simulate_tmux_cluster import Pilot, Pane

def test_cycle_and_allowlist():
    p = Pilot([Pane('one','OK',''), Pane('two','FAIL','error')])
    p.next(); assert p.index == 1
    p.next(); assert p.index == 0
    assert p.proposed_macro('pytest') == 'pytest -lf'
    with pytest.raises(ValueError): p.proposed_macro('rm')
    with pytest.raises(ValueError): Pilot([])
