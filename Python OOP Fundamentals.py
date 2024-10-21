'''
Question 1. City Infrastructure Management System
Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

- Code Example: Provide a basic structure for the Vehicle class without methods.

    class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
'''

# Vehicle class with attributes and method to update owner
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num   # Vehicle registration number
        self.type = type                     # Vehicle type (e.g., car, bike, truck)
        self.owner = owner                   # Vehicle owner

    # Method to update the owner of the vehicle
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to: {self.owner}")

# Demonstration of creating Vehicle objects and updating their owners

# Create instances of the Vehicle class
vehicle1 = Vehicle("ABC123", "Car", "John reef")
vehicle2 = Vehicle("XYZ789", "Truck", "Alice Smith")
vehicle3 = Vehicle("LMN456", "Bike", "David Johnson")

# Display the details of the vehicles
print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, owned by {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, owned by {vehicle2.owner}")
print(f"Vehicle 3: {vehicle3.registration_number}, {vehicle3.type}, owned by {vehicle3.owner}")

# Update the owner of vehicle1
print("\nUpdating the owner of vehicle 1:")
vehicle1.update_owner("Jane Doe")

# Display the updated details of vehicle1
print(f"Vehicle 1 after update: {vehicle1.registration_number}, {vehicle1.type}, owned by {vehicle1.owner}")



'''
Question 1
Task 2: Event Management System Enhancement

- Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants.
 Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

- Code Example: Basic Event class without participant tracking.

    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
'''

class Event:
    def __init__(self, name, date):
        self.name = name         # Name of the event
        self.date = date         # Date of the event
        self.participant_count = 0  # Initialize participant count to zero

    # Method to add a participant
    def add_participant(self):
        self.participant_count += 1  # Increment the participant count
        print(f"Participant added. Total participants: {self.participant_count}")

    # Method to get the current participant count
    def get_participant_count(self):
        return self.participant_count  # Return the current count of participants

# Demonstration of creating an Event object and managing participants

# Create an instance of the Event class
event1 = Event("Tech Conference", "2024-11-15")

# Display initial details of the event
print(f"Event Name: {event1.name}, Date: {event1.date}, Initial Participants: {event1.get_participant_count()}")

# Adding participants
print("\nAdding participants:")
event1.add_participant()
event1.add_participant()
event1.add_participant()

# Display the final participant count
print(f"\nTotal participants after adding: {event1.get_participant_count()}")
