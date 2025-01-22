def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers in a matrix.
    
    Args:
        matrix (list of lists): 2D array of integers.
        
    Returns:
        list of lists: New matrix with squared values, same size as input matrix.
    """
    # Utiliser une compréhension de liste pour créer une nouvelle matrice avec les carrés des valeurs
    return [[element ** 2 for element in row] for row in matrix]
