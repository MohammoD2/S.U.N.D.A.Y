import os
import sys
import random
import time
import threading
# Update the system path to include the "FUNCTION" directory
sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))
# Import necessary modules
from FUNCTION.Zaki_listan.listan import listen
from FUNCTION.zaki_speak.speak import speak
from BRAIN.brain import brain_cmd
from AUTOMATION.INTEGRATION_ANIMATION.integretion_animation import Automation
from FUNCTION.INTEGRETION_FUNCTION.integration_funtion import Function_cmd
from DATA.zaki_dlg_dataset.DLG import *
from BRAIN.CHATBOT.chatbot import generate_response

def comain():
    while True:
        text = listen().lower()

        # Track whether Automation or Function_cmd handle the input
        automation_handled = Automation(text)  # Returns True if handled, False otherwise
        function_handled = Function_cmd(text)  # Returns True if handled, False otherwise
        
        # If neither Automation nor Function_cmd handle the input, call generate_response
        if not automation_handled and not function_handled and not "sunday" in text :
            generate_response(text)

        if text in bye_key_word:
            x = random.choice(res_bye)
            speak(x)
            break
        elif "sunday" in text:
            response = brain_cmd(text)
            speak(response)
        else:
            pass


# Main loop to listen for the wake word
def main():
    while True:
        wake_cmd = listen().lower()

        # If wake word is detected, proceed to handle commands
        if any(keyword in wake_cmd for keyword in wake_key_word):
            welcomedlg1 = random.choice(welcomedlg)
            speak(welcomedlg1)
            comain()

        # Optional: Sleep a bit to avoid a busy loop
        time.sleep(0.5)

# Threaded execution for different functions
def sunday():
    # Main thread to listen for wake word and handle responses
    t1 = threading.Thread(target=main)
    
    # Future threads (e.g., for battery alerts, online checks, etc.)
    # t2 = threading.Thread(target=battery_alert)
    # t3 = threading.Thread(target=check_plugin_status)
    # t4 = threading.Thread(target=realtime_online_checker)

    # Start the threads
    t1.start()
    # t2.start()
    # t3.start()
    # t4.start()

    # Ensure all threads complete execution
    t1.join()
    # t2.join()
    # t3.join()
    # t4.join()

# Run the AI assistant
sunday()
