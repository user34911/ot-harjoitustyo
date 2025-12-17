from enums import State, Option, Mode
from repository.config_repository import get_resolution, get_user

class Options:
    def __init__(self):
        resolution = get_resolution()
        user = get_user()
        grid_size = 4
        position = (100, 100)
        mode = Mode.STANDARD
        theme_path = r"src\ui\theme.json"
        state = State.MENU

        self._options = {Option.RESOLUTION: resolution,
                         Option.GRID_SIZE: grid_size,
                         Option.POSITION: position,
                         Option.MODE: mode,
                         Option.THEME_PATH: theme_path,
                         Option.STATE: state,
                         Option.USER: user}

    def get(self, option: Option):
        return self._options[option]

    def change(self, option: Option, new_value):
        self._options[option] = new_value
