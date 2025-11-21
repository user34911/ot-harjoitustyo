import unittest
from spirtes.cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell = Cell(size=50, x=54, y=93)

    def test_cell_is_constructed_in_the_right_place(self):
        self.assertEqual((self.cell.rect.x, self.cell.rect.y), (54, 93))

    def test_cell_is_constructed_with_correct_tile_status(self):
        self.assertFalse(self.cell.tile)
