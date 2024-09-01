##Question 1 Task 1: Decisions at the Crossroad

number = int(input("Enter a number: ")) # add int

if number > 0: 
    print("The number is positive.")
elif number == 0: # "=="
    print("The number is zero.")
else : # remove "number < 0:" and add ":"6 or change else to elif
     print("The number is negative.")

##Question 2: The Greatest Showdown
'''
Task 1: Identify the Greatest Write a Python program that asks the user to 
enter three numbers. Your code should then identify and print out the largest
number among the three.
'''
print("Please enter three numbers")
first_number = int(input())
second_number = int(input())
third_number = int(input())

#this checks for largest or equal to largest for first_number
if first_number >= second_number and first_number >= third_number:
    print(f"The largest number is {first_number}.")

#this checks for largest or equal to largest for second_number
elif second_number >= first_number and second_number >= third_number:
    print(f"The largest number is {second_number}.")

#this checks for largest or equal to largest for third_number 
elif third_number >= second_number and third_number >= first_number:
    print(f"The largest number is {third_number}.")
else :
    print(f"The largest number is {first_number}.") #if all numbers are equal

'''
Task 2: Identify the Smallest Improve upon your code from Task 1 to also
determine the smallest number among the three and print it out.
'''

print("Please enter three numbers")
first_number = int(input())
second_number = int(input())
third_number = int(input())

#this checks for largest or equal to largest for first_number
if first_number >= second_number and first_number >= third_number:
    print(f"The largest number is {first_number}.")
#this checks for largest or equal to largest for second_number
elif second_number >= first_number and second_number >= third_number:
    print(f"The largest number is {second_number}.")
#this checks for largest or equal to largest for third_number 
elif third_number >= second_number and third_number >= first_number:
    print(f"The largest number is {third_number}.")
else :
    print(f"The largest number is {first_number}.") #if all numbers are equal


#this checks for smallest or equal to smallest for first_number
if first_number <= second_number and first_number <= third_number:
    print(f"The smallest number is {first_number}.")
#this checks for smallest or equal to smallest for second_number
elif second_number <= first_number and second_number <= third_number:
    print(f"The smallest number is {second_number}.")
#this checks for smallest or equal to smallest for third_number 
elif third_number <= second_number and third_number <= first_number:
    print(f"The smallest number is {third_number}.")
else :
    print(f"The largest number is {first_number}.") #if all numbers are equal

##Question 3

'''Task 1: Leap Year Checker Write a Python program that prompts the user to input a 
year. The program should determine if the given year is a leap year or not and then 
display an appropriate message. Please note that this is the definition of a leap year:
 Every year that is exactly divisible by four is a leap year, except for years that are 
 exactly divisible by 100, but these centurial years are leap years if they are exactly
   divisible by 400.'''

#first step 1 ask for user's year [year]
#step 2 if evenly divisible 4 = true if not, false [leap]
#step 3 if evenly divisible 100 = Fasle if not, true [skip]
#step 4 if evenly divisible 400 = True [unless]
#step 5 if [unless] == True and skip == False then [skip] will = True
#step 6 if [leap] and [skip] == true then print true if not, false
#last step determine if the given year is a leap year

#this was harder and more copmlicated than it should be why are leap years like this?
year = int(input("Please enter your year "))

leap = year
skip = year
unless = year

if (leap % 4) == 0:
    leap = True
else : leap = False

if (skip % 100) == 0:
    skip = False
else : skip = True

if (unless % 400) == 0:
    unless = True
else : unless = False

if unless == True and skip == False:
    skip = True

if leap == True and skip == True:
    print(f"True, {year} is a leap year")
else:
    print(f"Fasle, {year} is not a leap year")