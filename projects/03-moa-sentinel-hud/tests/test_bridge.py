from fastapi.testclient import TestClient
from telemetry_bridge import app

def test_http():
    c=TestClient(app)
    assert c.get('/health').json() == {'status':'ok'}
    assert c.post('/heartbeat',json={'worker':'test'}).status_code == 200
    assert 'test' not in c.get('/stalled').json()['workers']
    assert c.post('/heartbeat',json={'worker':''}).status_code == 422
