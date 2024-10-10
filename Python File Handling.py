import os

def list_directory_contents(path):
    try:
        # List all files and subdirectories in the given path
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


directory_path = input("Please enter the directory path: ")

list_directory_contents(directory_path)