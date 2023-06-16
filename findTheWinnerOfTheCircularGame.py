class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        position = 0

        # Calculate the position of the winner
        for i in range(2, n + 1):
            position = (position + k) % i

        # Adjust the position to match 1-indexing
        return position + 1
