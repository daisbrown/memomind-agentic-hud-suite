from simulate_arch_call import cue

def test_trigger_requires_known_adr():
    assert cue('ordinary conversation').blank
    assert cue('ADR-999').blank
    assert 'ADR-014' in cue('check adr-014').lines[0]
