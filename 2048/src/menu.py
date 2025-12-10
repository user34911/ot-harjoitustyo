import pygame
from pygame_gui import UIManager
from ui.main_menu import MainMenu
from ui.leaderboard import Leaderboards
from ui.start_options import StartOptions
from options import Option, Options
from enums import MenuScreen
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
        opt = self.options.get_menu_options()
        self._manager = UIManager(opt[Option.RESOLUTION], opt[Option.THEME_PATH])
        main_menu = MainMenu(opt[Option.RESOLUTION])
        leaderboards = Leaderboards(opt[Option.RESOLUTION])
        start_options = StartOptions(opt[Option.RESOLUTION])
        screens = {MenuScreen.MAIN_MENU: main_menu,
                   MenuScreen.LEADERBOARDS: leaderboards,
                   MenuScreen.START_OPTIONS: start_options}
        self._set_menu_background()
        self._loop = MenuLoop(screens, self._manager, self.renderer, self.options)

    def _set_menu_background(self):
        background = pygame.Surface(self.options.get_resolution())
        background.fill((214, 189, 159))
        self.renderer.set_menu_background(background)
