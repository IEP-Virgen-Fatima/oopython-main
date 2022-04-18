from direction import Direction
from display import Display
from input import Input
from move import Move
from position import Position
from rushhourgameconstants import RushHourGameConstants
from vehicle import Vehicle


class RushHourGame:
    """
    Rush hour game.
    """

    def __init__(self, vehicles: list[Vehicle], game_input: Input, game_display: Display):
        """
        Creates a new rush hour game instance, with given vehicles on board.

        :param vehicles: (list(Vehicle)) vehicles on board
        :param game_input: (Input) input
        :param game_display: (Display) display

        """
        self._vehicles = vehicles
        self._game_input = game_input
        self._game_display = game_display

    @staticmethod
    def is_position_out_of_bounds(position: Position) -> bool:
        """
        Checks if a given position is out of board.

        :param position: (Position) position

        :return: (bool) True if position is out of board, False else

        """
        return position.row < 0 or position.column < 0 or position.row >= RushHourGameConstants.ROWS or position.column >= RushHourGameConstants.COLUMNS

    def play(self) -> None:
        """
        Plays game.

        :return: (None)

        """
        self._game_display.display_board(self._vehicles)
        turn_count = 1
        while not self._game_is_over():
            self._game_display.notify_new_turn(turn_count)
            self._play_new_turn()
            turn_count += 1
        self._game_display.notify_game_is_over(turn_count)

    def _game_is_over(self) -> bool:
        """
        (internal method) Checks if game is over.

        :return: (bool) True if read car has reached EXIT_POSITION, False else

        """
        return self._vehicles[0].is_at(RushHourGameConstants.EXIT_POSITION)

    def _play_new_turn(self) -> None:
        """
        (internal method) Plays a new turn.

        :return: (None)

        """
        while True:
            self._game_display.ask_for_move()
            move = self._game_input.get_move()
            self._game_display.notify_move(move)
            if self._process_move(move):
                self._game_display.display_board(self._vehicles)
                break

    def _process_move(self, move: Move) -> bool:
        """
        (internal method) Processes a move.

        :param move: (Move) move

        :return: (bool) True if move was valid and has been processed, False else

        """
        vehicle = self._get_vehicle_at(move.position)
        if vehicle is None:
            return False
        if not self._is_vehicle_shift_valid(vehicle, move.direction):
            return False
        vehicle.shift(move.direction)
        return True

    def _is_vehicle_shift_valid(self, vehicle: Vehicle, direction: Direction) -> bool:
        """
        (internal method) Checks if a vehicle shift is valid.

        :param vehicle: (Vehicle) vehicle to shift
        :param direction: (Direction) shifting direction

        :return: (bool) True if vehicle shift is valid, False else

        """
        heading_position_when_shifting = vehicle.head_position
        vehicle_heading_direction = vehicle.direction
        if direction != vehicle_heading_direction:
            if direction == vehicle_heading_direction.get_opposite():
                heading_position_when_shifting = vehicle.rear_position
            else:
                return False
        shifted_position = heading_position_when_shifting.get_neighbour(direction)
        return not RushHourGame.is_position_out_of_bounds(shifted_position) and self._get_vehicle_at(
            shifted_position) is None

    def _get_vehicle_at(self, position: Position) -> Vehicle or None:
        """
        (internal method) Returns vehicle occupying a given position, if it exists.

        :param position: (Position) position

        :return: (Vehicle) vehicle occupying position, or None if no vehicle is occupying position

        """
        for vehicle in self._vehicles:
            if vehicle.is_at(position):
                return vehicle
        return None
