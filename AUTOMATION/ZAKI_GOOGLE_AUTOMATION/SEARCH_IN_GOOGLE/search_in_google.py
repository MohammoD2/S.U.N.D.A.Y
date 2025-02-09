import pywhatkit
import random
import os, sys
sys.path.append(os.path.abspath(os.path.dirname("DATA")))
from DATA.zaki_dlg_dataset.DLG import search_result
from FUNCTION.zaki_speak.speak import speak


def search_google(text):
    dlg = random.choice(search_result)
    pywhatkit.search(text)
    speak(dlg)
