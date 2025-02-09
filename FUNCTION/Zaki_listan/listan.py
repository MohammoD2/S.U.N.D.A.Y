# import speech_recognition as sr
# import eel

# eel.init(r"E:\Work files\Ai\Z.A.K.I\web")

# @eel.expose
# def listen():
#     recognizer = sr.Recognizer()
#     recognizer.dynamic_energy_threshold = False
#     recognizer.energy_threshold = 34000
#     recognizer.dynamic_energy_adjustment_damping = 0.010
#     recognizer.dynamic_energy_ratio = 1.0
#     recognizer.pause_threshold = 0.8  # Increased to prevent cutting off speech
#     recognizer.operation_timeout = None
#     recognizer.non_speaking_duration = 0.5  # Slightly increased for better silence detection

#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source, duration=1)  # Longer duration for noise adjustment
#         while True:
#             print("I am Listening...", end="", flush=True)
#             try:
#                 audio = recognizer.listen(source, timeout=None)
#                 print("\rGot it, Now Recognizing...", end="", flush=True)
#                 recognized_txt = recognizer.recognize_google(audio).lower()
#                 if recognized_txt:
#                     print(f"\rMohammod Ibrahim: {recognized_txt}")
#                     return recognized_txt
#                 else:
#                     print("\rCould not recognize speech.", flush=True)
#                     return ""
#             except sr.UnknownValueError:
#                 print("\rSorry, I didn't catch that. Please try again.", flush=True)
#                 continue
#             except sr.RequestError as e:
#                 print(f"\rGoogle Speech Recognition service error: {e}")
#                 return ""
#             finally:
#                 print("\r", end="", flush=True)

# while True:
#     listen()


# import speech_recognition as sr
# import eel
# from googletrans import Translator, LANGUAGES
# import sys ,os
# sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))
# from FUNCTION.zaki_speak.speak import *

# eel.init(r"E:\Work files\Ai\Z.A.K.I\web")

# translator = Translator()
# translator_active = False  # Flag to track if translator is active

# @eel.expose
# def listen():
#     global translator_active  # Access the global variable to track translation status
#     recognizer = sr.Recognizer()
#     recognizer.dynamic_energy_threshold = False
#     recognizer.energy_threshold = 34000
#     recognizer.dynamic_energy_adjustment_damping = 0.010
#     recognizer.dynamic_energy_ratio = 1.0
#     recognizer.pause_threshold = 0.8  # Increased to prevent cutting off speech
#     recognizer.operation_timeout = None
#     recognizer.non_speaking_duration = 0.5  # Slightly increased for better silence detection

#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source, duration=1)  # Longer duration for noise adjustment
#         while True:
#             print("I am Listening...", end="", flush=True)
#             try:
#                 audio = recognizer.listen(source, timeout=None)
#                 print("\rGot it, Now Recognizing...", end="", flush=True)
#                 recognized_txt = recognizer.recognize_google(audio).lower()

#                 # Check if user commands to activate/deactivate translator
#                 if "activate translator" in recognized_txt:
#                     translator_active = True
#                     speak("Activating the Translator Sir...")
#                     print("\rTranslator activated.")
#                     continue  # Continue listening after activating

#                 elif "deactivate" in recognized_txt:
#                     translator_active = False
#                     speak("I am deactivated the Translator Sir...")
#                     print("\rTranslator deactivated.")
#                     continue  # Continue listening after deactivating

#                 # If translator is active, detect and translate the language
#                 if translator_active:
#                     # Detect the language of the recognized text
#                     detected_lang = translator.detect(recognized_txt).lang
                    
#                     # Translate to English if it's not already in English
#                     if detected_lang != 'en':
#                         translated_text = translator.translate(recognized_txt, dest='en').text
#                         print(f"\rMohammod Ibrahim (Detected Language: {LANGUAGES[detected_lang]}): {translated_text}")
#                     else:
#                         print(f"\rMohammod Ibrahim: {recognized_txt}")
#                 else:
#                     # Just print the recognized text without translation
#                     print(f"\rMohammod Ibrahim: {recognized_txt}")
                
#                 return recognized_txt
#             except sr.UnknownValueError:
#                 print("\rSorry, I didn't catch that. Please try again.", flush=True)
#                 continue
#             except sr.RequestError as e:
#                 print(f"\rGoogle Speech Recognition service error: {e}")
#                 return ""
#             finally:
#                 print("\r", end="", flush=True)
# import speech_recognition as sr
# import eel
# import sys, os
# sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))
# from FUNCTION.zaki_speak.speak import *

# def listen():
#     recognizer = sr.Recognizer()
#     recognizer.dynamic_energy_threshold = False
#     recognizer.energy_threshold = 34000
#     recognizer.dynamic_energy_adjustment_damping = 0.010
#     recognizer.dynamic_energy_ratio = 1.0
#     recognizer.pause_threshold = 0.8  # Increased to prevent cutting off speech
#     recognizer.operation_timeout = None
#     recognizer.non_speaking_duration = 0.10  # Slightly increased for better silence detection

#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source, duration=1)  # Longer duration for noise adjustment
#         while True:
#             print("I am Listening...", end="", flush=True)
#             try:
#                 audio = recognizer.listen(source, timeout=None)
#                 print("\rGot it, Now Recognizing...", end="", flush=True)
#                 recognized_txt = recognizer.recognize_google(audio).lower()

#                 # Check if user commands to activate/deactivate a feature (previously translator)
#                 if "activate feature" in recognized_txt:
#                     speak("Activating the feature Sir...")
#                     print("\rFeature activated.")
#                     continue  # Continue listening after activating

#                 elif "deactivate feature" in recognized_txt:
#                     speak("I am deactivating the feature Sir...")
#                     print("\rFeature deactivated.")
#                     continue  # Continue listening after deactivating

#                 # Just print the recognized text
#                 print(f"\rMohammod Ibrahim: {recognized_txt}")
                
#                 return recognized_txt
#             except sr.UnknownValueError:
#                 print("\rSorry, I didn't catch that. Please try again.", flush=True)
#                 continue
#             except sr.RequestError as e:
#                 print(f"\rGoogle Speech Recognition service error: {e}")
#                 return ""
#             finally:

#                 print("\r", end="", flush=True)
# while True:
#     listen()
import os
import sys
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import eel

sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))
from FUNCTION.zaki_speak.speak import *

# Load the Vosk model
model_path = r"D:\Work file\S.U.N.D.A.Y\FUNCTION\vosk-model-en-us-0.22-lgraph"  # Ensure the model is in this directory or update the path
if not os.path.exists(model_path):
    print("Please download a Vosk model and unpack it into the 'model' directory.")
    sys.exit(1)

model = Model(model_path)

# Audio recording parameters
samplerate = 16000  # Sampling rate in Hz
device = None       # Use default audio input device
blocksize = 8000    # Number of samples per block

def listen():
    recognizer = KaldiRecognizer(model, samplerate)
    audio_queue = queue.Queue()

    def audio_callback(indata, frames, time, status):
        """Callback for audio input."""
        if status:
            print(f"Audio error: {status}", flush=True)
        audio_queue.put(bytes(indata))

    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize, dtype="int16",
                           channels=1, callback=audio_callback, device=device):
        print("I am Listening...", end="", flush=True)
        while True:
            try:
                # Retrieve audio data from the queue
                data = audio_queue.get()
                if recognizer.AcceptWaveform(data):
                    # Process the recognized speech
                    result = json.loads(recognizer.Result())
                    recognized_txt = result.get("text", "").lower()

                    if recognized_txt:
                        # Handle specific commands
                        if "activate feature" in recognized_txt:
                            speak("Activating the feature Sir...")
                            print("\rFeature activated.")
                            continue

                        elif "deactivate feature" in recognized_txt:
                            speak("I am deactivating the feature Sir...")
                            print("\rFeature deactivated.")
                            continue

                        # Print the recognized text
                        print(f"\rMohammod Ibrahim: {recognized_txt}")
                        return recognized_txt
            except Exception as e:
                print(f"\rAn error occurred: {e}")
                return ""
