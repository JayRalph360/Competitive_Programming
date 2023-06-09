class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Calculate the prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = (
                    prefix_sum[i - 1][j] +
                    prefix_sum[i][j - 1] -
                    prefix_sum[i - 1][j - 1] +
                    mat[i - 1][j - 1]
                )
        
        answer = [[0] * n for _ in range(m)]
        
        # Calculate the answer matrix using the prefix sum matrix
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m - 1, i + k), min(n - 1, j + k)
                answer[i][j] = (
                    prefix_sum[r2 + 1][c2 + 1] -
                    prefix_sum[r2 + 1][c1] -
                    prefix_sum[r1][c2 + 1] +
                    prefix_sum[r1][c1]
                )
        
        return answer
