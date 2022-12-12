# Import the random module
import random

# Define a list of possible choices
choices = ["rock", "paper", "scissors"]

# Define a function to play the game
def play_game():
  # Prompt the user to choose rock, paper, or scissors
  user_choice = input("Choose rock, paper, or scissors: ")

  # Generate a random choice for the computer
  computer_choice = random.choice(choices)

  # Compare the user's choice to the computer's choice
  # and print the result
  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
  elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
  elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
  else:
    print("The computer wins!")

# Play the game
play_game()
