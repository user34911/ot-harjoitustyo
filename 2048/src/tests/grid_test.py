import unittest
from grid import Grid
from spirtes.tile import Tile
from status import Status

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

    def test_grid_spawns_tile_if_tiles_moved(self):
        self.grid.tiles.empty()
        self.grid.tiles.add(Tile(self.cell_size, 2, 0, 0))
        self.assertAlmostEqual(len(self.grid.tiles), 1)
        self.grid.move_down()
        self.assertAlmostEqual(len(self.grid.tiles), 2)

    def test_grid_doesnt_spawn_tiles_if_none_moved(self):
        self.grid.tiles.empty()
        self.grid.tiles.add(Tile(self.cell_size, 2, 0, 0))
        self.assertAlmostEqual(len(self.grid.tiles), 1)
        self.grid.move_up()
        self.assertAlmostEqual(len(self.grid.tiles), 1)

    def test_two_same_value_tiles_combine(self):
        self.grid.tiles.empty()
        self.grid.tiles.add(Tile(self.cell_size, 2, 0, 0))
        self.grid.tiles.add(Tile(self.cell_size, 2, 200, 0))
        self.grid.move_left()
        self.assertAlmostEqual(len(self.grid.tiles), 2)
        self.assertEqual(self.grid.tiles.sprites()[0].value, 4)

    def test_two_different_value_tiles_collide(self):
        self.grid.tiles.empty()
        self.grid.tiles.add(Tile(self.cell_size, 2, 0, 0))
        self.grid.tiles.add(Tile(self.cell_size, 4, 200, 0))
        self.grid.move_left()
        tile = self.grid.tiles.sprites()[1]
        self.assertEqual((tile.rect.x, tile.rect.y), (100, 0))

    def test_two_same_value_tiles_dont_combine_if_locked(self):
        self.grid.tiles.empty()
        self.grid.tiles.add(Tile(self.cell_size, 2, 0, 0))
        self.grid.tiles.add(Tile(self.cell_size, 2, 200, 0))
        tile = self.grid.tiles.sprites()[1]
        tile.lock = True
        self.grid.move_left()
        self.assertEqual((tile.rect.x, tile.rect.y), (100, 0))

    def test_game_status_none_if_not_over(self):
        self.assertIsNone(self.grid.get_game_state())

    def test_game_status_over_if_over(self):
        self.grid.tiles.empty()
        i = 0
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                normalised_x = x * self.cell_size + self.x
                normalised_y = y * self.cell_size + self.y
                self.grid.tiles.add(Tile(size=self.cell_size, value=i, x=normalised_x, y=normalised_y))
                self.grid.cells.sprites()[i].tile = True
                i += 1
        self.assertIs(self.grid.get_game_state(), Status.OVER)
