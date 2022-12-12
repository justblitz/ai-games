# This is a simple guessing game in Python

import random

# Generate a random number between 1 and 10 (inclusive)
secret_number = random.randint(1, 10)

# Ask the player to guess the number
guess = int(input("Guess a number between 1 and 10: "))

# Keep track of the number of guesses the player has made
num_guesses = 1

# Keep asking the player to guess until they get it right
while guess != secret_number:
    # If the guess is too high, tell the player and ask them to guess again
    if guess > secret_number:
        print("Your guess is too high. Try again.")
    # If the guess is too low, tell the player and ask them to guess again
    else:
        print("Your guess is too low. Try again.")
        
    # Get the player's next guess
    guess = int(input("Guess a number between 1 and 10: "))
    
    # Increment the number of guesses the player has made
    num_guesses += 1

# If the player has made more than 3 guesses, tell them they lost
if num_guesses > 3:
    print("You lost! The secret number was {}".format(secret_number))
# Otherwise, tell the player they won
else:
    print("You won! It only took you {} guesses.".format(num_guesses))
