#!/usr/bin/python3
"""Module that generates Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): number of rows to generate.

    Returns:
        list: list of rows, or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_index in range(1, n):
        row = [1]

        for column in range(1, row_index):
            row.append(triangle[-1][column - 1] + triangle[-1][column])

        row.append(1)
        triangle.append(row)

    return triangle
