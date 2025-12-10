import pygame
from pygame_gui.elements import UIButton, UILabel, UIPanel
from pygame_gui.elements import UICheckBox, UIDropDownMenu

class StartOptions:
    def __init__(self, window_size):
        self._window_size = window_size

        self.container = None
        self.timed_mode_checkbox = None
        self.start_game_button = None
        self.back_button = None
        self.grid_size_dropdown = None

    def recreate(self, manager):
        self.container = UIPanel(pygame.Rect(50, 50, self._window_size[0] - 100, self._window_size[1] - 100),
                                               manager=manager,
                                               visible=True)
        
        self.timed_mode_checkbox = UICheckBox(
            relative_rect=pygame.Rect(50, 50, 30, 30),
            text="Timed mode",
            manager=manager,
            container=self.container
        )

        button_rect = pygame.Rect(0, 0, 175, 75)
        button_rect.bottomleft = (40, -20)
        self.start_game_button = UIButton(button_rect,
                                          "Start",
                                          manager,
                                          self.container,
                                          anchors={"left": "left",
                                                   "bottom": "bottom"})

        button_rect.bottomright = (-40, -20)
        self.back_button = UIButton(button_rect,
                                    "Back",
                                    manager,
                                    self.container,
                                    anchors={"right": "right",
                                            "bottom": "bottom"})

        UILabel(relative_rect=pygame.Rect(50, 110, 120, 30),
                                  text="Grid Size:",
                                  manager=manager,
                                  container=self.container,
                                  object_id="#start_option_label")

        options = ["4x4"]
        self.grid_size_dropdown = UIDropDownMenu(options_list=options,
                                                 starting_option="4x4",
                                                 relative_rect=pygame.Rect(190, 110, 70, 30),
                                                 manager=manager,
                                                 container=self.container)

        self.container.hide()
