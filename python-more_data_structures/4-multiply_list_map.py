def multiply_list_map(my_list=[], number=0):
    return my_list * 2

if __name__ == '__main__':
    numbers = [1, 2, 4, 5]
    my_list = multiply_list_map(numbers)
    result = map(multiply_list_map, numbers)
    print(numbers)
    print(list(result))