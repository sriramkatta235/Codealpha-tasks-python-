# Hangman Game in Python

## Overview

This is a simple command-line Hangman game written in Python. The program randomly selects a word from a predefined list, and the player attempts to guess it one letter at a time before running out of attempts.

## Features

- Randomly selects a word from a list.
- Displays hidden letters as underscores (`_`).
- Tracks guessed letters.
- Limits incorrect guesses to 6 attempts.
- Prevents repeated guesses.
- Displays a win or loss message at the end of the game.

## Requirements

- Python 3.x
- No external libraries are required (uses Python's built-in `random` module).

## How to Run

1. Save the file as `hangman_game.py`.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:

```bash
python hangman_game.py
```

## Gameplay

- The game randomly selects one word from a predefined list.
- The player guesses one letter at a time.
- Correct guesses reveal the letters in the word.
- Incorrect guesses reduce the remaining attempts.
- The player wins by guessing the complete word before using all six attempts.

## Future Enhancements

- Add a larger word database.
- Implement ASCII art for the hangman.
- Add input validation for invalid characters.
- Support multiple difficulty levels.
- Allow replay without restarting the program.

## Author

**Katta Sriram**  
**Computer Science Engineering**
