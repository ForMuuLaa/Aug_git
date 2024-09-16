
'''
Qestion 1. Product Review Analysis
Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average".
  We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."
'''

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
        ]

words = "good", "excellent", "bad", "poor", "average"

def word_highlights():
    global words
    global reviews
    
    for review in reviews:
        new_review = review  
        for word in words:
            if word in new_review:
                new_review = new_review.replace(word, word.upper())

        print(new_review)                      
word_highlights()


'''
Question 1 Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
'''

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
        ]
def negative_words_count():
    global negative_words
    global reviews
    neg_count = 0
    for review in reviews:
        new_review = review  
        for negative in negative_words:
            if negative in new_review:
                neg_count += 1
    return neg_count


def positive_words_count():
    global positive_words
    global reviews
    pos_count = 0
    for review in reviews:
        new_review = review  
        for positive in positive_words:
            if positive in new_review:
                pos_count += 1
    return pos_count


print(f"You have {negative_words_count()} negative reviews and {positive_words_count()} positive reviews.")

'''Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

Example: "This product is really good. I'm...",'''

for review in reviews:
    new_review = review
    index = 0
    for char in new_review:
        # print(char, end='')
        if index > 30 and char == ' ':
            slice_review = new_review[:index]
            new_str = slice_review + '...'
            print(f"{new_str} \n")
            break    
        else:
            index += 1
 

'''2. User Input Data Processor
Objective: The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name.
 Both should be at least 2 characters long. If not, print an error message.

NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top,
 all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.'''



def length_validator(name):
    count = 0
    for char in name:
        if char != ' ':
            count += 1
        elif char == ' ' and count > 2:
            print(f"Username '{name}' is a valid username")
            
        elif ' ' not in name:
            print("Error you need a first and last name")
        else:
            print("Error username must be minimun of two characters long for both first and last name")
            
    return name

while True:
    name = input("Please enter your username, Both first and last names: ex (First Last)\n")
    length_validator(name)
    if bool(name) == False:
        print("Pleae enter a username")
    elif ' ' not in name:
            print("Error you need a first and last name")
    continue_input = input('Would you like to in put another username: (yes/no)\n')
    if continue_input != 'yes'.lower():
        break
