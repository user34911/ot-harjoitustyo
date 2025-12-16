import pygame
from renderer import Renderer
from options import Options
from enums import State, Option
from game import Game
from menu import Menu

def main():
    options = Options()
    display = pygame.display.set_mode(options.get(Option.RESOLUTION))
    pygame.display.set_caption("2048")
    pygame.font.init()

    renderer = Renderer(display)

    pygame.init()
    while True:
        state = options.get(Option.STATE)
        if state is State.MENU:
            Menu(options, renderer).start()

        if state is State.GAME:
            Game(options, renderer).start()

        if state is State.EXIT:
            break

if __name__ == "__main__":
    main()
