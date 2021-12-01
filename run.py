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
    word_display = len(secret_word) * "_"
    while not game_score:
        guess = input("Guess the word or a letter contained in the word:")
        if guess in attempt_letter:
            print(f"You already tried {guess} before.")
        elif guess not in secret_word:
            attempt_letter.append(guess)
            attempts -= 1
            print(f"{guess} is not contained in the word.")
        elif:
            attempt_letter.append(guess)
            word_display_list = list(word_display)
            indices = [i for i, letter in enumerate(secret_word)
                       if letter == guess]
            for index in indices:
                word_display_list[index] = guess
            word_display = "".join(word_display_list)
            print(f"{guess} is contained in the word.")
        elif len(secret_word) = len(guess):
            if guess in attempt_word:
                print(f"You already tried {guess} before.")
            else:
                attempt_word.append(guess)
                attempts -= 1
                print(f"{guess} is not the word you're looking for.")

    # if guess == secret_word:
    #     print("You Won!")
    # else:
    #     print("You Lost!")
    # if guess is not secret_word:
    #     attempt_letter.append(guess)
    #     attempts -= 1


def main():
    secret_word = secret_random_word()
    game(secret_word)


main()