from grid import Grid
from game_loop import GameLoop
from clock import Clock
from event_queue import EventQueue
from enums import Option

class Game:
    def __init__(self, options, renderer):
        self.options = options
        self.renderer = renderer
        self._grid = None
        self._loop = None

    def start(self):
        self._initialise_game()
        self._loop.start()

    def _initialise_game(self):
        grid_size = self.options.get(Option.GRID_SIZE)
        position = self.options.get(Option.POSITION)
        cell_size = self._calculate_cell_size(grid_size, position)
        mode = self.options.get(Option.MODE)
        self._grid = Grid(grid_size, cell_size, position, mode)
        self._loop = GameLoop(self._grid, self.renderer, self.options, EventQueue(), Clock())
        self.renderer.set_grid(self._grid)

    def _calculate_cell_size(self, grid_size, position):
        resolution = self.options.get(Option.RESOLUTION)
        margin = position[0]
        total_width = resolution[0] - 2 * margin
        cell_size = total_width // grid_size
        return cell_size
