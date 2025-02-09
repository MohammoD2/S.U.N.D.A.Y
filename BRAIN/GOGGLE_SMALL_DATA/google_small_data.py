# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import re
# from selenium.webdriver.support.wait import WebDriverWait
# import undetected_chromedriver as uc
# import nltk
# # Download the 'punkt' tokenizer
# nltk.download('punkt')

# chrome_options = uc.ChromeOptions()
# chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)

# # Specify the path to your own ChromeDriver
# driver_path = 'e:\\OneDrive\\Desktop\\chromedriver.exe'  # Use double backslashes or raw string
# service = Service(driver_path)  # Create a Service object with the driver path

# # Create a Chrome driver instance with the specified options
# driver = webdriver.Chrome(service=service, options=chrome_options)

# def search_and_extract(text):
#     try:
#         # Open Google in the browser
#         driver.get("https://www.google.com")

#         # Find the search box using its name attribute value
#         search_box = driver.find_element("name", "q")

#         # Clear the search box content
#         search_box.clear()

#         # Type the search query
#         search_box.send_keys(text)

#         # Submit the form
#         search_box.send_keys(Keys.RETURN)

#         # Wait for a few seconds (you may need to adjust this based on your internet speed)
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

#         # Find the first search result element
#         first_result = driver.find_element(By.CSS_SELECTOR, 'div.g')

#         # Extract the text from the first search result
#         first_result_text = first_result.text
#         sentences = re.split(r'(?<=[.!?])\s', first_result_text)

#         # Filter out sentences containing common link and date patterns
#         filtered_sentences = [sentence for sentence in sentences if not re.search(r'https?://\S+|(\d{1,2} [A-Za-z]+ \d{10})', sentence)]

#         # Join the remaining sentences into one single line
#         result_text = ' '.join(filtered_sentences[:10])  # Limiting to the first 10 sentences if needed
#         result_text = result_text.replace("Featured snippet from the web", "")
        
#         # Clean the result text
#         result_text = re.sub(r'[^a-zA-Z0-9\s\.]', '', result_text)
        
#         # Merge the filtered sentences into a single line
#         final_result = " ".join(result_text.split())

#         # Print the final extracted text
#         print("Merged Extracted Text: ", final_result)

#         # Call the speak function to read out the text
#         speak(final_result)
#     except Exception as e:
#         print("An error occurred:", e)

import requests
import re
import sys, os
sys.path.append(os.path.abspath(os.path.dirname("FUNCTION")))
from FUNCTION.zaki_speak.speak import speak

def google_search(query):
    api_key = "AIzaSyBjHZNMLJZRTU6RzNgXiKw7aJGNhU6toOs"
    cse_id = "430a3db99edb24403"
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}"
    response = requests.get(url)
    results = response.json()

    search_results = []
    
    if 'items' in results:
        for item in results['items']:
            snippet = item.get('snippet', 'N/A')
            # Use the first sentence of the snippet for a concise output
            first_sentence = snippet.split('. ')[0] + '.'
            search_results.append(first_sentence)
    else:
        search_results.append("No results found.")
        
    # return search_results
    # search_results = google_search(query)
    summary = " ".join(search_results[:3])
    summary = re.sub(r'[^a-zA-Z\s\.,]', '', summary) 
    # return summary
    print(summary)
    speak(summary)
    
# #example
# google_search("what is supermen?")

