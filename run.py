import random

MAX_ATTEMPTS = 6

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



def choose_random_word():
    word_list = ['apple', 'baker', 'crane', 'delta', 'eagle']
    word = random.choice(word_list).upper()

    return word

def display_grid():
    print("Guess The Word:\n")
    grid = [['_' for _ in range(5)] for _ in range(MAX_ATTEMPTS)]
    
    for row in grid:
        print(' '.join(row))
        print()

def get_player_input():
    player_guess = input("Enter your 5-letter word: ").strip().upper()
    print(player_guess)
    validate_input(player_guess)

def validate_input(guess):
    if len(guess) != 5:
        print(f"Your guess must be a 5-letter word. You provided a {len(guess)}-letter word")
    else:
        print("Valid input")

display_intro()
choose_random_word()
display_grid()
get_player_input()