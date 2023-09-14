#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_matrix = []

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    i = 0
    for matrice in matrix :
        if len(matrice) == len(matrix[i]) is False:
            raise TypeError("Each row of the matrix must have the same size")
        if type(matrice) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_list=[]
        for x in matrice:
            if type(x)==int or type(x)==float:
                divided_number = round((x/div), 2)
                new_list.append(divided_number)
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        i+=1
        new_matrix.append(new_list)

    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
