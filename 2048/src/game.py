from grid import Grid
from game_loop import GameLoop
from clock import Clock
from event_queue import EventQueue
from options import Option

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
        opt = self.options.get_game_options()
        self._grid = Grid(opt[Option.GRID_SIZE], opt[Option.CELL_SIZE],
                          opt[Option.POSITION], opt[Option.MODE])
        self._loop = GameLoop(self._grid, self.renderer, self.options, EventQueue(), Clock())
        self.renderer.set_grid(self._grid)
