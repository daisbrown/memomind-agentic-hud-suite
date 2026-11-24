from obd_watchdog import check_readings

def test_faults_and_missing_data():
    assert check_readings({'rear_psi': 36}) == []
    assert [a.field for a in check_readings({'rear_psi': 26, 'coolant_c': 120})] == ['rear_psi', 'coolant_c']
    assert check_readings({}) == []
