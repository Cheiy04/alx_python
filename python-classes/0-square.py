class Square:
    """A class representing a square.

    The Square class is designed to create square objects with a specified size.
    It initializes the size attribute during object creation.

    Attributes:
        We are using a private attribute that allocates the size.

    Methods:
        Only the __init__  method has been utilised in this class

    Results of the class should be as follows:
        >>> square = Square(5)
        >>> print(square.__size)
        5
    """
    def __init__(self, size):
        """Initialize a Square object with a specified size.

        Args:
            size: The size of the square.
        """
        self.size = size

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)


if __name__ == '__main__':


    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)