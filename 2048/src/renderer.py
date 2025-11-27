import pygame

class Renderer:
    def __init__(self, display, grid):
        self._display = display
        self._grid = grid

        pygame.font.init()
        self._font = pygame.font.SysFont("Arial", 30)
        self._font.bold = True

    def render(self):
        self._display.fill((214, 189, 159))
        self._grid.tiles.draw(self._display)
        self._grid.cells.draw(self._display)
        self._grid.borders.draw(self._display)
        self._render_score()

        pygame.display.update()

    def _render_score(self):
        text = self._font.render(self._grid.score.get_score(), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = self._grid.x
        text_rect.y = self._grid.y + (self._grid.cell_size * self._grid.grid_size) + 10
        self._display.blit(text, text_rect)
