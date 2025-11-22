import pygame

TILE_COLOURS = {2: pygame.Color(255, 233, 196),
                4: pygame.Color(255, 220, 161),
                8: pygame.Color(250, 199, 112),
                16: pygame.Color(255, 161, 0),
                32: pygame.Color(207, 132, 58)}

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, value, x=0, y=0):
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
        pygame.font.init()
        font = pygame.font.SysFont("Arial", size // 3)
        font.bold = True
        return font
