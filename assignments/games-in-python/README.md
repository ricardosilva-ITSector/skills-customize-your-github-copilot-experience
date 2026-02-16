# 📘 Assignment: Games in Python

## 🎯 Objective

In this assignment, students build a text-based Hangman game in Python. They will practice loops, conditionals, string handling, and user input while implementing core game logic.

## 📝 Tasks

### 🛠️ Build the Game Setup

#### Description
Create the initial game setup by preparing a word list, selecting one word at random, and displaying the hidden word state.

#### Requirements
Completed program should:

- Store at least 5 possible words in a predefined list
- Randomly select one word at the start of the game
- Display the hidden word using placeholders (for example, `_ _ _ _`)


### 🛠️ Implement Guessing Logic

#### Description
Add the main game loop so the player can guess letters, see progress, and track incorrect attempts.

#### Requirements
Completed program should:

- Ask the player to enter one letter per turn
- Reveal correctly guessed letters in all matching positions
- Decrease remaining attempts for incorrect guesses
- Show the updated word state and attempts remaining after each turn


### 🛠️ Handle Game End Conditions

#### Description
Finish the game by checking win/lose conditions and displaying a clear final message.

#### Requirements
Completed program should:

- End with a win message when all letters in the word are guessed
- End with a lose message when remaining attempts reach zero
- Display the correct word at the end of the game
