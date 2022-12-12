// Welcome the player to the game
console.log("Welcome to the guessing game!");

// Generate a random number between 1 and 100
const secretNumber = Math.floor(Math.random() * 100) + 1;

while (true) {
  // Get a guess from the player
  const guess = prompt("Enter a guess: ");
  
  // Convert the guess to a number
  const guessNumber = Number(guess);
  
  // Check if the guess is a valid number
  if (isNaN(guessNumber)) {
    console.log("Invalid input. Please enter a number.");
    continue;
  }
  
  // Check if the guess is correct
  if (guessNumber === secretNumber) {
    console.log("You guessed the correct number! Well done.");
    break;
  } else if (guessNumber < secretNumber) {
    console.log("Your guess is too low. Try again.");
  } else {
    console.log("Your guess is too high. Try again.");
  }
}
