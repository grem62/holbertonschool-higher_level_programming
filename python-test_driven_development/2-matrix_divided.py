#!/usr/bin/python3


def matrix_divided(matrix, div):
    size_error = "Each row of the matrix must have the same size"
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    div_error = "div must be a number"
    if not matrix:
        raise TypeError(matrix_error)
    if not isinstance(matrix, list):
        raise TypeError(matrix_error)
    for list1 in matrix:
        if not isinstance(list1, list):
            raise TypeError(matrix_error)
        for index in list1:
            if not isinstance(index, (float, int)):
                raise TypeError(matrix_error)
    for list1 in matrix:
        if len(list1) == 0:
            raise TypeError(matrix_error)
    if not div:
        raise TypeError(div_error)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(list1) == len(matrix[0]) for list1 in matrix):
        raise TypeError(size_error)
    return [[round(item / div, 2) for item in list1] for list1 in matrix]
