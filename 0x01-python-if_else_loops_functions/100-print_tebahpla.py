#!/usr/bin/python3

answer = ""
letter = 122
for i in range(1, 27):
    if i % 2 == 0:
        answer = answer + chr(letter - 32)
    else:
        answer = answer + chr(letter)
    letter = letter - 1
print("{}".format(answer), end="")
