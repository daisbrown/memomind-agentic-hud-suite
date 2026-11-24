from abc import ABC, abstractmethod

class HUDTransport(ABC):
    @abstractmethod
    async def send(self, frame):
        """Send a frame, including an empty frame to blank the display."""
