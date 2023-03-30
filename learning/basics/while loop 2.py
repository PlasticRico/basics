name = ""
while name == "":
    name = input("What is you name? ")

age = 0
while age == 0:
    age_str = input("What is your age ")
    try:
        age = int(age_str)
    except:
        print("ERROR: age must be number")


print()
print("Your name is " + name + " and you are " + str(age) + " years old.")
print("Soon you will be " + str(age+1))
print()
print("Your name is {} and you are {} years old.".format(name, str(age)))
print("Soon you will be {}".format(age+1))


