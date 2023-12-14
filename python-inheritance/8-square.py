'''Importing from file 7'''
Rectangle = __import__("7-rectangle").Rectangle

'''Create a Square class that inherits rectangle'''
class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        '''Returns a string rep of our square'''
        return "[Square] {}/{}".format(self.__size, self.__size)
    
    '''Function that calculates the area of our square'''
    def area(self):
        return self.__size ** 2
    


    


