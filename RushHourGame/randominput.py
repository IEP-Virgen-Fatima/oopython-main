from input import Input
from move import Move


class RandomInput(Input):
    """
    Random implementation of Input interface.
    """

    def get_move(self) -> Move:
        return Move.get_random_move()
