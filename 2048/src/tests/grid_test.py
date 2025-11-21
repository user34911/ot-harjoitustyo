import unittest
from grid import Grid
from spirtes.tile import Tile

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.cell_size = 100
        self.grid_size = 4
        self.x = 0
        self.y = 0
        self.grid = Grid(self.grid_size, self.cell_size, (self.x, self.y))
    
    def test_constructor_sets_cell_size_correctly(self):
        self.assertAlmostEqual(self.grid.cell_size, 100)

    def test_constructor_adds_correct_amount_of_cells_to_grid(self):
        self.assertAlmostEqual(len(self.grid.cells), 4*4)
    
    def test_constructor_makes_cells_the_right_width(self):
        self.assertAlmostEqual(self.grid.cells.sprites()[0].rect.width, 100)

    def test_constructor_makes_cells_the_right_height(self):
        self.assertAlmostEqual(self.grid.cells.sprites()[0].rect.height, 100)
    
    def test_constructors_spawns_grid_with_2_tiles(self):
        self.assertAlmostEqual(len(self.grid.tiles), 2)
    
    def test_move_down_moves_tiles(self):
        self.grid.tiles.empty()
        self.grid.tiles.add(Tile(self.cell_size, 2, 0, 0))
        self.grid.move_down()
        tile = self.grid.tiles.sprites()[0]
        self.assertEqual((tile.rect.x, tile.rect.y), (0, 300))

    def test_move_up_moves_tiles(self):
        self.grid.tiles.empty()
        self.grid.tiles.add(Tile(self.cell_size, 2, 0, 200))
        self.grid.move_up()
        tile = self.grid.tiles.sprites()[0]
        self.assertEqual((tile.rect.x, tile.rect.y), (0, 0))

    def test_move_left_moves_tile(self):
        self.grid.tiles.empty()
        self.grid.tiles.add(Tile(self.cell_size, 2, 200, 0))
        self.grid.move_left()
        tile = self.grid.tiles.sprites()[0]
        self.assertEqual((tile.rect.x, tile.rect.y), (0, 0))

    def test_move_right_moves_tile(self):
        self.grid.tiles.empty()
        self.grid.tiles.add(Tile(self.cell_size, 2, 100, 0))
        self.grid.move_right()
        tile = self.grid.tiles.sprites()[0]
        self.assertEqual((tile.rect.x, tile.rect.y), (300, 0))
