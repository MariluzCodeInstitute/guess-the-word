import random
from word_list import word_list  # Import the list of words from word_list.py
import nltk
from nltk.corpus import words
import colorama
from colorama import Fore, Back, Style

nltk.download('words')
dictionary = set(words.words())  # Dictionary to verify English words

colorama.init(autoreset=True)

coloured_words_list = []


class Game:
    """
    Game class that handles target word choice, user input,
    validations, checks and feedback
    """
    MAX_ATTEMPTS = 6  # This number will not change

    def __init__(self):
        """
        Constructor function to initialise the variables that the game will use
        """
        self.target_word = random.choice(word_list)
        self.attempt = 0
        self.guess_list = []

    def get_player_input(self):
        """
        Asks the player to enter a word/guess and runs validations on it
        """
        player_guess = input("Enter a 5-letter word: ").strip().upper()
        self.validate_input(player_guess)

    def validate_input(self, guess):
        """
        Validates player's input and returns feedback accordingly
        """
        if len(guess) != 5:
            print(
                f"Your word must be a 5-letter word. "
                f"You provided a {len(guess)}-letter word. Please try again"
            )
            self.get_player_input()
        elif guess.isalpha() is False:
            print("Your word must contain only letters. Please try again.")
            self.get_player_input()
        elif guess.lower() not in dictionary:
            print(f"{guess} is not an English word. Please try again.")
            self.get_player_input()
        elif guess in self.guess_list:
            print(
                f"You already tried the word {guess}. "
                f"Please choose another word."
            )
            self.get_player_input()
        else:
            print("Valid word!")
            self.guess_list.append(guess)
            self.update_game_state(guess)

    def assign_colours(self, guess):
        """
        This function handles the colours that get assigned to each letter
        and prints the word to the terminal afterwards
        """
        coloured_word = ""

        for index, letter in enumerate(guess):
            if letter.lower() == self.target_word[index]:
                coloured_word += f"{Back.GREEN}{letter}{Style.RESET_ALL} "
            elif letter.lower() in self.target_word:
                coloured_word += f"{Back.YELLOW}{letter}{Style.RESET_ALL} "
            else:
                coloured_word += (
                    f"{Back.LIGHTBLACK_EX}{letter}{Style.RESET_ALL} "
                )
        return coloured_word

    def update_game_state(self, guess):
        """
        This function gets the word coloured and send the guess for checking
        """
        global coloured_words_list
        coloured_word = self.assign_colours(guess)
        coloured_words_list.append(coloured_word)

        for word in coloured_words_list:
            print(word)
            print()  # Printing extra line so that is easier to see

        self.attempt += 1
        self.check_guess(guess)

    def check_guess(self, guess):
        """
        Check if the guess is correct and gives feedback
        """
        if (
            self.attempt <= self.MAX_ATTEMPTS
            and guess.lower() == self.target_word
        ):
            print("Congratulations! Your guess is right!")
            self.restart_game()
        elif self.attempt < self.MAX_ATTEMPTS:
            self.get_player_input()
        else:
            print(f"Sorry, the word was {self.target_word.upper()}.")
            self.restart_game()

    def restart_game(self):
        """
        Asks the player if they want to play again and resets variables
        """
        global coloured_words_list
        coloured_words_list = []
        self.__init__()

        players_choice = input("Would you like to play again? Y/N \n").upper()

        if players_choice == "Y":
            self.get_player_input()
        elif players_choice == "N":
            print("Thanks for playing. Good bye!")
        else:
            print("Please enter either y/Y or n/N")
            self.restart_game()


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
        "If any of the letters are present in the word but not "
        "in the right position, they will be yellow"
    )
    print("If the letter is not in the word, it will be grey\n")
    print("Good luck!")


def main():
    """
    Main function to run the entire game
    """
    display_intro()
    game = Game()
    game.get_player_input()


main()
