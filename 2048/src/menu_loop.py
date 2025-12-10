import pygame
import pygame_gui
from pygame_gui import UIManager
from enums import Status
from enums import MenuScreen
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
        self._screens[MenuScreen.START_OPTIONS].container.hide()

        while True:
            status = self._handle_events()
            if status is not True:
                return

            time_delta = self._clock.tick(60) / 1000.0
            self._manager.update(time_delta)
            self._render()

    def _handle_events(self):
        for event in pygame.event.get():
            self._manager.process_events(event)

            if event.type == pygame.QUIT:
                return self._options.set_state(Status.EXIT)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    try:
                        self._screens[MenuScreen.START_OPTIONS].container.hide()
                        self._screens[MenuScreen.LEADERBOARDS].container.hide()
                    except AttributeError:
                        pass

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self._screens[MenuScreen.MAIN_MENU].start_button:
                    self._screens[MenuScreen.START_OPTIONS].container.show()

                if event.ui_element == self._screens[MenuScreen.START_OPTIONS].start_game_button:
                    if self._screens[MenuScreen.START_OPTIONS].timed_mode_checkbox.is_checked:
                        self._options.set_timed(True)
                    else:
                        self._options.set_timed(False)
                    return self._options.set_state(Status.GAME)

                if event.ui_element == self._screens[MenuScreen.START_OPTIONS].back_button:
                    self._screens[MenuScreen.START_OPTIONS].container.hide()

                if event.ui_element == self._screens[MenuScreen.MAIN_MENU].exit_button:
                    return self._options.set_state(Status.EXIT)

                if event.ui_element == self._screens[MenuScreen.MAIN_MENU].leaderboard_button:
                    self._screens[MenuScreen.LEADERBOARDS].recreate(self._manager)
                    self._screens[MenuScreen.LEADERBOARDS].container.show()

        return True

    def _render(self):
        self._renderer.render_menu(self._manager)
