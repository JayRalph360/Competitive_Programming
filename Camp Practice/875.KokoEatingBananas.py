class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, piles[-1]
        
        while l <= r:
            mid = l+(r-l)//2

            count, isK = 0, False
            for i in range(len(piles)):
                count += piles[i] // mid
                if (piles[i] % mid):
                    count += 1
                
            if count <= h:
                isK = True

            if isK:
                r = mid - 1
            else:
                l = mid + 1
        return l
