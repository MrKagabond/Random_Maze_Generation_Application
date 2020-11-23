from src.Tile import Tile
from src.MazeGenerator import MazeGenerator
import pygame

# global variables
TILES = -1  # will change upon user input
TILE_CAP = 50  # MAX number of tiles is capped at 50, REMOVE at your own RISK
SHOW_SOLUTION = False  # will change upon user input


def maze_init():
    padding_w = WIDTH - (WIDTH * 0.96)
    padding_h = HEIGHT - (HEIGHT * 0.96)

    # The tile that will contain the maze
    maze_bounds = Tile(int(0 + padding_w), int(0 + padding_h), int(WIDTH - (2 * padding_w)),
                       int(HEIGHT - (2 * padding_h)), screen)

    maze_gen = MazeGenerator(maze_bounds, screen, TILES)
    maze_gen.gen_maze()  # generates the maze

    if SHOW_SOLUTION:
        maze_gen.path_back(TILES - 1, TILES - 1)  # displays shortest solution


'''
Run this to launch the program! 
'''
if __name__ == "__main__":

    # User Input
    print(
        "--- Random Maze Generation Application ---\nPlease consult the README document for details on how to run "
        "this application...")
    while True:
        t = input("\n\tENTER NUMBER OF TILES <INT>: ")
        if t.isdigit():
            if int(t) >= 1:
                if int(t) > TILE_CAP:
                    TILES = TILE_CAP
                else:
                    TILES = int(t)
                break
            else:
                print("\t\tERROR: Cannot have a negative TILE count")
        else:
            print("\t\tERROR: Input " + t + " is not recognized, type a natural number")
    while True:
        t = input("\n\tWOULD YOU LIKE THE SOLUTION TO BE DISPLAYED? <Y or N>: ")
        if t == 'Y' or t == 'y':
            SHOW_SOLUTION = True
            break
        elif t == 'N' or t == 'n':
            SHOW_SOLUTION = False
            break
        print("\t\tERROR: Input " + t + " is not recognized, type Y or N")

    # Display
    pygame.init()
    pygame.mixer.init()
    HEIGHT = int(pygame.display.Info().current_h)
    WIDTH = HEIGHT
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Random Maze Generation Application")
    clock = pygame.time.Clock()
    screen.fill([15, 15, 15])

    # Generate Maze
    maze_init()

    # Refresh display
    pygame.display.update()

    # App loop
    running = True
    while running:
        # keep running at the at the right speed
        clock.tick(60)
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
                    pygame.quit()
