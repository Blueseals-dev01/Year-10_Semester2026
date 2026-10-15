# Error checking
# Sam M
# 16 October 2026

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
'''def input_check(question): # 'question' is a placeholder
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
print(f"Your numbers added together result in {sum}.")'''

# V1.4 Checking for a vaild input using try/except method
# Using parameters (placeholders) to help make the code more phytonic
# Function that asks user to enter a number from a range.
def valid_num(question, low, high):
    error = f"Whoops, that is not an integer between {low} and {high}."
    while True: 
        try:
            response = int(input(question))
            # if the response is >= to the low number or <= high nr, then continue
            if low <= response <= high:
                break # Stop the loop

            else:
                print(f"{error}\n")

        except ValueError:
            print(error)
    return response # This makes the response available
                    # to be used outside the function

# Main rountine
if __name__ =="__main__":

    num1 = valid_num("Enter a number between 1-10: ",1,10)
    print(f"The number you entered is {num1}.\n")

    num2 = valid_num("Enter a number between 15 and 20: ", 15, 20)
    print(f"The number you entered is {num2}.\n")

    num3 = valid_num("Enter a number between 70 and 90: ",70,90)
    print(f"The number you entered is {num3}.\n")

    # Multiply the reslult of num1, num2 and num3
    multiply = num1 * num2 * num3
    print(f"Your numbers multipled together result in {multiply}.")

    # Adding the numbers
    sum = num1 * num2 * num3
    print(f"Your numbers added together result in {sum}.")
    
    