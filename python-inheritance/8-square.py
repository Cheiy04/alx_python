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

    def __dir__(self):
        return sorted(['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
                       '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
                       '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', 
                       '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
                       '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator'
                       ])
    


    


