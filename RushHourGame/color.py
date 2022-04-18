from __future__ import annotations
import random
from enum import Enum


class Color(Enum):
    """
    Enumeration of colors.
    The character associated to each color is used to export color as string.
    """

    RED = "0"
    GREEN = "1"
    LIGHT_GREEN = "2"
    DARK_GREEN = "3"
    BLUE = "4"
    LIGHT_BLUE = "5"
    DARK_BLUE = "6"
    PURPLE = "7"
    LIGHT_PURPLE = "8"
    YELLOW = "9"
    LIGHT_YELLOW = "A"
    BROWN = "B"
    LIGHT_BROWN = "C"
    BLACK = "D"
    ORANGE = "E"
    PINK = "F"

    def __str__(self) -> str:
        """
        Exports color as a string.

        :return: (str) a single character string representing the color

        """
        return self.value

    @staticmethod
    def get_random_color() -> Color:
        """
        Returns a randomly chosen color.

        :return: (Color) a randomly chosen color

        """
        colors = list(Color)
        index = random.randrange(0, len(colors))
        return colors[index]

    @staticmethod
    def value_of(color_string: str) -> Color or None:
        """
        Parses a color from its string representation (supposed valid).

        :param color_string: (str) color string representation

        :return: (Color) parsed color

        """
        for color in list(Color):
            if color.value == color_string:
                return color
        return None
