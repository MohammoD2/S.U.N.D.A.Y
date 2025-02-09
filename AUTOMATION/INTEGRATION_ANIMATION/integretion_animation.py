import os, sys
sys.path.append(os.path.abspath(os.path.dirname("AUTOMATION")))

# Import automation modules
from AUTOMATION.ZAKI_GOOGLE_AUTOMATION.GOOGLE_INTEGRATION.google_intregation_main import *
from AUTOMATION.ZAKI_YOUTUBE_AUTOMATION.YOUTUBE_INTEGRATION_MAIN.youtube_intregation_main import *
from AUTOMATION.COMMON_INTREGRATION.common_intregretion import *
from AUTOMATION.FILE_MANAGEMENT.file_management import *

def Automation(text):
    # Check for YouTube command first
    if youtube_cmd(text):
        return True  # If YouTube command handled the text, return
    
    # Check for Google command next
    if google_cmd(text):
        return True  # If Google command handled the text, return

    # Check for common commands last
    if common_cmd(text):
        return True  # If common command handled the text, return

    
    


    # If no command was handled, return False
    return False

