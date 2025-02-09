# import os
# import pygame
# import sys

# def resource_path(relative_path):
#     """ Get the absolute path to the resource, works for dev and for PyInstaller """
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)

# def speak(text, voice='en-US-EricNeural', file_name="D:\Work file\S.U.N.D.A.Y\data.mp3"):
#     try:
#         # Use edge-tts to generate the audio file
#         command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "{file_name}"'
#         os.system(command)
        
#         # Use resource_path to locate the file inside the PyInstaller package
#         file_name = resource_path(file_name)

#         # Check if the file was created
#         if not os.path.exists(file_name):
#             raise FileNotFoundError(f"Audio file '{file_name}' not found.")
        
#         # Initialize pygame mixer
#         pygame.init()
#         pygame.mixer.init()

#         # Load and play the audio
#         pygame.mixer.music.load(file_name)
#         pygame.mixer.music.play()

#         # Wait until the audio finishes playing
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)
    
#     except Exception as e:
#         print(f"Error: {e}")
    
#     finally:
#         # Stop and quit the mixer
#         pygame.mixer.music.stop()
#         pygame.mixer.quit()
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import undetected_chromedriver as uc

# chrome_options = uc.ChromeOptions()
# chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)

# # Create a Chrome driver instance with the specified options
# driver = webdriver.Chrome(options=chrome_options)

# # Navigate to the website
# driver.get("https://tts.5e7en.me/")

# # Navigate to the website

# def speak(text):
#     try:
#         # Wait for the element to be clickable
#         element_to_click = WebDriverWait(driver, 1).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
#         )

#         # Perform the click action
#         element_to_click.click()

#         # Input text into the element
#         text_to_input = text
#         element_to_click.send_keys(text_to_input)
#         print(text_to_input)

#         # Calculate sleep duration based on sentence length
#         sleep_duration = min(0.1 + len(text) // 5, 15)  # Minimum sleep is 3 seconds, maximum is 10 seconds

#         # Wait for the button to be clickable
#         button_to_click = WebDriverWait(driver, 2).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
#         )

#         # Perform the click action on the button
#         button_to_click.click()

#         # Sleep for dynamically calculated duration
#         time.sleep(sleep_duration)

#         # Clear the text box for the next sentence
#         element_to_click.clear()

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         # Handle the error as needed, e.g., log it, raise it again, etc.



import pyttsx3

def detect_style(text):
    """
    Detects the style of the text based on its content and punctuation.

    Parameters:
    - text (str): The input text.

    Returns:
    - style (str): Detected style ('happy', 'sad', 'angry', 'question', or 'normal').
    """
    text = text.strip().lower()
def detect_style(text):
    """
    Detects the style of the text based on its content and punctuation.

    Parameters:
    - text (str): The input text.

    Returns:
    - style (str): Detected style ('happy', 'sad', 'angry', 'question', or 'normal').
    """
    text = text.strip().lower()

# Happy words
    happy_words = [
            'happy', 'excited', 'amazing', 'great', 'wonderful', 'awesome', 'fantastic', 
            'joy', 'cheerful', 'delight', 'smile', 'love', 'peaceful', 'fun', 'enthusiastic', 
            'eager', 'brilliant', 'bright', 'superb', 'ecstatic', 'incredible', 'good', 
            'positive', 'hopeful', 'celebrate', 'sparkling', 'sunny', 'perfect', 'magic', 
            'beautiful', 'pleasure', 'grateful', 'elated', 'thrilled', 'energetic', 
            'optimistic', 'proud', 'laugh', 'success', 'win', 'gleeful', 'marvelous', 
            'radiant', 'cheery', 'blissful', 'jovial', 'bubbly', 'vibrant', 'uplifted', 
            'content', 'satisfied', 'blessed', 'jolly', 'hopeful', 'brightened', 'jovial'
        ]

        # Sad words
    sad_words = [
            'sad', 'sorry', 'unfortunate', 'bad', 'terrible', 'regret', 'miserable', 
            'unhappy', 'lonely', 'gloomy', 'disheartened', 'depressed', 'hurt', 
            'tears', 'broken', 'loss', 'cry', 'grief', 'pain', 'melancholy', 'dark', 
            'sorrow', 'blue', 'tragic', 'worried', 'low', 'heartache', 'down', 
            'mourn', 'helpless', 'defeated', 'pathetic', 'grim', 'discouraged', 
            'troubled', 'cold', 'negative', 'fading', 'forgotten', 'empty', 'weak', 
            'hopeless', 'hurtful', 'isolated', 'heavy', 'aching', 'weary', 'dismal', 
            'grief-stricken', 'hopeless', 'forlorn', 'unfortunate', 'desolate', 'despairing', 
            'sullen', 'disconsolate', 'pessimistic', 'dejection', 'doleful', 'unfulfilled', 
            'disappointed', 'empty-hearted', 'downhearted'
        ]

        # Angry words
    angry_words = [
            'angry', 'mad', 'furious', 'hate', 'disappointed', 'rage', 'annoyed', 
            'irritated', 'agitated', 'bitter', 'hostile', 'resentful', 'outraged', 
            'yell', 'shout', 'fume', 'blame', 'criticism', 'fight', 'unfair', 
            'offended', 'harsh', 'insult', 'provoked', 'intolerant', 'argument', 
            'tense', 'grudge', 'stormy', 'vindictive', 'hostility', 'revenge', 
            'frustrated', 'vengeful', 'conflict', 'irate', 'enraged', 'brutal', 
            'violent', 'wrathful', 'abusive', 'sarcastic', 'mocking', 'belligerent', 
            'scorn', 'sharp', 'heated', 'fury', 'incensed', 'infuriated', 'volatile', 
            'spiteful', 'irrational', 'venomous', 'defiant', 'unreasonable', 'enraged', 
            'raging', 'combative', 'irritability', 'reckless', 'rageful', 'belligerence', 
            'displeased', 'indignant'
        ]

        # Question words (extended)
    question_words = [
            'why', 'how', 'what', 'when', 'where', 'who', 'can', 'could', 'is', 'are', 
            'does', 'did', 'would', 'should', 'will', 'howcome', 'anyone', 'somewhere', 
            'someone', 'which', 'why not', 'wherefore', 'whereabouts', 'whatsoever', 
            'whenever', 'wherein', 'how long', 'how much', 'how many', 'what time', 
            'whom', 'what kind', 'how far', 'how fast', 'how often', 'whatsoever', 'couldn’t'
        ]




    # Detect style based on text content
    if text.endswith('?') or any(word in text for word in question_words):
        return 'question'
    elif any(word in text for word in happy_words):
        return 'happy'
    elif any(word in text for word in sad_words):
        return 'sad'
    elif any(word in text for word in angry_words):
        return 'angry'
    else:
        return 'normal'


def speak(text, voice_id=1, rate=150, volume=0.9):
    """
    Speaks the given text, automatically adjusting style based on the content.

    Parameters:
    - text (str): The text to be spoken.
    - voice_id (int): The ID of the desired voice.
    - rate (int): The speed of speech (default is 150 words per minute).
    - volume (float): The volume level (between 0.0 and 1.0, default is 0.9).

    Returns:
    - None
    """
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Fetch available voices and set the desired one
    voices = engine.getProperty('voices')
    if 0 <= voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
    else:
        engine.setProperty('voice', voices[0].id)  # Fallback to default voice

    # Adjust the speaking rate and volume
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Detect the style from the text
    style = detect_style(text)

    # Modify speaking style based on detection
    if style == 'happy':
        engine.setProperty('rate', rate + 30)  # Faster for a cheerful tone
        text = f"Wow! {text}"
    elif style == 'sad':
        engine.setProperty('rate', rate - 30)  # Slower for a melancholy tone
        text = f"Well... {text}. I hope things get better."
    elif style == 'angry':
        engine.setProperty('rate', rate + 50)  # Much faster for anger
        text = f"{text}! This is unbelievable!"
    elif style == 'question':
        text = f"{text}? Could you explain further?"
    else:
        # Normal speaking style
        text = text

    # Speak the text
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError as e:
        print(f"Error during speech synthesis: {e}")





