def square_matrix(matrix=[] ):
    result = [] #to output our result
    for i in matrix:
        square_list = [] #
        for element in i:
            square_list.append(element**2)
        result.append(square_list)
    return result

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(square_matrix(matrix))
