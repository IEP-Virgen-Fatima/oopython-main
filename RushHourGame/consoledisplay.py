from RushHourGame.display import Display
from RushHourGame.move import Move
from RushHourGame.position import Position
from RushHourGame.rushhourgameconstants import RushHourGameConstants
from RushHourGame.vehicle import Vehicle


class ConsoleDisplay(Display):
    """
    Console implementation of Display interface.
    """

    def notify_new_turn(self, turn_count: int) -> None:
        print("Turn " + str(turn_count))

    def display_board(self, vehicles: list[Vehicle]) -> None:
        for row in range(RushHourGameConstants.ROWS):
            for column in range(RushHourGameConstants.COLUMNS):
                position = Position(row, column)
                char = "X"
                for vehicle in vehicles:
                    if vehicle.is_at(position):
                        char = str(vehicle.color)
                        break
                print(char, end="")
            print()

    def notify_game_is_over(self, turn_count: int) -> None:
        print("Exit reached in " + str(turn_count) + " turns")

    def ask_for_move(self) -> None:
        print("Enter a move (ex. [1,2] N)")

    def notify_move(self, move: Move) -> None:
        print(move)
