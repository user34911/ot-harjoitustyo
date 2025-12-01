import pygame
import pygame_gui
from pygame_gui.elements import UIButton
from pygame_gui.elements import UITextBox
from pygame_gui.elements import UIScrollingContainer
from leaderboard.leaderboard import get_leaderboard

class Menu:
    def __init__(self, window_size):
        self.window_size = window_size

        self.background_surface = None
        self.start_button = None
        self.exit_button = None
        self.leaderboard_button = None
        self.leaderboard_container = None
        self.leaderboard_panel = None
    
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
                                                 int(self.window_size[1] - 200)),
                                                (button_width, button_height),),
                                    "Exit",
                                    manager,
                                    object_id='#exit_button')

        self.leaderboard_button = UIButton(pygame.Rect((int(self.window_size[0] / 2) - button_width / 2,
                                                 int(self.window_size[1] - 350)),
                                                (button_width, button_height),),
                                    "Leaderboards",
                                    manager,
                                    object_id='#lb_button')

    def make_leaderboard(self, manager):
        content = get_leaderboard()

        panel_height = len(content) * 40 + 100
        panel_min_height = 500

        self.leaderboard_container = UIScrollingContainer(pygame.Rect(50, 50, self.window_size[0] - 100, self.window_size[1] - 100),
                                                       manager=manager,
                                                       visible=False,
                                                       should_grow_automatically=True,
                                                       allow_scroll_x=False)

        self.leaderboard_panel = pygame_gui.elements.UIPanel(pygame.Rect(0, 0, self.window_size[0] - 100, max(panel_height, panel_min_height)),
            manager=manager,
            container=self.leaderboard_container)

        entry_width = 100
        entry_height = 40

        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(140, 0, entry_width, entry_height),
            text="Player",
            manager=manager,
            container=self.leaderboard_container)

        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(240, 0, entry_width, entry_height),
            text="Score",
            manager=manager,
            container=self.leaderboard_container) 

        for i in range(len(content)):
            pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect(100, 40 + i * entry_height, 40, entry_height),
                text=f"{i+1}",
                manager=manager,
                container=self.leaderboard_container)

            pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect(140, 40 + i * entry_height, entry_width, entry_height),
                text=f"{content[i][0]}",
                manager=manager,
                container=self.leaderboard_container)

            pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect(240, 40 + i * entry_height, entry_width, entry_height),
                text=f"{content[i][1]}",
                manager=manager,
                container=self.leaderboard_container)
