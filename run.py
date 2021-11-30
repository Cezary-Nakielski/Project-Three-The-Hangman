import random
from random_words import random_list

def secret_random_word():
    secret_word = random.choice(random_list)
    return secret_word

secret_random_word()