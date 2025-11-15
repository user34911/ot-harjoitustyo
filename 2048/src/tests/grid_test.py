import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(grid_size=4, cell_size=100, position=(50, 50))
    
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
