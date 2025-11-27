import random
import pygame
from spirtes.cell import Cell
from spirtes.tile import Tile
from spirtes.border import Border
from direction import Direction
from score import Score
from status import Status

class Grid:
    def __init__(self, grid_size: int, cell_size: int, position: tuple):
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.x = position[0]
        self.y = position[1]
        self.score = Score()

        self.tiles = pygame.sprite.Group()
        self.cells = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialise_grid(self.grid_size)

    def _initialise_grid(self, grid_size):
        # Initialise playing grid tiles are on
        for y in range(grid_size):
            for x in range(grid_size):
                # X pos of cell calulated by x index * size of a cell + starting x
                normalised_x = x * self.cell_size + self.x
                # Y pos of cell calulated by y index * size of a cell + starting y
                normalised_y = y * self.cell_size + self.y
                self.cells.add(Cell(size=self.cell_size, x=normalised_x, y=normalised_y))

        # Init help variables
        thickness = self.cell_size // 20
        length = self.cell_size * self.grid_size + thickness
        offset = self.cell_size * self.grid_size
        # Top border
        self.borders.add(Border(length, thickness, self.x, self.y-thickness))
        # Bottom border
        self.borders.add(Border(length, thickness, self.x-thickness, self.y+offset))
        # Left border
        self.borders.add(Border(thickness, length, self.x-thickness, self.y-thickness))
        # Right border
        self.borders.add(Border(thickness, length, self.x+offset, self.y))

        # Add 2 tiles to grid
        self._spawn_tile()
        self._spawn_tile()

        self.all_sprites.add(self.tiles, self.cells, self.borders)

    def _spawn_tile(self):
        # Pick value for new tile, 75% of picking 2
        value = random.choice([2, 2, 2, 4])
        # Pick a cell that hasn't got a tile on it by random
        spawn_cell = random.choice([cell for cell in self.cells.sprites() if not cell.tile])
        # Make a new tile on picked cell's postion
        new_tile = Tile(size=self.cell_size, value=value, x=spawn_cell.rect.x, y=spawn_cell.rect.y)
        # Set picked cell's status indicating if a cell has a tile on to True
        spawn_cell.tile = True
        # Add new tile to sprite groups
        self.tiles.add(new_tile)
        self.all_sprites.add(new_tile)

    def update(self):
        self.tiles.update()

    def move_down(self):
        # Varibale to keep track of how many tiles were moved
        counter = 0
        # Make a loop that moves tiles down for as long as there are movable tiles
        move_loop = True
        while move_loop:
            # Get list of tiles that can move DOWN
            movable_tiles = self._get_movable_tiles(Direction.DOWN)
            # Sort tiles to check BOTTOM row first to make sure tiles move and combine correctly
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.y, reverse=True)
            # When no movable tiles left break the loop
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                # Move the tile down one cell
                tile.rect.move_ip(0, self.cell_size)
                counter += 1
                # Check if tile can combine
                self._combine_tiles(tile)

        self._update_cell_tiles()
        # Only spawn new tile if tiles were moved
        if counter > 0:
            self._spawn_tile()
        self._unlock_all_tiles()

    def move_up(self):
        # Varibale to keep track of how many tiles were moved
        counter = 0
        # Make a loop that moves tiles up for as long as there are movable tiles
        move_loop = True
        while move_loop:
            # Get list of tiles that can move UP
            movable_tiles = self._get_movable_tiles(Direction.UP)
            # Sort tiles to check TOP row first to make sure tiles move and combine correctly
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.y)
            # When no movable tiles left break the loop
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                # Move the tile up one cell
                tile.rect.move_ip(0, -self.cell_size)
                counter += 1
                # Check if tile can combine
                self._combine_tiles(tile)

        self._update_cell_tiles()
        # Only spawn new tile if tiles were moved
        if counter > 0:
            self._spawn_tile()
        self._unlock_all_tiles()

    def move_left(self):
        # Varibale to keep track of how many tiles were moved
        counter = 0
        # Make a loop that moves tiles left for as long as there are movable tiles
        move_loop = True
        while move_loop:
            # Get list of tiles that can move LEFT
            movable_tiles = self._get_movable_tiles(Direction.LEFT)
            # Sort tiles to check LEFT column first to make sure tiles move and combine correctly
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.x)
            # When no movable tiles left break the loop
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                # Move the tile left one cell
                tile.rect.move_ip(-self.cell_size, 0)
                counter += 1
                # Check if tile can combine
                self._combine_tiles(tile)

        self._update_cell_tiles()
        # Only spawn new tile if tiles were moved
        if counter > 0:
            self._spawn_tile()
        self._unlock_all_tiles()

    def move_right(self):
        # Varibale to keep track of how many tiles were moved
        counter = 0
        # Make a loop that moves tiles right for as long as there are movable tiles
        move_loop = True
        while move_loop:
            # Get list of tiles that can move RIGHT
            movable_tiles = self._get_movable_tiles(Direction.RIGHT)
            # Sort tiles to check RIGHT column first to make sure tiles move and combine correctly
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.x, reverse=True)
            # When no movable tiles left break the loop
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                # Move the tile right one cell
                tile.rect.move_ip(self.cell_size, 0)
                counter += 1
                # Check if tile can combine
                self._combine_tiles(tile)

        self._update_cell_tiles()
        # Only spawn new tile if tiles were moved
        if counter > 0:
            self._spawn_tile()
        self._unlock_all_tiles()

    def _get_movable_tiles(self, direction):
        # How much tile is moved when testing for collisions
        move_test_value = 10
        movables = []

        for tile in self.tiles:

            if direction is Direction.DOWN:
                # Move tile
                tile.rect.move_ip(0, move_test_value)
                # Check for collisions
                if not self._collisions(tile):
                    # If no collisions add tile to movables
                    movables.append(tile)
                # Move tile back to original position
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
        # Check if tile collides with grid borders
        border_collisions = pygame.sprite.spritecollide(tile, self.borders, False)
        # Make a test group which doesnt include the tile itself
        test_tiles = pygame.sprite.Group([t for t in self.tiles if t != tile])
        # Check if tile collides with other tiles
        tile_collisions = pygame.sprite.spritecollide(tile, test_tiles, False)

        if tile_collisions:
            # Make a list for corrected tile collisions
            corrected_collisions = []
            # Iter through tile collisions ignoring tiles that can be combined with
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

        # If tile collided with something return True
        if border_collisions or tile_collisions:
            return True
        return False

    def _combine_tiles(self, tile):
        # If tile is locked do nothing
        if tile.lock is True:
            return
        # Make a test group which doesnt include the tile itself
        test_tiles = pygame.sprite.Group([t for t in self.tiles if t != tile])
        # Collision checker let's tiles that can be combined stack on top of each other
        # Get stacked tile and kill it
        tile_collisions = pygame.sprite.spritecollide(tile, test_tiles, True)
        if tile_collisions:
            # Make a new tile with double value of current tile
            new_tile = Tile(self.cell_size, tile.value*2, tile.rect.x, tile.rect.y)
            self.score.add_score(tile.value*2)
            # Lock new tile so it can't combine on the same move
            new_tile.lock = True
            # Add new tile to sprite groups
            self.tiles.add(new_tile)
            self.all_sprites.add(new_tile)
            # Kill the old tile
            tile.kill()

    def _update_cell_tiles(self):
        # Iter through every cell on grid and check if there's a tile on it
        for cell in self.cells:
            tile_on_cell = pygame.sprite.spritecollide(cell, self.tiles, False)
            if tile_on_cell:
                cell.tile = True
            else:
                cell.tile = False

    def _unlock_all_tiles(self):
        for tile in self.tiles:
            tile.lock = False

    def _get_game_state(self):
        if len([cell for cell in self.cells.sprites() if not cell.tile]) == 0:
            return Status.OVER
