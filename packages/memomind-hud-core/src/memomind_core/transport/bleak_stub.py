from .base import HUDTransport

class BleakTransport(HUDTransport):
    async def send(self, frame):
        # TODO(memomind-sdk): Bind the documented SDK protocol after hardware access.
        raise NotImplementedError("MemoMind hardware protocol has not been verified")
