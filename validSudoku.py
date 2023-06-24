class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            if not self.is_valid_unit(row):
                return False

        # Check columns
        for col in zip(*board):
            if not self.is_valid_unit(col):
                return False

        # Check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid_unit(sub_box):
                    return False

        return True

    def is_valid_unit(self, unit):
        seen = set()
        for num in unit:
            if num != '.' and num in seen:
                return False
            seen.add(num)
        return True
