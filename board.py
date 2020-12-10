from cell import *
import time


class Board:

    def __init__(self, puzzle, width, height):
        self.puzzle = puzzle
        self.width = width
        self.height = height
        self.cols = 9
        self.rows = 9
        self.grid = []
        for i in range(self.rows):
            r = []
            for j in range(self.cols):
                if puzzle[i][j] != 0:
                    r.append(Cell(i, j, puzzle[i][j], width, height, True))
                else:
                    r.append(Cell(i, j, puzzle[i][j], width, height, False))
            self.grid.append(r)
        self.fixed_cells = self.get_fixed_cells()
        self.selected_cell = None

    def get_grid(self):
        return self.grid

    def get_fixed_cells(self):
        fixed_cells = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.puzzle[i][j] != 0:
                    fixed_cells.append((i, j))
        return fixed_cells

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j].draw(win)

    def get_cell_pos(self, position):
        if position[0] < self.width and position[1] < self.height:
            gap = self.width / 9
            col = position[0] // gap
            row = position[1] // gap
            return int(row), int(col)
        else:
            return None

    def select_cell(self, pos):
        # clears the last selected cell
        if self.selected_cell is not None:
            self.grid[self.selected_cell[0]][self.selected_cell[1]].selected = False

        self.grid[pos[0]][pos[1]].selected = True
        self.selected_cell = (pos[0], pos[1])

    def update_cell(self, val, mouse_side):
        row, col = self.selected_cell
        if (row, col) not in self.fixed_cells:
            if mouse_side == 1:
                self.grid[row][col].set_value(val)
            else:
                self.grid[row][col].set_temp_value(val)

    def reset(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) not in self.fixed_cells:
                    self.grid[i][j].set_value(0)

    def solve(self, logic, win):

        empty_cell = self.get_empty_cell()
        if empty_cell is None:
            return True
        else:
            row, col = empty_cell

        for i in range(1, 10):
            if logic.check_valid((row, col), i):
                self.select_cell((row, col))
                self.update_cell(i, 1)
                win.fill((255, 255, 255))
                self.draw(win)
                pygame.display.update()
                time.sleep(.3)

                if self.solve(logic, win):
                    return True
                else:
                    self.select_cell((row, col))
                    self.update_cell(0, 1)
                    win.fill((255, 255, 255))
                    self.draw(win)
                    pygame.display.update()

        return False

    def get_empty_cell(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) not in self.fixed_cells and self.grid[i][j].value == 0:
                    return i, j
        return None
