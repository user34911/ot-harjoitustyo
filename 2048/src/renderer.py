import pygame

class Renderer:
    def __init__(self, display, grid):
        self._display = display
        self._grid = grid

    def render(self):
        self._display.fill((0, 0, 0))
        self._grid.all_sprites.draw(self._display)

        pygame.display.update()
