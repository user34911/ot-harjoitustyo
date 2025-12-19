import pygame
from pygame_gui.elements import UIButton

class MainMenu:
    def __init__(self, window_size):
        self.window_size = window_size

        self.start_button = None
        self.exit_button = None
        self.leaderboard_button = None
        self.username_button = None
    
    def recreate(self, manager):
        button_width = 300
        button_height = 100

        self.start_button = UIButton(pygame.Rect((int(self.window_size[0] // 2) - button_width // 2,
                                                (int(self.window_size[1] // 2) - button_height // 2) - button_height - 50),
                                                (button_width, button_height),),
                                    "Start",
                                    manager,
                                    object_id='#start_button')

        self.leaderboard_button = UIButton(pygame.Rect((int(self.window_size[0] // 2) - button_width // 2,
                                                (int(self.window_size[1] // 2) - button_height // 2)),
                                                (button_width, button_height),),
                                    "Leaderboards",
                                    manager,
                                    object_id='#lb_button')

        self.exit_button = UIButton(pygame.Rect((int(self.window_size[0] // 2) - button_width // 2,
                                                 (int(self.window_size[1] // 2) - button_height // 2) + button_height + 50),
                                                (button_width, button_height),),
                                    "Exit",
                                    manager,
                                    object_id='#exit_button')

        button_height = 50
        self.username_button = UIButton(pygame.Rect((int(self.window_size[0] // 2) - button_width // 2,
                                                 int(self.window_size[1]) - button_height),
                                                (button_width, button_height),),
                                    "Change Username",
                                    manager,
                                    object_id='#username_button')
