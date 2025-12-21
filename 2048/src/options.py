from enums import State, Option, Mode
from repository.config_repository import get_resolution, get_user

class Options:
    """class that handles options of the game"""
    def __init__(self):
        """set initial values of options"""
        resolution = get_resolution()
        user = get_user()
        grid_size = 4
        mode = Mode.STANDARD
        theme_path = r"src\ui\theme.json"
        state = State.MENU

        self._options = {Option.RESOLUTION: resolution,
                         Option.GRID_SIZE: grid_size,
                         Option.MODE: mode,
                         Option.THEME_PATH: theme_path,
                         Option.STATE: state,
                         Option.USER: user}

    def get(self, option: Option):
        """get the desired option

        Args:
            option (Option): what option to get

        Returns:
            desired option
        """
        return self._options[option]

    def change(self, option: Option, new_value):
        """change the desired option

        Args:
            option (Option): what option to change
            new_value (_type_): what to change option to
        """
        self._options[option] = new_value
