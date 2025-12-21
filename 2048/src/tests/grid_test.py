import unittest
from grid import Grid
from spirtes.tile import Tile
from enums import Game, Object, Direction, Mode

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.cell_size = 100
        self.grid_size = 4
        self.x = 0
        self.y = 0
        self.grid = Grid(self.grid_size, self.cell_size, (self.x, self.y))

    def _fill_grid(self):
        i = 0
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                normalised_x = x * self.cell_size + self.x
                normalised_y = y * self.cell_size + self.y
                tile = Tile(size=self.cell_size, value=i, x=normalised_x, y=normalised_y)
                self.grid.objects[Object.TILE].add(tile)
                self.grid.objects[Object.CELL].sprites()[i].tile = tile
                i += 1     

    def test_constructor_sets_cell_size_correctly(self):
        self.assertAlmostEqual(self.grid.cell_size, 100)

    def test_constructor_adds_correct_amount_of_cells_to_grid(self):
        self.assertAlmostEqual(len(self.grid.objects[Object.CELL]), 4*4)
    
    def test_constructor_makes_cells_the_right_width(self):
        self.assertAlmostEqual(self.grid.objects[Object.CELL].sprites()[0].rect.width, 100)

    def test_constructor_makes_cells_the_right_height(self):
        self.assertAlmostEqual(self.grid.objects[Object.CELL].sprites()[0].rect.height, 100)
    
    def test_constructors_spawns_grid_with_2_tiles(self):
        self.assertAlmostEqual(len(self.grid.objects[Object.TILE]), 2)
    
    def test_move_down_moves_tiles(self):
        self.grid.objects[Object.TILE].empty()
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 0, 0))
        self.grid.move(Direction.DOWN)
        tile = self.grid.objects[Object.TILE].sprites()[0]
        self.assertEqual((tile.rect.x, tile.rect.y), (0, 300))

    def test_move_up_moves_tiles(self):
        self.grid.objects[Object.TILE].empty()
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 0, 200))
        self.grid.move(Direction.UP)
        tile = self.grid.objects[Object.TILE].sprites()[0]
        self.assertEqual((tile.rect.x, tile.rect.y), (0, 0))

    def test_move_left_moves_tile(self):
        self.grid.objects[Object.TILE].empty()
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 200, 0))
        self.grid.move(Direction.LEFT)
        tile = self.grid.objects[Object.TILE].sprites()[0]
        self.assertEqual((tile.rect.x, tile.rect.y), (0, 0))

    def test_move_right_moves_tile(self):
        self.grid.objects[Object.TILE].empty()
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 100, 0))
        self.grid.move(Direction.RIGHT)
        tile = self.grid.objects[Object.TILE].sprites()[0]
        self.assertEqual((tile.rect.x, tile.rect.y), (300, 0))

    def test_grid_spawns_tile_if_tiles_moved(self):
        self.grid.objects[Object.TILE].empty()
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 0, 0))
        self.assertAlmostEqual(len(self.grid.objects[Object.TILE]), 1)
        self.grid.move(Direction.DOWN)
        self.assertAlmostEqual(len(self.grid.objects[Object.TILE]), 2)

    def test_grid_doesnt_spawn_tiles_if_none_moved(self):
        self.grid.objects[Object.TILE].empty()
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 0, 0))
        self.assertAlmostEqual(len(self.grid.objects[Object.TILE]), 1)
        self.grid.move(Direction.UP)
        self.assertAlmostEqual(len(self.grid.objects[Object.TILE]), 1)

    def test_two_same_value_tiles_combine(self):
        self.grid.objects[Object.TILE].empty()
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 0, 0))
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 200, 0))
        self.grid.move(Direction.LEFT)
        self.assertAlmostEqual(len(self.grid.objects[Object.TILE]), 2)
        self.assertEqual(self.grid.objects[Object.TILE].sprites()[0].value, 4)

    def test_two_different_value_tiles_collide(self):
        self.grid.objects[Object.TILE].empty()
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 0, 0))
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 4, 200, 0))
        self.grid.move(Direction.LEFT)
        tile = self.grid.objects[Object.TILE].sprites()[1]
        self.assertEqual((tile.rect.x, tile.rect.y), (100, 0))

    def test_two_same_value_tiles_dont_combine_if_locked(self):
        self.grid.objects[Object.TILE].empty()
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 0, 0))
        self.grid.objects[Object.TILE].add(Tile(self.cell_size, 2, 200, 0))
        tile = self.grid.objects[Object.TILE].sprites()[1]
        tile.lock = True
        self.grid.move(Direction.LEFT)
        self.assertEqual((tile.rect.x, tile.rect.y), (100, 0))

    def test_game_state_ongoing_if_not_over(self):
        self.assertIs(self.grid.get_game_state(), Game.ONGOING)

    def test_game_state_lost_if_grid_full(self):
        self.grid.objects[Object.TILE].empty()
        self._fill_grid()
        self.assertIs(self.grid.get_game_state(), Game.LOST)

    def test_game_state_won_if_timed_and_2048(self):
        grid = Grid(4, 100, (0, 0), Mode.TIMED)
        grid.objects[Object.TILE].add(Tile(100, 2048, 0, 0))
        self.assertIs(grid.get_game_state(), Game.WON)

    def test_game_state_ongoing_if_standard_and_2048(self):
        self.grid.objects[Object.TILE].add(Tile(100, 2048, 0, 0))
        self.assertIs(self.grid.get_game_state(), Game.ONGOING)

    def test_any_empty_cells_returns_correct(self):
        self.assertTrue(self.grid._any_empty_cells())
        self._fill_grid()
        self.assertFalse(self.grid._any_empty_cells())

    def test_any_movable_tiles_returns_correct(self):
        self.assertTrue(self.grid._any_movable_tiles())
        self._fill_grid()
        self.assertFalse(self.grid._any_movable_tiles())

    def test_tile_on_grid_retursn_correct(self):
        self.assertFalse(self.grid._tile_on_grid(2048))
        self.grid.objects[Object.TILE].add(Tile(100, 2048, 0, 0))
        self.assertTrue(self.grid._tile_on_grid(2048))
