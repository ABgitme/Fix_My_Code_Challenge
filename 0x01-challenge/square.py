#!/usr/bin/python3
""" Module for square class"""

class Square():
    """
    A class representing a square.

    Attributes:
        width (int): The width of the square.
        height (int): The height of the square.
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initialize the Square object with given width and height.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """
        Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Return a string representation of the Square object.

        Returns:
            str: A string representation of the Square object.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
