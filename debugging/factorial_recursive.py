#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Computes the factorial of a given number using a recursive approach.

    Parameters:
        n (int): A non-negative integer value for which the factorial will be calculated.

    Returns:
        int: The factorial of the input number n.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Read argument from command line and compute factorial
f = factorial(int(sys.argv[1]))
print(f)
