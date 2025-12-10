import random
import pygame
from spirtes.cell import Cell
from spirtes.tile import Tile
from spirtes.border import Border
from score import Score
from enums import Status, Direction

class Grid:
    """class that handles the playing grid"""
    def __init__(self, grid_size: int, cell_size: int, position: tuple, timed = False):
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
        self.timed = timed

        self.tiles = pygame.sprite.Group()
        self.cells = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialise_grid(self.grid_size)

    def _initialise_grid(self, grid_size):
        """Generates the initial grid adding 2 starting tiles

        Args:
            grid_size (int): what size is the grid ex. 4 = 4 x 4
        """
        for y in range(grid_size):
            for x in range(grid_size):
                normalised_x = x * self.cell_size + self.x
                normalised_y = y * self.cell_size + self.y
                self.cells.add(Cell(size=self.cell_size, x=normalised_x, y=normalised_y))

        thickness = self.cell_size // 20
        length = self.cell_size * self.grid_size + thickness
        offset = self.cell_size * self.grid_size

        self.borders.add(Border(length, thickness, self.x, self.y-thickness))
        self.borders.add(Border(length, thickness, self.x-thickness, self.y+offset))
        self.borders.add(Border(thickness, length, self.x-thickness, self.y-thickness))
        self.borders.add(Border(thickness, length, self.x+offset, self.y))

        self._spawn_tile()
        self._spawn_tile()

        self.all_sprites.add(self.tiles, self.cells, self.borders)

    def _spawn_tile(self):
        """Function to spawn a tile of a weighted random value to a random empty cell on the grid"""
        value = random.choice([2, 2, 2, 4])
        # Pick a cell that hasn't got a tile on it by random
        spawn_cell = random.choice([cell for cell in self.cells.sprites() if not cell.tile])
        new_tile = Tile(size=self.cell_size, value=value, x=spawn_cell.rect.x, y=spawn_cell.rect.y)
        spawn_cell.tile = True
        self.tiles.add(new_tile)
        self.all_sprites.add(new_tile)

    def update(self):
        """Updates tiles"""
        self.tiles.update()

    def move_down(self):
        """Function that moves all the tiles down on the grid and spawns a new tile
        if any were moved"""
        counter = 0
        move_loop = True
        while move_loop:
            movable_tiles = self._get_movable_tiles(Direction.DOWN)
            # Sort tiles to check BOTTOM row first to make sure tiles move and combine correctly
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.y, reverse=True)
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                tile.rect.move_ip(0, self.cell_size)
                counter += 1
                self._combine_tiles(tile)

        self._update_cell_tiles()
        if counter > 0:
            self._spawn_tile()
        self._unlock_all_tiles()

    def move_up(self):
        """Function that moves all the tiles up on the grid and spawns a new tile
        if any were moved"""
        counter = 0
        move_loop = True
        while move_loop:
            movable_tiles = self._get_movable_tiles(Direction.UP)
            # Sort tiles to check TOP row first to make sure tiles move and combine correctly
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.y)
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                tile.rect.move_ip(0, -self.cell_size)
                counter += 1
                self._combine_tiles(tile)

        self._update_cell_tiles()
        if counter > 0:
            self._spawn_tile()
        self._unlock_all_tiles()

    def move_left(self):
        """Function that moves all the tiles left on the grid and spawns a new tile
        if any were moved"""
        counter = 0
        move_loop = True
        while move_loop:
            movable_tiles = self._get_movable_tiles(Direction.LEFT)
            # Sort tiles to check LEFT column first to make sure tiles move and combine correctly
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.x)
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                tile.rect.move_ip(-self.cell_size, 0)
                counter += 1
                self._combine_tiles(tile)

        self._update_cell_tiles()
        if counter > 0:
            self._spawn_tile()
        self._unlock_all_tiles()

    def move_right(self):
        """Function that moves all the tiles right on the grid and spawns a new tile
        if any were moved"""
        counter = 0
        move_loop = True
        while move_loop:
            movable_tiles = self._get_movable_tiles(Direction.RIGHT)
            # Sort tiles to check RIGHT column first to make sure tiles move and combine correctly
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.x, reverse=True)
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                tile.rect.move_ip(self.cell_size, 0)
                counter += 1
                self._combine_tiles(tile)

        self._update_cell_tiles()
        if counter > 0:
            self._spawn_tile()
        self._unlock_all_tiles()

    def _get_movable_tiles(self, direction):
        """Get all the tiles that can move in specified direction

        Args:
            direction (Direction): direction which the ability to move to is checked

        Returns:
            list: list of tiles that can be moved to specified direction
        """
        move_test_value = 10
        movables = []

        for tile in self.tiles:

            if direction is Direction.DOWN:
                tile.rect.move_ip(0, move_test_value)
                if not self._collisions(tile):
                    movables.append(tile)
                tile.rect.move_ip(0, -move_test_value)

            elif direction is Direction.UP:
                tile.rect.move_ip(0, -move_test_value)
                if not self._collisions(tile):
                    movables.append(tile)
                tile.rect.move_ip(0, move_test_value)

            elif direction is Direction.LEFT:
                tile.rect.move_ip(-move_test_value, 0)
                if not self._collisions(tile):
                    movables.append(tile)
                tile.rect.move_ip(move_test_value, 0)

            elif direction is Direction.RIGHT:
                tile.rect.move_ip(move_test_value, 0)
                if not self._collisions(tile):
                    movables.append(tile)
                tile.rect.move_ip(-move_test_value, 0)

        return movables

    def _collisions(self, tile):
        """Check if tile collides with other tiles or borders, the function ignores
            collision between unlocked tiles of same value to make them
            stack and be combined later

        Args:
            tile (Tile): tile that is tested

        Returns:
            bool: True if there were collisions
        """
        border_collisions = pygame.sprite.spritecollide(tile, self.borders, False)
        test_tiles = pygame.sprite.Group([t for t in self.tiles if t != tile])
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

        test_tiles = pygame.sprite.Group([t for t in self.tiles if t != tile])
        tile_collisions = pygame.sprite.spritecollide(tile, test_tiles, True)

        if tile_collisions:
            new_tile = Tile(self.cell_size, tile.value*2, tile.rect.x, tile.rect.y)
            self.score.add_score(tile.value*2)
            new_tile.lock = True

            self.tiles.add(new_tile)
            self.all_sprites.add(new_tile)
            tile.kill()

    def _update_cell_tiles(self):
        """Checks every cell for tiles"""
        for cell in self.cells:
            tile_on_cell = pygame.sprite.spritecollide(cell, self.tiles, False)
            if tile_on_cell:
                cell.tile = True
            else:
                cell.tile = False

    def _unlock_all_tiles(self):
        """unlocks all tiles so they can combine again"""
        for tile in self.tiles:
            tile.lock = False

    def get_game_state(self):
        """get state if game is still going or over

        Returns:
            Status: returns game over status if game is over None otherwise
        """
        if self.timed and self._tile_on_grid(64):
            return Status.TIMED_OVER
        if len([cell for cell in self.cells.sprites() if not cell.tile]) == 0:
            return Status.OVER
        return None

    def _tile_on_grid(self, value):
        """check if a tile of specified value is on the grid

        Args:
            value (int): the target value

        Returns:
            bool: True if a tile of desired value is on the grid
        """
        for tile in self.tiles:
            if tile.value == value:
                return True
        return False
