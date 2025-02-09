import random
import sys ,os
sys.path.append(os.path.abspath(os.path.dirname("DATA")))
from DATA.zaki_dlg_dataset.DLG import welcomedlg
from FUNCTION.zaki_speak.speak import speak


def welcome():
    welcome = random.choice(welcomedlg)
    speak(welcome)
welcome()