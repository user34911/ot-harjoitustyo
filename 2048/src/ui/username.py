import pygame
from pygame_gui.elements import UITextEntryLine, UIPanel, UILabel
from repository.config_repository import get_user

class Username:
    def __init__(self, window_size):
        self.window_size = window_size
        self.container = None
        self.input_box = None

    def recreate(self, manager):
        self.container = UIPanel(pygame.Rect(0, 0, self.window_size[0], self.window_size[1]),
                                 manager=manager,
                                 visible=True,
                                 object_id="username_container")


        input_box_rect = pygame.Rect(self.window_size[0] // 2 - 150, self.window_size[1] // 2 - 25, 300, 50)
        username = get_user()
        self.input_box = UITextEntryLine(relative_rect=input_box_rect,
                                         initial_text=f"{username}",
                                          manager=manager,
                                          container=self.container)

        label_rect = pygame.Rect(self.window_size[0] // 2 - 150, self.window_size[1] // 2 - 150, 300, 100)
        UILabel(relative_rect=label_rect,
                text="Change Username",
                manager=manager,
                container=self.container,
                object_id="change_username_text")

        self.container.hide()
