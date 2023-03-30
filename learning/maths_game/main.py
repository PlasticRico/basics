import random

MIN_NUMBER = 1
MAX_NUMBER = 10
NB_QUESTIONS = 4
LEVEL = 1  # dificulty


def ask_question():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    o = random.randint(0, LEVEL)
    operator_str = "+"
    if o == 1:
        operator_str = "-"
    elif o == 2:
        operator_str = "*"
    number_str = input(f"Compute {a} {operator_str} {b} = ")
    number_int = int(number_str)
    compute = a+b
    if o == 1:
        compute = a-b
    elif o == 2:
        compute = a*b
    if number_int == compute:
        # print("Correnct")
        return True     # needs to return True for the points
    # print("Wrong")
    return False


# for i in range(0, NB_QUESTIONS):
#     question = i + 1
#     print(f"Question n°{question} out of {NB_QUESTIONS}")
#     ask_question()
#     print()
def game():
    nb_points = 0
    for i in range(0, NB_QUESTIONS):
        print(f"Question {i+1} out of {NB_QUESTIONS}")
        if ask_question():
            print("Correnct")   # in ask_question() the sum is tru it will add 1 point
            nb_points += 1
        else:
            print("Wrong")
        print()
    print(f"Your points : {nb_points} out of {NB_QUESTIONS}")
    # 4/4 --> Excellent
    # adverage = int(NB_QUESTIONS/2)    5/2 = 2.5 -> 2
    # > adverage -> Good
    # < adverage -> You can do better
    adverage = int(NB_QUESTIONS / 2)
    if nb_points == NB_QUESTIONS:
        print("Excellent!")
    elif nb_points == 0:
        print("Improve your maths!")
    elif nb_points >= adverage:
        print("Good!")
    else:
        print("You can do better")


game()
