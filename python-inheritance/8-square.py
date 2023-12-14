"""
    The BaseGeometry class is the base class for geometry-related classes.
"""
# base_geometry.py
class BaseGeometry:
    """
    The BaseGeometry class is the base class for geometry-related classes.
    """

    def area(self):
        """
        Public instance method to calculate the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    The Rectangle class represents a rectangle and inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The calculated area.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The formatted string representation.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


"""
    The Square class represents a square and inherits from Rectangle.
"""
class Square(Rectangle):
    """
    Attributes:
        __size (int): The size of the square.
    """

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