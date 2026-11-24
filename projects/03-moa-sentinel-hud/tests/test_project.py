from simulate_moa_batch import status_frame

def test_monitor_silent_stall_complete():
    assert status_frame('MOA', 2, 10).blank
    assert 'STALLED' in status_frame('MOA', 11, 10).lines[0]
    assert 'COMPLETE' in status_frame('MOA', 0, 10, completed=True).lines[0]

def test_decorator_reports_and_preserves_failure():
    import pytest
    from decorator import hud_watch
    events = []
    @hud_watch('batch', events.append, clock=lambda: 1)
    def work(fail):
        if fail: raise ValueError('problem')
        return 42
    assert work(False) == 42
    with pytest.raises(ValueError): work(True)
    assert [e['status'] for e in events] == ['complete', 'error']
