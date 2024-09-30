import numpy as np

class SudokuSolver:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.size = 9  # Size of the Sudoku grid (9x9)
        
    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else '.' for num in row))
    
    def is_safe(self, row, col, num):
        # Check if num is not in the current row and column
        if num in self.grid[row] or num in self.grid[:, col]:
            return False
        
        # Check the 3x3 subgrid
        start_row, start_col = row - row % 3, col - col % 3
        if num in self.grid[start_row:start_row + 3, start_col:start_col + 3]:
            return False
        
        return True
    
    def solve(self, row=0, col=0):
        if row == self.size - 1 and col == self.size:
            return True
        if col == self.size:
            row += 1
            col = 0
        if self.grid[row][col] != 0:
            return self.solve(row, col + 1)
        
        for num in range(1, self.size + 1):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if self.solve(row, col + 1):
                    return True
                self.grid[row][col] = 0  # Backtrack
        return False

# Initial grid with 0s representing empty cells
initial_grid = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
]

if __name__ == "__main__":
    solver = SudokuSolver(initial_grid)
    if solver.solve():
        solver.print_grid()
    else:
        print("Solution does not exist :(")
