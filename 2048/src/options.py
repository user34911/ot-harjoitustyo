from enums import Status, Option

class Options:
    def __init__(self):
        self._resolution = (600, 600)
        self._grid_size = 4
        self._cell_size = 100
        self._position = (100, 100)
        self._timed = False

        self._theme_path = r"src\ui\theme.json"

        self._state = Status.MENU

    def get_game_options(self):
        options = {Option.RESOLUTION: self._resolution,
                   Option.GRID_SIZE: self._grid_size,
                   Option.CELL_SIZE: self._cell_size,
                   Option.POSITION: self._position,
                   Option.TIMED: self._timed}
        return options

    def get_menu_options(self):
        options = {Option.RESOLUTION: self._resolution,
                   Option.THEME_PATH: self._theme_path}
        return options

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def set_timed(self, state: bool):
        self._timed = state

    def is_timed(self):
        return self._timed

    def get_resolution(self):
        return self._resolution
