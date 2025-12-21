import pygame
from pygame_gui import UIManager
from ui.main_menu import MainMenu
from ui.leaderboard import Leaderboards
from ui.start_options import StartOptions
from ui.username import Username
from options import Options
from enums import MenuScreen, Option
from menu_loop import MenuLoop

class Menu:
    """class that manages menu and its loop"""
    def __init__(self, options: Options, renderer):
        """init menu

        Args:
            options (Options): consturcts the menu based on options
            renderer (Renderer): renderer that renders the menu
        """
        self.options = options
        self.renderer = renderer
        self._manager = None
        self._loop = None

    def start(self):
        """create menu and start its loop"""
        self._initialise_menu()
        self._loop.start()

    def _initialise_menu(self):
        """create the menu screens and loop using options"""
        resolution = self.options.get(Option.RESOLUTION)
        theme_path = self.options.get(Option.THEME_PATH)
        self._manager = UIManager(resolution, theme_path)
        main_menu = MainMenu(resolution)
        leaderboards = Leaderboards(resolution)
        start_options = StartOptions(resolution)
        username = Username(resolution)
        screens = {MenuScreen.MAIN_MENU: main_menu,
                   MenuScreen.LEADERBOARDS: leaderboards,
                   MenuScreen.START_OPTIONS: start_options,
                   MenuScreen.USERNAME: username}
        self._set_menu_background()
        self._loop = MenuLoop(screens, self._manager, self.renderer, self.options)

    def _set_menu_background(self):
        """sets background of menu"""
        background = pygame.Surface(self.options.get(Option.RESOLUTION))
        background.fill((214, 189, 159))
        self.renderer.set_menu_background(background)
