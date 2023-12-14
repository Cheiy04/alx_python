'''Importing from file 7'''
Rectangle = __import__("7-rectangle").Rectangle

'''Create a Square class that inherits rectangle'''
class Square(Rectangle):

    '''This is an initializer for the size of the square'''
    def __init__(self, size):
        """
        Initialize a Square instance with the specified size.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)  # Call the constructor of the parent class (Rectangle)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The formatted string representation.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)