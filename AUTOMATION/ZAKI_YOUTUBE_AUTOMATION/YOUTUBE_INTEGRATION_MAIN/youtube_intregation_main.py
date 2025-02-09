import sys
import os
import random
sys.path.append(os.path.abspath(os.path.dirname("DATA")))
sys.path.append(os.path.abspath(os.path.dirname("FUNTION")))
from AUTOMATION.ZAKI_YOUTUBE_AUTOMATION.ANOTHER_AUTOMATION_IN_YOUTUBE.Another_Automation_in_youtube import *
from AUTOMATION.ZAKI_YOUTUBE_AUTOMATION.CAPTION_IN_VEDIO.caption_in_video import *
from AUTOMATION.ZAKI_YOUTUBE_AUTOMATION.MANUAL_SEARCH_IN_YOUTUBE.manual_search_in_youtube import *
from AUTOMATION.ZAKI_YOUTUBE_AUTOMATION.PLAY_MUSIC_IN_YOUTUBE.play_music_in_youtube import *
from AUTOMATION.ZAKI_YOUTUBE_AUTOMATION.PLAY_PAUSE_VIDEO_IN_YOUTUBE.play_pause_video_in_youtube import *
from AUTOMATION.ZAKI_YOUTUBE_AUTOMATION.SEARCH_IN_YOUTUBE.search_in_youtube import *
from DATA.zaki_dlg_dataset.DLG import *
from FUNCTION.Zaki_listan.listan import listen

# Add dataset path to system path
def youtube_cmd(text):
    # Check if the text contains a known play command
    matching_command = next((command for command in x if command in text), None)
    
    if matching_command:
        # Extract the song name by removing the found command part
        song_name = text.replace(matching_command, "")
        play_music_on_youtube(song_name)

    # Other controls (playback, volume, etc.) remain unchanged
    elif text in x1:
        stop()
    elif text in x2:
        play()

    
    # Volume control
    elif text in x3:
        volume_up()
    elif text in x4:
        volume_down()
    elif text in x5:
        seek_forward()
    elif text in x6:
        seek_backward()
    elif text in x7:
        seek_forward_10s()
    elif text in x8:
        seek_backward_10s()
    elif text in x9:
        seek_to_beginning()
    elif text in x10:
        seek_to_end()
    elif text in x11:
        seek_to_previous_chapter()
    elif text in x12:
        seek_to_next_chapter()
    elif text in x13:
        increase_playback_speed()
    elif text in x14:
        decrease_playback_speed()
    elif text in x15:
        move_to_next_video()
    elif text in x16:
        move_to_previous_video()
    elif text in x17:
        toggle_subtitles()
    elif text in x18:
        increase_font_size()
    elif text in x19:
        decrease_font_size()
    elif text in x20:
        rotate_text_opacity()
    elif text in x21:
        rotate_window_opacity()
    elif text in x22:
        pan_up()
    elif text in x23:
        pan_down()
    elif text in x24:
        pan_left()
    elif text in x25:
        pan_right()
    elif text in x26:
        zoom_in()
    elif text in x27:
        zoom_out()
    
    # Search-related commands
    elif "search in youtube" in text or "search on youtube" in text:
        query = text.replace("search in youtube", "").replace("search on youtube", "").strip()
        youtube_search(query)
    elif "search in current youtube window" in text or text.startswith("search"):
        query = (text.replace("search in current youtube window", "")
                      .replace("search on current youtube window", "")
                      .replace("search current youtube window", "")
                      .replace("search", "")
                      .strip())
        search_manual(query)
    
    # Playback, mute, and screen mode toggles
    elif text in x28:
        toggle_play_pause()
    elif text in x29:
        toggle_mute_unmute()
    elif text in x30:
        toggle_full_screen()
    elif text in x31:
        toggle_theater_mode()
    elif text in x32:
        toggle_miniplayer_mode()
    elif text in x33:
        toggle_party_mode()
    elif text in x34:
        navigate_forward()
    elif text in x35:
        
        navigate_backward()
    
    else:
        pass  # If no command matches, do nothing
    