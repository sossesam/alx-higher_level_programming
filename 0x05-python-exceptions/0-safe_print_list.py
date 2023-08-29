#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    z = 0
    for y in my_list:
        i += 1
    while z < i and z < x:
        try:
            print(my_list[z], end="")
            z += 1
        except Exception:
            ""
            return z
    print("", end="\n")
    return z
