#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ----------------------
    This function calculates the factorial of a non-negative integer `n` recursively.
    The factorial of a number is the product of all positive integers less than or equal to `n`.
    Specifically, factorial(n) = n * (n-1) * (n-2) * ... * 1. By definition, factorial(0) is 1.

    Parameters:
    -----------
    n : int
        A non-negative integer for which the factorial needs to be calculated.
    
    Returns:
    --------
    int
        The factorial of the integer `n`. Returns 1 if `n` is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the argument passed from the command line, which is expected to be an integer
f = factorial(int(sys.argv[1]))

# Output the result of the factorial calculation
print(f)
