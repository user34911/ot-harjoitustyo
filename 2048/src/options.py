from enums import Status, Option, Mode

class Options:
    def __init__(self):
        self._resolution = (600, 600)
        self._grid_size = 4
        self._cell_size = 100
        self._position = (100, 100)
        self._mode = Mode.STANDARD

        self._theme_path = r"src\ui\theme.json"

        self._state = Status.MENU

    def get_game_options(self):
        options = {Option.RESOLUTION: self._resolution,
                   Option.GRID_SIZE: self._grid_size,
                   Option.CELL_SIZE: self._cell_size,
                   Option.POSITION: self._position,
                   Option.MODE: self._mode}
        return options

    def get_menu_options(self):
        options = {Option.RESOLUTION: self._resolution,
                   Option.THEME_PATH: self._theme_path}
        return options

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def set_mode(self, mode: Mode):
        self._mode = mode

    def get_mode(self):
        return self._mode

    def get_resolution(self):
        return self._resolution
