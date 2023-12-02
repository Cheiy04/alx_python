# define a function that returns the number of arguments in a list
def args(index):
    
    output = ""

    if len(index) > 0:
        output += "{} arguments: \n".format(len(index))
    else:
        output += "{} arguments.\n".format(len(index))

    for x, i in enumerate(index, 1):
        output += "{}: {}\n".format(x, i)

    return output
