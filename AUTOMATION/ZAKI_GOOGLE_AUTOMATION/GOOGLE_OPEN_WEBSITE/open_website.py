import random
import difflib
import webbrowser
import os, sys
from AppOpener import open as open_app

sys.path.append(os.path.abspath(os.path.dirname("DATA")))
from DATA.zaki_dlg_dataset.DLG import websites, open_dld, success_open, open_maybe, sorry_open
from FUNCTION.zaki_speak.speak import speak


def openweb(text):
    # Convert the input to lowercase for case-insensitive matching
    text_lower = text.lower()

    # Step 1: Try to open as a website
    if text_lower in websites:
        try:
            random_dlg = random.choice(open_dld)
            speak(random_dlg + text)
            url = websites[text_lower]
            webbrowser.open(url)
            randonsuccess = random.choice(success_open)
            speak(randonsuccess)
            return  # Exit if successful
        except Exception as e:
            print(f"Failed to open website '{text}': {e}")

    # Step 2: If website opening fails, try to open as a desktop application
    try:
        random_maybe = random.choice(open_maybe)
        speak(random_maybe + text)
        open_app(text, match_closest=True)  # AppOpener functionality
        randonsuccess = random.choice(success_open)
        speak(randonsuccess)
        return  # Exit if successful
    except Exception as e:
        print(f"Failed to open application '{text}': {e}")

    # Step 3: If both website and application fail, try closest match using difflib
    matches = difflib.get_close_matches(text_lower, websites.keys(), n=1, cutoff=0.6)
    if matches:
        try:
            closest_match = matches[0]
            random_dlg = random.choice(open_dld)
            speak(random_dlg + " " + closest_match)
            url = websites[closest_match]
            webbrowser.open(url)
            randonsuccess = random.choice(success_open)
            speak(randonsuccess)
        except Exception as e:
            print(f"Failed to open closest match website '{closest_match}': {e}")
    else:
        # Step 4: No application or website found
        randonsorry = random.choice(sorry_open)
        speak(randonsorry + " named " + text)


# # Example usage
# openweb("clock")  # First tries website, then application
# # No match for application or website
