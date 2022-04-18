from move import Move
from vehicle import Vehicle


class Display:
    """
    Interface for game events display.
    """

    def notify_new_turn(self, turn_count: int) -> None:
        """
        Notifies that a new turn is being played.

        :param turn_count: (int) turn count

        :return: (None)

        """
        pass

    def display_board(self, vehicles: list[Vehicle]) -> None:
        """
        Displays board.

        :param vehicles: (list(vehicles)) vehicles on board

        :return: (None)

        """
        pass

    def notify_game_is_over(self, turn_count: int) -> None:
        """
        Notifies that game is over.

        :param turn_count: turn count

        :return: (None)

        """
        pass

    def ask_for_move(self) -> None:
        """
        Notifies that a move is requested by the player.

        :return: (None)

        """
        pass

    def notify_move(self, move: Move) -> None:
        """
        Notifies that a move has been given by the player.

        :param move: move

        :return: (None)

        """
        pass
