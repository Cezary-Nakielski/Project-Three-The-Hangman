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
    return secret_word


def game(secret_word):
    """
    Handle the main functionality of the game.
    Receive a secret_word from secret_random_word function,
    then ask the user for input and compare the input with the hidden word,
    then display information about the result and how to proceed accordingly.
    """
    game_score = False
    attempt_word = []
    attempt_letter = []
    attempts = 6
    word_display = len(secret_word) * "_"
    while not game_score and attempts > 0:
        guess = input("Guess the word or a letter contained in the word:\n")
        if len(guess) == 1:
            if guess in attempt_letter:
                print(f"You already tried {guess} before.")
            elif guess not in secret_word:
                attempt_letter.append(guess)
                attempts -= 1
                print(f"{guess} is not contained in the word.")
            else:
                attempt_letter.append(guess)
                word_display_list = list(word_display)
                indices = [i for i, letter in enumerate(secret_word)
                           if letter == guess]
                for index in indices:
                    word_display_list[index] = guess
                word_display = "".join(word_display_list)
                print(f"{guess} is contained in the word.")
                if "_" not in word_display:
                    game_score = True
        elif len(secret_word) == len(guess):
            if guess in attempt_word:
                print(f"You already tried the word {guess} before.")
            elif guess != secret_word:
                attempt_word.append(guess)
                attempts -= 1
                print(f"{guess} is not the word you're looking for.")
            else:
                word_display = secret_word
                game_score = True
        else:
            print("It must be a letter or a whole word")
    if game_score:
        print("You Won!")
    else:
        print(f"You lost! It was {secret_word}.")
    restart()

def restart()
    """
    Display options to restart the game and react to users input accordingly
    """
    option_restart = input("Do you want to restart the game? y/n")
    if option_restart == "y":
        secret_word = secret_random_word()
        game(secret_word)
    elif option_restart == "n"::
        main()
    else:
        print("Type either 'y' or 'n'")
        restart()


def main():
    """
    Initiate the game
    """
    secret_word = secret_random_word()
    game(secret_word)

def main_menu():
    """
    Main menu of the game
    """
    print("1 to play")
    print("2 for instructions")
    print("3 to choose difficulty")
    select = False
    while not select:
        option = input(" \n")
        if option == "1":
            select = True
            secret_word = secret_random_word()
            game(secret_word)
        elif option == "2":
            select = True
            instructions()
        else:
            select = True
            menu_difficulty()

def instructions():
    """
    Display instructions for the game to the user
    """
    print(
        """
        Find the hidden word by either guessing a letter contained in the hidden word
        or the whole word at once.
        Each failed attempt will subtract one chance of guessing from the number of
        chances given to you at the start of the game. If you run out of chances,
        the game will be over and the hangman will hang you.
        """
    )


def menu_difficulty():
    """
    Display options to choose difficulty to the user and react to user's input
    """


main()
