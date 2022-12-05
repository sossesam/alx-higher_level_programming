#!/usr/bin/python3

def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]
    tuple_sentence = (x, y)
    if x <= 0:
        return None
    else:
        return tuple_sentence
