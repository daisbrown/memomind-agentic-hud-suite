from simulate_ride import RIDE, ride_frame

def test_ride_replay_priority_and_dark():
    assert ride_frame(RIDE[0]).blank
    assert 'EXIT' in ride_frame(RIDE[1]).lines[0]
    assert 'TPMS' in ride_frame(RIDE[2]).lines[0]
    assert ride_frame(RIDE[3]).blank

def test_gpx_waypoint_parsing(tmp_path):
    from nav_prealert import read_waypoints
    path = tmp_path / 'ride.gpx'
    path.write_text('<gpx xmlns="http://www.topografix.com/GPX/1/1"><wpt lat="35.2" lon="-80.8"><name>Turn</name></wpt></gpx>')
    point = read_waypoints(path)[0]
    assert (point.latitude, point.longitude, point.name) == (35.2, -80.8, 'Turn')
