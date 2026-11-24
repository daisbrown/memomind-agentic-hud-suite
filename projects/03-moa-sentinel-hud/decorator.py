"""Small execution observer; the caller owns event handling."""
from functools import wraps
from time import monotonic


def hud_watch(pipeline_name, emit, clock=monotonic):
    def decorate(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            started = clock()
            try:
                result = fn(*args, **kwargs)
            except Exception as exc:
                emit({'pipeline': pipeline_name, 'status': 'error', 'elapsed': clock() - started, 'error': type(exc).__name__})
                raise
            emit({'pipeline': pipeline_name, 'status': 'complete', 'elapsed': clock() - started})
            return result
        return wrapped
    return decorate
