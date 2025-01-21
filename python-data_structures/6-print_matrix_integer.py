#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    lenght = len(matrix)
    for x in range(lenght):
        for y in range(len(matrix[x])):
            print('{:d}'.format(matrix[x][y]), end='')
            if y is not (len(matrix[x]) - 1):
                print(end=" ")
        print("")
