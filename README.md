# Hangman Game in Python

## Description
This is a simple implementation of the classic Hangman game in Python. The player has to guess a randomly selected word by suggesting letters within a limited number of attempts. Each incorrect guess reduces the number of available attempts, and the player must try to figure out the word before running out of chances.

## Features
- Randomly selects a word from a predefined list.
- Player can guess one letter at a time.
- The game ends when the player either guesses the word correctly or exhausts all attempts.
- Simple console-based interface.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Daniel-Abiy/hangman-game.git
   ```

2. Navigate to the project folder:

   ```bash
   cd hangman-game
   ```

3. Make sure you have Python installed (version 3.x).

4. Run the game script:

   ```bash
   python Hangman.py
   ```

## How to Play
- The game will display a series of underscores representing each letter of the word.
- You will have 6 chances to guess the correct letters.
- Each time you guess a correct letter, it will reveal the letter in the word.
- If you guess incorrectly, you lose one attempt.
- The game ends when you either guess the entire word or run out of chances.

## Example Gameplay
```
_ _ _ _ _ _ 
Enter Your alphabet: E
_ _ E _ _ _
Enter Your alphabet: A
_ _ E A _ _
Enter Your alphabet: X
Sorry, you have finished all of your chances
The word was: EXAMPLE
```

## Contributing
Feel free to fork the project, make improvements, and submit pull requests.

## License
This project is open-source and available under the MIT License.
