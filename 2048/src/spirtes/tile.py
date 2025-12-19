import pygame

TILE_COLOURS = {2: pygame.Color(236, 228, 219),
                4: pygame.Color(235, 227, 207),
                8: pygame.Color(233, 179, 131),
                16: pygame.Color(233, 155, 115),
                32: pygame.Color(231, 132, 111),
                64: pygame.Color(230, 109, 84),
                128: pygame.Color(234, 214, 153),
                256: pygame.Color(233, 213, 142),
                512: pygame.Color(240, 213, 113),
                1024: pygame.Color(232, 207, 122),
                2048: pygame.Color(229, 198, 67),
                "other": pygame.Color(59, 57, 51)}

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
            colour = TILE_COLOURS["other"]
        self.image.fill(colour)

        text_colour = self._get_text_color(self.value)
        text = self.font.render(str(self.value), True, text_colour)
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

    def _get_text_color(self, value):
        if value < 8:
            return pygame.Color(0, 0, 0)
        return pygame.Color(255, 255, 255)
