import turtle


def stairs(size, nb):
    for i in range(0, nb):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
        # size = size - 10
        # size -= 10
    t.forward(size)


def square(size):
    for i in range(0, 4):
        t.forward(size)
        t.left(90)


def squares_2(starting_size, nb):
    for i in range(0, nb):
        square(starting_size)
        starting_size += 10


def squares(beginning_size, nb):
    for i in range(0, nb):
        # size = (i + 1) * (i + 1) * beginning_size
        size = (i + 1) * beginning_size
        square(size)
        # t.left(10)


t = turtle.Turtle()
# stairs(60, 5)
# square(100)
# squares_2(10, 10)
squares(10, 36)
turtle.done()

