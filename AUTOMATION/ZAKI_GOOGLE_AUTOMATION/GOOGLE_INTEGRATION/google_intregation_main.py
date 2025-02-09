import os
import sys

# Append paths for the specified modules
sys.path.append(os.path.abspath(os.path.dirname("AUTOMATION")))

# Import necessary modules
from AUTOMATION.ZAKI_GOOGLE_AUTOMATION.TAB_AUTOMATION.tab_automation import *
from AUTOMATION.ZAKI_GOOGLE_AUTOMATION.SEARCH_IN_GOOGLE.search_in_google import *
from AUTOMATION.ZAKI_GOOGLE_AUTOMATION.SCROLE_AUTOMATION.scrole_automation import *
from AUTOMATION.ZAKI_GOOGLE_AUTOMATION.GOOGLE_OPEN_WEBSITE.open_website import *
from AUTOMATION.ZAKI_GOOGLE_AUTOMATION.GOOGLE_OPEN_WEBSITE.open import *
from DATA.zaki_dlg_dataset.DLG import *

def google_cmd(text):
    text = text.lower().strip()

    # Handle opening websites
    if "open" in text:
        text = text.replace("open", "").replace("website", "").replace("site", "").strip()
        if text:
            try:
                openweb(text)
                return True  # Stop after opening a website
            except :
                print(f"Error opening website: {e}")
        return False
    if "open" in text:
        text = text.replace("open", "").replace("website", "").replace("site", "").strip()
        if text:
            try:
                openweb(text)
                return True  # Stop after opening a website
            except :
                print(f"Error opening website: {e}")
        return False
    

    # Handle Google search
    elif "search in google" in text or "search on google" in text:
        text = text.replace("search in google", "").replace("search on google", "").strip()
        if text:
            try:
                search_google(text)
                return True  # Stop after handling the search
            except Exception as e:
                print(f"Error searching on Google: {e}")
        return False

    # Handle browser actions
    action_map = {
        tuple(y1): scroll_up,
        tuple(y2): scroll_down,
        tuple(y3): scroll_to_top,
        tuple(y4): scroll_to_bottom,
        tuple(y5): close_tab,
        tuple(y6): open_browser_menu,
        tuple(y7): zoom_in,
        tuple(y8): zoom_out,
        tuple(y9): refresh_page,
        tuple(y10): switch_to_next_tab,
        tuple(y11): switch_to_previous_tab,
        tuple(y12): open_history,
        tuple(y13): open_bookmarks,
        tuple(y14): go_back,
        tuple(y15): go_forward,
        tuple(y16): open_dev_tools,
        tuple(y17): toggle_full_screen,
        tuple(y18): open_private_window,
        tuple(y19): open_new_tab,
    }

    # Find and execute the matching action
    for keywords, action in action_map.items():
        if text in keywords:
            try:
                action()
                return True  # Action executed, stop further processing
            except Exception as e:
                print(f"Error executing command: {e}")
            break

    else:
        pass
