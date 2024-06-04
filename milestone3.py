# milestone_3.py

import random

def check_guess(guess, secret_word):
    """
    Check if the guessed letter is in the secret word.
    """
    # Step 2: Convert the guess into lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    """
    Continuously ask the user for a letter and validate it.
    """
    # Step 1: Create a while loop to continuously ask the user for a letter
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Guess a letter: ")

        # Step 3: Check if the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 4: If the guess passes the checks, break out of the loop
            break
        else:
            # If the guess does not pass the checks, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Step 3 (continued): Call the check_guess function to check if the guess is in the word
    check_guess(guess, secret_word)

# Secret word chosen by the computer
secret_word = random.choice(["apple", "banana", "cherry", "mango", "grape"])

# Call the ask_for_input function
ask_for_input()
