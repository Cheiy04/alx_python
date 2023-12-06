def square_matrix_simple(matrix=[]):
    result = []  # Initialize an empty list to store the squared values
    for row in matrix:
        square_row = []  # Initialize a list for each row in the result matrix
        for element in row:
            square_row.append(element ** 2)  # Square each element and add to the row
        result.append(square_row)  # Add the squared row to the result matrix
    return result  # Return the resulting matrix

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    squared_matrix = square_matrix_simple(matrix)
    print(squared_matrix)
    print(matrix)