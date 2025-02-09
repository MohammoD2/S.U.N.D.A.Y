# import sys, os
# sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))  # Fixed potential typo

# from FUNCTION.zaki_speak.speak import *
# from BRAIN.GOOGLE_BIG_DATA.google_big_data import *
# from BRAIN.GOGGLE_SMALL_DATA.google_small_data import *

# # Function to load the Q&A data from a file into a dictionary
# def load_qa_data(file_path):
#     qa_dict = {}
#     with open(file_path, "r", encoding="utf-8", errors="replace") as f:
#         for line in f:
#             line = line.strip()
#             if not line:
#                 continue
#             parts = line.split(":")
#             if len(parts) != 2:
#                 continue
#             q, a = parts
#             qa_dict[q.strip()] = a.strip()  # Ensure question and answer are stripped of extra spaces
#     return qa_dict

# # Specify the path to your Q&A file
# qa_file_path = r"E:\Work files\Ai\S.U.N.D.A.Y\DATA\BRAIN_DATA\qna.txt"
# qa_dict = load_qa_data(qa_file_path)

# # Main command processing function
# def brain_cmd(text):
#     if "sunday" in text.lower():  # Case-insensitive check for "Zaki"
#         text = text.replace("sunday", "").strip()  # Clean up "Zaki" from the input

#         if text in qa_dict:  # Check for predefined Q&A
#             ans = qa_dict[text]
#             speak(ans)
#         elif "define" in text:  # Handle "define" queries
#             ans = deep_search(text)
#             speak(ans)
#         else:  # Handle general search queries
#             ans = search_and_extract(text)
#             speak(ans)

#         return ans  # Return the final answer
#     else:
#         return None  # Return None if "Zaki" is not in the text

import sys, os
sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))  # Fixed potential typo

from FUNCTION.zaki_speak.speak import *  # Speak function import
from FUNCTION.Zaki_listan.listan import *  # Listen function import
from BRAIN.GOOGLE_BIG_DATA.google_big_data import *  # Big data search import
from BRAIN.GOGGLE_SMALL_DATA.google_small_data import *  
from BRAIN.KNOWLEDGE_BOT.bot import *# Small data search import

def brain_cmd(text):
    if "sunday" in text.lower():  # Case-insensitive check for "Sunday"
        text = text.replace("sunday", "").strip()  # Clean up "Sunday" from the input
        gen_bot(text)
    else:
        return None  # Return None if "Sunday" is not in the text

#         if "i want to know about" in text:  # Check for the query pattern
#             # Extract the word/phrase after "i want to know about"
#             query = text.split("i want to know about", 1)[1].strip()  # Get the part after the phrase
#             ans = wiki(query)  # Perform a deep search with the extracted query
#             print(f"Define Result: {ans}")
#  # Debugging: print search result
#         else:  # Handle general search queries
#             ans = google_search(text)  # Perform a general search # Call speak function to vocalize the response
#             print(f"Search Result: {ans}")  # Debugging: print search result

#         return ans  # Return the final answer
#     else:
#         return None  # Return None if "Sunday" is not in the text

# brain_cmd("Sunday tell me a small joke ")