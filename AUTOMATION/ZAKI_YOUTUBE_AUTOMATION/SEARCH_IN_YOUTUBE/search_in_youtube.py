import random
import time
import pyautogui as ui
import webbrowser
import os 
import sys
sys.path.append(os.path.abspath(os.path.dirname("DATA")))
from DATA.zaki_dlg_dataset.DLG import yt_search, s1, s2
from FUNCTION.zaki_speak.speak import speak
def youtube_search(text):
    dlg = random.choice(yt_search)
    speak(dlg)
    webbrowser.open("https://www.youtube.com/")
    time.sleep(5)
    ui.press("/")
    ui.write(text)
    s12 = random.choice(s1)
    speak( s12 )
    time.sleep(0.5)
    ui.press("enter")
    s12 = random.choice(s2)
    speak(s12)
