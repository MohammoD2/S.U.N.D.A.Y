import os
import sys
import random
import threading
import time
import tkinter as tk
from tkinter import scrolledtext
sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))

from FUNCTION.Zaki_listan.listan import listen
from FUNCTION.zaki_speak.speak import speak
from BRAIN.brain import brain_cmd
from AUTOMATION.INTEGRATION_ANIMATION.integretion_animation import Automation
from FUNCTION.INTEGRETION_FUNCTION.integration_funtion import Function_cmd
from DATA.zaki_dlg_dataset.DLG import *

class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistant GUI")
        self.create_widgets()
        
    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=15)
        self.text_area.grid(column=0, row=0, padx=10, pady=10)
        
        self.start_button = tk.Button(self.root, text="Start Assistant", command=self.start_assistant)
        self.start_button.grid(column=0, row=1, padx=10, pady=10)
        
    def start_assistant(self):
        t1 = threading.Thread(target=self.main_loop)
        t1.start()
    
    def main_loop(self):
        while True:
            wake_cmd = listen().lower()
            if wake_cmd in wake_key_word:
                self.update_text_area("Wake word detected")
                self.comain()
            time.sleep(0.5)
    
    def comain(self):
        while True:
            text = listen().lower()
            Automation(text)
            Function_cmd(text)
            if text in bye_key_word:
                x = random.choice(res_bye)
                speak(x)
                self.update_text_area(x)
                break
            elif "sunday" in text:
                response = brain_cmd(text)
                speak(response)
                self.update_text_area(response)
            time.sleep(0.5)
    
    def update_text_area(self, message):
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()
