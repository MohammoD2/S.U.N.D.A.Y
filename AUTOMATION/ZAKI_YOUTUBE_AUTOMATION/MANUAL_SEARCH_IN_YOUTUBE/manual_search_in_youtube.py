import pyautogui as ui
import random
import time
import sys
import os

# Add dataset and speak paths to system path
sys.path.append(os.path.abspath(os.path.dirname("DATA")))
from DATA.zaki_dlg_dataset.DLG import s2, s1  # Import dialog responses
from FUNCTION.zaki_speak.speak import speak  # Import text-to-speech function

def search_manual(text):
    text = text.replace("search", "").strip()  # Clean the input text
    ui.press("/")  
    ui.hotkey('ctrl', 'a')  
    ui.press('backspace') 
    # Type the new query
    ui.write(text)
    # Speak a random response from s1
    s12 = random.choice(s1)
    speak(s12)
    time.sleep(0.5)  # Wait before executing the search
    ui.press("enter")  # Execute the search
    # Speak a random response from s2 after search
    s12 = random.choice(s2)
    speak(s12)



