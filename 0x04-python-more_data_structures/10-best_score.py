#!/usr/bin/python3

def best_score(a_dictionary):
    best_student = ""
    highest_score = 0
    if a_dictionary:
        for k in a_dictionary.keys():
            if a_dictionary[k] >= highest_score:
                best_student = k
                highest_score = a_dictionary[k]
        return best_student
    else:
        return None
