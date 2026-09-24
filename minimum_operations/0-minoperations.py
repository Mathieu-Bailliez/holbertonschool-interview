def minOperations(n):

    total_operations = 0
    divisor = 2

    while divisor <= n:
        while n % divisor == 0:
            total_operations += divisor
            n //= divisor
        divisor += 1

    return total_operations
