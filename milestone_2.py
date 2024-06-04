# Step 1: Import the random module
import random

# Step 2: Create a list containing the names of your 5 favorite fruits
favorite_fruits = ["apple", "banana", "cherry", "mango", "grape"]

# Step 3: Assign this list to a variable called word_list
word_list = favorite_fruits

# Step 4: Use random.choice to pick a random word from the list
word = random.choice(word_list)

# Step 5: Print out the randomly chosen word to the standard output
print(word)

# Step 6: Ask the user to enter a single letter
guess = input("Enter a single letter: ")

# Step 7: Create an if statement to check the validity of the input
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")