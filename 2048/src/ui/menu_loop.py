import pygame
import pygame_gui
from status import Status

class MenuLoop:
    def __init__(self, menu, renderer):
        self._menu = menu
        self._clock = pygame.time.Clock()
        self._renderer = renderer
        self.manager = pygame_gui.UIManager(self._menu.window_size, r"src\ui\theme.json")

        self._menu.recreate_menu(self.manager)
        self._menu.start_options(self.manager)

    def start(self):
        self._menu.start_options_container.hide()
        while True:
            status = self._handle_events()
            if status is not None:
                return status

            time_delta = self._clock.tick(60) / 1000.0
            self.manager.update(time_delta)
            self._render()

    def _handle_events(self):
        for event in pygame.event.get():
            self.manager.process_events(event)

            if event.type == pygame.QUIT:
                return Status.EXIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    try:
                        self._menu.start_options_container.hide()
                        self._menu.leaderboard_container.hide()
                    except AttributeError:
                        pass

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self._menu.start_button:
                    self._menu.start_options_container.show()
                if event.ui_element == self._menu.start_game_button:
                    if self._menu.timed_mode_checkbox.is_checked:
                        return Status.TIMED_GAME
                    return Status.GAME
                if event.ui_element == self._menu.back_button:
                    self._menu.start_options_container.hide()
                if event.ui_element == self._menu.exit_button:
                    return Status.EXIT
                if event.ui_element == self._menu.leaderboard_button:
                    self._menu.make_leaderboard(self.manager)
                    self._menu.leaderboard_container.show()

        return None

    def _render(self):
        self._renderer.render_menu(self.manager)
