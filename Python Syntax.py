##Question 1 Task 1: Code Correction

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!") #tab
else:
    print("Take an umbrella!") #tab


##Question 1 Task 2: Your Mood Today

UserMood = input("How are you feeling today? ")

if UserMood == "Happy":
    print("That's great to hear!")
if UserMood == "happy":
    print("That's great to hear!")

if UserMood == "Sad":
    print("I hope your day gets better!")
if UserMood == "sad":
    print("I hope your day gets better!")

##Question 2 Task 1: Python Naming Convention Practice

PI_VALUE = 3.14 #I don't think this should be touched
UserAge = 25 #Uppercase "U"?
user_location = "New York"
MAXLIMIT = 1000 #don't touch

##Question 3 Task 1: Arithmetic Operations in Daily Life

bread = 2.99
peanut = 4.99
butter = 5.99
jelly = 4.99

Total_Price = (bread + peanut + butter + jelly)
print ("Your total cost is:  $",Total_Price )

##Question 3 Task 2: Bank Interest

#Step 1: make input for Annaul income
#Step 2: make a FIXED interest rate
#Step 3: interest * Annaul

INTEREST_RATE = 1.07 # 7%
annual_income = float(input("What's your annaul income "))
after_interest = INTEREST_RATE * annual_income

print("Your annaul income after interest is: $", after_interest)