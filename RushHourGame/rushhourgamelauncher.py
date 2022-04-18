from RushHourGame.vehicle import Vehicle
from RushHourGame.color import Color
from RushHourGame.consoledisplay import ConsoleDisplay
from RushHourGame.direction import Direction
from RushHourGame.position import Position
from RushHourGame.randominput import RandomInput
from RushHourGame.rushhourgame import RushHourGame
from RushHourGame.vehicle import Vehicle


"""
Rush hour game launcher (random input, console output)
"""

vehicles = [Vehicle(Color.RED, Position(2, 2), 2, Direction.E),
            Vehicle(Color.GREEN, Position(0, 1), 2, Direction.E),
            Vehicle(Color.YELLOW, Position(0, 5), 3, Direction.N),
            Vehicle(Color.PURPLE, Position(3, 0), 3, Direction.S),
            Vehicle(Color.ORANGE, Position(5, 0), 2, Direction.S),
            Vehicle(Color.DARK_BLUE, Position(3, 3), 3, Direction.S),
            Vehicle(Color.LIGHT_BLUE, Position(4, 5), 2, Direction.E),
            Vehicle(Color.LIGHT_GREEN, Position(5, 2), 3, Direction.W)]

game = RushHourGame(vehicles, RandomInput(), ConsoleDisplay())
game.play()


