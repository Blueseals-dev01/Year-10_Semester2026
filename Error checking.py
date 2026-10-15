# Error checking
# Sam M
# 14 October 2026

# Code that tests whether a vaild input was given (v1)
'''done = True # Boolean variable set to True
while done:
    num = int(input("Please enter your value as an integer: "))
    done = False

print(f"The number you entered is {num}")'''

# Using a try and except method to catch errors (V2)
#Use try and except method to catch errors
'''done = False
while not done: 
    try: # This method tries for a vaild input
        num = float(input("Please enter a number: "))
        done = True

    except ValueError: 
        print("That is not a valid float number. \nUse a fullstop as decimal indicator")

print(f"The number you entered is {num}.")'''

# Check for valid input and recyling code with a function (V1.2)
# Create a function to call every time I ask the user
# for a number. A function is a chunk of code that does
# something.
# Functions can be used over and over again.
# To use a function (call it), write out its name with
# parenthesis at the end.
# To create a function, start with the word def
'''def input_check():
    while True:
        try:
            num = float(input("Please enter a number: "))
            break
        except ValueError:
            print("That is not a valid float number.\n")

    print(f"The number you entered is {num}")

# Main routine
input_check() # This call the function to be used.'''

# V1.3 Valid input checker
# Use parameters in the function
# More Pythonic
def input_check(question): # 'question' is a placeholder
    while True:
        error = "That is not a valid number."
        print(question)
        try:
            num = float(input())
            break
        except ValueError:
            print(error)

    return(num) # Gives back the value of num
# So that I can use it outside of
# The function.

# Main rountine
num1 = input_check("Please enter your first number:")
print(f"The number you stored is {num1}")

num2 = input_check("Please enter the second number:")
print(f"The second number you stored is {num2}")

sum = num1 + num2
print(f"Your numbers added together result in {sum}.")