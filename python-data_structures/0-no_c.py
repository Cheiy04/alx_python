def no_c(my_string):
    result = ""

    for i in my_string:
        if i.lower() != "c" or i.upper() != "C":
            result += i
    return result

if __name__ == '__main__':
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
