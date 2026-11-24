import sys
from types import SimpleNamespace
from obd_adapter import read_standard

def test_standard_pids_and_missing_response(monkeypatch):
    commands = SimpleNamespace(COOLANT_TEMP='temp', CONTROL_MODULE_VOLTAGE='voltage')
    monkeypatch.setitem(sys.modules, 'obd', SimpleNamespace(commands=commands))
    value = SimpleNamespace(to=lambda unit: SimpleNamespace(magnitude=91))
    class Connection:
        def query(self, command):
            return SimpleNamespace(is_null=lambda: command == 'voltage', value=value)
    assert read_standard(Connection()) == {'coolant_c': 91.0}
