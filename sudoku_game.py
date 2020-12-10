from board import *
from logic import Logic


class Game:
    RIGHT_CLICK = 3
    LEFT_CLICK = 1

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.win = pygame.display.set_mode((540, 630))
        pygame.display.set_caption("Sudoku")
        self.puzzle = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        self.board = Board(self.puzzle, 540, 540)
        self.logic = Logic()
        self.logic.set_board(self.board.get_grid())
        self.text_font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.instruction1 = self.text_font.render(
            "Q - quit, S - Solve, R - Reset,0 - delete cell content",
            True, (0, 0, 0))
        self.instruction2 = self.text_font.render(
            "left click on a cell to type a number, right click to sketch",
            True, (0, 0, 0))
        self.not_valid = self.text_font.render(
            "not valid by the rules!",
            True, (0, 0, 0))
        self.finished = self.text_font.render(
            "You've finished! hooray!",
            True, (0, 0, 0))

    def run(self):
        key = None
        solved = False
        run = True
        mouse_side = 0
        valid = True
        keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                pygame.K_8,
                pygame.K_9]

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    for i in range(len(keys)):
                        if event.key == keys[i]:
                            key = i
                        if event.key == pygame.K_r:
                            self.board.reset()
                            solved = False
                        if event.key == pygame.K_s and not solved:
                            self.board.reset()
                            self.board.solve(self.logic, self.win)
                            solved = True
                        if event.key == pygame.K_q:
                            run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_side = self.RIGHT_CLICK if event.button == self.RIGHT_CLICK else self.LEFT_CLICK
                    pos = pygame.mouse.get_pos()
                    cell_pos = self.board.get_cell_pos(pos)
                    if cell_pos:
                        self.board.select_cell(cell_pos)
                        key = None

            if self.board.selected_cell is not None and key is not None:
                if self.logic.check_valid(self.board.selected_cell, key):
                    self.board.update_cell(key, mouse_side)
                    self.logic.set_board(self.board.get_grid())
                    valid = True
                else:
                    valid = False
                key = None
            if self.board.get_empty_cell() is None and not solved:
                solved = True

            # Draw board
            self.win.fill((255, 255, 255))
            self.win.blit(self.instruction1, (0, 560))
            self.win.blit(self.instruction2, (0, 570))
            if solved:
                self.win.blit(self.finished, (0, 600))
                valid = True
            if not valid:
                self.win.blit(self.not_valid, (0, 585))
            self.board.draw(self.win)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
