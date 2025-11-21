import unittest
from spirtes.tile import Tile

class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = Tile(size=50, value=4, x=54, y=93)
    
    def test_tile_is_constructed_the_right_value(self):
        self.assertAlmostEqual(self.tile.value, 4)

    def test_tile_is_constructed_in_the_right_place(self):
        self.assertEqual((self.tile.rect.x, self.tile.rect.y), (54, 93))

    def test_tile_is_constructed_in_right_lock_state(self):
        self.assertFalse(self.tile.lock)
