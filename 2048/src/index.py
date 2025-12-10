import pygame
from renderer import Renderer
from options import Options
from enums import Status
from game import Game
from menu import Menu

def main():
    options = Options()
    display = pygame.display.set_mode(options.get_resolution())
    pygame.display.set_caption("2048")
    pygame.font.init()

    renderer = Renderer(display)

    pygame.init()
    while True:
        state = options.get_state()
        if state is Status.MENU:
            Menu(options, renderer).start()

        if state is Status.GAME:
            Game(options, renderer).start()

        if state is Status.EXIT:
            break

if __name__ == "__main__":
    main()
