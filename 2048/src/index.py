import pygame
from grid import Grid
from clock import Clock
from event_queue import EventQueue
from renderer import Renderer
from game_loop import GameLoop

def main():
    grid_size = 4
    cell_size = 100
    position = (50, 50)
    display = pygame.display.set_mode((800, 600))

    grid = Grid(grid_size, cell_size, position)

    event_queue = EventQueue()
    renderer = Renderer(display, grid)
    clock = Clock()
    game_loop = GameLoop(grid, renderer, event_queue, clock)

    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()