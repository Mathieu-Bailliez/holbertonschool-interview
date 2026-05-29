#!/usr/bin python3
"""
Module minimum operations
"""


def min_operations(n):
    """
    calculate the minimum number of operations
    needed to obtain exactly n H characters
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n != 1:
        if n % divisor == 0:
            n = n / divisor
            operations = operations + divisor
            n //= divisor
        else:
            divisor += 1

    return operations



