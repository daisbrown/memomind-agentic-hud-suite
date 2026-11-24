"""Local telemetry HTTP API; run on loopback only in a trusted environment."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from time import monotonic
from stall_detector import StallDetector

app = FastAPI(title='MOA telemetry')
detector = StallDetector()

class Heartbeat(BaseModel):
    worker: str = Field(min_length=1, max_length=80)

@app.post('/heartbeat')
def heartbeat(event: Heartbeat):
    detector.heartbeat(event.worker, monotonic())
    return {'status': 'recorded'}

@app.get('/stalled')
def stalled(): return {'workers': detector.stalled(monotonic())}

@app.get('/health')
def health(): return {'status': 'ok'}
