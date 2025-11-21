import unittest
from spirtes.border import Border

class TestBorder(unittest.TestCase):
    def setUp(self):
        self.border = Border(width=20, height=70, x=54, y=93)

    def test_cell_is_constructed_in_the_right_place(self):
        self.assertEqual((self.border.rect.x, self.border.rect.y), (54, 93))
