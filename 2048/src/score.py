import math

class Score:
    def __init__(self):
        self.score = 0

    def add_score(self, value):
        n = int(math.log2(value))
        self.score += (n - 1) * (2 ** n)

    def get_score(self):
        return str(self.score)
