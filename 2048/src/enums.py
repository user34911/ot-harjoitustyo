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
    MODE = 5
    THEME_PATH = 6

class State(Enum):
    MENU = 1
    GAME = 2
    EXIT = 3

class Game(Enum):
    ONGOING = 1
    LOST = 2
    WON = 3

class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4

class Mode(Enum):
    STANDARD = 1
    TIMED = 2

class Object(Enum):
    TILE = 1
    CELL = 2
    BORDER = 3
