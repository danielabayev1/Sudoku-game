class Logic:
    def __init__(self):
        self.current_board = None
        self.rows = 9
        self.cols = 9

    def check_valid(self, coords, val):
        if val != 0:
            for i in range(self.rows):
                if self.current_board[i][coords[1]].value == val:
                    return False

            for j in range(self.cols):
                if self.current_board[coords[0]][j].value == val:
                    return False

            # Check box
            box_x = coords[1] // 3
            box_y = coords[0] // 3

            for i in range(box_y * 3, box_y * 3 + 3):
                for j in range(box_x * 3, box_x * 3 + 3):
                    if self.current_board[i][j].value == val:
                        return False

            return True
        return True

    def set_board(self, board):
        self.current_board = board
