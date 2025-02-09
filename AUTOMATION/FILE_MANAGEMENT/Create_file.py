import os
def create_folder(folder_name):
    global current_directory
    new_folder_path = os.path.join(current_directory, folder_name)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Folder '{folder_name}' created at {current_directory}")
    else:
        print(f"Folder '{folder_name}' already exists.")

def create_text_file(file_name, content=""):
    global current_directory
    file_path = os.path.join(current_directory, file_name)
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Text file '{file_name}' created at {current_directory}")