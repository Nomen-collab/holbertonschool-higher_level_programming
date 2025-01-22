def square_matrix_simple(matrix=[]):
	"""
	Compute the square of all integers in a matrix.

	Args:
		matrix (list of lists): A 2D list of integers.

	Returns:
		list of lists: A new matrix with each integer squared.
	"""
	return [[value ** 2 for value in row] for row in matrix]
