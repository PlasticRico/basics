import random


def ask_number(nb_min, nb_max):
    nb_int = 0
    while nb_int == 0:
        nb_str = input(f"What is the magic number(between {min(nb_min, nb_max)} and {max(nb_min, nb_max)})? ")
        try:
            nb_int = int(nb_str)
        except:
            print("Error: You have to enter a number. Please retry")
        else:
            if nb_int < nb_min or nb_int > nb_max:
                print(f"Error: You must enter a number between {nb_min} and {nb_max}. Please retry")
                nb_int = 0
    return nb_int


def display_info(magic_nb, user_nb):
    if user_nb == magic_nb:
        print("You won!")
    elif user_nb < magic_nb:
        print("The magic number is greater")
    else:
        print("The magic number is lower")


MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NB_LIVES = 4
nb = 0
lives = NB_LIVES
while not nb == MAGIC_NUMBER and lives > 0:
    print(f"You have {lives} lives.")
    nb = ask_number(MIN_NUMBER, MAX_NUMBER)
    if nb == MAGIC_NUMBER:
        print("You won!")
    elif nb > MAGIC_NUMBER:
        print("The magic number is lower")
        lives -= 1
    else:
        print("The magic number is greater")
        lives -= 1
if lives == 0:
    print(f"You lost! The magic number was: {MAGIC_NUMBER}")
