class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Use first row and first column as markers
        # to indicate if a row or column should be set to 0
        first_row_has_zero = any(x == 0 for x in matrix[0])
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # Scan the matrix and use the first row and first column
        # to mark the rows and columns that need to be set to 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set the rows and columns to 0 based on the markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row and first column to 0 if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
