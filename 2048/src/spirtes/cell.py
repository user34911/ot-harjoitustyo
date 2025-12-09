import pygame

class Cell(pygame.sprite.Sprite):
    """Class that handles information about cells of playing grid"""
    def __init__(self, size=50, x=0, y=0):
        """Constructor that generates a cell

        Args:
            size (int, optional): size of cell in pixels. Defaults to 50.
            x (int, optional): x position of cell. Defaults to 0.
            y (int, optional): y position of cell. Defaults to 0.
        """
        super().__init__()

        self.cell_colour = pygame.Color(255, 243, 209)
        self.border_colour = pygame.Color(128, 100, 73)

        self.image = pygame.Surface((size, size))
        self.image.fill(self.cell_colour)
        self.image.set_colorkey(self.cell_colour)

        self.rect = self.image.get_rect()
        self.border_width = size // 20
        pygame.draw.rect(self.image, self.border_colour, self.rect, width=self.border_width)

        self.rect.x = x
        self.rect.y = y

        self.tile = False
