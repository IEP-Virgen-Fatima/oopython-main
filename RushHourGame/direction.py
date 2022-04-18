from __future__ import annotations
import random
from enum import Enum


class Direction(Enum):
    """
    Enumeration of directions.
    The couple of ints associated to each direction is used to compute neighbouring.
    """

    N = (-1, 0)
    S = (1, 0)
    W = (0, -1)
    E = (0, 1)

    def __init__(self, row_offset: int, column_offset: int):
        """
        Creates a new Direction instance, with given offsets.

        :param row_offset: (int) row offset
        :param column_offset: (int) column offset

        """
        self._row_offset = row_offset
        self._column_offset = column_offset

    def __str__(self) -> str:
        """
        Exports direction as a string.

        :return: (str) a single character string representing the direction (actually taken from its name)

        """
        return self.name

    def __eq__(self, other: Direction) -> bool:
        """
        Checks for equality.

        :param other: (Direction) other position

        :return: (bool) True if directions share row_offset/column_offset values, False else

        """
        return (other.row_offset == self._row_offset) and (other.column_offset == self._column_offset)

    @property
    def row_offset(self) -> int:
        """
        getter property for row offset.

        :return: (int) row offset value

        """
        return self._row_offset

    @property
    def column_offset(self) -> int:
        """
        getter property for column offset.

        :return: (int) column offset value

        """
        return self._column_offset

    def get_opposite(self) -> Direction:
        """
        Returns opposite direction.

        :return: (Direction) opposite direction
        """
        if self is Direction.N:
            return Direction.S
        if self is Direction.S:
            return Direction.N
        if self is Direction.W:
            return Direction.E
        return Direction.W

    @staticmethod
    def get_random_direction() -> Direction:
        """
        Returns a randomly chosen direction.

        :return: (Direction) a randomly chosen direction

        """
        directions = list(Direction)
        index = random.randrange(0, len(directions))
        return directions[index]

    @staticmethod
    def value_of(direction_string: str) -> Direction:
        """
        Parses a direction from its string representation (supposed valid).

        :param direction_string: (str) direction string representation

        :return: (Direction) parsed direction

        """
        return Direction.__members__[direction_string]
