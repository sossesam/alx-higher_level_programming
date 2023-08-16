#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square = lambda x: x * x
    newMatrix = []
    for firstMatrix in matrix:
        newValue = map(square, firstMatrix)
        newMatrix.append(list(newValue))
    return newMatrix
