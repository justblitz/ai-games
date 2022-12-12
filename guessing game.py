import random

print("Welcome to the guessing game!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

while True:
    # Get a guess from the player
    guess = input("Enter a guess: ")
    
    # Convert the guess to a number
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    # Check if the guess is correct
    if guess == secret_number:
        print("You guessed the correct number! Well done.")
        break
    elif guess < secret_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
