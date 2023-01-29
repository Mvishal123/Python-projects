import random
import string
from words import words


def valid_word(words):
    the_word = random.choice(words)
    while " " not in the_word and "-" not in the_word:
        return the_word.upper()
    the_word = random.choice(words)


def hangman():
    word = valid_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0:
        print("Words used: ", " ".join(used_letters))
        the_word = [letters if letters in used_letters else "-" for letters in word]
        print(" ".join(the_word))
        user_input = (input("enter a letter: ")).upper()
        if user_input in alphabets - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
        elif user_input in used_letters:
            print("You have already used this letter. Try again.")
        else:
            print("Invalid character")


hangman()
