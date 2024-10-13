import random
import nltk
from nltk.corpus import words

nltk.download('words')
dictionary = set(words.words())

MAX_ATTEMPTS = 6
grid = [['_' for _ in range(5)] for _ in range(MAX_ATTEMPTS)]
word_list = ['apple', 'baker', 'crane', 'delta', 'eagle']
guess_list = []

class Word:
    """
    Word class
    """
    def __init__(self, target_word):
        self.target_word = random.choice(word_list)

def display_grid():
    """
    Function to display a 5x6 grid in the terminal
    Code inspired from suggestions on StackOverflow:
    https://stackoverflow.com/questions/77174842/how-to-print-a-grid-with-multiple-columns-in-the-terminal-using-for-loops
    """
    print("Guess The Word:\n")

    for row in grid:
        print(' '.join(row))

def display_intro():
    """
    Diplays the welcome message and instructions for the game   
    """
    print("Welcome to Guess The Word!\n")
    print("You have 6 attempts to guess a 5-letter word\n")
    print(
        "On each attempt, if any of letters are in the right position, "
        "they will be green")
    print(
        "If any of the letters are present in the word but not in the right position, "
        "they will be yellow"
    )
    print("If the letter is not in the word, it will not be coloured\n")
    print("Good luck!")


def get_player_input():
    """
    Asks the player to enter a word/guess and runs validations on it
    """
    player_guess = input("Enter your 5-letter word: ").strip().upper()
    validate_input(player_guess)

def validate_input(guess):
    """
    Validates player's input and returns feedback accordingly
    """
    if len(guess) != 5:
        print(f"Your word must be a 5-letter word. You provided a {len(guess)}-letter word. Please try again")
        get_player_input()
    elif guess.isalpha() == False:
        print("Your word must contain only letters. Please try again.")
        get_player_input()
    elif guess.lower() not in dictionary:
        print(f"{guess} is not an English word. Please try again.")
        get_player_input()
    elif guess in guess_list:
        print(f"You already tried the word {guess}. Please choose another word")
        get_player_input()
    else:
        print("Valid word!")
        guess_list.append(guess)
        update_grid(guess)

def update_grid(guess):
    grid[0] = guess
    display_grid()


display_intro()
display_grid()
get_player_input()

