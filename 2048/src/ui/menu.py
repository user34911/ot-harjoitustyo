import pygame
from pygame_gui.elements import UIButton

class Menu:
    def __init__(self, window_size):
        self.window_size = window_size

        self.background_surface = None
        self.start_button = None
        self.exit_button = None
    
    def recreate_menu(self, manager):
        manager.set_window_resolution(self.window_size)
        manager.clear_and_reset()

        self.background_surface = pygame.Surface(self.window_size)
        self.background_surface.fill((214, 189, 159))

        button_width = 300
        button_height = 100

        self.start_button = UIButton(pygame.Rect((int(self.window_size[0] / 2) - button_width / 2,
                                                 int(self.window_size[1] - 500)),
                                                (button_width, button_height),),
                                    "Start",
                                    manager,
                                    object_id='#start_button')
        self.exit_button = UIButton(pygame.Rect((int(self.window_size[0] / 2) - button_width / 2,
                                                 int(self.window_size[1] - 350)),
                                                (button_width, button_height),),
                                    "Exit",
                                    manager,
                                    object_id='#exit_button')
