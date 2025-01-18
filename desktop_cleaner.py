
import os
import shutil

def clean_folder(folder_path):
    for file_name in os.listdir(folder_path): #listdir gets the list of files and folders in the folder, it then itterates through each one
       if os.path.isfile(os.path.join(folder_path, filename)): #checks whether the current is a file
            file_extension = file_name.split('.')[-1].lower() #gets the file extension
            if file_extension:
                subfolder_name = f"{file_extension.upper()} files" #create the subfolder name
                subfolder_path = create_subfolder(folder_path, subfolder_name) #links to a function to create the subfolder
                file_path = os.path.join(folder_path, file_name) #creates the path to the current file
                shutil.move(file_path, subfolder_path) #moves the file to the newly created subfolder
                print(f"Moved {file_name} to {subfolder_name}")

def create_subfolder(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name) #create the path to the subfolder
    if not os.path.exists(subfolder_path): #if the folder does not exist, create it
        os.mkdir(subfolder_path) #creates the folder
    return subfolder_path

if __name__ == '__main__':
    print("Desktop cleaner script started")
    folder_path = input("Enter the path to the folder: ") #asks the user for the path to the folder that wants to be cleaned
    if not os.path.exists(folder_path): #checks if the folder exists
        print("Folder not found, please check the path with the 'pwd' command")
        exit()
    else:
        print("Folder found")
        clean_folder(folder_path)
        print("cleaning completed")