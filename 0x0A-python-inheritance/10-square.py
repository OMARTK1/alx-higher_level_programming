#!/usr/bin/python3

class BaseGeometry:
    """Empty class BaseGeometry"""
    
    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates value as an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __str__(self):
        """Returns the rectangle description [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    
    def __init__(self, width, height):
        """Initializes a Rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the area of the rectangle"""
        return self.__width * self.__height

class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    
    def __init__(self, size):
        """Initializes a Square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns the rectangle description [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
