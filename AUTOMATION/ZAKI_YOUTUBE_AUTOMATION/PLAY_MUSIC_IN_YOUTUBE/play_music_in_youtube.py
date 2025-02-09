import sys
import os

# Get the absolute path of the Z.A.K.I directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.dirname("DATA")))

import time
import pywhatkit as kt
import random
from DATA.zaki_dlg_dataset.DLG import playsong, playing_dlg
from FUNCTION.zaki_speak.speak import speak

def play_music_on_youtube(text):
    playdlg = random.choice(playsong)
    speak(playdlg)
    kt.playonyt(text)
    time.sleep(3)
    playdlg = random.choice(playing_dlg)
    speak(playdlg + text)

