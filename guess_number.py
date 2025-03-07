# Guess my number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random



print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
max_tries = 3

# guessing loop
while guess != the_number:
    if tries == max_tries:
        print("CURVA!!!!")
        break
    elif guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")

    tries += 1    

    guess = int(input("Take a guess: "))   

if tries == max_tries:
    print ("YOU FINALY A LAW!")
else:           
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")        

input("\n\nPress the enter key to exit.") 