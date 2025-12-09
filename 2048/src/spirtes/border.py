import pygame

class Border(pygame.sprite.Sprite):
    """Class that handles the borders of playing grid so tiles
        stay in of bounds"""
    def __init__(self, width, height, x=0, y=0):
        """Constructor that generates a border

        Args:
            width (int): width of the border
            height (int): height of the border
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
        """
        super().__init__()

        self.colour = pygame.Color(128, 100, 73)
        self.image = pygame.Surface((width, height))
        self.image.fill(self.colour)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
