import pygame
import pygame_gui
from grid import Grid
from clock import Clock
from event_queue import EventQueue
from renderer import Renderer
from game_loop import GameLoop
from ui.menu_loop import MenuLoop
from ui.menu import Menu
from ui.menu_renderer import MenuRenderer
from options import Options
from status import Status


def main():
    options = Options()
    display = pygame.display.set_mode(options.resolution)
    pygame.display.set_caption("2048")
    pygame.font.init()

    menu = Menu(options.resolution)
    manager = pygame_gui.UIManager(options.resolution, r"src\ui\theme.json")
    menu_renderer = MenuRenderer(display, menu)
    menu_loop = MenuLoop(menu, menu_renderer, manager)

    status = Status.MENU

    pygame.init()
    while True:
        if status is Status.MENU:
            status = menu_loop.start()

        if status is Status.GAME:
            grid = Grid(options.grid_size, options.cell_size, options.position)
            event_queue = EventQueue()
            renderer = Renderer(display, grid)
            clock = Clock()
            game_loop = GameLoop(grid, renderer, event_queue, clock)

            status = game_loop.start()

        if status is Status.EXIT:
            break

if __name__ == "__main__":
    main()
