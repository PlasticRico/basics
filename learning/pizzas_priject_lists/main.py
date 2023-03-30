# --------------first option-----------
# def display(collection):
#     nb_pizzas = len(collection)
#     print(f"--------------PIZZAS ({nb_pizzas})--------------")
#
#     if nb_pizzas == 0:
#         print("NO PIZZAS")
#     else:
#         for i in collection:
#             print(i)
#         print()
#         print(f"first pizza : {collection[0]}")
#         print(f"last pizza : {collection[-1]}")

# --------------second option-----------
def add_user_pizza(collection):
    add_pizza = input("Add your pizza :")
    # if pizza_exists(add_pizza, collection):  # checking if pizza is in the list with funcion pizza_exists
    if add_pizza.lower() in collection:  # better way how to check if the pizza is in the list
        print(f"EROOR : {add_pizza} pizza already exists")
    else:
        collection.append(add_pizza)


# -----------check if pizaa is in the list------------
# def pizza_exists(pizza, collection):
#     for i in collection:
#         if pizza == i:
#             return True
#     return False


# def custom_sort(e):
#     return len(e)  # return e = abc

def display(collection, nb_pizza=-1):
    # collection.sort(key=custom_sort)  # collection.sort() abc  reverse collection.sort(revarse=True) cba
    # showing x nr of pizzas
    c = collection
    if not nb_pizza == -1:
        c = collection[:nb_pizza]
    nb_pizzas = len(c)
    print(f"--------------PIZZAS ({nb_pizzas})--------------")

    if nb_pizzas == 0:
        print("NO PIZZAS")
        return

    for i in c[:nb_pizza]:
        print(i)
    print()
    print(f"first pizza : {c[0]}")
    print(f"last pizza : {c[-1]}")


pizzas = ["4 cheeses", "vegetarian", "havai", "calzone", "four seasons"]
empty = ()
add_user_pizza(pizzas)
display(pizzas)
