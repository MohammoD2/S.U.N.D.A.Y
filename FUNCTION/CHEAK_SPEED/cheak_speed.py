import sys, os
import time
import speedtest

sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))
from FUNCTION.zaki_speak.speak import speak

def get_internet_speed():
    speak("Checking your internet speed, sir... please wait...")
    st = speedtest.Speedtest()
    # Fetch best server based on ping
    st.get_best_server()
    # Perform download and upload speed tests
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping
    return download_speed, upload_speed, ping

def check_internet_speed():
    try:
        download_speed, upload_speed, ping = get_internet_speed()
        # Shortened speech with slight pauses
        speak(f"Sir, your download speed is {download_speed:.2f} Mbps.")
        speak(f"Your upload speed is {upload_speed:.2f} Mbps.")
        speak(f"And your ping is {ping} milliseconds.")
    except Exception as e:
        speak("Error: Unable to retrieve internet speed.")
        print(f"An error occurred: {e}")

# check_internet_speed()
