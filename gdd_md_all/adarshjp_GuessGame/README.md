## Guessing Game Design Document

### Introduction

This document outlines the design of a simple guessing game where the computer generates a random number and the user tries to guess it. This project will focus on implementing basic object-oriented programming (OOP) concepts such as classes, objects, methods, and conditional statements.

### System Requirements

* The game should generate a random number within a user-defined range (e.g., 1 to 100).
* The user should be able to guess the number by providing input.
* The game should provide feedback after each guess, indicating if it's too high, too low, or correct.
* The game should keep track of the number of guesses made.
* The user should have the option to play again or quit after each round.

### System Design

The system will be designed using an object-oriented approach, consisting of the following classes:

* **Game:** This class manages the overall game flow, including:
    * Generating the random number.
    * Taking user input (guesses).
    * Providing feedback on guesses.
    * Tracking guesses and game state (playing, won, lost).
    * Handling play again requests.
* **Guesser:** This class represents the user and handles:
    * Taking user input for guesses.
    * Interacting with the Game class for feedback and game state information.

### Class Details

* **Game:**
    * Methods:
        * `generateRandomNumber(int min, int max)`: Generates a random number within the specified range.
        * `getGuess()`: Receives user input for guessing the number.
        * `checkGuess(int guess)`: Compares the guess with the generated number and returns feedback (too high, too low, or correct).
        * `incrementGuessCount()`: Increases the number of guesses made.
        * `isGameOver()`: Checks if the game is over (won or lost).
        * `playAgain()`: Prompts the user to play again and resets the game state if yes.
    * Attributes:
        * `randomNumber`: The randomly generated number.
        * `userGuess`: The user's current guess.
        * `guessCount`: The number of guesses made.
        * `gameState`: The current state of the game (playing, won, lost).
* **Guesser:**
    * Methods:
        * `getUserInput()`: Takes user input as an integer representing the guess.
    * Attributes:
        * None (stateless)

### User Interface

The user interface can be implemented using simple text input and output for commands and feedback.

### Error Handling

The system should handle invalid user input (e.g., non-numeric characters) and gracefully provide error messages.

### Testing

The system should be tested with various scenarios to ensure its functionality and responsiveness. Unit tests can be used to test individual methods and integration tests can test the overall game flow.

### Future Enhancements

* Offering different difficulty levels with smaller or larger number ranges.
* Providing additional feedback or hints based on the user's guesses.
* Implementing leaderboards or scores to track past performance.
