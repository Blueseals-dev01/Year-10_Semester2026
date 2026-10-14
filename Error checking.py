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
def input_check():
    while True:
        try:
            num = float(input("Please enter a number: "))
            break
        except ValueError:
            print("That is not a valid float number.\n")

    print(f"The number you entered is {num}")

# Main routine
input_check() # This call the function to be used.SS
