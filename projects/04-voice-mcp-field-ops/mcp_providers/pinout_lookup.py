"""Reference pin labels only; verify against the device documentation."""
PINOUTS = {'OBD-II': {4: 'chassis ground', 6: 'CAN high', 14: 'CAN low', 16: 'battery positive'}, 'RJ45-ETHERNET': {1: 'pair 2', 2: 'pair 2', 3: 'pair 3', 6: 'pair 3'}}

def lookup(name):
    return dict(PINOUTS[name.upper()])
