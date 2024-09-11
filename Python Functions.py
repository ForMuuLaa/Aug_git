
# Question 1. The Calculator App
# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

num_1 = 6
num_2 = 8
numbers = [num_1, num_2]

def addition_():
    global numbers
    add = numbers[0] + numbers[1]
    return add
def subtraction_():
    global numbers
    sub = numbers[0] - numbers[1]
    return sub
def multiplication_():
    global numbers
    mult = numbers[0] * numbers[1]
    return mult
def division_():
    global numbers
    div = numbers[0] / numbers[1]
    return div


print(f"Your numbers added are {addition_()}.")
print(f"Your numbers Subtract are {subtraction_()}.")
print(f"Your numbers Multiplyed are {multiplication_()}.")
print(f"Your numbers divided are {division_()}.")


# Question Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.



num_one = 0
num_two = 0
number = [num_one, num_two]


def addition():
    global number
    add = number[0] + number[1]
    return add
def subtraction():
    global number
    sub = number[0] - number[1]
    return sub
def multiplication():
    global number
    mult = number[0] * number[1]
    return mult
def division():
    global number
    div = number[0] / number[1]
    return div

while True:
    condition = input("""------------------------------------------------------------------\n(FIRST) Please choose the calculation you would like to perform\n------------------------------------------------------------------\n\n[A]ddition  [S]ubtraction  [M]ultiplication  [D]ivision  [Q]uit\n\nPlease choose (A/S/M/D/Q)\n\n------------------------------------------------------------------\n\n"""
                      ).upper()
    
    if condition == 'A':
        number[0] = int(input("Please enter your first number: "))
        number[1] = int(input("Please enter your second number: "))
        print(f"{number[0]} + {number[1]} = {addition()}\n\n------------------------------------------------------------------\n\n ")
        
    elif condition == 'S':
        number[0] = int(input("Please enter your first number: "))
        number[1] = int(input("Please enter your second number: "))
        print(f"{number[0]} - {number[1]} = {subtraction()}\n\n------------------------------------------------------------------\n\n ")
        
    elif condition == 'M':
        number[0] = int(input("Please enter your first number: "))
        number[1] = int(input("Please enter your second number: "))
        print(f"{number[0]} * {number[1]} = {multiplication()}\n\n------------------------------------------------------------------\n\n ")
        
    elif condition == 'D':
        number[0] = int(input("Please enter your first number: "))
        number[1] = int(input("Please enter your second number: "))
        print(f"{number[0]} / {number[1]} = {division()}\n\n------------------------------------------------------------------\n\n ")
        
    elif condition == 'Q':
        print("Have a nice day!")
        break
    
    else:
        print("Please try again, please choose (A/S/M/D/Q)\n\n------------------------------------------------------------------\n\n ")

  
# Question 1 Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error 
# handling set up to prevent an error from showing in the console.
        
                       
num_one = 0
num_two = 0
number = [num_one, num_two]


def addition():
    global number
    add = number[0] + number[1]
    return add
def subtraction():
    global number
    sub = number[0] - number[1]
    return sub
def multiplication():
    global number
    mult = number[0] * number[1]
    return mult
def division():
    global number
    div = number[0] / number[1]
    return div

while True:
    condition = input("""------------------------------------------------------------------\n(SECOND) Please choose the calculation you would like to perform\n------------------------------------------------------------------\n\n[A]ddition  [S]ubtraction  [M]ultiplication  [D]ivision  [Q]uit\n\nPlease choose (A/S/M/D/Q)\n\n------------------------------------------------------------------\n\n"""
                      ).upper()
    
    if condition == 'A':
        try:
            number[0] = int(input("Please enter your first number: "))
            number[1] = int(input("Please enter your second number: "))
            print(f"{number[0]} + {number[1]} = {addition()}\n\n------------------------------------------------------------------\n\n ")
        except(ValueError):
             print("Error please enter a integer\n\n------------------------------------------------------------------\n\n")
    elif condition == 'S':
        try:
            number[0] = int(input("Please enter your first number: "))
            number[1] = int(input("Please enter your second number: "))
            print(f"{number[0]} - {number[1]} = {subtraction()}\n\n------------------------------------------------------------------\n\n ")
        except(ValueError):
            print("Error please enter a integer\n\n------------------------------------------------------------------\n\n")
            
    elif condition == 'M':
        try:
            number[0] = int(input("Please enter your first number: "))
            number[1] = int(input("Please enter your second number: "))
            print(f"{number[0]} * {number[1]} = {multiplication()}\n\n------------------------------------------------------------------\n\n ")
        except(ValueError):
            print("Error please enter a integer\n\n------------------------------------------------------------------\n\n")
            
    elif condition == 'D':
        try:
            number[0] = int(input("Please enter your first number: "))
            number[1] = int(input("Please enter your second number: "))
            print(f"{number[0]} / {number[1]} = {division()}\n\n------------------------------------------------------------------\n\n ")
        except(ValueError):
            print("Error please enter a integer\n\n------------------------------------------------------------------\n\n")
        except(ZeroDivisionError):
            print("ZeroDivisionError, You can't divid by '0'\n\n------------------------------------------------------------------\n\n")
    elif condition == 'Q':
        print("Have a nice day!")
        break
    
    else:
        print("Please try again, please choose (A/S/M/D/Q)\n\n------------------------------------------------------------------\n\n ")

  



# Question 2. The Shopping List Maker
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
shopping_list = []
shopping_item = ""


def add_list():
    global shopping_list
    global shopping_item
    shopping_list.append(shopping_item)
    return shopping_item

while True:
    shopping_item = input("(FIRST) Please enter the item you will like to add to your shopping list enter 'quit' when you want to leave.\n\n")
    if shopping_item == 'quit':
        print("\nHere's your list of items\n-------------------------------------")
        for i in shopping_list:
            print(i)
        print("-------------------------------------\nHave a nice a day!\n")
        break
    
    add_list()


# Qustion 2 Task 2: Include a function to remove items from the list.




shopping_list = []
shopping_item = ""
back = 0

def add_list():
    global shopping_list
    global shopping_item
    shopping_list.append(shopping_item)
    return shopping_item

def remove_list():
    global shopping_list
    global shopping_item
    shopping_list.remove(shopping_item)
    return shopping_item


while True:
    shopping_item = input("(SECOND) Please enter [A]dd or [R]emove to edit your shopping list, enter 'quit' when you want to leave.\n\n")
    if shopping_item == 'quit':
        print("\nHere's your list of items\n-------------------------------------")
        for i in shopping_list:
            if i == 'back':
                continue
            print(i)
        print("-------------------------------------\nHave a nice a day!\n")
        break
    
    if shopping_item.upper() == 'A':
        back += 1
        while back == 1:
            shopping_item = input("Please enter the item(s) you would like to add enter 'back' to go back\n\n")
            add_list()
            if shopping_item.lower() == 'back':
                back -= 1


    if shopping_item.upper() == 'R':
        back += 2
        print("-------------------------------------\n")
        for i in shopping_list:
            if i == 'back':
                continue
            print(i)
        while back == 2:
            print("\nHere's your list of items\n-------------------------------------")
            shopping_item = input("Please enter the item(s) you would like to add enter 'back' to go back\n\n")
            remove_list()
            
            if shopping_item != shopping_list:
                print(f"Your ({shopping_item}) has been remove to your list\n")
            else:
                print(f"Something has went wrong please tty again.")
            if shopping_item.lower() == 'back':
                back -= 2



# Question 2 Task 3: Add a function that prints out the entire list in a formatted way.



shopping_list = []
shopping_item = ""
back = 0

def add_list():
    global shopping_list
    global shopping_item
    shopping_list.append(shopping_item)
    return shopping_item

def remove_list():
    global shopping_list
    global shopping_item
    shopping_list.remove(shopping_item)
    return shopping_item


while True:
    shopping_item = input("(THIRD) Please enter [A]dd or [R]emove to edit your shopping list, enter [V]iew list, enter 'quit' when you want to leave.\n\n")
    if shopping_item == 'quit':
        print("\nHere's your list of items\n-------------------------------------")
        for i in shopping_list:
            if i == 'back':
                continue
            print(i)
        print("-------------------------------------\nHave a nice a day!\n")
    
    
    if shopping_item.upper() == 'A':
        back += 1
        while back == 1:
            shopping_item = input("Please enter the item(s) you would like to add enter 'back' to go back\n\n")
            add_list()
            if shopping_item.lower() == 'back':
                back -= 1


    if shopping_item.upper() == 'R':
        back += 2
        print("-------------------------------------\n")
        for i in shopping_list:
            if i == 'back':
                continue
            print(i)
        while back == 2:
            print("\nHere's your list of items\n-------------------------------------")
            shopping_item = input("Please enter the item(s) you would like to add enter 'back' to go back\n\n")
            remove_list()
            
            if shopping_item != shopping_list:
                print(f"Your ({shopping_item}) has been remove to your list\n")
            else:
                print(f"Something has went wrong please tty again.")
            if shopping_item.lower() == 'back':
                back -= 2

    if shopping_item.upper() == 'V':
        print("\nHere's your list of items\n-------------------------------------")
        for i in shopping_list:
            if i == 'back':
                continue
            print(i)
        break
    