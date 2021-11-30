import random
from random_words import random_list


def secret_random_word():
    secret_word = random.choice(random_list)
    return secret_word


def game(secret_word):
    guess = input("Guess the word:")
    if guess == secret_word:
        print("You Won!")
    else:
        print("You Lost!")