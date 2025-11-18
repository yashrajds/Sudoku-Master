import random

class Sudoku:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.original_board = [[0 for _ in range(size)] for _ in range(size)]

    def is_valid(self, row, col, num):
        # Check row
        if num in self.board[row]:
            return False
        # Check column
        for i in range(self.size):
            if self.board[i][col] == num:
                return False
        return True

    def solve(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    for num in range(1, self.size + 1):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def generate_puzzle(self, difficulty):
        # Fill the board
        self.solve()
        self.original_board = [row[:] for row in self.board]

        # Remove cells based on difficulty
        if difficulty == 'easy':
            cells_to_remove = int(self.size * self.size * 0.4)  # Remove 40%
        elif difficulty == 'medium':
            cells_to_remove = int(self.size * self.size * 0.5)  # Remove 50%
        else:  # hard
            cells_to_remove = int(self.size * self.size * 0.6)  # Remove 60%

        positions = [(i, j) for i in range(self.size) for j in range(self.size)]
        random.shuffle(positions)
        for i, j in positions[:cells_to_remove]:
            self.board[i][j] = 0

    def check_solution(self):
        # Check if all cells are filled
        for row in self.board:
            if 0 in row:
                return False
        # Check rows for uniqueness
        for row in self.board:
            if len(set(row)) != self.size:
                return False
        # Check columns for uniqueness
        for col in range(self.size):
            column = [self.board[row][col] for row in range(self.size)]
            if len(set(column)) != self.size:
                return False
        return True

    def get_board(self):
        return self.board

    def set_cell(self, row, col, value):
        if 0 <= value <= self.size:
            self.board[row][col] = value
