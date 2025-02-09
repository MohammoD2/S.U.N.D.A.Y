import random
import pyautogui as ui
import os, sys
sys.path.append(os.path.abspath(os.path.dirname("DATA")))
from DATA.zaki_dlg_dataset.DLG import closedlg
from FUNCTION.zaki_speak.speak import speak

closedlg_random = random.choice(closedlg)
def close():
    speak(closedlg_random)
    ui.hotkey("alt","f4")
    