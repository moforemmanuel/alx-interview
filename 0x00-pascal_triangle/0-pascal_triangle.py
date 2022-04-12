#!/usr/bin/python3

"""
Program that generates pascal triangle based on user input number of rows
"""

# pylint: disable=invalid-name


def pascal_triangle(number_of_rows):
    """
    function that returns pascal's triangle in 2D
    """
    triangle = []
    if number_of_rows <= 0:
        pass
    elif number_of_rows == 1:
        triangle.append([1])
    elif number_of_rows == 2:
        triangle.append([1])
        triangle.append([1, 1])
    else:
        triangle.append([1])
        triangle.append([1, 1])
        for i in range(2, number_of_rows):
            sub = []
            sub.append(1)
            for j in range(0, i-1):
                sub.append(triangle[i-1][j] + triangle[i-1][j+1])
            sub.append(1)
            triangle.append(sub)

    return triangle
