# collections : Arrays, Lists, Tuples...
# Tuples : immutalbe : you cannot change it
# List : mutable : You can add/delete items or modify them
# multiple items


# -----------------------TUPLES-----------------------------

# persons = ("Brian", "Bob", "Alice", "Jean")  # Tuple []->list
# print(len(persons))
# print(persons[-1])  # the last element

# for i in range(0, len(persons)):
#     print(persons[i])

# for i in persons:
#     print(i)
#     print(len(i))
#     print(i[0]) # print first letter
#     print(i[-1])  # print last letter
#     print()

# values = range(0, 5)  # the range(0, 5) works as Tuple -> (0, 1, 2, 3, 4)
# print(values[-1])


# --------------------LISTS---------------------

# persons = ["Brian", "Bob", "Alice", "Jean"]
# new_person = "David"

# print(persons)
# persons.append(new_person)
# persons[0] = "Steven"
# del persons[1]  # deleting Bob
# print(persons)

# for i in persons:
#     print(i)

# ------------------------------------------
# def change_value(a):
#     a = 10
#     print(a)
#
# test = 5
# change_value(test)  # prited 10
# print(test)  # printed 5
# ------------------------------------------
# def change_value(a):
#     a[0] = 10
#     print(a)
#
# test = [1, 2, 3, 4]
# print(test)
# change_value(test)  # prited 10
# print(test)  # printed 5


# --------------------TUPLES AND FUNCTIONS---------------------
#
#
# def get_informations():
#     return "Alice", 20, 1.6
#
#
# def display_information(name, age, height):
#     print(f"Name: {name}, Age: {age}, Height: {height}")
#
#
# infos = get_informations()
# print(infos)
# display_information(*infos)  # unpack tuple -> infos[0], infos[1], infos[2]
# print(infos)
#
# print("Name: " + infos[0])
# print("Age: " + str(infos[1]))
# print("height: " + str(infos[2]))


# name, age, height = get_informations()
# display_information(name, age, height)


# --------------------SLICES---------------------
persons = ["Brian", "Bob", "Alice", "Jean", "Steav", "John"]

# print(persons)
# [start:stop:step]
for i in persons[0:2]:
    print(i)

name = "Alice"
print(name[::-1])
