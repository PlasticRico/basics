import time


def clock():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print("\rCurrent time: {}".format(current_time), end="")
        time.sleep(1)


