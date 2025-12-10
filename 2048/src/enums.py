from enum import Enum

class MenuScreen(Enum):
    MAIN_MENU = 1
    START_OPTIONS = 2
    LEADERBOARDS = 3

class Option(Enum):
    RESOLUTION = 1
    GRID_SIZE = 2
    CELL_SIZE = 3
    POSITION = 4
    TIMED = 5
    THEME_PATH = 6

class Status(Enum):
    MENU = 1
    GAME = 2
    EXIT = 3
    OVER = 4
    TIMED_GAME = 5
    TIMED_OVER = 6

class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4
