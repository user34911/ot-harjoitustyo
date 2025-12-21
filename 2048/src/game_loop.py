import pygame
from enums import State, Direction, Mode, Game, Option
from repository.leaderboard_repository import add_to_leaderboard
from options import Options
from grid import Grid

class GameLoop:
    """Class that handles the game loop"""
    def __init__(self, grid: Grid, renderer, options: Options, event_queue, clock):
        """init GameLoop

        Args:
            grid (Grid): Grid game is played on
            renderer (Renderer): renders the game
            options (Options): options to enable change
            event_queue
            clock
        """
        self._grid = grid
        self._clock = clock
        self._event_queue = event_queue
        self._renderer = renderer
        self._options = options

    def start(self):
        """Function to start the game loop"""
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
        """called when game is over, submits score to leaderboard
        if eligible and starts the game over loop

        Args:
            final_state (Game): was the game won or lost

        Returns:
            starts game over loop
        """
        mode = self._grid.get_game_mode()
        if final_state is Game.WON and mode is Mode.TIMED and self._grid.grid_size == 4:
            self._submit_to_leaderboards(mode)
        elif mode is Mode.STANDARD and self._grid.grid_size == 4:
            self._submit_to_leaderboards(mode)

        self._renderer.render_game_over()
        return self._game_over_loop()

    def _game_over_loop(self):
        """keeps game over text on screen"""
        while True:
            if self._handle_events() is not True:
                return
            self._clock.tick(60)

    def _submit_to_leaderboards(self, mode):
        """fetches username and adds score to right leaderboard"""
        player = self._options.get(Option.USER)
        if mode is Mode.STANDARD:
            add_to_leaderboard([player, self._grid.score.get_score()], Mode.STANDARD)
        else:
            add_to_leaderboard([player, self._grid.timer.get_time()], Mode.TIMED)

    def _handle_events(self):
        """Checks user inputs and makes game perform actions accordingly

        Returns:
            bool: should loop continue
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
        """renders the grid"""
        self._renderer.render_grid()
