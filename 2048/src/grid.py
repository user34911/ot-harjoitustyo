import pygame
import random
from spirtes.cell import Cell
from spirtes.tile import Tile
from spirtes.border import Border
from direction import Direction

class Grid:
    def __init__(self, grid_size: int, cell_size: int, position: tuple):
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.x = position[0]
        self.y = position[1]

        self.tiles = pygame.sprite.Group()
        self.cells = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialise_grid(self.grid_size)

    def _initialise_grid(self, grid_size):
        # Initialise playing grid tiles are on
        for y in range(grid_size):
            for x in range(grid_size):
                normalised_x = x * self.cell_size + self.x
                normalised_y = y * self.cell_size + self.y
                self.cells.add(Cell(size=self.cell_size, x=normalised_x, y=normalised_y))

        # Init help variables
        border_thickness = self.cell_size // 20
        border_length = self.cell_size * self.grid_size + border_thickness
        border_offset = self.cell_size * self.grid_size
        # Top border
        self.borders.add(Border(width=border_length, height=border_thickness, x=self.x, y=self.y-border_thickness))
        # Bottom border
        self.borders.add(Border(width=border_length, height=border_thickness, x=self.x-border_thickness, y=self.y+border_offset))
        # Left border
        self.borders.add(Border(width=border_thickness, height=border_length, x=self.x-border_thickness, y=self.y-border_thickness))
        # Right border
        self.borders.add(Border(width=border_thickness, height=border_length, x=self.x+border_offset, y=self.y))

        # Get 2 random cells and spawn a tile on them
        self._spawn_tile()
        self._spawn_tile()
        self._spawn_tile()
        self._spawn_tile()
        self._spawn_tile()

        self.all_sprites.add(self.tiles, self.cells, self.borders)

    def _spawn_tile(self):
        value = random.choice([2, 2, 2, 4])
        spawn_cell = random.choice([cell for cell in self.cells.sprites() if not cell.tile])
        new_tile = Tile(size=self.cell_size, value=value, x=spawn_cell.rect.x, y=spawn_cell.rect.y)
        spawn_cell.tile = True
        self.tiles.add(new_tile)
        self.all_sprites.add(new_tile)

    def update(self):
        self.tiles.update()

    def move_down(self):
        move_loop = True

        while move_loop:
            movable_tiles = self._get_movable_tiles(Direction.DOWN)
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.y, reverse=True)
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                tile.rect.move_ip(0, self.cell_size)
                self._combine_tiles(tile)

        self._update_cell_tiles()
        self._spawn_tile()

    def move_up(self):
        move_loop = True

        while move_loop:
            movable_tiles = self._get_movable_tiles(Direction.UP)
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.y)
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                tile.rect.move_ip(0, -self.cell_size)
                self._combine_tiles(tile)

        self._update_cell_tiles()
        self._spawn_tile()

    def move_left(self):
        move_loop = True

        while move_loop:
            movable_tiles = self._get_movable_tiles(Direction.LEFT)
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.x)
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                tile.rect.move_ip(-self.cell_size, 0)
                self._combine_tiles(tile)

        self._update_cell_tiles()
        self._spawn_tile()

    def move_right(self):
        move_loop = True

        while move_loop:
            movable_tiles = self._get_movable_tiles(Direction.RIGHT)
            movable_tiles = sorted(movable_tiles, key=lambda tile: tile.rect.x, reverse=True)
            if len(movable_tiles) == 0:
                move_loop = False

            for tile in movable_tiles:
                tile.rect.move_ip(self.cell_size, 0)
                self._combine_tiles(tile)

        self._update_cell_tiles()
        self._spawn_tile()

    def _get_movable_tiles(self, direction):
        move_test_value = 10
        movables = []
        for tile in self.tiles:

            if direction is Direction.DOWN:
                tile.rect.move_ip(0, move_test_value)
                if self._collisions(tile):
                    movables.append(tile)
                tile.rect.move_ip(0, -move_test_value)

            elif direction is Direction.UP:
                tile.rect.move_ip(0, -move_test_value)
                if self._collisions(tile):
                    movables.append(tile)
                tile.rect.move_ip(0, move_test_value)

            elif direction is Direction.LEFT:
                tile.rect.move_ip(-move_test_value, 0)
                if self._collisions(tile):
                    movables.append(tile)
                tile.rect.move_ip(move_test_value, 0)

            elif direction is Direction.RIGHT:
                tile.rect.move_ip(move_test_value, 0)
                if self._collisions(tile):
                    movables.append(tile)
                tile.rect.move_ip(-move_test_value, 0)

        return movables

    def _collisions(self, tile):
        border_collisions = pygame.sprite.spritecollide(tile, self.borders, False)
        # Make a test group which doesnt include the tile itself
        test_tiles = pygame.sprite.Group([t for t in self.tiles if t != tile])

        tile_collisions = pygame.sprite.spritecollide(tile, test_tiles, False)
        if tile_collisions:
            corrected_collisions = []
            for collided_tile in tile_collisions:
                if collided_tile.value != tile.value:
                    corrected_collisions.append(tile)

            if len(corrected_collisions) < 1:
                corrected_collisions = None
            tile_collisions = corrected_collisions

        if border_collisions or tile_collisions:
            return False
        return True

    def _combine_tiles(self, tile):
        test_tiles = pygame.sprite.Group([t for t in self.tiles if t != tile])
        tile_collisions = pygame.sprite.spritecollide(tile, test_tiles, True)
        if tile_collisions:
            new_tile = Tile(size=self.cell_size, value=tile.value*2, x=tile.rect.x, y=tile.rect.y)
            self.tiles.add(new_tile)
            self.all_sprites.add(new_tile)
            tile.kill()

    def _update_cell_tiles(self):
        for cell in self.cells:
            tile_on_cell = pygame.sprite.spritecollide(cell, self.tiles, False)
            if tile_on_cell:
                return True
            return False
