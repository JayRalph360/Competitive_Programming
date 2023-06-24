class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # Check if reshape operation is possible
        if m * n != r * c:
            return mat
        
        # Initialize the reshaped matrix
        reshaped = [[0] * c for _ in range(r)]
        
        # Fill the reshaped matrix
        for i in range(m):
            for j in range(n):
                # Calculate the corresponding position in the reshaped matrix
                index = i * n + j
                row = index // c
                col = index % c
                reshaped[row][col] = mat[i][j]
        
        return reshaped
