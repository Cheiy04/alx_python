'''Importing from file 7'''
Rectangle = __import__("7-rectangle").Rectangle

'''Create a Square class that inherits rectangle'''
class Square(Rectangle):

    '''This is an initializer for the size of the square'''
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    '''Functon to return our string'''
    def __str__(self):
        '''Returns a string rep of our square'''
        return "[Square] {}/{}".format(self.__size, self.__size)
    
    '''Function that calculates the area of our square'''
    def area(self):
        return self.__size ** 2
    


    


