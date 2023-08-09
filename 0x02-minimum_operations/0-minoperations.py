#!/usr/bin/python3
""" method to calculate fewest number of operations """


def minOperations(n):
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + 1
    return n


# Example usage:
n = 9
result = minOperations(n)
print(result)  # Output will be 6
