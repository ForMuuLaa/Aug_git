'''
Question 1. Exploring Python's OS Module
Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

Code Example:
    import os

    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.
'''
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