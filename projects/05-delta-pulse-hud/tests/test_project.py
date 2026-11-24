from simulate_options_tape import ConfluenceEngine, Tick, tape

def test_filter_and_cooldown():
    e = ConfluenceEngine()
    assert len([x for x in tape() if e.accept(x)]) == 2
    e = ConfluenceEngine(); t = Tick('X','1C',3,.3,1,10,0)
    assert e.accept(t)
    assert not e.accept(Tick('X','1C',3,.3,1,10,299))
    assert e.accept(Tick('X','1C',3,.45,1,10,300))
