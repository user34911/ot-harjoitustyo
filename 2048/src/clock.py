import pygame

class Clock:
    """clock to allow injecting dependencies"""
    def __init__(self):
        """init clock"""
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """tick the clock"""
        self._clock.tick(fps)

    def get_ticks(self):
        """get the ticks of the clock"""
        return pygame.time.get_ticks()
