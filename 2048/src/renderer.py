import pygame
from enums import Object
from grid import Grid

class Renderer:
    def __init__(self, display):
        self._display = display
        self._grid = None
        self._menu_background = None

        pygame.font.init()
        self._font = pygame.font.SysFont("Arial", 30)
        self._font.bold = True

    def set_grid(self, grid: Grid):
        self._grid = grid

    def set_menu_background(self, background):
        self._menu_background = background

    def render_grid(self):
        self._display.fill((214, 189, 159))
        self._grid.objects[Object.TILE].draw(self._display)
        self._grid.objects[Object.CELL].draw(self._display)
        self._grid.objects[Object.BORDER].draw(self._display)
        self._render_score()
        self._render_timer()

        pygame.display.update()

    def _render_timer(self):
        text = self._font.render(str(self._grid.timer.get_time()), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = self._grid.x
        text_rect.y = self._grid.y + (self._grid.cell_size * 4) + 50
        self._display.blit(text, text_rect)

    def _render_score(self):
        text = self._font.render(self._grid.score.get_score(), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = self._grid.x
        text_rect.y = self._grid.y + (self._grid.cell_size * 4) + 10
        self._display.blit(text, text_rect)

    def render_game_over(self):
        font = pygame.font.SysFont("Arial", 100)
        text = font.render("GAME OVER", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = self._display.width // 2 - text_rect.width // 2
        text_rect.y = -10
        self._display.blit(text, text_rect)
        pygame.display.update()

    def render_menu(self, manager):
        self._display.blit(self._menu_background, (0, 0))
        manager.draw_ui(self._display)

        pygame.display.update()
