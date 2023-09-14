#!/usr/bin/python3
""" Doc """


def matrix_divided(matrix, div):
    """ Doc """

    new_matrix = []

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for dlist in range(len(matrix)):
        if len(matrix[dlist]) != len(matrix[dlist - 1]):
            raise TypeError("Each row of the matrix must have the same size")


    for matrice in matrix :
        if type(matrice) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_list=[]
        for x in matrice:
            if type(x)==int or type(x)==float:
                divided_number = round((x/div), 2)
                new_list.append(divided_number)
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        new_matrix.append(new_list)

    return new_matrix


