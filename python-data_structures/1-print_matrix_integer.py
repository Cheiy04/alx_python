def print_matrix_integer(matrix=[[]]):
    result = []
    for row_index, row in enumerate(matrix):
        result.extend(row)
        if row_index != len(matrix) - 1:  # Add newline if not the last row
            result.append('\n')

    # Convert integers to strings except for '\n'
    return " ".join("{:d}".format(item) if isinstance(item, int) else item for item in result)

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    result = print_matrix_integer(matrix)
    print(result)
    print("--")

