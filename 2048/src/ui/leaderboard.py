import pygame
from pygame_gui.elements import UIScrollingContainer, UILabel, UIPanel, UIButton
from repository.leaderboard_repository import get_leaderboard
from enums import Mode

class Leaderboards:
    """leaderboard window"""
    def __init__(self, window_size):
        """init

        Args:
            window_size (Tuple): size of the window
        """
        self._window_size = window_size

        self.container = None
        self.standard_container = None
        self.timed_container = None
        self.standard_button = None
        self.timed_button = None

    def recreate(self, manager):
        """create the window

        Args:
            manager (UIManager): pygame_gui asset that controls pygame_gui elements
        """
        self.container = UIPanel(pygame.Rect(50, 50, self._window_size[0] - 100, self._window_size[1] - 100),
                                 manager=manager,
                                 visible=True)

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

        self.standard_container = UIScrollingContainer(pygame.Rect(0, 0, self._window_size[0] - 103, self._window_size[1] - 170),
                                                       manager=manager,
                                                       container=self.container,
                                                       visible=False,
                                                       should_grow_automatically=True,
                                                       allow_scroll_x=False)

        content = get_leaderboard(Mode.STANDARD)
        self._recreate_leaderboard(manager, self.standard_container, content)

        self.timed_container = UIScrollingContainer(pygame.Rect(0, 0, self._window_size[0] - 103, self._window_size[1] - 170),
                                                    manager=manager,
                                                    container=self.container,
                                                    visible=False,
                                                    should_grow_automatically=True,
                                                    allow_scroll_x=False)

        content = get_leaderboard(Mode.TIMED)
        self._recreate_leaderboard(manager, self.timed_container, content)

        self.container.hide()

    def _recreate_leaderboard(self, manager, container, content):
        """creates the actual leaderboard entries

        Args:
            manager (UIManager)
            container: container entries go inside
            content (list): leaderboard entries
        """
        entry_width = 100
        entry_height = 40

        UILabel(
            relative_rect=pygame.Rect(140, 0, entry_width, entry_height),
            text="Player",
            manager=manager,
            container=container)

        UILabel(
            relative_rect=pygame.Rect(240, 0, entry_width, entry_height),
            text="Score",
            manager=manager,
            container=container) 

        for i in range(len(content)):
            UILabel(
                relative_rect=pygame.Rect(100, 40 + i * entry_height, 40, entry_height),
                text=f"{i+1}",
                manager=manager,
                container=container)

            UILabel(
                relative_rect=pygame.Rect(140, 40 + i * entry_height, entry_width, entry_height),
                text=f"{content[i][0]}",
                manager=manager,
                container=container)

            UILabel(
                relative_rect=pygame.Rect(240, 40 + i * entry_height, entry_width, entry_height),
                text=f"{content[i][1]}",
                manager=manager,
                container=container)

    def show_standard_leaderboards(self):
        self.timed_container.hide()
        self.standard_container.show()

    def show_timed_leaderboards(self):
        self.standard_container.hide()
        self.timed_container.show()
