'''
 Question 1. The Range Riddle
Objective: The aim of this assignment is to deepen your understanding of Python's range() function.

Task 1: Your Mood Today Write a program that prints off different moods for each day of the week. 
Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, 
randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."
'''

# #First:  randomize each day of the week with a mood

# create list for moods with random.
# create a list for week days
# list for week days increase by 1 and resets at 7
    
# #Last: Print the week day and mood

import random

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday', 'Saturday', 'Sunday']
moods = ['Happy', 'Sad', 'Calm', 'Energetic']

num = 0
while num < 7:
    mood_type = random.randint(0,3)
    input()
    print(f"(First Loop) On {week_days[num]}, you were feeling {moods[mood_type]}")
    num += 1


'''
2. Double Scoop with Nested Loops
Objective: The aim of this assignment is to practice using nested loops in Python.

Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the 
day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer 
loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, 
randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.

Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" 
"On Wednesday morning you were tired"
'''

import random


week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday', 'Saturday', 'Sunday']
moods = ['Happy', 'Sad', 'Calm', 'Energetic']
day_time = ['morning', 'afternoon', 'evening']
ones = ['one']
num = 0
while num < 7:
    input()
    for time in day_time:
        for one in ones:
            mood = random.randint(0,3)
            print(f"On {week_days[num]}, at {time} you were feeling {moods[mood]}")

    num += 1