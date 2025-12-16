import pygame
import pygame_gui
from pygame_gui import UIManager
from enums import State, Mode, MenuScreen, Option
from options import Options

class MenuLoop:
    def __init__(self, screens: dict, manager: UIManager, renderer, options: Options):
        self._screens = screens
        self._manager = manager
        self._renderer = renderer
        self._options = options
        self._clock = pygame.time.Clock()

    def start(self):
        self._screens[MenuScreen.MAIN_MENU].recreate(self._manager)
        self._screens[MenuScreen.START_OPTIONS].recreate(self._manager)
        self._screens[MenuScreen.LEADERBOARDS].recreate(self._manager)

        while True:
            if self._handle_events() is not True:
                return

            time_delta = self._clock.tick(60) / 1000.0
            self._manager.update(time_delta)
            self._render()

    def _handle_events(self):
        for event in pygame.event.get():
            self._manager.process_events(event)

            if event.type == pygame.QUIT:
                return self._options.change(Option.STATE, State.EXIT)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._screens[MenuScreen.START_OPTIONS].container.hide()
                    self._screens[MenuScreen.LEADERBOARDS].container.hide()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if self._screens[MenuScreen.LEADERBOARDS].container.visible:
                    state = self._handle_leaderboards_event(event)
                elif self._screens[MenuScreen.START_OPTIONS].container.visible:
                    state = self._handle_start_option_event(event)
                else:
                    state = self._handle_main_menu_event(event)
                return state if state is not True else True

        return True

    def _handle_leaderboards_event(self, event):
        if event.ui_element == self._screens[MenuScreen.LEADERBOARDS].standard_button:
            self._screens[MenuScreen.LEADERBOARDS].show_standard_leaderboards()

        if event.ui_element == self._screens[MenuScreen.LEADERBOARDS].timed_button:
            self._screens[MenuScreen.LEADERBOARDS].show_timed_leaderboards()

        return True

    def _handle_start_option_event(self, event):
        if event.ui_element == self._screens[MenuScreen.START_OPTIONS].back_button:
            self._screens[MenuScreen.START_OPTIONS].container.hide()

        if event.ui_element == self._screens[MenuScreen.START_OPTIONS].start_game_button:
            if self._screens[MenuScreen.START_OPTIONS].timed_mode_checkbox.is_checked:
                self._options.change(Option.MODE, Mode.TIMED)
            else:
                self._options.change(Option.MODE, Mode.STANDARD)

            grid_size = self._screens[MenuScreen.START_OPTIONS].grid_size_dropdown.selected_option[0]
            grid_size = int(self._parse_option_string(grid_size)[0])
            self._options.change(Option.GRID_SIZE, grid_size)

            return self._options.change(Option.STATE, State.GAME)

        return True

    def _handle_main_menu_event(self, event):
        if event.ui_element == self._screens[MenuScreen.MAIN_MENU].exit_button:
            return self._options.change(Option.STATE, State.EXIT)

        if event.ui_element == self._screens[MenuScreen.MAIN_MENU].leaderboard_button:
            self._screens[MenuScreen.LEADERBOARDS].container.show()
            self._screens[MenuScreen.LEADERBOARDS].show_standard_leaderboards()

        if event.ui_element == self._screens[MenuScreen.MAIN_MENU].start_button:
            self._screens[MenuScreen.START_OPTIONS].container.show()

        return True

    def _render(self):
        self._renderer.render_menu(self._manager)

    def _parse_option_string(self, string: str):
        parsed = string.split("x")
        return (parsed[0], parsed[1])
