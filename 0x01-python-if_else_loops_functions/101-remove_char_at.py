#!/usr/bin/python3

def remove_char_at(str, n):
    answer =""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            answer = answer + str[i]
    return answer