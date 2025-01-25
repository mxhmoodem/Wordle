import random

def main():
    title = 'Wordle'
    print(f"Welcome to {title}!")
    print("Press q to quit at anytime.")

    word_bank = []
    with open("words.txt") as word_file:
        for line in word_file:
            word_bank.append(line.strip().lower())
    
    while True:
        play_word_game(word_bank, max_turns=5)
        choice = input("\nPlay again? (y/n): ").lower()
        if choice not in ("y", "yes"):
            print("Goodbye!")
            break


def play_word_game(word_bank, max_turns=5):
    """
    Plays one round of the word game.
    """
    word_to_guess = random.choice(word_bank)
    misplaced_guesses = []
    incorrect_guesses = []
    previous_guesses = []
    turns_taken = 0

    print(f"\nThere are {len(word_to_guess)} letters in the word to guess.")
    print(f"You have {max_turns} turns total.")

    while turns_taken < max_turns:
        guess = input("\nWhat is your guess?: ").lower()
        
        if guess in ('q', 'quit'):
            print("You chose to quit this round.")
            return

        if len(guess) != len(word_to_guess) or not guess.isalpha():
            print(f"Please enter a valid {len(word_to_guess)}-letter word.")
            continue

        previous_guesses.append(guess)

        revealed_positions = []
        remaining_letters = list(word_to_guess)  # Track unmatched letters in the word to guess

        # Check for correct letters in the correct positions
        for i in range(len(guess)):
            if guess[i] == word_to_guess[i]:
                revealed_positions.append(guess[i])
                remaining_letters[i] = None  # Mark this letter as matched
            else:
                revealed_positions.append("_")

        # Check for misplaced letters
        for i in range(len(guess)):
            if guess[i] != word_to_guess[i] and guess[i] in remaining_letters:
                if guess[i] not in misplaced_guesses:
                    misplaced_guesses.append(guess[i])
                remaining_letters[remaining_letters.index(guess[i])] = None  # Mark as used

        # Update incorrect guesses
        for letter in guess:
            if letter not in word_to_guess and letter not in incorrect_guesses:
                incorrect_guesses.append(letter)

        print(" ".join(revealed_positions))
        print(f"Misplaced letters: {misplaced_guesses}")
        print(f"Incorrect letters: {incorrect_guesses}")
        print(f"Previous guesses: {previous_guesses}")

        turns_taken += 1

        if guess == word_to_guess:
            print("Congratulations, you guessed it!")
            return

        if turns_taken < max_turns:
            print(f"You have {max_turns - turns_taken} turns left.")
        else:
            print(f"\nSorry, you've used all {max_turns} turns.")
            print(f"The word was '{word_to_guess}'.")
            return


if __name__ == "__main__":
    main()
