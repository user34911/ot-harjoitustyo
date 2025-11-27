import pygame
import pygame_gui
from status import Status

class MenuLoop:
    def __init__(self, menu, renderer, manager):
        self._menu = menu
        self._clock = pygame.time.Clock()
        self._renderer = renderer
        self.manager = manager

        self._menu.recreate_menu(self.manager)

    def start(self):
        while True:
            status = self._handle_events()
            if status is Status.EXIT:
                return Status.EXIT
            if status is Status.GAME:
                return Status.GAME

            time_delta = self._clock.tick(60) / 1000.0
            self.manager.update(time_delta)
            self._render()

    def _handle_events(self):
        for event in pygame.event.get():
            self.manager.process_events(event)

            if event.type == pygame.QUIT:
                return Status.EXIT

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self._menu.start_button:
                    return Status.GAME
                if event.ui_element == self._menu.exit_button:
                    return Status.EXIT

        return None

    def _render(self):
        self._renderer.render(self.manager)
