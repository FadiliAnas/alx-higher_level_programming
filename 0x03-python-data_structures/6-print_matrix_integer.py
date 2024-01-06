#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Loop through each row in the matrix
    i = 0
    while i < len(matrix):
        # Initialize j for the inner loop
        j = 0
        while j < len(matrix[i]):
            # Print the element at the current position
            print("{:d}".format(matrix[i][j]), end=" ")
            j += 1
        print("$", end=" ")
        print()  # Move to the next line after printing each row
        i += 1
