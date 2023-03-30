"""
First program
zzzz
Python corse
"""


def display_person_info(name, age, height=0):
    print()
    print("Your name is  " + name + ", you are " + str(age) + " years old.")
    # print(f"Your name is {name}, you are {age} years old.")
    # print(f"Your name is %s, you are %s years old." % (name, age))
    print("Soon you will be  " + str(age + 1))
    if age < 10:
        print("You are a Kid")
    elif age == 17:
        print("You are almost an adult")
    elif 10 <= age < 18:
        print("You are a teenager")
    elif age == 1 or age == 2:
        print("You are a baby")
    elif age == 18:
        print("You are now an adult : congrats!")
    elif age > 60:
        print("You are senior")
    elif age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

    if not height == 0:
        print("Your height: " + str(height) + "m")


def ask_for_the_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("What is your name? ")
    return name_answer


def ask_for_the_age(person_name):
    age_int = 0
    while age_int == 0:
        age_str = input(person_name + " what is your age? ")
        # name = "foo"
        # age = 30
        # convert str -> int
        try:
            age_int = int(age_str)
        except:
            print("ERROR: Age must be a nummber")
    return age_int


# ask for a name
# name1 = ask_for_the_name()
# name2 = ask_for_the_name()
# ask for the age
# age1 = ask_for_the_age(name1)
# age2 = ask_for_the_age(name2)
# print(type(name))
# print(type(age))

# int : interger : 0, 1, 2, 3  -1, -2, ... but not 1.4
# str(30) -> "30"
# float : 1.4
# booleans : true/false
# display the results
# print("Your name is  " + name1 + ", you are " + str(age1) + " years old.")
# print("Soon you will be  " + str(age1 + 1))
# print()
# print("Your name is  " + name2 + ", you are " + str(age2) + " years old.")
# print("Soon you will be  " + str(age2 + 1))
# display_person_info(name1, age1)
# display_person_info(name2, age2)
# print("Have a nice day")
# print("ERROR: Age must be a nummber")

NB_PERSONS = 1

for i in range(0, NB_PERSONS):
    name = "martin" + str(i+1)
    age = ask_for_the_age(name)
    display_person_info(name, age)

print("""A first line
    I can write
        what
            I want
""")
# while loop

# n = 0  # create n
# print(n)
# n = 1   # assign new value
# print(n)
# n = n + 1   # incement
# print(n)


# while n < 5:
#     print("Value of n: " + str(n))
#     n = n + 1
# print("End of the loop")

# password = ""
# while not password == "1234":
#      password = input("What is your password? ")
#
# print("Password is correct")
