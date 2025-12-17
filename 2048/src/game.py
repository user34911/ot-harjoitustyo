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
        cell_size = self._calculate_cell_size(grid_size)
        position = self._calculate_position(grid_size, cell_size)
        mode = self.options.get(Option.MODE)
        self._grid = Grid(grid_size, cell_size, position, mode)
        self._loop = GameLoop(self._grid, self.renderer, self.options, EventQueue(), Clock())
        self.renderer.set_grid(self._grid)

    def _calculate_cell_size(self, grid_size):
        resolution = self.options.get(Option.RESOLUTION)
        margin = max(100, min(resolution[0] // 10, resolution[1] // 10))
        max_width = resolution[0] - 2 * margin
        max_height = resolution[1] - 2 * margin
        cell_size = min(max_width, max_height) // grid_size
        return cell_size

    def _calculate_position(self, grid_size, cell_size):
        resolution = self.options.get(Option.RESOLUTION)
        offset = (grid_size * cell_size) // 2
        x = (resolution[0] // 2) - offset
        y = (resolution[1] // 2) - offset
        return (x, y)
