
# Author Sam Mackenzie
# 25 September 2026
# Version 2
# While loop to test the program

keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? ")
    
    # print(like_coffee) # checking the input is stored
    print(f"Your answer was '{like_coffee}'.")
    
    # Check the input and respond
    if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee == "Y" or like_coffee == " Yas":
        print("That is great! I like coffee too.")
        keep_going = "Finish"
    elif like_coffee == "No" or like_coffee == "no" or like_coffee == "N" or like_coffee == "n" or like_coffee == "Nah":
        print("You are missing out! Why not give it a try?")
        keep_going = "End"
    else:
       print("I don't understand. Please try again.")
    