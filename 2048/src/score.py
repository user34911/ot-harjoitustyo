import math

class Score:
    """class that keeps track of game score"""
    def __init__(self):
        """score is 0 when created"""
        self.score = 0

    def add_score(self, value: int):
        """adds correct amount of score depending on tile value

        Args:
            value (int): value of new tile
        """
        n = int(math.log2(value))
        self.score += (n - 1) * (2 ** n)

    def get_score(self):
        """returns score as string

        Returns:
            str: current score
        """
        return str(self.score)
