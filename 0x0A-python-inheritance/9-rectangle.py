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

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def __str__(self):
        """Returns the rectangle description [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.get_width(), self.get_height())
