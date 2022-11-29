#!/usr/bin/python3


def uppercase(str):
    result = ' '
    for i in str:
        letter = ord(i)
        if  letter <= 96 and letter <= 122:
            result = result + chr(letter)
        else:
            result = result + chr((letter - 32))
    print("{}".format(result), end="\n")