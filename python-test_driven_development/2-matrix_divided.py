#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and returns a new matrix with the result.

    Parameters:
    matrix (list of lists of int/float): A matrix (a list of lists) containing integers or floats.
    div (int/float): The number by which each element of the matrix will be divided. Must be a number (integer or float) and cannot be zero.

    Returns:
    list of lists of float: A new matrix with each element divided by the divisor, rounded to 2 decimal places.

    Raises:
    TypeError: If `matrix` is not a list of lists or if `div` is not a number (integer or float).
    TypeError: If each row in the matrix does not have the same size.
    ZeroDivisionError: If `div` is zero.

    Example:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix_divided([[5, 10], [15, 20]], 5)
    [[1.0, 2.0], [3.0, 4.0]]

    >>> matrix_divided([[1, 2], [3, 4]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

    >>> matrix_divided([[1, 2], [3, 4]], "string")
    Traceback (most recent call last):
        ...
    TypeError: div must be a number
    """
    # Validate matrix: check if it's a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Validate rows: check if each row has the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Validate divisor: it should be a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Validate divisor: check if divisor is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create the new matrix with elements divided by div
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(element / div, 2) for element in row])
    
    return new_matrix
