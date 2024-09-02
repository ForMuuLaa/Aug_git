#   Python List Transformation

'''Objective: The aim of this assignment is to practice list operations and transformations.

Problem Statement: You've been given a list of grades from an exam. You need to process and analyze these grades.'''

# question 1 Task 1: Given the list of grades:
# Sort the grades in descending order and print the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)

print(grades)


# question 1 Task 2: Calculate the average grade and print it.

grades_copy = grades.copy()
total = 0
for i in grades_copy:
    total = total + i
grade_average = total/ 10

print(f"{grade_average}%")

# question 2 Task 1  Advanced List Methods and Identity Operators

'''Problem Statement: You have two lists of student names. One list contains the names of students who have submitted their
 assignments, and the other list contains the names of students who attended the last class.

Given the two lists

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here?
And how can you check to see if Alice is in both submitted and attended in one if statement?
'''

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print("True") if "Alice" in submitted and "Alice" in attended else "False"


# question 3 Task 1 Advanced Slicing Techniques
'''
Objective: The aim of this assignment is to use Python list slicing.

Problem Statement: You have a list of daily temperatures for one month, and you'd like to extract specific data from it.

Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). Expected Outcome:

83, 85, 86, 87, 88, 89, 90,
''' 
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

slice_temp = temperatures[7:14]
print(slice_temp)

'''
Task 2: Extract all the temperatures above 100. HINT: add the temperatures over 100 
to a new list, or use list slicing to get the temperatures.
'''

above_100_temp = temperatures[24:30]
print(above_100_temp)