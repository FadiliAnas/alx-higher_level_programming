#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    if matrix == [[]]:
        print()
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            # Print the element at the current position followed by a space
            
            if j == len(matrix) - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
            j += 1
        i += 1
