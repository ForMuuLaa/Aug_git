# question 1
'''
question 1 Task 1: Code Correction You are provided with a Python script that is supposed to guide
a user through an adventure game, but it has some errors. Identify and fix them.
'''
# Task 1: Code Correction
# # Buggy Code:
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    

    # question 1 Task 2: Setting the Scene

'''Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want 
to "light a torch" or "proceed in the dark", and provide outcomes for each decision.'''

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action_one = input("climb a tree or cross a river? ")
    if action_one == "climb a tree":
        print("You found a bird's nest!")
    elif action_one == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action_two = input("Do you want to (light a torch) or (proceed in the dark)? ")
    if action_two == "light a torch":
        print("You find a hidden treasure!")
    else:
        print("You have gotten lost")


 # question 1 Task 3: Default Path
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action_one_ = input("climb a tree or cross a river? ")
    if action_one_ == "climb a tree":
        print("You found a bird's nest!")
    elif action_one_ == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action_two_ = input("Do you want to (light a torch) or (proceed in the dark)? ")
    if action_two_ == "light a torch":
        print("You find a hidden treasure!")
    else:
        print("You have gotten lost")
else:
    print("Default Path has been chosen")

# 2.  question 1 Quick Decisions: The Event Planner

'''Task 1: Code Correction You are provided with a Python script that is supposed to help
 in event planning, but it has errors. Identify and fix them.'''

# Task 1: Code Correction
# Buggy Code:

attendees = int(input("Enter number of attendees: "))

venue = "large" if attendees > 100 else "conference room"
if venue == "large":
    venue = "Large Hall"
print(f"Venue is a {venue}")


## Task 2: Venue Selection

'''Based on the corrected code from Task 1, further enhance your code to recommend
 additional things like "audio system" or "projector" based on the number of attendees'''


attendees = int(input("Enter number of attendees: "))
projector = False
audio_system = False
# Determine the type of venue
if attendees > 100:
    venue = "Large Hall"
    projector = True
    audio_system = True
elif attendees > 50:
    venue = "Conference Room"
    audio_system = True
else:
    venue = "conference room"

# Determine the venue setup
if projector and audio_system:
    print(f"Your venue is a {venue} with a projector and audio system.")
elif not projector and audio_system:
    print(f"Your venue is a {venue} with an audio system.")
else:
    print(f"Your venue is a {venue}.")


## Task 3: Catering Choices
'''Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if
 yes, otherwise recommend "Gourmet Meals Caterers".'''

attendees = int(input("Enter number of attendees: "))
projector = False
audio_system = False
food = input("would you like (veg/non-veg)? ")
# Determine the type of venue
if food == "veg":
    food = True
else:
    food = False
if attendees > 100:
    venue = "Large Hall"
    projector = True
    audio_system = True
elif attendees > 50:
    venue = "Conference Room"
    audio_system = True
else:
    venue = "conference room"

# Determine the venue setup
if food == True:
    food = "Veggie Delight Caterers as your recommendation"
else:
    food = "Gourmet Meals Caterers as your recommendation"
if projector and audio_system and food:
    print(f"Your venue is a {venue} with a projector and audio system with {food}.")
elif not projector and audio_system and food:
    print(f"Your venue is a {venue} with an audio system with {food}.")
elif projector and audio_system and not food:
    print(f"Your venue is a {venue} with a projector and audio system with {food}.")
elif not projector and audio_system and not food:
    print(f"Your venue is a {venue} with an audio system with {food}.")
else:
    print(f"Your venue is a {venue} with {food}.")

