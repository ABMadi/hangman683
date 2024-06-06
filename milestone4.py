# milestone_4.py

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the attributes of the Hangman class.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the secret word.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Continuously ask the user for a letter and validate it.
        """
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

# Test the Hangman class
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "mango", "grape"]
    game = Hangman(word_list)
    
    while game.num_lives > 0 and game.num_letters > 0:
        print(" ".join(game.word_guessed))
        game.ask_for_input()

    if game.num_lives == 0:
        print(f"You ran out of lives. The word was '{game.word}'.")
    else:
        print(f"Congratulations! You guessed the word '{game.word}'!")
