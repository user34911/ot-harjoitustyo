import pygame
from pygame_gui import UIManager
from ui.main_menu import MainMenu
from ui.leaderboard import Leaderboards
from ui.start_options import StartOptions
from options import Options
from enums import MenuScreen, Option
from menu_loop import MenuLoop

class Menu:
    def __init__(self, options: Options, renderer):
        self.options = options
        self.renderer = renderer
        self._manager = None
        self._loop = None

    def start(self):
        self._initialise_menu()
        self._loop.start()

    def _initialise_menu(self):
        resolution = self.options.get(Option.RESOLUTION)
        theme_path = self.options.get(Option.THEME_PATH)
        self._manager = UIManager(resolution, theme_path)
        main_menu = MainMenu(resolution)
        leaderboards = Leaderboards(resolution)
        start_options = StartOptions(resolution)
        screens = {MenuScreen.MAIN_MENU: main_menu,
                   MenuScreen.LEADERBOARDS: leaderboards,
                   MenuScreen.START_OPTIONS: start_options}
        self._set_menu_background()
        self._loop = MenuLoop(screens, self._manager, self.renderer, self.options)

    def _set_menu_background(self):
        background = pygame.Surface(self.options.get(Option.RESOLUTION))
        background.fill((214, 189, 159))
        self.renderer.set_menu_background(background)
