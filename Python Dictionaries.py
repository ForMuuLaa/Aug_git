'''
Question 1. Real-World Python Dictionary Applications
Objective: The aim of this assignment is to reinforce your understanding and application
 of Python dictionaries, nested collections, and dictionary methods.

Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu
 stored in a nested dictionary. Your task is to update this menu based on given instructions

Problem Statement: Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
- Add a new category called "Beverages" with at least two items

- Update the price of "Steak" to 17.99.

- Remove "Bruschetta" from "Starters". 
'''

def add_category(menu, category):
   
    
    if category not in menu:
        menu[category] = {}
        print(f"Category '{category}' has been added ")
    else:
        print(f"-----------]\nThis '{category}' calegory already exist.")
    


def update_category(menu, category, item, price):
    
    if category in menu:
        menu[category].update({item: price}) 
        print(f"-----------]\nUpdated '{item}' in '{category}' to ${price:.2f}.")
    else:
        print(f"-----------]\nThis '{category}' calegory doesn't exist.")
    


def remove_item_in_category(menu, category, item):
    try:
        if item in menu[category]:
            menu[category].pop(item) 
            print(f"-----------]\nItem '{item}' has been removed")
        else:
            print(f"-----------]\nThis '{item}' item doesn't exist.")
    except detailsError:
        print(f"-----------]\nThis '{item}' item doesn't exist.")


restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}



add_category(restaurant_menu, "Beverages")
update_category(restaurant_menu, "Main Course", "Steak", 17.99)
remove_item_in_category(restaurant_menu, "Starters", "Bruschetta")

print(restaurant_menu)

'''2. Python Programming Challenges for Customer Service Data Handling
Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.

'''
def add_tickets(service, ticket, customer, issue, status):
    if ticket not in service:
        service[ticket] = {"Customer":customer, "Issue": issue, "Status": status}
    else:
        print(f"This '{ticket}' ticket already exist")

def update_tickets(service, ticket, customer, issue, status):
    if ticket in service:
        service[ticket].update({"Customer":customer, "Issue": issue, "Status": status})
    else:
        print(f"This '{ticket}' ticket does not exist")
def disaplay_tickets(service):
    for tic, details in service.items():
        print(f"---------------|\n{tic}\n---------------|")
        print (f"-Customer:{details['Customer']}\n-Issue: {details['Issue']}\n-Status: {details['Status']}")


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

add_tickets(service_tickets,"Ticket003", "Tom", "Login problem", "open")
update_tickets(service_tickets,"Ticket001" ,"Alice", "Login problem","closed")
disaplay_tickets(service_tickets)
