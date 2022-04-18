from move import Move


class Input:
    """
    Interface for player input
    """

    def get_move(self) -> Move:
        """
        Requests a move from player.

        :return: (Move) move given by the player

        """
        pass
