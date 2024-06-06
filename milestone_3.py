# milestone_3.py

import random

def check_guess(guess, secret_word):
    """
    Check if the guessed letter is in the secret word.
    """
    # Convert the guess into lower case
    guess = guess.lower()

    # Check if the guess is in the word
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def validate_guess(guess):
    """
    Validate the user's guess.
    """
    if len(guess) == 1 and guess.isalpha():
        return True
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        return False

def ask_for_input(secret_word):
    """
    Continuously ask the user for a letter and validate it.
    """
    # Create a while loop to continuously ask the user for a letter
    while True:
        # Ask the user to guess a letter
        guess = input("Guess a letter: ")

        # Validate the guess
        if validate_guess(guess):
            break

    # Call the check_guess function to check if the guess is in the word
    check_guess(guess, secret_word)

if __name__ == "__main__":
    # Secret word chosen by the computer
    secret_word = random.choice(["apple", "banana", "cherry", "mango", "grape"])

    # Call the ask_for_input function
    ask_for_input(secret_word)
