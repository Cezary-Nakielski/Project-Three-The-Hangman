import random
from random_words import random_list


def secret_random_word():
    secret_word = random.choice(random_list)
    return secret_word


def pass_word():
    secret_word = secret_random_word()
    game(secret_word)


pass_word()


game_score = False


def game(secret_word):
    while game_score:
        guess = input("Guess the word:")

    if guess == secret_word:
        not game_score

    if game_score:
        print("Win")
    else:
        print("Defeat")
