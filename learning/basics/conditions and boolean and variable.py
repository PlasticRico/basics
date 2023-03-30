def ask_for_the_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("What is you name? ")
    return name_answer


def ask_for_the_age(persons_name):
    age_int = 0
    while age_int == 0:
        age_str = input(persons_name + " what is your age ")
        try:
            age_int = int(age_str)
        except:
            print("ERROR: age must be number")
    return age_int


def display_persons_info(name, age):
    print()
    print("Your name is " + name + " and you are " + str(age) + " years old.")
    print("Soon you will be " + str(age + 1))
    # == equality
    # > >=
    # < <=
    # bool : True/False
    # elif -> else + if
    # age > 60 : You are senior
    # age < 10 : You are a kid
    if age < 10:
        print("You are a kid")
    elif age == 17:
        print("You are almost an adult")
    elif 10 <= age < 18:
        print("You are teenager")
    elif age == 1 or age ==2:
        print("you are a baby")
    elif age == 18:
        print("You are an adult : Congrats")
    elif age > 60:
        print("You are senior")
    elif age > 18:
        print("You are an adult")
    else:
        print("You are an minor")


def display_person_info_2(name, age):
    print()
    print("Your name is {} and you are {} years old.".format(name, str(age)))
    print("Soon you will be {}".format(age + 1))


def display_persons_info_3():
    print()
    print(f"{name1}, you are {age1} years old, and {name2}, you are {age2} years old.")
    print(f"In {max(age1, age2) - min(age1, age2)} years, {min(name1, name2)} will be as old as {max(name1, name2)} is now.")


# ask for the name
name1 = ask_for_the_name()
name2 = ask_for_the_name()
# aks for the age
age1 = ask_for_the_age(name1)
age2 = ask_for_the_age(name2)

display_persons_info(name1, age1)
display_persons_info(name2, age2)

display_person_info_2(name1, age1)
display_person_info_2(name2, age2)

display_persons_info_3()
