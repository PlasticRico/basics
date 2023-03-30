def ask_for_the_name():
    player = ""
    while player == "":
        player = input("What is your name? ")
    return player


def ask_if_wants_to_play(player):
    answer = ""
    # loops till you type in yes or no,
    # answer.lower()-> method is used to convert the user's input to lowercase to make the check case-insensitive.
    while answer.lower() not in ["yes", "no"]:
        print(player + " do you what to play a game")
        answer = input("Type yes or no: ")
    if answer == "yes":
        print("Lets go")
        return True
    else:
        print("Maybe next time")
        return False


def the_game():
    score = 0
    answer = ""
    while answer.lower() not in ["a", "b", "c", "d"]:
        answer = input("""What is the capital of France?
    a. Paris
    b. London
    c. Madrid
    d. Berlin
    """)
    if answer == "a":
        print("correct")
        score += 1  # adds +1 to score
    else:
        print("wrong")

    answer = ""
    while answer.lower() not in ["a", "b", "c", "d"]:
        answer = input("""Which of the following is not a programming language?
    a. Python
    b. Java
    c. HTML
    d. MySQL
    """)
        if answer == "c":
            print("correct")
            score += 1
        else:
            print("wrong")

    answer = ""
    while answer.lower() not in ["a", "b", "c", "d"]:
        answer = input("""Who played the character of Iron Man in the Marvel Cinematic Universe?
    a. Robert Downey Jr.
    b. Chris Evans
    c. Tom Hiddleston
    d. Mark Ruffalo
    """)
    if answer == "a":
        print("correct")
        score += 1
    else:
        print("wrong")
    print("Your score is " + str(score) + " out of 3.")


def game():
    name = ask_for_the_name()
    if ask_if_wants_to_play(name):
        the_game()


game()
