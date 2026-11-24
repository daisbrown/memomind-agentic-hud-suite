import pytest
from nav_distance import distance_miles

def test_distance():
    assert distance_miles(35,-80,35,-80) == 0
    assert 68 < distance_miles(35,-80,36,-80) < 70
    with pytest.raises(ValueError): distance_miles(100,0,0,0)
