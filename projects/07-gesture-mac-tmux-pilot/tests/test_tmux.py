import pytest
from gesture_macro_router import dispatch
from pane_watcher import list_panes
from types import SimpleNamespace

def test_read_and_confirm():
    def read(*a, **kw): return SimpleNamespace(stdout='dev\t0\t%2\tpython\t0\t\n')
    assert list_panes(read)[0]['pane'] == '%2'
    calls = []
    def run(cmd, **kw): calls.append(cmd)
    with pytest.raises(PermissionError): dispatch('%2', 'pytest', runner=run)
    with pytest.raises(ValueError): dispatch('bad', 'pytest', True, run)
    dispatch('%2', 'pytest', True, run)
    assert len(calls) == 2 and calls[0][-1] == 'pytest -lf'
