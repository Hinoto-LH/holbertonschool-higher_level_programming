#!/usr/bin/python3
class BaseGeometry:
    """Write an empty class BaseGeometry."""
    def area(self):
        """
        Public instance method: def area(self): that raises an Exception
          with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """exception of TypeError and ValueError"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
