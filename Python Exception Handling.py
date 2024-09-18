'''1. Exceptional Weather Forecast
Objective: The aim of this assignment is to enhance your understanding of exception handling by creating
 a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.'''

try:
    weather_temp = int(input(" Please enter your weather temp in Fahrenheit: "))
    print(f"Your weather temp is {weather_temp} degrees Fahrenheit")
    print("-----------------------------\n")
except(ValueError, TypeError):
    print("Error must enter a integer. Please try again")
    print("-----------------------------\n")


'''Task 2: Temperature Conversion Write a function that converts the Fahrenheit 
temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.'''


try:
    weather_temp = int(input(" Please enter your weather temp in Fahrenheit to convert to Celsius: "))
    converted_temp = (weather_temp - 32) * 5/9
    print(f"{weather_temp} degrees in Fahrenheit is {converted_temp:.2f} degrees in Celsius")
    print("-----------------------------\n")
except(ValueError, TypeError):
    print("Error must enter a integer. Please try again")
    print("-----------------------------\n")



'''Task 3: User Experience Implement an else block that prints the 
converted temperature in a user-friendly format. 

Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."'''


try:
    weather_temp = int(input(" Please enter your weather temp in Fahrenheit to convert to Celsius: "))
except(ValueError, TypeError):
    print("Error must enter a integer. Please try again")
    print("-----------------------------\n")
else:
    converted_temp = (weather_temp - 32) * 5/9
    print(f"{weather_temp} degrees in Fahrenheit is {converted_temp:.2f} degrees in Celsius")
    print("-----------------------------\n")


'''Task 4: Finally Add a finally block that thanks the user for
 using the weather forecast application, ensuring that this message is
 displayed regardless of whether an exception was caught or not.'''


try:
    weather_temp = int(input(" Please enter your weather temp in Fahrenheit to convert to Celsius: "))
except(ValueError, TypeError):
    print("Error must enter a integer. Please try again")
else:
    converted_temp = (weather_temp - 32) * 5/9
    print(f"{weather_temp} degrees in Fahrenheit is {converted_temp:.2f} degrees in Celsius")
finally:
    print("Thank you for use our weather forecast application today")
    print("-----------------------------\n")


