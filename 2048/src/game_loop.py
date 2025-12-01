import pygame
from status import Status
from leaderboard.leaderboard import add_score_to_lb
class GameLoop:
    def __init__(self, grid, renderer, event_queue, clock):
        self._grid = grid
        self._clock = clock
        self._event_queue = event_queue
        self._renderer = renderer

    def start(self):
        while True:
            if self._handle_events() is False:
                return Status.EXIT

            if self._grid.get_game_state() is Status.OVER:
                player = "guest"
                score = self._grid.score.get_score()
                add_score_to_lb(player, score)
                return Status.MENU

            self._grid.update()
            self._render()
            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    self._grid.move_left()
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    self._grid.move_right()
                if event.key in (pygame.K_UP, pygame.K_w):
                    self._grid.move_up()
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    self._grid.move_down()

            elif event.type == pygame.QUIT:
                return False
        return None

    def _render(self):
        self._renderer.render()
