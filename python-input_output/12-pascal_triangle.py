#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        ligne = [1]
        ligne_prec = triangle[i - 1]
        for j in range(1, i):
            ligne.append(ligne_prec[j - 1] + ligne_prec[j])
        ligne.append(1)
        triangle.append(ligne)

    return triangle
