import random

def get_valid_user_input(prompt):
    """
    Prompt the user for input and validate it.
    Only accept single alphabetical characters.
    """
    while True:
        user_input = input(prompt)
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("Oops! Please enter a single alphabetical character.")

def play_hangman():
    favorite_fruits = ["apple", "banana", "cherry", "mango", "grape"]
    chosen_word = random.choice(favorite_fruits)

    print("Welcome to Hangman!")

    while True:
        user_guess = get_valid_user_input("Enter a single letter: ")
        print(f"You guessed: {user_guess}")

        # Add game logic here

if __name__ == "__main__":
    play_hangman()
