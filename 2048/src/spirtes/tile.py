import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x=0, y=0, colour="orange"):
        super().__init__()

        self.image = pygame.Surface((size, size))
        self.image.fill(colour)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y