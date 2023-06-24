class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])

        for i in range(m - 2):
            for j in range(n - 2):
                if self.is_magic_square(grid, i, j):
                    count += 1

        return count

    def is_magic_square(self, grid, row, col):
        """
        Check if the subgrid starting at (row, col) is a magic square.
        """
        digits = set()
        sum_diag1 = sum_diag2 = 0

        # Check if any digit is repeated or outside the range 1-9
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                digit = grid[i][j]
                if digit in digits or digit < 1 or digit > 9:
                    return False
                digits.add(digit)

        # Check row sums
        for i in range(row, row + 3):
            if sum(grid[i][col:col+3]) != 15:
                return False

        # Check column sums
        for j in range(col, col + 3):
            if sum(grid[i][j] for i in range(row, row + 3)) != 15:
                return False

        # Check diagonal sums
        sum_diag1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
        sum_diag2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
        if sum_diag1 != 15 or sum_diag2 != 15:
            return False

        return True
