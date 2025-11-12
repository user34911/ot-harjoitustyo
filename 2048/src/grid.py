import pygame
import random
from spirtes.cell import Cell
from spirtes.tile import Tile

class Grid:
    def __init__(self, grid_size, cell_size):
        self.cell_size = cell_size

        self.tiles = pygame.sprite.Group()
        self.cells = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialise_grid(grid_size)

    def _initialise_grid(self, grid_size):

        # Initialise playing grid tiles are on
        for y in range(grid_size):
            for x in range(grid_size):
                normalised_x = x * self.cell_size + x * 10
                normalised_y = y * self.cell_size + y * 10
                colour = random.choice(["green", "blue", "lightpink", "yellow"])
                self.cells.add(Cell(colour=colour, size=self.cell_size, x=normalised_x, y=normalised_y))
        
        # Get 2 random cells and spawn a tile on them
        cells = random.choices(self.cells.sprites(), k=2)
        for cell in cells:
            self.tiles.add(Tile(size=self.cell_size, x=cell.rect.x, y=cell.rect.y))

        self.all_sprites.add(self.cells, self.tiles)