from typing_extensions import Final
from position import Position


class RushHourGameConstants:
    """
    Rush hour game constants.
    """

    ROWS: Final[int] = 6
    """
    Row count (int).
    """

    COLUMNS: Final[int] = 6
    """
    Column count (int).
    """

    EXIT_POSITION: Final[Position] = Position(2, 5)
    """
    Exit position (Position).
    """
