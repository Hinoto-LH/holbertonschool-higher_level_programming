#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """use method of BaseGeometry"""
        self.integer_validator("width", width)
        self.__width__ = width
        self.integer_validator("height", height)
        self.__height__ = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width__ * self.__height__

    def __str__(self):
        """str() should return"""
        return "[Rectangle] {}/{}".format(self.__width__, self.__height__)
