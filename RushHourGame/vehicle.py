from color import Color
from direction import Direction
from position import Position


class Vehicle:
    """
    Vehicle (head position, heading direction, size, color).
    """

    def __init__(self, color: Color, head_position: Position, size: int, direction: Direction):
        """
        Creates a new vehicle instance, for given color/position/size/direction.

        :param color: (Color) color
        :param head_position: (Position) head position
        :param size: (int) size
        :param direction: (Direction) heading direction

        """
        self._head_position: Position = head_position
        self._direction: Direction = direction
        self._color: Color = color
        self._size: int = size

    def __str__(self) -> str:
        """
        Exports vehicle as a string.

        :return: (str) a string representing vehicle

        """
        return self._color.name + " at " + str(self._head_position) + " -> " + str(self._direction) + " size " + str(self._size)

    @property
    def head_position(self) -> Position:
        """
        Returns head position.

        :return: (Position) head position

        """
        return self._head_position

    @property
    def rear_position(self) -> Position:
        """
        Returns rear position.

        :return: (Position) rear position

        """
        return self._get_positions()[self._size - 1]

    @property
    def direction(self) -> Direction:
        """
        Returns heading direction.

        :return: (direction) heading direction

        """
        return self._direction

    @property
    def color(self) -> Color:
        """
        Returns color.

        :return: (color) color

        """
        return self._color

    @property
    def size(self) -> int:
        """
        Returns size.

        :return: (int) size

        """
        return self._size

    def shift(self, direction: Direction) -> None:
        """
        Shifts vehicle in a direction (one position). Shifting is supposed to be valid.

        :param direction: (Direction) direction

        :return: (None)

        """
        self._head_position = self._head_position.get_neighbour(direction)

    def is_at(self, position: Position) -> bool:
        """
        Checks if vehicle occupies a given position.

        :param position: (Position) position

        :return: (bool) True if vehicle occupies position, False else

        """
        #positions = self._get_positions()
        #check =  position in positions
        #return check
        return position in self._get_positions()

    def _get_positions(self) -> list[Position]:
        """
        (internal method) Returns all occupied positions.

        :return: (list(Position)) occupied positions (from head to rear)

        """
        positions = []
        position = self._head_position
        opposite_direction = self._direction.get_opposite()
        for _ in range(0, self._size):
            positions.append(position)
            position = position.get_neighbour(opposite_direction)
        return positions
