#!/usr/bin/python3
"""
Module minimum operations
"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    needed to obtain exactly n H characters.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n != 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
