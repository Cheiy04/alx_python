def print_matrix_integer(matrix=[[]]):
    result = []
    for i in matrix:
        result += i
    return result

if __name__ == '__main__':
    matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    result = print_matrix_integer([matrix])
    print("{}\n{}\n{}".format(matrix[0], matrix[1], matrix[2]))
    print("--")