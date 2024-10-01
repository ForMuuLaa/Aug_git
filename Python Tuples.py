'''
Question 1. Tuple Mastery in Python
Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"
'''
flight_itinerary = []

def add_flight_itinerary():
    global flight_itinerary

    name = input('Please enter your name: ')
    origin = input('Please enter your origin: ')
    destination = input('Please enter your destination: ')

    flight_itinerary.append((name, origin, destination))

def display_flight_itinerary(flight_itinerary):
    
    for num, flight in enumerate(flight_itinerary):
        print(f"Itinerary {num + 1}: {flight[0]} - From {flight[1]} to {flight[2]}")

def main():
    while True:
        action = input('Would your like to [A]dd or [D]isplay your flights. Enter "Done" to quit\n ').lower()
        if action == 'done':
            break
        elif action == 'a':
            add_flight_itinerary()
        elif action == 'd':
            display_flight_itinerary(flight_itinerary)
        else:
            print("Please enter (A/D/Done)")

main()


'''
Question 2. Python Data Structure Challenges in Real-World Scenarios
Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.
'''

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    while True:
        name = input("Please enter the name of the book. Enter 'done' to go back: ")

        if name == 'done':
            break
        if any(book[0] == name for book in library):
            #"if (book[0] == name for book in library)" will always be Truthy because its a non-empty object.
            #not actually comparing the values. just creating a generator object, which will always be considered a truthy in python.
            #The any() function forces this generator to be evaluated.
            print(f"This '{name}' book is already in the libraty")
            break
        else:
            author = input("Please enter the name of the author: ")
            library.append((name, author))
            print("Your book has been added")
        

add_book(library)
print(library)

