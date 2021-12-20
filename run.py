"""
The game of Hangman:
Upon start, computer chooses a random word from a list of words.
Then user is asked to guess a letter that is inside the hidden word
or the whole word.
The user wins if the word is guessed
or loses if he/she runs out of allowed attempts before guessing the word.
"""
import random
from random_words import random_list


def secret_random_word():
    """
    Pick a random word from imported random_words list
    which later is passed to the 'game' function.
    """
    secret_word = random.choice(random_list)
    return secret_word.lower()


def game(secret_word, number_attempts):
    """
    Handle the main functionality of the game.
    Receive a secret_word from secret_random_word function,
    then ask the user for input and compare the input with the hidden word,
    then display information about the result and how to proceed accordingly.
    """
    game_score = False
    attempt_word = []
    attempt_letter = []
    word_display = len(secret_word) * "_"
    attempts = number_attempts
    print("Game begins!\n")
    print("  " + " ".join(word_display) + "\n")
    print(f"Attempts: {attempts}\n")
    while not game_score and attempts > 0:
        guess = input("Guess the word or \
a letter inside in the word \n").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in attempt_letter:
                print(f"You already tried '{guess}' before.\n")
            elif guess not in secret_word:
                attempt_letter.append(guess)
                attempts -= 1
                print(f"'{guess}' is not contained in the word.\n")
            else:
                attempt_letter.append(guess)
                word_display_list = list(word_display)
                indices = [i for i, letter in enumerate(secret_word)
                           if letter == guess]
                for index in indices:
                    word_display_list[index] = guess
                word_display = "".join(word_display_list)
                print(f"'{guess}' is contained in the word.\n")
                if "_" not in word_display:
                    game_score = True
        elif len(secret_word) == len(guess) and guess.isalpha():
            if guess in attempt_word:
                print(f"You already tried the word '{guess}' before.\n")
            elif guess != secret_word:
                attempt_word.append(guess)
                attempts -= 1
                print(f"'{guess}' is not the word you're looking for.\n")
            else:
                word_display = secret_word
                game_score = True
        else:
            print("It must be a letter or the whole word.")
        print("  " + " ".join(word_display) + "\n")
        print(f"Attempts: {attempts}\n")
    if game_score:
        print("You Won!")
        victory()
    else:
        print(f"You lost! It was '{secret_word}'.")
        defeat()
    restart(number_attempts)


def restart(number_attempts):
    """
    Display options to restart the game and react to users input accordingly
    """
    option_restart = input("Do you want to restart the game? y/n\n")
    if option_restart == "y":
        secret_word = secret_random_word()
        game(secret_word, number_attempts)
    elif option_restart == "n":
        main()
    else:
        print("Type either 'y' or 'n'")
        restart(number_attempts)


def main():
    """
    Initiate the game
    """
    game_intro()
    level = main_menu()
    if level == "level_chosen":
        number_attempts = 6
    else:
        number_attempts = menu_difficulty()

    secret_word = secret_random_word()
    game(secret_word, number_attempts)


def main_menu():
    """
    Main menu of the game
    """
    print("Press:\n")
    print("1 - To play")
    print("2 - For instructions")
    print("3 - To choose difficulty")
    select = False
    while not select:
        option = input(" \n")
        if option == "1":
            select = True
            level = "level_chosen"
            return level
        elif option == "2":
            select = True
            instructions()
        elif option == "3":
            select = True
        else:
            print("Incorrect input. Choose one of the above options.")


def instructions():
    """
    Display instructions for the game to the user
    """
    print(
        """
        Find the hidden word by either
        guessing a letter contained in the hidden word or
        the whole word at once.
        Each failed attempt will subtract one chance of guessing
        from the number of chances
        given to you at the start of the game.
        If you run out of chances, the game will be over and
        the hangman will hang you.
        """
    )


def menu_difficulty():
    """
    Display options to choose difficulty to the user and react to user's input
    """
    print("Choose game difficulty:\n")
    print("1 - For Beginner")
    print("2 - For Player")
    print("3 - For Veteran")
    choice = False
    while not choice:
        difficulty = input(" \n")
        if difficulty == "1":
            choice = True
            number_attempts = 9
            return number_attempts
        elif difficulty == "2":
            choice = True
            number_attempts = 6
            return number_attempts
        elif difficulty == "3":
            choice = True
            number_attempts = 3
            return number_attempts
        else:
            print("Choose between 1, 2 and 3 to select difficulty.")


def game_intro():
    """
    Display the game title in the main menu
    """
    print(
        """
      _____  _           _  _
     |_   _|| |_   ___  | || | __ _  _ _   __ _  _ __   __ _  _ _
       | |  | ' \ / -_) | __ |/ _` || ' \ / _` || '  \ / _` || ' \\
       |_|  |_||_|\___| |_||_|\__,_||_||_|\__, ||_|_|_|\__,_||_||_|
                                          |___/
        """
    )


def victory():
    """
    Display the 'Victory' graphic upon players win
    """
    print(
        """
     __   __ _      _
     \ \ / /(_) __ | |_  ___  _ _  _  _
      \ V / | |/ _||  _|/ _ \| '_|| || |
       \_/  |_|\__| \__|\___/|_|   \_, |
                                   |__/
        """
    )


def defeat():
    """
    Display the 'Defeat' graphic upon players loss
    """
    print(
        """
      ___         __             _
     |   \  ___  / _| ___  __ _ | |_
     | |) |/ -_)|  _|/ -_)/ _` ||  _|
     |___/ \___||_|  \___|\__,_| \__|
        """
    )


def progress():
    """
    Display the graphic which represents the progress of game
    based on diminishing number of attempts left to the user
    """
    progress_count = [
        """
           +========++
           |      \ ||
           |       \||
           O        ||
          /|\       ||
           |        ||
          / \       ||
                    ||
                    ||
         =============
        """,
        """
           +========++
           |      \ ||
           |       \||
           O        ||
          /|\       ||
           |        ||
          /         ||
                    ||
                    ||
         =============
        """,
        """
           +========++
           |      \ ||
           |       \||
           O        ||
          /|\       ||
           |        ||
                    ||
                    ||
                    ||
         =============
        """,
        """
           +========++
           |      \ ||
           |       \||
           O        ||
          /|        ||
           |        ||
                    ||
                    ||
                    ||
         =============
        """,
        """
           +========++
           |      \ ||
           |       \||
           O        ||
           |        ||
           |        ||
                    ||
                    ||
                    ||
         =============
        """,
        """
           +========++
           |      \ ||
           |       \||
           O        ||
                    ||
                    ||
                    ||
                    ||
                    ||
         =============
        """,
        """
           +========++
                  \ ||
                   \||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
         =============
        """,
        """
                      
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||
         =============
        """,
        """
                      
                     
                     
                     
                     
                     
                     
                     
                     
         =============
        """
    ]


main()
