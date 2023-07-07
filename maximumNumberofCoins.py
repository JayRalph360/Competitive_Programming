class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = 0
        total = 0

        for i in range(1, len(piles), 2):
            total += piles[i]
            n += 1
            if n == len(piles) // 3:
                break

        return total
