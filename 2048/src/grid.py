import random
import pygame
from spirtes.cell import Cell
from spirtes.tile import Tile
from spirtes.border import Border
from score import Score
from game_timer import Timer
from enums import Direction, Object, Mode, Game

class Grid:
    """class that handles the playing grid"""
    def __init__(self, grid_size: int, cell_size: int, position: tuple, mode = Mode.STANDARD):
        """Constructor that generates the grid and starts the game

        Args:
            grid_size (int): what size is the grid ex. 4 = 4 x 4
            cell_size (int): size of a single cell in pixels
            position (tuple): top left position of the top left cell, 
                                borders are drawn left and above of this value
            timed (bool, optional): is the game timed or not. Defaults to False.
        """
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.x = position[0]
        self.y = position[1]
        self.score = Score()
        self._mode = mode
        self.timer = Timer()

        self.objects = {object_type: pygame.sprite.Group() for object_type in Object}

        self._initialise_grid(grid_size)

    def _initialise_grid(self, grid_size):
        """Generates the initial grid adding 2 starting tiles

        Args:
            grid_size (int): what size is the grid ex. 4 = 4 x 4
        """
        for y in range(grid_size):
            for x in range(grid_size):
                normalised_x = x * self.cell_size + self.x
                normalised_y = y * self.cell_size + self.y
                cell = Cell(size=self.cell_size, x=normalised_x, y=normalised_y)
                self.objects[Object.CELL].add(cell)

        width = self.cell_size // 20
        length = self.cell_size * grid_size + width
        offset = self.cell_size * grid_size

        self.objects[Object.BORDER].add(Border(length, width, self.x, self.y - width))
        self.objects[Object.BORDER].add(Border(length, width, self.x - width, self.y + offset))
        self.objects[Object.BORDER].add(Border(width, length, self.x - width, self.y - width))
        self.objects[Object.BORDER].add(Border(width, length, self.x + offset, self.y))

        self._spawn_tile()
        self._spawn_tile()

    def _spawn_tile(self):
        """Function to spawn a tile of a weighted random value to a random empty cell on the grid"""
        value = random.choice([2, 2, 2, 4])
        # Pick a cell that hasn't got a tile on it by random
        available = [cell for cell in self.objects[Object.CELL].sprites() if not cell.tile]
        spawn_cell = random.choice(available)
        new_tile = Tile(size=self.cell_size, value=value, x=spawn_cell.rect.x, y=spawn_cell.rect.y)
        spawn_cell.tile = new_tile
        self.objects[Object.TILE].add(new_tile)

    def update(self):
        """Updates tiles"""
        self.objects[Object.TILE].update()

    def move(self, direction: Direction):
        """Function that moves tiles in desired direction

        Args:
            direction (Direction): which direction to move tiles
        """
        counter = 0
        while True:
            movable_tiles = self._get_movable_tiles(direction)
            movable_tiles = self._sort_movable_tiles(movable_tiles, direction)
            if len(movable_tiles) == 0:
                break

            for tile in movable_tiles:
                self._move_tile(tile, direction, self.cell_size)
                self._combine_tiles(tile)
                counter += 1

        self._update_cell_tiles()
        if counter > 0:
            self._spawn_tile()
        self._unlock_all_tiles()

    def _move_tile(self, tile, direction, amount: int):
        if direction is Direction.DOWN:
            tile.rect.move_ip(0, amount)
        if direction is Direction.UP:
            tile.rect.move_ip(0, -amount)
        if direction is Direction.LEFT:
            tile.rect.move_ip(-amount, 0)
        if direction is Direction.RIGHT:
            tile.rect.move_ip(amount, 0)

    def _get_movable_tiles(self, direction: Direction):
        """Function that gets all tiles that are movable in specified direction

        Args:
            direction (Direction): Direction to check

        Returns:
            list: every movable tile
        """

        opposite = {Direction.DOWN: Direction.UP,
                     Direction.UP: Direction.DOWN,
                     Direction.LEFT: Direction.RIGHT,
                     Direction.RIGHT: Direction.LEFT}

        test_move_value = 10
        movables = []

        for tile in self.objects[Object.TILE]:
            self._move_tile(tile, direction, test_move_value)
            if not self._collisions(tile):
                movables.append(tile)
            self._move_tile(tile, opposite[direction], test_move_value)

        return movables

    def _sort_movable_tiles(self, tiles: list, direction: Direction):
        """Sorts movable tiles so game can move them in the right order

        Args:
            tiles (list): list of tiles to be sorted
            direction (Direction): what direction are tiles sorted by

        Returns:
            list: sorted list
        """
        if direction is Direction.DOWN:
            return sorted(tiles, key=lambda tile: tile.rect.y, reverse=True)
        if direction is Direction.UP:
            return sorted(tiles, key=lambda tile: tile.rect.y)
        if direction is Direction.LEFT:
            return sorted(tiles, key=lambda tile: tile.rect.x)
        return sorted(tiles, key=lambda tile: tile.rect.x, reverse=True)

    def _collisions(self, tile):
        """Check if tile collides with other tiles or borders, the function ignores
            collision between unlocked tiles of same value to make them
            stack and be combined later

        Args:
            tile (Tile): tile that is tested

        Returns:
            bool: True if there were collisions
        """
        border_collisions = pygame.sprite.spritecollide(tile, self.objects[Object.BORDER], False)
        test_tiles = pygame.sprite.Group([t for t in self.objects[Object.TILE] if t != tile])
        tile_collisions = pygame.sprite.spritecollide(tile, test_tiles, False)

        if tile_collisions:
            corrected_collisions = []
            for collided_tile in tile_collisions:
                # If tile collides with a tile of different value count it as a collision
                if collided_tile.value != tile.value:
                    corrected_collisions.append(tile)

                # If either of tiles is locked count it as a collision
                elif collided_tile.lock is True or tile.lock is True:
                    corrected_collisions.append(tile)

            # If there were no collisions after correction set list to None
            if len(corrected_collisions) < 1:
                corrected_collisions = None
            tile_collisions = corrected_collisions

        if border_collisions or tile_collisions:
            return True
        return False

    def _combine_tiles(self, tile):
        """Combines tiles of the same value

        Args:
            tile (Tile): tile that is checked
        """
        if tile.lock is True:
            return

        test_tiles = pygame.sprite.Group([t for t in self.objects[Object.TILE] if t != tile])
        tile_collisions = pygame.sprite.spritecollide(tile, test_tiles, True)

        if tile_collisions:
            new_tile = Tile(self.cell_size, tile.value*2, tile.rect.x, tile.rect.y)
            self.score.add_score(tile.value*2)
            new_tile.lock = True

            self.objects[Object.TILE].add(new_tile)
            tile.kill()

    def _update_cell_tiles(self):
        """Checks every cell for tiles"""
        for cell in self.objects[Object.CELL]:
            tiles_on_cell = pygame.sprite.spritecollide(cell, self.objects[Object.TILE], False)
            if tiles_on_cell:
                cell.tile = tiles_on_cell[0]
            else:
                cell.tile = None

    def _unlock_all_tiles(self):
        """unlocks all tiles so they can combine again"""
        for tile in self.objects[Object.TILE]:
            tile.lock = False

    def get_game_state(self):
        """get state if game is still going or over

        Returns:
            Status: returns game over status if game is over None otherwise
        """
        if self._mode is Mode.TIMED and self._tile_on_grid(2048):
            self.timer.stop()
            return Game.WON

        if self._any_empty_cells() or self._any_movable_tiles():
            return Game.ONGOING

        self.timer.stop()
        return Game.LOST

    def get_game_mode(self):
        return self._mode

    def _tile_on_grid(self, value):
        """check if a tile of specified value is on the grid

        Args:
            value (int): the target value

        Returns:
            bool: True if a tile of desired value is on the grid
        """
        for tile in self.objects[Object.TILE]:
            if tile.value == value:
                return True
        return False

    def _any_movable_tiles(self):
        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        for direction in directions:
            if len(self._get_movable_tiles(direction)) != 0:
                return True
        return False

    def _any_empty_cells(self):
        empty_cells = [cell for cell in self.objects[Object.CELL].sprites() if not cell.tile]
        if len(empty_cells) == 0:
            return False
        return True
