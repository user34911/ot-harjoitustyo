import pygame

class GameLoop:
    def __init__(self, grid, renderer, event_queue, clock):
        self._grid = grid
        self._clock = clock
        self._event_queue = event_queue
        self._renderer = renderer

    def start(self):
        while True:
            if self._handle_events() is False:
                break

            self._grid.update()
            self._render()
            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._grid.move_left()
                if event.key == pygame.K_RIGHT:
                    self._grid.move_right()
                if event.key == pygame.K_UP:
                    self._grid.move_up()
                if event.key == pygame.K_DOWN:
                    self._grid.move_down()
            elif event.type == pygame.QUIT:
                return False
        return None

    def _render(self):
        self._renderer.render()
