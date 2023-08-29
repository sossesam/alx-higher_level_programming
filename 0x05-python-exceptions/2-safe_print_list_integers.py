#!/usr/bin/python3
def is_int(x):

    try:
        if x + 1:
            return x
    except Exception:
        return


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    check = 0
    for y in my_list:
        try:
            if y + 1:
                i += 1
        except Exception:
            i

    y = 0
    for z in range(x):
        try:
            if is_int(my_list[z]):
                print("{:d}".format(my_list[z]), end="")
                y += 1
            check += 1

        except (ValueError):
            return ""

    print("", end="\n")
    return y
