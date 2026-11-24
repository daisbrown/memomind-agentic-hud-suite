from types import SimpleNamespace
from mcp_providers.docker_health import list_containers
from mcp_providers.pinout_lookup import lookup

def test_docker_and_copy():
    def fake(cmd, **kwargs):
        assert cmd == ['docker', 'ps', '--format', '{{json .}}']
        return SimpleNamespace(stdout='{"Names":"demo"}\n')
    assert list_containers(fake)[0]['Names'] == 'demo'
    a = lookup('obd-ii'); a[4] = 'changed'
    assert lookup('obd-ii')[4] == 'chassis ground'
