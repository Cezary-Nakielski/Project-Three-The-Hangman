import random
from random_words import random_list


def secret_random_word():
    secret_word = random.choice(random_list)
    return secret_word


def game(secret_word):
    game_score = False
    attempt_word = []
    attempt_letter = []
    attempts = 6
    word_display = list(len(secret_random_word)*"_")
    guess = input("Guess the word:")
    if guess == secret_word:
        print("You Won!")
    else:
        print("You Lost!")


def main():
    secret_word = secret_random_word()
    game(secret_word)


main()