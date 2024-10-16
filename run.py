import random
import nltk
from nltk.corpus import words
import colorama
from colorama import Fore, Back, Style

nltk.download('words')
dictionary = set(words.words())

colorama.init(autoreset=True)

word_list = ['apple', 'baker', 'crane', 'delta', 'eagle'] # Small list for testing purposes

class Game:
    """
    Game class that handles target word choice, user input, validations, checks and feedback
    """
    MAX_ATTEMPTS = 6 # This number will not change so it makes sense that is a constant

    def __init__(self):
        self.target_word = random.choice(word_list)
        self.grid = [['_' for _ in range(5)] for _ in range(self.MAX_ATTEMPTS)]
        self.attempt = 0
        self.guess_list = []
    
    def display_grid(self):
        """
        Function to display a 5x6 grid in the terminal
        Code inspired from suggestions on StackOverflow:
        https://stackoverflow.com/questions/77174842/how-to-print-a-grid-with-multiple-columns-in-the-terminal-using-for-loops
        """
        print("Guess The Word:\n")
        # for row_index, row in enumerate(self.grid):
        #     for col_index, letter in enumerate(row):
        #         colour = colour_list[col_index]
        #         print(f"{colour}{letter}{Style.RESET_ALL}")

        for row in self.grid:
            print(' '.join(row))
    
    def get_player_input(self):
        """
        Asks the player to enter a word/guess and runs validations on it
        """
        print(self.target_word)
        player_guess = input("Enter a 5-letter word: ").strip().upper()
        self.validate_input(player_guess)

    def validate_input(self, guess):
        """
        Validates player's input and returns feedback accordingly
        """
        if len(guess) != 5:
            print(f"Your word must be a 5-letter word. You provided a {len(guess)}-letter word. Please try again")
            self.get_player_input()
        elif guess.isalpha() == False:
            print("Your word must contain only letters. Please try again.")
            self.get_player_input()
        elif guess.lower() not in dictionary:
            print(f"{guess} is not an English word. Please try again.")
            self.get_player_input()
        elif guess in self.guess_list:
            print(f"You already tried the word {guess}. Please choose another word")
            self.get_player_input()
        else:
            print("Valid word!")
            self.guess_list.append(guess)
            self.update_game_state(guess)
    
    def colour_and_print_word(self, guess):
        """
        This function handles the colours that get assigned to each letter
        and prints the word to the terminal afterwards
        """
        coloured_word = ""

        for index, letter in enumerate(guess):
            if letter.lower() == self.target_word[index]:
                # print(f"letter{letter} in index {index} green")
                coloured_word += f"{Back.GREEN}{letter}{Style.RESET_ALL} " 
            elif letter.lower() in self.target_word:
                # print(f"letter{letter} in index {index} yellow")
                coloured_word += f"{Back.YELLOW}{letter}{Style.RESET_ALL} "
            else:
                # print(f"letter{letter} in index {index} grey")
                coloured_word += f"{Back.LIGHTBLACK_EX}{letter}{Style.RESET_ALL} "

        print(coloured_word)

        
    def update_game_state(self, guess):
        """
        In this function we handle the colouring of the word, check the word
        and give feedback to the user
        """
        self.colour_and_print_word(guess)

        self.attempt +=1

        self.check_guess(guess)

        if self.attempt < self.MAX_ATTEMPTS:
            self.get_player_input()
        else:
            print(f"Sorry, the word was {self.target_word.upper()}.")

    def check_guess(self, guess):
        if guess.lower() == self.target_word:
            print("Congratulations! Your guess is right!")
        else:
            if self.attempt < self.MAX_ATTEMPTS:
                self.get_player_input()
            else:
                print(f"Sorry, the word was {self.target_word.upper()}.")


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


display_intro()
game = Game()
game.get_player_input()

