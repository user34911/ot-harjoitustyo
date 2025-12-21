import unittest
from options import Options
from enums import Option, State

class TestGame(unittest.TestCase):
    def setUp(self):
        self.options = Options()

    def test_get_gets_right_option(self):
        option = self.options.get(Option.GRID_SIZE)
        self.assertEqual(option, 4)
        option = self.options.get(Option.STATE)
        self.assertIs(option, State.MENU)

    def test_change_changes_right_option(self):
        old_option = self.options.get(Option.GRID_SIZE)
        self.options.change(Option.GRID_SIZE, 6)
        new_option = self.options.get(Option.GRID_SIZE)
        self.assertNotEqual(new_option, old_option)