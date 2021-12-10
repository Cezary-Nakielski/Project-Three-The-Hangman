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
    while not game_score:
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
                print("You Won!")
        else:
            print("It must be a letter or a whole word")


def main():
    """
    Initiate the game
    """
    secret_word = secret_random_word()
    game(secret_word)


main()
