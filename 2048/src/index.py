import pygame
from grid import Grid
from clock import Clock
from event_queue import EventQueue
from renderer import Renderer
from game_loop import GameLoop
from ui.menu_loop import MenuLoop
from ui.menu import Menu
from options import Options
from status import Status
from game_timer import Timer

def main():
    options = Options()
    display = pygame.display.set_mode(options.resolution)
    pygame.display.set_caption("2048")
    pygame.font.init()

    renderer = Renderer(display)
    clock = Clock()
    event_queue = EventQueue()

    menu = Menu(options.resolution)
    renderer.set_menu(menu)
    menu_loop = MenuLoop(menu, renderer)

    status = Status.MENU

    pygame.init()
    while True:
        if status is Status.MENU:
            status = menu_loop.start()

        if status is Status.GAME or status is Status.TIMED_GAME:
            if status is Status.GAME:
                grid = Grid(options.grid_size, options.cell_size, options.position)
            else:
                grid = Grid(options.grid_size, options.cell_size, options.position, True)
                timer = Timer()
                timer.start()
                renderer.timer = timer

            renderer.set_grid(grid)
            game_loop = GameLoop(grid, renderer, event_queue, clock)

            status = game_loop.start()

        if status is Status.EXIT:
            break

if __name__ == "__main__":
    main()
