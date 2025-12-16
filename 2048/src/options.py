from enums import State, Option, Mode

class Options:
    def __init__(self):
        self._resolution = (600, 600)
        self._grid_size = 4
        self._cell_size = 100
        self._position = (100, 100)
        self._mode = Mode.STANDARD

        self._theme_path = r"src\ui\theme.json"

        self._state = State.MENU

        self._options = {Option.RESOLUTION: self._resolution,
                         Option.GRID_SIZE: self._grid_size,
                         Option.CELL_SIZE: self._cell_size,
                         Option.POSITION: self._position,
                         Option.MODE: self._mode,
                         Option.THEME_PATH: self._theme_path,
                         Option.STATE: self._state}

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

    def get(self, option: Option):
        return self._options[option]

    def change(self, option: Option, new_value):
        self._options[option] = new_value
