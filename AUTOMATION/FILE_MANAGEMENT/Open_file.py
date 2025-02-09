import os
import difflib

# Start from the user's root directory (can be set to a specific drive if needed)
current_directory = os.path.expanduser("~")  # This expands to 'C:/Users/YourUsername'
drive_opened = False  # Flag to track if a drive has been opened
current_drive = None  # Track which drive is currently active

def find_similar_folder_or_file(name):
    global current_directory
    # List all files and folders in the current directory
    try:
        items_list = os.listdir(current_directory)
    except FileNotFoundError:
        print(f"Directory '{current_directory}' not found.")
        return None
    
    # Find the closest match for the name
    similar_items = difflib.get_close_matches(name, items_list, n=1, cutoff=0.6)
    
    # Return the closest match, or None if no match is found
    return similar_items[0] if similar_items else None

def go_to_folder_or_file(name):
    global current_directory, drive_opened, current_drive
    
    # Normalize input for drive detection
    if "C drive" in name or "C:" in name or "c drive" in name or "sea" in name or "see" in name or "seeing" in name:
        name = "C:"
    elif "D drive" in name or "D:" in name or "d drive" in name or "the" in name or "tree" in name or "free" in name:
        name = "D:"
    
    # Check if the input is a drive (C: or D:)
    if name in ["C:", "D:"]:
        current_directory = f"{name}/"
        print(f"Changed to drive: {current_directory}")
        os.startfile(current_directory)  # Open the drive in File Explorer
        drive_opened = True  # Set flag to indicate the drive is opened
        current_drive = name  # Track the current drive
        return True
    
    if drive_opened:
        # Find a file or folder with a name similar to the input
        similar_item = find_similar_folder_or_file(name)
        
        if similar_item:
            # Construct the full path based on the current directory
            new_path = os.path.join(current_directory, similar_item)
            
            if os.path.isdir(new_path):
                current_directory = new_path
                print(f"Moved to folder: {current_directory}")
                os.startfile(current_directory)  # Open the folder in File Explorer
                return True
            
            elif os.path.isfile(new_path):
                print(f"Opening file: {new_path}")
                os.startfile(new_path)  # Open the file
                return True
        
        else:
            print(f"No similar folder or file found for '{name}' in {current_directory}.")
            return False
    
    else:
        print("Please switch to a drive first (e.g., 'C:' or 'D:').")
        return False

def create_folder(folder_name):
    global current_directory
    new_folder_path = os.path.join(current_directory, folder_name)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Folder '{folder_name}' created at {current_directory}")
    else:
        print(f"Folder '{folder_name}' already exists.")



def create_file(file_name, extension, content=""):
    global current_directory
    # Ensure the file has the correct extension
    if not file_name.endswith(extension):
        file_name += extension
    # Construct the full path to the file
    file_path = os.path.join(current_directory, file_name)
    # Create the file with the provided content
    with open(file_path, "w") as file:
        file.write(content)
    print(f"File '{file_name}' created at {current_directory}")

def create_text_file(file_name, content=""):
    create_file(file_name, ".txt", content)

def create_python_file(file_name, content="# This python file created by sunday \n"):
    create_file(file_name, ".py", content)

def create_html_file(file_name, content="<!-- This html file created by sunday -->"):
    create_file(file_name, ".html", content)

def create_css_file(file_name, content="/* This css file created by sunday */"):
    create_file(file_name, ".css", content)

def create_javascript_file(file_name, content="//This javascript file created by sunday"):
    create_file(file_name, ".js", content)


# # Example usage of the functions
# go_to_folder("d drive")         # Change to D drive
# go_to_folder("Desktop")        # Navigate to 'work file' folder (if it exists in D drive)
# create_text_file("my_text_file", "This is a text file.")
# create_python_file("script", "# This is a Python script")
# create_html_file("index", "<html><body>Hello, world!</body></html>")
# create_css_file("style", "body { background-color: lightblue; }")
# create_javascript_file("app", "console.log('Hello, JavaScript!');")
