import re
def number_check(phone_number):
        pattern = r"^\d{3}-\d{3}-\d{4}$"
        if re.match(pattern, phone_number):
            return True
        else:
            print(f"{phone_number} is not a valid phone number.\nValid phone numer Ex( 123-456-7890 ).")


def list_check(name_list, contact_list, number_list):
    con = False
    num = False
    
    if contact_list:                                
        for contact in contact_list:
            if contact['name'].lower() == name_list.lower():
                con = True
            else:
                con = False
            if contact['number'] == number_list:
                num = True
            else:
                num = False
            
            if con == True and num == True:
                return False

def file_check(filename, name_file, number_file):
    con = False
    num = False
    
    with open(filename, 'r') as file:
            content = file.read()  
            if name_file.lower() in content.lower():
                con = True
            else:
                con = False
            
            if number_file in content:
                num = True
            else:
                num = False

            if con == True and num == True:
                return False
 


        
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


def edit_contact(contacts, filename):
    truly = True
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]{3}$'
    with open(filename, 'r') as file:
        if not file.read(1) == '':
            action = input("Would you like to edit your contacts in your file? [y/n]: ")
            
            if action.lower() == 'y':
                name = input("Please enter your contact name you would like to edit: ").strip()
                number = input("Please enter your contact number you would like to edit: ")
                
                if file_check('Contact_Management.txt', name, number):
                    updated_name = input("Please enter new contact name: ").strip()
                    
                    while True:
                        updated_number = input("Please enter the new contact's phone number: ")
                        if number_check(updated_number):
                            break
                        else:
                            print("Please try again")
                            
                    updated_email = input("Would you like to edit the email address [y/n]: ").lower()
                    if updated_email == 'y':
                        while True:
                            updated_email = input ("Please enter the contact's email or 'quit' to go back: ")
                            if updated_email.lower() == 'quit':
                                break
                            if re.match(pattern, updated_email):
                                print(f"This '{updated_email}' email has been added.")
                                break
                            else:
                                print("Error please enter a valid email.")
                    else:
                        updated_email = 'N/A'
                    updated_notes = input("Would you like to add new Additional information(e.g., address, notes) [y/n]: ").lower()
                    if updated_notes == 'y':
                        updated_notes = input("What would you like to add? ")
                    else:
                        updated_notes = 'N/A'
                    
                    
                    with open(filename, 'r') as file:
                        lines = file.readlines()
                    updated_lines = []    
                    for line in lines:
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
                            
                    with open(filename, 'w') as file:
                        file.writelines(updated_lines)
                    truly = False
                else:
                    print("Error non-vaild entry of number or name")
                        
    if truly == True:
        name = input("Please enter your contact name you would like to edit: ").strip()
        while True:
            number = input("Please enter the contact's phone number: ")
            if number_check(number):
                break
            else:
                print("Please try again")
        if not list_check(name, contacts, number):
            updated_name = input("Please enter new contact name: ").strip()
            while True:
                updated_number = input("Please enter the new contact's phone number: ")
                if number_check(updated_number):
                    break
                else:
                    print("Please try again")
            updated_email = input("Would you like to edit the email address [y/n]: ").lower()
            if updated_email == 'y':
                while True:
                    updated_email = input ("Please enter the contact's email or 'quit' to go back: ")
                    if updated_email.lower() == 'quit':
                        break
                    if re.match(pattern, updated_email):
                        print(f"This '{updated_email}' email has been added.")
                        break
                    else:
                        print("Error please enter a valid email.")
            else:
                updated_email = 'N/A'
            updated_notes = input("Would you like to add new Additional information(e.g., address, notes) [y/n]: ").lower()
            if updated_notes == 'y':
                updated_notes = input("What would you like to add? ")
            else:
                updated_notes = 'N/A'

            updated_contact = {'name':updated_name, 'number':updated_number, 'email':updated_email, 'notes':updated_notes }
            for contact in contacts:
                if contact['name'].lower() == name.lower():
                    contact.update(updated_contact)
                    break
        else:
            print(f"Name: '{name}' does not yet exist in your contacts.")
            


def delete_contact(filename, contacts):
    truly = True
    with open(filename, 'r') as file:
        if not file.read(1) == '':
            action = input("Would you like to remove a contact in your file? [y/n]: ")
            
            if action.lower() == 'y':
                name = input("Please enter the contact's name that you would like to remove: ").strip()
                while True:
                    number = input("Please enter the contact's phone number: ")
                    if number_check(number):
                        break
                    else:
                        print("Please try again")
                if not file_check('Contact_Management.txt', name, number):
                    with open(filename, 'r') as file:
                        lines = file.readlines()
                    updated_lines = []    
                    for line in lines:
                        if name.lower() in line.lower():
                            continue
                        else:
                            updated_lines.append(line)
                            
                    with open(filename, 'w') as file:
                        file.writelines(updated_lines)
                    truly = False
        if truly == True:
            name = input("Please enter the contact's name that you would like to remove: ").strip()
            while True:
                    number = input("Please enter the contact's phone number: ")
                    if number_check(number):
                        break
                    else:
                        print("Please try again")
            if not file_check('Contact_Management.txt', name, number):
                for contact in contacts:
                    if contact['name'].lower() == name.lower() and contact['number'] == number:
                        contacts.remove(contact)
                        break
                    else:
                        print(f"Error name '{name}' does not yet exist.")
                        break
                
            
def search_contact(filename, contacts):
    name = input(f"Please enter the name you would like to search for: ").strip()
    with open(filename, 'r') as file:
        lines = file.readlines() 
        if not file.read(1) == '':
            for line in lines:
                if name.lower() in line.lower():
                    parts = line.strip().split(', ')
                    print(f"\nContact was found in your file \nName: {parts[0]}\n-Number: {parts[1]}\n-Email: {parts[2]}\n-Notes: {parts[3]}")
                    

    if contacts:
        for contact in contacts:
           if contact['name'].lower() == name.lower():
               print(f"\nContact was found in your current list \nName: {contact['name']}\n-Number: {contact['number']}\n-Email: {contact['email']}\n-Notes: {contact['notes']}")
               



def display_contacts(filename, contacts):
    with open(filename, 'r') as file:
        lines = file.readlines() 
        if file.read(1) == '':
            for line in lines:
                parts = line.strip().split(', ')
                print(f"\nContact was found in your file \nName: {parts[0]}\n-Number: {parts[1]}\n-Email: {parts[2]}\n-Notes: {parts[3]}")
    if contacts:
            for contact in contacts:
                print(f"\nContact was found in your current list \nName: {contact['name']}\n-Number: {contact['number']}\n-Email: {contact['email']}\n-Notes: {contact['notes']}")

def export_contacts(filename, contacts):
    updated_lines = []
    if contacts:
        for contact in contacts:
            name = contact['name']
            number = contact['number']
            email = contact['email']
            notes = contact['notes'] 
            imported_line = f"{name}, {number}, {email}, {notes}"
            updated_lines.append(imported_line + '\n')
        with open(filename, 'r') as file:
            lines = file.readlines()
            if file.read(1) == '':
                for line in lines:
                    updated_lines.append(line)
                with open(filename, 'w') as file:
                    file.writelines(updated_lines)
            with open(filename, 'w') as file:
                file.writelines(updated_lines)
    else:
        print("Contact list is empty")

def import_contacts(filename, contact): 
    with open(filename, 'r') as file:
        lines = file.readlines()   
    for line in lines:
            parts = line.strip().split(', ')
            name = parts[0]
            number = parts[1]
            email = parts[2]
            notes = parts[3] 
            imported_line = {'name':name, 'number':number, 'email':email, 'notes':notes }
            contact.append(imported_line)

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
    menu()
    action = input("Please choose a option: ")

    if action == '1':
        add_contact('Contact_Management.txt')
    elif action == '2':
        edit_contact(contact,'Contact_Management.txt')
    elif action == '3':
        delete_contact('Contact_Management.txt', contact)
    elif action == '4':
        search_contact('Contact_Management.txt', contact)
    elif action == '5':
        display_contacts('Contact_Management.txt', contact)
    elif action == '6':
        export_contacts('Contact_Management.txt', contact)
    elif action == '7':
        print("Please note that the file must be in this format and the contact\n must be on different line an separate by (', ')\n -(name, 123-456-7890, name@domaim.com, notes)\n -(2name, 123-456-7890, name@domaim.org, N/A)\n -(3name, 123-456-7890, N/A, 3notes)\n")
        file_name = input("Please enter the file name/ Relaitve path")
        import_contacts(file_name, contact)
    elif action == '8':
        break
    else:
        print("Error please enter (1/2/3.etc..)")



