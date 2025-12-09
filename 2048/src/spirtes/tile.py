import pygame

TILE_COLOURS = {2: pygame.Color(255, 233, 196),
                4: pygame.Color(255, 220, 161),
                8: pygame.Color(250, 199, 112),
                16: pygame.Color(255, 161, 0),
                32: pygame.Color(207, 132, 58)}

class Tile(pygame.sprite.Sprite):
    """Class that handles the tiles"""
    def __init__(self, size, value, x=0, y=0):
        """Constructor that generates a tile

        Args:
            size (int): size of tile in pixels
            value (int): value of tile used when combining
            x (int, optional): x position of tile. Defaults to 0.
            y (int, optional): y position of tile. Defaults to 0.
        """
        super().__init__()

        self.value = value
        self.font = self._get_font(size)

        self.image = pygame.Surface((size, size))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self._draw_image()

        self.lock = False

    def _draw_image(self):
        """Function that draws the tile on scren"""
        try:
            colour = TILE_COLOURS[self.value]
        except KeyError:
            colour = pygame.Color(137, 96, 204)
        self.image.fill(colour)

        text = self.font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.rect.width//2, self.rect.height//2)
        self.image.blit(text, text_rect)

    def _get_font(self, size):
        """Function to get the font tile value is typed with

        Args:
            size (int): size of the tile which is used to determine a fontsize fitting inside tile

        Returns:
            font: the desired font
        """
        pygame.font.init()
        font = pygame.font.SysFont("Arial", size // 3)
        font.bold = True
        return font
