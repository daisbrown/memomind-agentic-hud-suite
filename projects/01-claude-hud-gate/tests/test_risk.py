from risk_analyzer import classify


def test_replay_risks():
    assert classify('ruff check .') == 'LOW'
    assert classify('pip install example') == 'MED'
    assert classify('DROP idx_users_email') == 'HIGH'
    assert classify('rm -rf build') == 'HIGH'
    assert classify('git push --force') == 'HIGH'
    assert classify('edit', ['.env']) == 'HIGH'
