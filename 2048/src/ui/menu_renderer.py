import pygame

class MenuRenderer:
    def __init__(self, display, menu):
        self._display = display
        self._menu = menu
        pygame.font.init()

    def render(self, manager):
        # Draw background
        self._display.blit(self._menu.background_surface, (0, 0))
        # Draw menu
        manager.draw_ui(self._display)

        pygame.display.update()
