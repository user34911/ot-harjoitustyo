import pygame

class Border(pygame.sprite.Sprite):
    def __init__(self, width, height, x=0, y=0):
        super().__init__()

        self.colour = pygame.Color(138, 138, 138)
        self.image = pygame.Surface((width, height))
        self.image.fill(self.colour)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
