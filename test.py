# shopping_list = []
# shopping_item = ""


# def add_list():
#     global shopping_list
#     global shopping_item
#     shopping_list.append(shopping_item)
#     return shopping_item

# while True:
#     shopping_item = input("(FIRST) Please enter the item you will like to add to your shopping list enter 'quit' when you want to leave.\n\n")
#     if shopping_item == 'quit':
#         print("\nHere's your list of items\n-------------------------------------")
#         for i in shopping_list:
#             print(i)
#         print("-------------------------------------\nHave a nice a day!\n")
#         break
    
#     add_list()






# shopping_list = []
# shopping_item = ""
# back = 0

# def add_list():
#     global shopping_list
#     global shopping_item
#     shopping_list.append(shopping_item)
#     return shopping_item

# def remove_list():
#     global shopping_list
#     global shopping_item
#     shopping_list.remove(shopping_item)
#     return shopping_item


# while True:
#     shopping_item = input("(SECOND) Please enter the item you will like to [A]dd or [R]emove from you shopping list, enter 'quit' when you want to leave.\n\n")
#     if shopping_item == 'quit':
#         print("\nHere's your list of items\n-------------------------------------")
#         for i in shopping_list:
#             if i == 'back':
#                 continue
#             print(i)
#         print("-------------------------------------\nHave a nice a day!\n")
#         break
    
#     if shopping_item.upper() == 'A':
#         back += 1
#         while back == 1:
#             shopping_item = input("Please enter the item(s) you would like to add enter 'back' to go back\n\n")
#             add_list()
#             if shopping_item.lower() == 'back':
#                 back -= 1


#     if shopping_item.upper() == 'R':
#         back += 2
#         print("-------------------------------------\n")
#         for i in shopping_list:
#             if i == 'back':
#                 continue
#             print(i)
#         while back == 2:
#             print("\nHere's your list of items\n-------------------------------------")
#             shopping_item = input("Please enter the item(s) you would like to add enter 'back' to go back\n\n")
#             remove_list()
            
#             if shopping_item != shopping_list:
#                 print(f"Your ({shopping_item}) has been remove to your list\n")
#             else:
#                 print(f"Something has went wrong please tty again.")
#             if shopping_item.lower() == 'back':
#                 back -= 2









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
    