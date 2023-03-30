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


MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NB_LIVES = 4
win = False
for i in range(0, NB_LIVES):
    lives = NB_LIVES - 1
    print(f"You have {lives} lives.")
    nb = ask_number(MIN_NUMBER, MAX_NUMBER)
    if nb == MAGIC_NUMBER:
        print("You won!")
        win = True
        break
    elif nb > MAGIC_NUMBER:
        print("The magic number is lower")
    else:
        print("The magic number is greater")

if not win:
    print(f"You lost! The magic number was: {MAGIC_NUMBER}")
