##Question 1 Task 1: Code Correction

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!") #tab
else:
    print("Take an umbrella!") #tab


##Question 1 Task 2: Your Mood Today

user_mood = input("How are you feeling today? ")

if user_mood == "Happy":
    print("That's great to hear!")
if user_mood == "happy":
    print("That's great to hear!")

if user_mood == "Sad":
    print("I hope your day gets better!")
if user_mood == "sad":
    print("I hope your day gets better!")

##Question 2 Task 1: Python Naming Convention Practice

PI_VALUE = 3.14 #I don't think this should be touched
user_age = 25 #snakecase?
user_location = "New York"
MAXLIMIT = 1000 #don't touch

##Question 3 Task 1: Arithmetic Operations in Daily Life

item_bread = 2.99 
item_peanut = 4.99
item_butter = 5.99
item_jelly = 4.99

item_total_price = (item_bread + item_peanut + item_butter + item_jelly)
print ("Your total cost is:  $",item_total_price)

##Question 3 Task 2: Bank Interest

#Step 1: make input for Annaul income
#Step 2: make a FIXED interest rate
#Step 3: interest * Annaul

INTEREST_RATE = 1.07 # 7%
annual_income = float(input("What's your annaul income "))
annual_after_interest = INTEREST_RATE * annual_income

print("Your annaul income after interest is: $", annual_after_interest)