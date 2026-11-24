"""Straight-line waypoint distance, not turn-by-turn routing."""
import math

def distance_miles(lat1, lon1, lat2, lon2):
    if not all(-90 <= lat <= 90 for lat in (lat1,lat2)) or not all(-180 <= lon <= 180 for lon in (lon1,lon2)):
        raise ValueError('invalid coordinates')
    p1,p2=map(math.radians,(lat1,lat2)); dp=p2-p1; dl=math.radians(lon2-lon1)
    a=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 3958.7613 * 2 * math.atan2(math.sqrt(a), math.sqrt(max(0,1-a)))
