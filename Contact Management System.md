number_check(phone_number):
- This function validates whether a given phone number follows the pattern 123-456-7890.
- It uses a regular expression (r"^\d{3}-\d{3}-\d{4}$") to match this format.
- If the phone number is valid, the function returns True; otherwise, it prints an error message with the correct format.

list_check(name_list, contact_list, number_list):
- This function checks if a specific name and phone number exist in a list of contacts (contact_list).
- The function loops through each contact and compares the lowercase version of the contact's name
  and their phone number with the provided name and number.
- If both the name and number match, it returns False (indicating a duplicate).

file_check(filename, name_file, number_file):
- This function checks if a specific name and phone number exist within a file's content.
- It opens the file, reads the content, and checks if the provided name and phone number are present.
- Similar to list_check, if both the name and number are found, it returns False.
- In both list_check and file_check, the return value of False implies that a match (duplicate) was found.
  If no match is found, the functions do not return any value explicitly (hence returning None).
        
        import re

        def number_check(phone_number):
            # Check if the phone number follows the format 123-456-7890
            pattern = r"^\d{3}-\d{3}-\d{4}$"
            if re.match(pattern, phone_number):
                return True
            else:
                print(f"{phone_number} is not a valid phone number. Valid format: 123-456-7890.")
                return False
        
        def list_check(name_list, contact_list, number_list):
            # Check if both name and number exist in the contact list
            for contact in contact_list:
                if contact['name'].lower() == name_list.lower() and contact['number'] == number_list:
                    return True  # Match found
            return False  # No match found
        
        def file_check(filename, name_file, number_file):
            # Check if both name and number exist in the file
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    if name_file.lower() in content.lower() and number_file in content:
                        return True  # Match found
            except FileNotFoundError:
                print(f"Error: {filename} not found.")
            
            return False  # No match found or file not found
         
function, add_contact
- User Input: It prompts the user to enter the contact's name and validates the phone number format.
- Duplicate Check: It checks if the contact (name and number) already exists in both the contact list and a file named Contact_Management.txt.
- Optional Email: It asks if the user wants to add an email, validating the email format if provided.
- Optional Notes: It allows the user to add additional information (notes, address, etc.).
- Error Handling: It handles cases where the file doesn't exist or other exceptions occur.
- Updating List: If no duplicates are found, the contact is added to the contact list.
                
        contact = []
        def add_contact(filename):
            global contact
            try:
                pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]{3}$'
                
                name = input("Please enter the contact's name: ").strip()
                while True:
                    number = input("Please enter the contact's phone number: ")
                    if number_check(number):
                        break
                    else:
                       print("Please try again")
                       
                if not list_check(name, contact, number) and not file_check('Contact_Management.txt', name, number): # add a 'and' to check for name in nested list "contact"
                    email = input("Would you like to add email address [y/n]").lower()
                    if email == 'y':
                        while True:
                            email = input ("Please enter the contact's email or 'quit' to go back: ")
                            if email.lower() == 'quit':
                                break
                            if re.match(pattern, email):
                                print(f"This '{email}' email has been added.")
                                break
                            else:
                                print("Error please enter a valid email.")
                    else:
                        email = 'N/A'
                    notes = input("Would you like to add any Additional information(e.g., address, notes) [y/n]: ").lower()
                    if notes == 'y':
                        notes = input("What would you like to add? ")
                    else:
                        notes = 'N/A'
                    
                    contact.append({'name':name, 'number':number, 'email':email, 'notes':notes })
                    return contact
        
        
                else:
                    print(f"'{name}' is present in your contacts.")
            except FileNotFoundError:
                print(f"Error: The file '{filename}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
        

File Check: The function first checks if the contact file is empty.
If not, it asks the user if they want to edit their contacts.
Contact Identification:
- The user is prompted to enter the name and phone number of the contact they want to edit.
- It uses the file_check function to verify if the contact exists in the file.

Updating Contact Information:
- If the contact exists, the user can enter a new name, phone number, email, and additional notes.
- Email input is validated against a regex pattern.
- The function reads all lines from the file, updates the relevant contact information, and writes the updated lines back to the file.

Fallback to List Check:
- If the contact is not found in the file, the function prompts the user again for the contact's name and phone number.
- It checks against the contacts list and allows the user to update the contact's information similarly.

Contact Update:
- If a matching contact is found in the contacts list, it updates the details.

Error Handling:
- If the contact name or number is invalid, an error message is displayed.

        def edit_contact(contacts, filename):
            contact_edit = True
            pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]{3}$'  # Regex pattern for email validation
            
            # Check if the contact file is empty
            with open(filename, 'r') as file:
                if not file.read(1) == '':
                    action = input("Would you like to edit your contacts in your file? [y/n]: ")
        
                    if action.lower() == 'y':
                        # Prompt user for contact name and number to edit
                        name = input("Please enter your contact name you would like to edit: ").strip()
                        number = input("Please enter your contact number you would like to edit: ")
        
                        # Check if the contact exists in the file
                        if file_check(filename, name, number):
                            updated_name = input("Please enter new contact name: ").strip()
        
                            # Validate and update phone number
                            while True:
                                updated_number = input("Please enter the new contact's phone number: ")
                                if number_check(updated_number):
                                    break
                                else:
                                    print("Invalid number, please try again.")
                            
                            # Optionally update email
                            updated_email = input("Would you like to edit the email address [y/n]: ").lower()
                            if updated_email == 'y':
                                while True:
                                    updated_email = input("Please enter the contact's email or 'quit' to go back: ")
                                    if updated_email.lower() == 'quit':
                                        break
                                    if re.match(pattern, updated_email):
                                        print(f"This '{updated_email}' email has been added.")
                                        break
                                    else:
                                        print("Error: please enter a valid email.")
                            else:
                                updated_email = 'N/A'  # Default value if no email is provided
                            
                            # Optionally update additional notes
                            updated_notes = input("Would you like to add new Additional information (e.g., address, notes) [y/n]: ").lower()
                            if updated_notes == 'y':
                                updated_notes = input("What would you like to add? ")
                            else:
                                updated_notes = 'N/A'  # Default value if no notes are provided
        
                            # Read the file and update the contact information
                            with open(filename, 'r') as file:
                                lines = file.readlines()
                            updated_lines = []
                            for line in lines:
                                # Update the specific contact line
                                if name.lower() in line.lower():
                                    parts = line.strip().split(', ')
                                    parts[0] = updated_name
                                    parts[1] = updated_number
                                    parts[2] = updated_email
                                    parts[3] = updated_notes
                                    updated_line = ', '.join(parts)
                                    updated_lines.append(updated_line + '\n')
                                else:
                                    updated_lines.append(line)
        
                            # Write updated contacts back to the file
                            with open(filename, 'w') as file:
                                file.writelines(updated_lines)
                            contact_edit = False  # Successfully edited the contact
                        else:
                            print("Error: Invalid entry for number or name")
        
            # If no contact was edited from the file, check in the contacts list
            if contact_edit:
                name = input("Please enter your contact name you would like to edit: ").strip()
                
                # Validate phone number input
                while True:
                    number = input("Please enter the contact's phone number: ")
                    if number_check(number):
                        break
                    else:
                        print("Invalid number, please try again.")
        
                # Check if contact exists in the provided contacts list
                if not list_check(name, contacts, number):
                    updated_name = input("Please enter new contact name: ").strip()
                    
                    # Validate and update phone number
                    while True:
                        updated_number = input("Please enter the new contact's phone number: ")
                        if number_check(updated_number):
                            break
                        else:
                            print("Invalid number, please try again.")
                    
                    # Optionally update email
                    updated_email = input("Would you like to edit the email address [y/n]: ").lower()
                    if updated_email == 'y':
                        while True:
                            updated_email = input("Please enter the contact's email or 'quit' to go back: ")
                            if updated_email.lower() == 'quit':
                                break
                            if re.match(pattern, updated_email):
                                print(f"This '{updated_email}' email has been added.")
                                break
                            else:
                                print("Error: please enter a valid email.")
                    else:
                        updated_email = 'N/A'  # Default value if no email is provided
                    
                    # Optionally update additional notes
                    updated_notes = input("Would you like to add new Additional information (e.g., address, notes) [y/n]: ").lower()
                    if updated_notes == 'y':
                        updated_notes = input("What would you like to add? ")
                    else:
                        updated_notes = 'N/A'  # Default value if no notes are provided
        
                    # Create a new contact dictionary with the updated information
                    updated_contact = {
                        'name': updated_name,
                        'number': updated_number,
                        'email': updated_email,
                        'notes': updated_notes
                    }
        
                    # Update the contact in the contacts list
                    for contact in contacts:
                        if contact['name'].lower() == name.lower():
                            contact.update(updated_contact)  # Update existing contact
                            print(f"Contact '{name}' updated successfully.")
                            break
                else:
                    print(f"Error: Name '{name}' does not exist in your contacts.")

delete_contact function allows users to remove a contact from a specified file and a list of contacts.
File Check:
- It first checks if the contact file is empty. If not, it prompts the user to decide if they want to remove a contact.
Input Name and Number:
- The user is prompted to enter the contact's name and phone number, with validation for the phone number format.
File Update:
- If the contact exists in the file, the function reads the existing contacts, constructs a new list excluding the specified contact, and updates the file.
List Update:
- If the contact isn't found in the file, it checks against the in-memory contacts list. If a match is found, it removes the contact from the list.
Error Handling:
- If the contact name does not exist in either the file or the list, an error message is displayed.

        def delete_contact(filename, contacts):
            del_contact = True  # Flag to track whether a contact has been deleted
        
            # Open the contact file to check if it is empty
            with open(filename, 'r') as file:
                if not file.read(1) == '':  # If the file is not empty
                    action = input("Would you like to remove a contact in your file? [y/n]: ")
        
                    if action.lower() == 'y':
                        # Prompt for the name of the contact to be deleted
                        name = input("Please enter the contact's name that you would like to remove: ").strip()
                        
                        # Validate the phone number input
                        while True:
                            number = input("Please enter the contact's phone number: ")
                            if number_check(number):
                                break
                            else:
                                print("Invalid number, please try again.")
        
                        # Check if the contact exists in the file
                        if not file_check(filename, name, number):
                            # Read the existing contacts from the file
                            with open(filename, 'r') as file:
                                lines = file.readlines()
                            updated_lines = []    
        
                            # Build a new list of lines excluding the contact to be deleted
                            for line in lines:
                                if name.lower() in line.lower():
                                    continue  # Skip the line for the contact to be deleted
                                else:
                                    updated_lines.append(line)
        
                            # Write the updated list back to the file
                            with open(filename, 'w') as file:
                                file.writelines(updated_lines)
                            del_contact = False  # Mark that deletion was successful
        
            # If no contact was deleted from the file, check in the contacts list
            if del_contact:
                name = input("Please enter the contact's name that you would like to remove: ").strip()
        
                # Validate the phone number input again
                while True:
                    number = input("Please enter the contact's phone number: ")
                    if number_check(number):
                        break
                    else:
                        print("Invalid number, please try again.")
        
                # Check if the contact exists in the contacts list
                if not file_check(filename, name, number):
                    for contact in contacts:
                        # Check for matching name and number
                        if contact['name'].lower() == name.lower() and contact['number'] == number:
                            contacts.remove(contact)  # Remove the contact from the list
                            print(f"Contact '{name}' removed successfully.")
                            break
                    else:
                        # This else corresponds to the for loop; it executes if no break occurs
                        print(f"Error: Name '{name}' does not exist in your contacts.")

The search_contact function allows users to search for a contact by name in both a specified file and a local list of contacts.
User Input:
- It prompts the user to enter a contact name to search.
File Search:
- Opens the specified file and reads all lines.
- Checks each line for a match with the input name (case-insensitive).
- If a match is found, it extracts and displays the contact's details (name, number, email, and notes).
List Search:
- If the local contacts list is not empty, it searches for a matching name.
- Displays the contact's details if found in the local list.
- Output: If a contact is found in either the file or the local list, its details are printed to the console.              
                    
        def search_contact(filename, contacts):
            # Prompt the user for the contact name to search
            name = input(f"Please enter the name you would like to search for: ").strip()
            
            # Open the contact file for reading
            with open(filename, 'r') as file:
                lines = file.readlines()  # Read all lines from the file
                
                # Check if the file is not empty
                if not file.read(1) == '':
                    # Search for the contact name in each line of the file
                    for line in lines:
                        if name.lower() in line.lower():  # Case-insensitive search
                            parts = line.strip().split(', ')  # Split line into parts
                            # Print the found contact's details
                            print(f"\nContact was found in your file \nName: {parts[0]}\n-Number: {parts[1]}\n-Email: {parts[2]}\n-Notes: {parts[3]}")
        
            # Check if the contacts list is not empty
            if contacts:
                # Search for the contact in the current contacts list
                for contact in contacts:
                    if contact['name'].lower() == name.lower():  # Case-insensitive match
                        # Print the found contact's details
                        print(f"\nContact was found in your current list \nName: {contact['name']}\n-Number: {contact['number']}\n-Email: {contact['email']}\n-Notes: {contact['notes']}")

                       
        
The display_contacts function is designed to display contacts stored in both a specified file and a local list.
File Handling:
- Opens the specified file for reading.
- Reads all lines from the file to get the contact information.
- Checks if the file is empty. If it is not, it prints each contact's details found in the file
  (name, number, email, notes) by splitting the line into parts.
Local List Handling:
- Checks if the local contacts list is not empty.
- If there are contacts in the list, it iterates through them and prints each contact's details (name, number, email, notes).
Output:
- The function provides a way to view all contacts in both storage formats, formatted clearly for the user.
        
        def display_contacts(filename, contacts):
            empty_check_list = False
            empty_check_file = False
  
            with open(filename, 'r') as file:
                lines = file.readlines() 
                if file.read(1) == '':
                    # Loop through each line and print contact details
                    for line in lines:
                        parts = line.strip().split(', ')  # Split line into parts
                        # Print the contact's details
                        print(f"\nContact was found in your file \nName: {parts[0]}\n-Number: {parts[1]}\n-Email: {parts[2]}\n-Notes: {parts[3]}")
                else:
                   empty_check_file = True
            # Check if the contacts list is not empty
            if contacts:
                # Loop through the contacts list and print each contact's details
                for contact in contacts:
                    print(f"\nContact was found in your current list \nName: {contact['name']}\n-Number: {contact['number']}\n-Email: {contact['email']}\n-Notes: {contact['notes']}")
            else:
               empty_check_list = True

            if empty_check_list and empty_check_file: # Checks for if rhe list and the file is empty
                print("You have no contacts to display.")



  export_contacts function:
This function exports the contacts from the contacts list to a specified file. 
If the file already contains contacts, it appends the new contacts.
        
        def export_contacts(filename, contacts):
            updated_lines = []
        
            # Check if the contact list is not empty
            if contacts:
                try:
                    # Loop through each contact in the list
                    for contact in contacts:
                        name = contact['name']
                        number = contact['number']
                        email = contact['email']
                        notes = contact['notes']
                        # Create a formatted string for each contact and append to updated_lines
                        imported_line = f"{name}, {number}, {email}, {notes}"
                        updated_lines.append(imported_line + '\n')
                    
                    # Open the file for reading existing lines
                    with open(filename, 'r') as file:
                        lines = file.readlines()
                        # Append the existing lines to the updated lines list if the file is not empty
                        if len(lines) > 0:
                            updated_lines.extend(lines)
                    
                    # Write the updated contact lines into the file
                    with open(filename, 'w') as file:
                        file.writelines(updated_lines)
        
                    print(f"Contacts successfully exported to {filename}.")
                
                except FileNotFoundError:
                    print(f"Error: The file '{filename}' does not exist.")
                except Exception as e:
                    print(f"An error occurred while exporting contacts: {e}")
            else:
                print("Contact list is empty")


  import_contacts function:
This function imports contacts from a file into the contact list. 
It reads the file line by line, splits the data, and appends it to the list.              
                
        def import_contacts(filename, contact):
            try:
                # Open the specified file and read all lines
                with open(filename, 'r') as file:
                    lines = file.readlines()
                
                # Loop through each line in the file
                for line in lines:
                    # Split each line by commas and strip whitespace
                    parts = line.strip().split(', ')
                    name = parts[0]
                    number = parts[1]
                    email = parts[2]
                    notes = parts[3]
                    
                    # Create a dictionary for the contact and append to the contact list
                    imported_line = {'name': name, 'number': number, 'email': email, 'notes': notes}
                    contact.append(imported_line)
                
                print(f"Contacts successfully imported from {filename}.")
        
            except FileNotFoundError:
                print(f"Error: The file '{filename}' does not exist.")
            except Exception as e:
                print(f"An error occurred while importing contacts: {e}")
export_contacts:
- Loops through the contacts list and prepares each contact as a formatted string.
- Reads existing contacts from the file (if any), then appends the new contacts and writes everything back to the file.
- Handles cases where the contact list is empty and informs the user.

import_contacts:
- Reads contact data from the file, splits the data into its components
  (name, number, email, notes), and appends it to the provided contact list.



Menu Presentation:
- Displays a list of options for the user to manage contacts.
Action Handling:
- Based on user input, different functions like adding, editing, deleting, searching, displaying, exporting, or importing contacts are invoked.
- Quit Option: Allows the user to exit the program by choosing option 8.

        def menu():
            print(
            '''
            Welcome to the Contact Management System! 
            Menu:
            1. Add a new contact
            2. Edit an existing contact
            3. Delete a contact
            4. Search for a contact
            5. Display all contacts
            6. Export contacts to a text file
            7. Import contacts from a text file
            8. Quit
            '''
            )
        
        
        while True:    
            menu()  # Display the menu
            action = input("Please choose an option (1-8): ").strip()
            
            if action == '1':
                add_contact('Contact_Management.txt')  # Add a contact
            elif action == '2':
                edit_contact(contact, 'Contact_Management.txt')  # Edit a contact
            elif action == '3':
                delete_contact('Contact_Management.txt', contact)  # Delete a contact
            elif action == '4':
                search_contact('Contact_Management.txt', contact)  # Search for a contact
            elif action == '5':
                display_contacts('Contact_Management.txt', contact)  # Display all contacts
            elif action == '6':
                export_contacts('Contact_Management.txt', contact)  # Export contacts
            elif action == '7':
                print("Please note that the file must be in this format:\n")
                print("name, 123-456-7890, name@domain.com, notes")
                print("Example:\n")
                print("John Doe, 123-456-7890, johndoe@example.com, Work\nJane Smith, 123-456-7890, N/A, Friend\n")
                
                # File name input with basic validation
                file_name = input("Please enter the file name/Relative path to import: ").strip()
                if file_name:
                    import_contacts(file_name, contact)
                else:
                    print("Error: Invalid file name. Please try again.")
            elif action == '8':
                print("Exiting the Contact Management System. Goodbye!")
                break  # Exit the loop and quit
            else:
                print("Error: Invalid option. Please enter a number between 1 and 8.")  # Invalid option handling
        
