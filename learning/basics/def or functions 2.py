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


# ask for the name
name1 = ask_for_the_name()
name2 = ask_for_the_name()
# aks for the age
age1 = ask_for_the_age(name1)
age2 = ask_for_the_age(name2)

print()
print("Your name is " + name1 + " and you are " + str(age1) + " years old.")
print("Soon you will be " + str(age1 + 1))
print()
print("Your name is " + name2 + " and you are " + str(age2) + " years old.")
print("Soon you will be " + str(age2 + 1))
print()
print("Your name is {} and you are {} years old.".format(name1, str(age1)))
print("Soon you will be {}".format(age1 + 1))
print()
print("Your name is {} and you are {} years old.".format(name2, str(age2)))
print("Soon you will be {}".format(age2 + 1))
print()
print(f"{name1}, you are {age1} years old, and {name2}, you are {age2} years old.")
print(f"In {max(age1, age2) - min(age1, age2)} years, {min(name1, name2)} will be as old as {max(name1, name2)} is now.")
