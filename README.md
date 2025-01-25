# Wordle Game
A command-line implementation of the popular word-guessing game, Wordle. Players must guess a hidden word within a limited number of turns, receiving feedback on their guesses after each attempt.

## Features
- **Random Word Selection**: A word is chosen randomly from a `words.txt` file.
- **Turn-Based Gameplay**: Players have a configurable number of turns (default: 5) to guess the word.
- **Feedback**:
  - Letters in the correct position are revealed.
  - Letters in the word but in the wrong position are flagged as "misplaced."
  - Letters not in the word are marked as incorrect.
- **Quit Anytime**: Players can type `q` or `quit` to exit the game.
- **Replay Option**: Players can choose to play multiple rounds.

## How to Play
1. Clone the repository or download the game files.
2. Ensure you have Python 3 installed on your machine.
3. Place a `words.txt` file in the same directory as the script. The file should contain a list of valid words, one per line.
4. Run the script:

   ```bash
   python wordle.py
