import pygame
from enums import State, Direction, Mode, Game, Option
from leaderboard.leaderboard_repository import add_to_leaderboard
from options import Options
from grid import Grid

class GameLoop:
    """Class that handles the game loop"""
    def __init__(self, grid: Grid, renderer, options: Options, event_queue, clock):
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
            if self._handle_events() is not True:
                return None

            self._grid.update()
            self._render()
            self._clock.tick(60)

            game_state = self._grid.get_game_state()
            if game_state is not Game.ONGOING:
                return self._game_over(game_state)

    def _game_over(self, final_state):
        mode = self._grid.get_game_mode()
        if final_state is Game.WON and mode is Mode.TIMED:
            self._submit_to_leaderboards(mode)
        elif mode is Mode.STANDARD:
            self._submit_to_leaderboards(mode)

        self._renderer.render_game_over()
        return self._game_over_loop()

    def _game_over_loop(self):
        while True:
            if self._handle_events() is not True:
                return
            self._clock.tick(60)

    def _submit_to_leaderboards(self, mode):
        player = "guest"
        if mode is Mode.STANDARD:
            add_to_leaderboard([player, self._grid.score.get_score()], Mode.STANDARD)
        else:
            add_to_leaderboard([player, self._grid.timer.get_time()], Mode.TIMED)

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
                    return self._options.change(Option.STATE, State.MENU)

            elif event.type == pygame.QUIT:
                return self._options.change(Option.STATE, State.EXIT)
        return True

    def _render(self):
        self._renderer.render_grid()
