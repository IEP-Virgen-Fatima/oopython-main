from __future__ import annotations
import random
from direction import Direction


class Position:
    """
    Position (row / column).
    """

    def __init__(self, row: int, column: int):
        """
        Creates a new position instance, from given row/column.

        :param row: (int) row
        :param column: (int) column

        """
        self._row = row
        self._column = column

    def __str__(self) -> str:
        """
        Exports position as a string.

        :return: (str) position as "[row,column]"

        """
        return "[" + str(self._row) + "," + str(self._column) + "]"

    @property
    def row(self) -> int:
        """
        Returns row.

        :return: (int) row value

        """
        return self._row

    @property
    def column(self) -> int:
        """
        Returns column.

        :return: (int) column value

        """
        return self._column

    def __eq__(self, other: Position) -> bool:
        """
        Checks for equality.

        :param other: (Position) other position

        :return: (bool) True if positions share row/column values, False else

        """
        return (other.row == self._row) and (other.column == self._column)

    def get_neighbour(self, direction: Direction) -> Position:
        """
        Returns neighbour position, for a given direction.

        :param direction: (Direction) direction

        :return: (Position) neighbour position in the given direction

        """
        return Position(self._row + direction.row_offset, self._column + direction.column_offset)

    @staticmethod
    def get_random_position(max_row: int, max_column: int) -> Position:
        """
        Returns a randomly chosen direction, within given bounds.

        :return: (Position) a randomly chosen position, within [0, max_row[ and [0, max_column[

        """
        row = random.randint(0, max_row-1)
        column = random.randint(0, max_column-1)
        return Position(row, column)

    @staticmethod
    def value_of(position_string: str) -> Position:
        """
        Parses a position from its string representation (supposed valid).

        :param position_string: (str) position string representation

        :return: (Position) parsed position

        """
        comma_index = position_string.index(',')
        row = int(position_string[1:comma_index])
        column = int(position_string[comma_index + 1:-1])
        return Position(row, column)
