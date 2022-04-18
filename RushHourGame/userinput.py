from input import Input
from move import Move


class UserInput(Input):
    """
    Console implementation of Input interface.
    """

    def get_move(self) -> Move:
        return Move.value_of(input())
