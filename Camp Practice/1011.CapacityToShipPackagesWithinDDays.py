class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = l+(r-l)//2
            x, d = 0, 1
            for i in range(len(weights)):
                x += weights[i]
                if x > mid:
                    d += 1
                    x = weights[i]
            if d > days:
                l = mid + 1
            else:
                r = mid - 1
        return l
