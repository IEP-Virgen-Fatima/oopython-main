from __future__ import annotations
from direction import Direction
from position import Position
from rushhourgameconstants import RushHourGameConstants


class Move:
    """
    Move (position + direction)
    """

    def __init__(self, position: Position, direction: Direction):
        """
        Creates a new move instance, from given position/direction.
        :param position: (Position) position
        :param direction: (Direction) direction
        """
        self._position = position
        self._direction = direction

    def __str__(self) -> str:
        """
        Exports move as a string.
        :return: (str) move as "position direction"
        """
        return str(self._position) + " " + str(self._direction)

    @property
    def position(self) -> Position:
        """
        getter property for position.
        :return: (Position) position value
        """
        return self._position

    @property
    def direction(self) -> Direction:
        """
        getter property for direction.

        :return: (Direction) direction value

        """
        return self._direction

    @staticmethod
    def get_random_move() -> Move:
        """
        Returns a randomly chosen move.

        :return: (Move) a randomly chosen move

        """
        position = Position.get_random_position(RushHourGameConstants.ROWS, RushHourGameConstants.COLUMNS)
        direction = Direction.get_random_direction()
        return Move(position, direction)

    @staticmethod
    def value_of(move_string: str) -> Move:
        """
        Parses a move from its string representation (supposed valid).

        :param move_string: (str) move string representation

        :return: (Move) parsed move

        """
        space_index = move_string.index(' ')
        position = Position.value_of(move_string[0:space_index])
        direction = Direction.value_of(move_string[space_index + 1:])
        return Move(position, direction)
