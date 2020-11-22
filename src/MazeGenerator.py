from src.Tile import Tile
import random
import time


class MazeGenerator:
    def __init__(self, bounds: Tile, screen, tiles: int):
        self.bounds = bounds
        self.tiles = tiles

        # colours
        self.blue = [0, 150, 200]
        self.red = [250, 25, 3]
        self.yellow = [230, 235, 16]
        self.green = [0, 227, 5]

        # each tiles width and height
        self.tw = int(self.bounds.w / self.tiles)
        self.th = int(self.bounds.h / self.tiles)

        self.screen = screen

        self.starting_pos = ()
        self.maze = self._build_maze()
        self.solution = {}

        # TODO display solution path

    def _build_maze(self) -> dict:
        base_maze = {}

        # temp variables
        x = int(self.bounds.x)
        y = int(self.bounds.y)

        # key index's
        i = 0
        j = 0

        while y < self.bounds.h:
            while x < self.bounds.w:
                base_maze[(i, j)] = (Tile(x, y, self.tw, self.th, self.screen))
                x += self.tw
                i += 1
            y += self.th
            j += 1
            x = int(self.bounds.x)
            i = 0
        return base_maze

    def gen_maze(self):
        i = 0
        j = 0

        # TODO Randomize
        self.starting_pos = (0, 0)

        maze = self._build_maze()
        maze_grid = []  # list of keys
        for key in maze:
            maze_grid.append(key)
        visited = []
        stack = []

        for key in maze:
            self._draw_tile(key[0], key[1])

        self._draw_tile(i, j)
        stack.append((i, j))
        visited.append((i, j))

        while len(stack) > 0:
            time.sleep(0.05)
            cell = []

            if (i, j - 1) not in visited and (i, j - 1) in maze_grid:
                cell.append("U")

            if (i, j + 1) not in visited and (i, j + 1) in maze_grid:
                cell.append("D")

            if (i - 1, j) not in visited and (i - 1, j) in maze_grid:
                cell.append("L")

            if (i + 1, j) not in visited and (i + 1, j) in maze_grid:
                cell.append("R")

            if len(cell) > 0:
                cell_chosen = (random.choice(cell))  #

                if cell_chosen == "R":
                    self._build_right(i, j)
                    self.solution[(i + 1, j)] = i, j
                    i += 1
                    visited.append((i, j))
                    stack.append((i, j))

                elif cell_chosen == "L":
                    self._build_left(i, j)
                    self.solution[(i - 1, j)] = i, j
                    i -= 1
                    visited.append((i, j))
                    stack.append((i, j))

                elif cell_chosen == "D":
                    self._build_down(i, j)
                    self.solution[(i, j + 1)] = i, j
                    j += 1
                    visited.append((i, j))
                    stack.append((i, j))

                elif cell_chosen == "U":
                    self._build_up(i, j)
                    self.solution[(i, j - 1)] = i, j
                    j -= 1
                    visited.append((i, j))
                    stack.append((i, j))
            else:
                i, j = stack.pop()
                self._draw_tile(i, j)
                time.sleep(0.075)
                self._draw_tile(i, j, self.blue)

    def path_back(self, i, j):
        self._solution_cell(i, j)
        while (i, j) != (self.starting_pos[0], self.starting_pos[1]):
            i, j = self.solution[i, j]  #
            self._solution_cell(i, j)
            time.sleep(.05)

    def _build_up(self, i, j):
        temp = self.maze[(i, j)]
        temp.draw(temp.x + 1, temp.y - temp.h + 1, temp.w - 1, (2 * temp.h) - 1, self.blue)

    def _build_down(self, i, j):
        temp = self.maze[(i, j)]
        temp.draw(temp.x + 1, temp.y + 1, temp.w - 1, (2 * temp.h) - 1, self.blue)

    def _build_left(self, i, j):
        temp = self.maze[(i, j)]
        temp.draw(temp.x - temp.w + 1, temp.y + 1, (2 * temp.w) - 1, temp.h - 1, self.blue)

    def _build_right(self, i, j):
        temp = self.maze[(i, j)]
        temp.draw(temp.x + 1, temp.y + 1, (2 * temp.w) - 1, temp.h - 1, self.blue)

    def _draw_tile(self, *args):
        l = len(args)
        i = 0
        j = 0
        c = self.green
        # TODO - Condense error check
        if l >= 2:
            if isinstance(args[0], int) and isinstance(args[1], int):
                i = args[0]
                j = args[1]
                if l == 3:
                    if isinstance(args[2], list):
                        c = args[2]
                        if len(c) != 3:
                            raise ValueError('Faulty colour')
                        for val in c:
                            if not isinstance(val, int):
                                raise ValueError('Faulty colour')
                    else:
                        raise ValueError('Faulty arguments 1.')
                elif l != 2:
                    raise ValueError('Incorrect number of arguments ')
            else:
                raise ValueError('Faulty arguments 2.')

        temp = self.maze[(i, j)]
        temp.draw(temp.x + 1, temp.y + 1, temp.w - 2, temp.h - 2, c)

    def _solution_cell(self, i: int, j: int):
        temp = self.maze[(i, j)]
        temp.draw(temp.x + 8, temp.y + 8, temp.w / 2, temp.h / 2, self.red)
