from .base import HUDTransport
from ..simulator import render

class SimulatedTransport(HUDTransport):
    async def send(self, frame):
        print(render(frame))
