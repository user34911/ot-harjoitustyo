import pygame

class EventQueue:
    """alternative eventqueue to inject dependencies"""
    def get(self):
        """gets pygame event"""
        return pygame.event.get()
