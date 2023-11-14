#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        self.validate_non_negative_int("width", value)
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        self.validate_non_negative_int("height", value)
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        self.validate_non_negative_int("x", value)
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        self.validate_non_negative_int("y", value)
        self.__y = value

    def validate_non_negative_int(self, attribute, value):
        """ Validate if value is a non-negative integer """
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")

    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Display the rectangle using '#' characters """
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """ Return a string representation of the rectangle """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def to_dictionary(self):
        """ Return dictionary representation of Rectangle instance """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
