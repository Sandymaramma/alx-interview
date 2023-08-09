#!/usr/bin/python3
""" method that calculates fewest number of operations """


def minOperations(n):
    if n == 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n


# Example usage:
n = 9
result = minOperations(n)
print(result)  # Output will be 6
