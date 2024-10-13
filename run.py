def display_intro():
    """
    Diplays the welcome message and instructions for the game    
    """
    print("Welcome to Guess The Word!\n")
    print("You have 6 attempts to guess a 5-character-long word\n")
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

