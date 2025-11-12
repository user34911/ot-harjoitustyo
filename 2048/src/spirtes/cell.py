import pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, colour="lightpink", size=50, x=0, y=0):
        super().__init__()

        self.image = pygame.Surface((size, size))
        self.image.fill(colour)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y