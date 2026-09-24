#!/usr/bin/env python3
"""Calculate the minimum operation"""


def minOperations(n):
    """Calculate and return the total operation for n number"""

    total_operations = 0
    divisor = 2

    while divisor <= n:
        while n % divisor == 0:
            total_operations += divisor
            n //= divisor
        divisor += 1

    return total_operations
