import pygame
from enums import Status, Direction, Leaderboard
from leaderboard.leaderboard_repository import add_to_leaderboard
from options import Options

class GameLoop:
    """Class that handles the game loop"""
    def __init__(self, grid, renderer, options: Options, event_queue, clock):
        """Constructor

        Args:
            grid (Grid): the grid object that handles game logic
            renderer (Renderer): responsible for drawing the game on screen
            event_queue (EventQueue): module that checks user inputs
            clock (Clock): module to update screen in set intervals
        """
        self._grid = grid
        self._clock = clock
        self._event_queue = event_queue
        self._renderer = renderer
        self._options = options

    def start(self):
        """Function to start the game loop

        Returns:
            Status: which state the game should go to next
        """
        self._grid.timer.start()
        while True:
            status = self._handle_events()
            if status is not True:
                return None

            self._grid.update()
            self._render()
            self._clock.tick(60)

            game_state = self._grid.get_game_state()

            if game_state is Status.OVER:
                player = "guest"
                score = self._grid.score.get_score()
                add_to_leaderboard([player, score], Leaderboard.STANDARD)
                return self.game_over()

            if game_state is Status.TIMED_OVER:
                player = "guest"
                add_to_leaderboard([player, self._grid.timer.get_time()], Leaderboard.TIMED)
                return self.game_over()

    def game_over(self):
        """Stops the game from being played showing the user the final alignmnet
            of tiles and their score / time

        Returns:
            Status: which state the game should go to next
        """
        self._renderer.render_game_over()
        while True:
            status = self._handle_events()
            if status is not True:
                return
            self._clock.tick(60)

    def _handle_events(self):
        """Checks user inputs and makes game perform actions accordingly

        Returns:
            Status: which status should the game go to next or None if game continues
        """
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    self._grid.move(Direction.LEFT)
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    self._grid.move(Direction.RIGHT)
                if event.key in (pygame.K_UP, pygame.K_w):
                    self._grid.move(Direction.UP)
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    self._grid.move(Direction.DOWN)

                if event.key == pygame.K_ESCAPE:
                    return self._options.set_state(Status.MENU)

            elif event.type == pygame.QUIT:
                return self._options.set_state(Status.EXIT)
        return True

    def _render(self):
        self._renderer.render_grid()
