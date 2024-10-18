# Guess The Word

[Link to the live site](https://guess-the-word-game-b6916961b4a4.herokuapp.com/)

Guess the Word is a fun and challenging word-guessing game inspired by the popular Wordle game. Built using Python, this game provides an interactive way to test your vocabulary and problem-solving skills. The objective is simple: guess the hidden word within a limited number of attempts. With each guess, you'll receive hints that guide you closer to the solution, making every round an exciting puzzle to solve!

This project is designed to be both engaging and educational, perfect for word game enthusiasts or anyone looking to practice their language skills. Whether you're playing casually or aiming to improve your guessing strategy, Guess the Word offers endless entertainment. Dive in, sharpen your mind, and see if you can unravel the mystery word before your attempts run out!

![Responsive Mockup](assets/images/guess_the_word_responsive_mockup.png)

## Index - Table of Contents

- [Design](#design)

- [UX](#ux)
    - [Programm Goals](#programm-goals)

- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)

- [Data Model](#data-model)

- [Testing](#testing)
    - [Validator Testing](#validator-testing)

- [Debugging](#debugging)
    - [Fixed bugs](#fixed-bugs)
    - [Unfixed bugs](#unfixed-bugs)

- [Deployment](#deployment)

- [Credits](#credits)
    - [Data](#data)
    - [Code](#code)
    - [Styling](#styling)


## Design

Since this is a command line application, the design is simple yet effective. There is a colour code (replicating the one in the original Wordle game): green for a letter in the right index, yellow for a letter present in the word but incorrect index, and grey if the letter is not present in the word. 
The maximum number of attempts is 6, like in the original game, and only English words are accepted.

After the player gives their input, the app displays the word (letterss with relevant colours) and if necessary the game prompts the player to input another word. The player can see all their guessed words on a list, so that it is easier to keep track of their guesses.

