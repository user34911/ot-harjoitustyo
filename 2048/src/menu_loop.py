import pygame
import pygame_gui
from pygame_gui import UIManager
from enums import State, Mode, MenuScreen, Option
from options import Options
from repository.config_repository import set_user

class MenuLoop:
    """loop that handles menu events"""
    def __init__(self, screens: dict, manager: UIManager, renderer, options: Options):
        """initialise loop

        Args:
            screens (dict): dict containing all the menu screens
            manager (UIManager): pygame_gui asset handling pygame_gui elements
            renderer (Renderer): renders menu
            options (Options): options off app to enable changing them
        """
        self._screens = screens
        self._manager = manager
        self._renderer = renderer
        self._options = options
        self._clock = pygame.time.Clock()

    def start(self):
        """start and run the loop"""
        self._screens[MenuScreen.MAIN_MENU].recreate(self._manager)
        self._screens[MenuScreen.START_OPTIONS].recreate(self._manager)
        self._screens[MenuScreen.LEADERBOARDS].recreate(self._manager)
        self._screens[MenuScreen.USERNAME].recreate(self._manager)

        while True:
            if self._handle_events() is not True:
                return

            time_delta = self._clock.tick(60) / 1000.0
            self._manager.update(time_delta)
            self._render()

    def _handle_events(self):
        """get event and check its type before delegating handling to subfunction

        Returns:
            bool: should loop continue running
        """
        for event in pygame.event.get():
            self._manager.process_events(event)

            if event.type == pygame.QUIT:
                return self._options.change(Option.STATE, State.EXIT)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._screens[MenuScreen.START_OPTIONS].container.hide()
                    self._screens[MenuScreen.LEADERBOARDS].container.hide()
                    self._screens[MenuScreen.USERNAME].container.hide()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if self._screens[MenuScreen.LEADERBOARDS].container.visible:
                    state = self._handle_leaderboards_event(event)
                elif self._screens[MenuScreen.START_OPTIONS].container.visible:
                    state = self._handle_start_option_event(event)
                else:
                    state = self._handle_main_menu_event(event)
                return state if state is not True else True

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                self._handle_username_event(event)

        return True

    def _handle_leaderboards_event(self, event):
        """handles an event occuring in leaderboard window

        Args:
            event

        Returns:
            bool: should loop continue running
        """
        if event.ui_element == self._screens[MenuScreen.LEADERBOARDS].standard_button:
            self._screens[MenuScreen.LEADERBOARDS].show_standard_leaderboards()

        if event.ui_element == self._screens[MenuScreen.LEADERBOARDS].timed_button:
            self._screens[MenuScreen.LEADERBOARDS].show_timed_leaderboards()

        return True

    def _handle_start_option_event(self, event):
        """handles an event occuring in start option window

        Args:
            event

        Returns:
            bool: should loop continue running
        """
        if event.ui_element == self._screens[MenuScreen.START_OPTIONS].back_button:
            self._screens[MenuScreen.START_OPTIONS].container.hide()

        if event.ui_element == self._screens[MenuScreen.START_OPTIONS].start_game_button:
            if self._screens[MenuScreen.START_OPTIONS].timed_mode_checkbox.is_checked:
                self._options.change(Option.MODE, Mode.TIMED)
            else:
                self._options.change(Option.MODE, Mode.STANDARD)

            grid_size = self._screens[MenuScreen.START_OPTIONS].grid_size_dropdown.selected_option
            grid_size = int(self._parse_option_string(grid_size[0])[0])
            self._options.change(Option.GRID_SIZE, grid_size)

            return self._options.change(Option.STATE, State.GAME)

        return True

    def _handle_main_menu_event(self, event):
        """handles an event occuring in main menu

        Args:
            event

        Returns:
            bool: should loop continue running
        """
        if event.ui_element == self._screens[MenuScreen.MAIN_MENU].exit_button:
            return self._options.change(Option.STATE, State.EXIT)

        if event.ui_element == self._screens[MenuScreen.MAIN_MENU].leaderboard_button:
            self._screens[MenuScreen.LEADERBOARDS].container.show()
            self._screens[MenuScreen.LEADERBOARDS].show_standard_leaderboards()

        if event.ui_element == self._screens[MenuScreen.MAIN_MENU].start_button:
            self._screens[MenuScreen.START_OPTIONS].container.show()

        if event.ui_element == self._screens[MenuScreen.MAIN_MENU].username_button:
            self._screens[MenuScreen.USERNAME].container.show()

        return True

    def _handle_username_event(self, event):
        """handles an event occuring in username window

        Args:
            event

        Returns:
            bool: should loop continue running
        """
        if event.ui_element == self._screens[MenuScreen.USERNAME].input_box:
            new_username = event.text
            set_user(new_username)
            self._options.change(Option.USER, new_username)
            self._screens[MenuScreen.USERNAME].container.hide()

    def _render(self):
        """call renderer to render manu"""
        self._renderer.render_menu(self._manager)

    def _parse_option_string(self, string: str):
        """parse the string from grid size dropdown

        Args:
            string (str): grid size ex. "4x4"

        Returns:
            int: grid size as only a single number ex. 4
        """
        parsed = string.split("x")
        return (parsed[0], parsed[1])
