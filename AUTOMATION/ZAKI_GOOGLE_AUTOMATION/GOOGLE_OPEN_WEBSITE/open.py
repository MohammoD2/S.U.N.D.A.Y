import time
import pyautogui as ui
import os, sys
sys.path.append(os.path.abspath(os.path.dirname("DATA")))
from DATA.zaki_dlg_dataset.DLG import open_dld
import random
from FUNCTION.zaki_speak.speak import speak



def open(text):
    # Select a random dialogue to announce the search
    x = random.choice(open_dld)
    
    # Announce the search action
    speak(x + text)
    
    # Pause briefly before initiating actions
    time.sleep(0.5)
    
    # Switch to Chrome or open it if it's not already open
    ui.hotkey("alt", "tab")  # Assumes Chrome is already open, otherwise use the Windows key to open it.
    
    # Pause to allow the browser to come into focus
    time.sleep(0.5)
    
    # Highlight the address bar using a common Chrome shortcut
    ui.hotkey("ctrl", "l")  # This selects the URL bar
    
    # Pause to ensure the address bar is selected
    time.sleep(0.2)
    
    # Type the search term or website
    ui.write(text)
    
    # Pause briefly after typing
    time.sleep(0.5)
    
    # Press "Enter" to execute the search or go to the website
    ui.press("enter")

# Call the function with your search term or website

