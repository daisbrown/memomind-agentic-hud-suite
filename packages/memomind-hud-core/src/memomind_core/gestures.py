from enum import Enum

class Gesture(str, Enum):
    SINGLE_TAP = "single_tap"
    DOUBLE_TAP = "double_tap"
    LONG_PRESS = "long_press"
    VOICE_ACK = "voice_ack"

def approval_for(gesture):
    if gesture in (Gesture.SINGLE_TAP, Gesture.VOICE_ACK):
        return True
    if gesture == Gesture.LONG_PRESS:
        return False
    return None
