"""Read route waypoints from GPX without connecting to a GPS device."""
from dataclasses import dataclass
import xml.etree.ElementTree as ET

@dataclass(frozen=True)
class Waypoint:
    latitude: float
    longitude: float
    name: str


def read_waypoints(path):
    root = ET.parse(path).getroot()
    points = []
    for node in root.iter():
        if node.tag.rsplit('}', 1)[-1] not in ('wpt', 'rtept'):
            continue
        name = next((child.text or '' for child in node if child.tag.rsplit('}', 1)[-1] == 'name'), '')
        lat, lon = float(node.attrib['lat']), float(node.attrib['lon'])
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            raise ValueError('invalid waypoint coordinates')
        points.append(Waypoint(lat, lon, name))
    return points
