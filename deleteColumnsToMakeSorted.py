class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        deletion_count = 0

        for col in range(m):
            for row in range(1, n):
                if strs[row][col] < strs[row - 1][col]:
                    deletion_count += 1
                    break

        return deletion_count
