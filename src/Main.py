from src.Tile import Tile
from src.MazeGenerator import MazeGenerator
import pygame

# global variables
WIDTH = 800
HEIGHT = 800
FPS = 60
TILES = 25


def maze_init():
    padding_w = WIDTH - (WIDTH * 0.95)
    padding_h = HEIGHT - (HEIGHT * 0.95)

    # The tile that will contain the maze
    maze_bounds = Tile(int(0 + padding_w), int(0 + padding_h), int(WIDTH - (2 * padding_w)),
                       int(HEIGHT - (2 * padding_h)), screen)

    maze_gen = MazeGenerator(maze_bounds, screen, TILES)
    maze_gen.gen_maze()


if __name__ == "__main__":
    # Window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Grid")
    clock = pygame.time.Clock()
    white = [255, 255, 255]
    screen.fill(white)

    # Generate Maze
    maze_init()

    # Refresh display
    pygame.display.update()

    # App loop
    running = True
    while running:
        # keep running at the at the right speed
        clock.tick(FPS)
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
