import random
import time
import threading
import sys
import os

# Add necessary directories to the Python path
sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))

# Import necessary modules
from FUNCTION.Zaki_listan.listan import listen
from FUNCTION.zaki_speak.speak import speak
from BRAIN.brain import brain_cmd
from AUTOMATION.INTEGRATION_ANIMATION.integretion_animation import Automation
from FUNCTION.INTEGRETION_FUNCTION.integration_funtion import Function_cmd
from DATA.zaki_dlg_dataset.DLG import res_bye, bye_key_word, wake_key_word, welcomedlg
from BRAIN.CHATBOT.chatbot import generate_response
# from playsound import playsound  # Uncomment if needed


def comain():
    """
    Handles continuous command input once the wake word is detected.
    Executes tasks based on automation, function commands, or general responses.
    """
    while True:
        try:
            text = listen().lower()

            # Automation and Function Command Handling
            automation_handled = Automation(text)  # Returns True if handled
            function_handled = Function_cmd(text)  # Returns True if handled

            if (
                not automation_handled
                and not function_handled
                and not any(kw in text for kw in bye_key_word)
                and "sunday" not in text
            ):
                print(f"Passing to generate_response: {text}")  # Debugging log
                generate_response(text)


            # Handle exit keywords
            if any(kw in text for kw in bye_key_word):
                farewell = random.choice(res_bye)
                speak(farewell)
                break

            # Special handling for "sunday" keyword
            if "sunday" in text:
                response = brain_cmd(text)
                speak(response)
        except Exception as e:
            print(f"Error in comain: {e}")
            speak("I encountered an issue. Please try again.")


def main():
    """
    Listens for the wake word to activate the AI assistant.
    """
    while True:
        try:
            wake_cmd = listen().lower()

            # Activate main functionality if a wake word is detected
            if any(keyword in wake_cmd for keyword in wake_key_word):
                welcome_message = random.choice(welcomedlg)
                speak(welcome_message)
                comain()

            # Optional: Avoid busy looping
            time.sleep(0.5)
        except Exception as e:
            print(f"Error in main loop: {e}")
            speak("An error occurred while listening. Please try again.")


def sunday():
    """
    Runs the AI assistant in a threaded environment to support additional features.
    """
    try:
        # Main thread for listening and handling commands
        main_thread = threading.Thread(target=main)

        # Placeholder for future threads (e.g., battery alerts, online checks, etc.)
        # battery_thread = threading.Thread(target=battery_alert)
        # plugin_status_thread = threading.Thread(target=check_plugin_status)
        # online_checker_thread = threading.Thread(target=realtime_online_checker)

        # Start the threads
        main_thread.start()
        # battery_thread.start()
        # plugin_status_thread.start()
        # online_checker_thread.start()

        # Ensure all threads complete execution
        main_thread.join()
        # battery_thread.join()
        # plugin_status_thread.join()
        # online_checker_thread.join()
    except Exception as e:
        print(f"Error in sunday: {e}")
        speak("An error occurred while starting the assistant.")


if __name__ == "__main__":
    """
    Entry point for the AI assistant.
    """
    sunday()
# def comain():
#     while True:
#         text = listen().lower()
#         Automation(text)
#         Function_cmd(text)
#         if text in bye_key_word:
#             x = random.choice(res_bye)
#             speak(x)
#             break
#         elif "sunday" in text:
#             response =  brain_cmd(text)
#             speak(response)
#         else:
#             pass


# def main():
#     while True:
#         wake_cmd = listen().lower()
#         if any(keyword in wake_cmd for keyword in wake_key_word):
#             welcome_message = random.choice(welcomedlg)
#             speak(welcome_message)
#             comain()
#         else:
#             pass


# def jarvis():
#     t1 = threading.Thread(target=main)
#     t1.start()
#     t1.join()

# jarvis()