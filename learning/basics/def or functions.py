def ask_for_the_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("What is you name? ")
    return name_answer


def ask_for_the_age():
    age_int = 0
    while age_int == 0:
        age_str = input("What is your age ")
        try:
            age_int = int(age_str)
        except:
            print("ERROR: age must be number")
    return age_int


# ask for the name
name = ask_for_the_name()
# aks for the age
age = ask_for_the_age()

print()
print("Your name is " + name + " and you are " + str(age) + " years old.")
print("Soon you will be " + str(age + 1))
print()
print("Your name is {} and you are {} years old.".format(name, str(age)))
print("Soon you will be {}".format(age + 1))
