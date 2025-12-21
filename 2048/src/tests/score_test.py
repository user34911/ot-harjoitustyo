import unittest
from score import Score

class TestScore(unittest.TestCase):
    def setUp(self):
        self.score = Score()

    def test_score_adds_values_correctly(self):
        self.assertAlmostEqual(self.score.score, 0)
        self.score.add_score(4)
        self.assertAlmostEqual(self.score.score, 4)
        self.score.add_score(16)
        self.assertAlmostEqual(self.score.score, 52)

    def test_get_score_returns_score_as_string(self):
        self.score.add_score(16)
        self.assertEqual(str(self.score.score), self.score.get_score())
