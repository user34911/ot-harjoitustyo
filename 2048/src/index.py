import pygame
from grid import Grid

def main():
    grid_size = 4
    cell_size = 100
    display = pygame.display.set_mode((800, 600))

    grid = Grid(grid_size, cell_size)

    pygame.init()
    grid.all_sprites.draw(display)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()