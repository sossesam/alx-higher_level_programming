#!/usr/bin/python3
"""pass"""


def pascal_triangle(n):
    """pass"""

    mainlist = []

    if n <= 0:
        return mainlist

    array_position = 1

    while array_position <= n:
        newlist = []
        newlist.append(1)

        if array_position >= 2:
            prev =mainlist[-1]
            for y in range(2, array_position):
                if y <= array_position and array_position > 1:
                    prev =mainlist[-1]
            for num in range(len(prev) - 1):
                sum = prev[num] + prev[num + 1]
                newlist.append(sum)


            newlist.append(1)



        mainlist.append(newlist)

        array_position += 1


    return mainlist
