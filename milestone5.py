import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman class with word list and number of lives.
        
        Parameters:
            word_list (list): List of words to choose from.
            num_lives (int): Number of lives the player has. Default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _check_guess(self, guess):
        """
        Check if the guessed letter is in the secret word.
        
        Parameters:
            guess (str): The guessed letter.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            self._update_word_guessed(guess)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def _update_word_guessed(self, guess):
        """
        Update the word_guessed list with the correct guessed letter.
        
        Parameters:
            guess (str): The guessed letter.
        """
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess

    def ask_for_input(self):
        """
        Continuously ask the user for a letter and validate it.
        """
        while True:
            guess = input("Guess a letter: ")
            if not self._is_valid_guess(guess):
                continue
            self.list_of_guesses.append(guess)
            self._check_guess(guess)
            break

    def _is_valid_guess(self, guess):
        """
        Check if the guess is a single alphabetical character and not already guessed.
        
        Parameters:
            guess (str): The guessed letter.
        
        Returns:
            bool: True if valid guess, False otherwise.
        """
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
            return False
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
            return False
        return True

def play_game(word_list):
    """
    Function to run the Hangman game.
    
    Parameters:
        word_list (list): List of words to choose from.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            print(" ".join(game.word_guessed))
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "mango", "grape"]
    play_game(word_list)
