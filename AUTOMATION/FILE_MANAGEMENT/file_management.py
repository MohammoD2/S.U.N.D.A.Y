import sys, os
sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))
from AUTOMATION.FILE_MANAGEMENT.Open_file import *

from FUNCTION.zaki_speak.speak import speak
from FUNCTION.Zaki_listan.listan import listen


def file_management(text):
    if "go to the" in text:
        text = text.replace("go to the", "").strip()
    go_to_folder_or_file(text)
    if "create a folder" in text:
        speak("tell the folder name sir")
        text= listen()
        create_folder(text)
    if "create a text file" in text:
        speak("tell the text file  name sir")
        text1= listen()
        speak("what should i write in the text file Sir")
        text2=listen()
        create_text_file(text1,text2)
    if "create a python file" in text:
        speak("tell the python file  name sir")
        text1= listen()
        create_python_file(text1)
    if "create a html file" in text:
        speak("tell the html file  name sir")
        text1= listen()
        create_html_file(text1)
    if "create a css file" in text:
        speak("tell the css file  name sir")
        text1= listen()
        create_css_file(text1)
    if "create a javascript file" in text:
        speak("tell the javascript file  name sir")
        text1= listen()
        create_javascript_file(text1)
