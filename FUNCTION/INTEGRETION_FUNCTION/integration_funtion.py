
import os ,sys
sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))
from FUNCTION.CHEAK_SPEED.cheak_speed import  check_internet_speed
from FUNCTION.CLOCk.clock import *

def Function_cmd(text):
    if "check my internet speed" in text or "check internet" in text or "speed test" in text:
        check_internet_speed()
        return True
    if "What is the time right now" in text or "tell me the time" in text or "say time" in text or "time" in text:
        what_is_the_time()
        return True
    else:
        return False