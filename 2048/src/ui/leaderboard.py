import pygame
from pygame_gui.elements import UIScrollingContainer, UILabel, UIPanel, UIButton
from leaderboard.leaderboard_repository import get_leaderboard
from enums import Leaderboard

class Leaderboards:
    def __init__(self, window_size):
        self._window_size = window_size

        self.container = None
        self.scroll_container = None
        self.panel = None
        self.standard_button = None
        self.timed_button = None

    def recreate(self, manager):
        content = get_leaderboard(Leaderboard.STANDARD)

        panel_height = len(content) * 40 + 100
        panel_min_height = 500

        self.container = UIPanel(pygame.Rect(50, 50, self._window_size[0] - 100, self._window_size[1] - 100),
                                 manager=manager)

        self.scroll_container = UIScrollingContainer(pygame.Rect(0, 0, self._window_size[0] - 103, self._window_size[1] - 170),
                                                       manager=manager,
                                                       container=self.container,
                                                       visible=False,
                                                       should_grow_automatically=True,
                                                       allow_scroll_x=False)

        self.panel = UIPanel(pygame.Rect(0, 0, self._window_size[0] - 100, max(panel_height, panel_min_height)),
            manager=manager,
            container=self.scroll_container)

        entry_width = 100
        entry_height = 40

        button_rect = pygame.Rect(0, 0, 175, 50)
        button_rect.bottomleft = (40, -10)
        self.standard_button = UIButton(relative_rect=button_rect,
                                        text="Standard",
                                        manager=manager,
                                        container=self.container,
                                        anchors={"left": "left",
                                                "bottom": "bottom"})
        
        button_rect.bottomright = (-40, -10)
        self.timed_button = UIButton(relative_rect=button_rect,
                                     text="Timed",
                                     manager=manager,
                                     container=self.container,
                                     anchors={"right": "right",
                                              "bottom": "bottom"})

        UILabel(
            relative_rect=pygame.Rect(140, 0, entry_width, entry_height),
            text="Player",
            manager=manager,
            container=self.panel)

        UILabel(
            relative_rect=pygame.Rect(240, 0, entry_width, entry_height),
            text="Score",
            manager=manager,
            container=self.panel) 

        for i in range(len(content)):
            UILabel(
                relative_rect=pygame.Rect(100, 40 + i * entry_height, 40, entry_height),
                text=f"{i+1}",
                manager=manager,
                container=self.panel)

            UILabel(
                relative_rect=pygame.Rect(140, 40 + i * entry_height, entry_width, entry_height),
                text=f"{content[i][0]}",
                manager=manager,
                container=self.panel)

            UILabel(
                relative_rect=pygame.Rect(240, 40 + i * entry_height, entry_width, entry_height),
                text=f"{content[i][1]}",
                manager=manager,
                container=self.panel)

        self.container.hide()
