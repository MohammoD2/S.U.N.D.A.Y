import os, sys
sys.path.append(os.path.abspath(os.path.dirname("AUTOMATION")))
from AUTOMATION.COMMON_INTREGRATION.close import *


def common_cmd(text):
    if "close" in text :
        close()
    else:
        pass