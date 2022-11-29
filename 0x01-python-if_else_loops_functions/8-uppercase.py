#!/usr/bin/python3


def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) <= 96 and ord(str[i]) <= 122:
            if i <= len(str):
                x=""
            else:
                x="\n"
            print("{}".format(chr((ord(str[i])))), end=x)
        else:
            if i != len(str):
                x=""
            else:
                x="\n"
            print("{}".format(chr((ord(str[i])) - 32)),end="")

    print("")
    