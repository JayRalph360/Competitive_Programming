class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations)-1
        res = 0
        while l <= r:
            mid = l+(r-l)//2
            y = len(citations) - mid
            if citations[mid] >= y:
                res = y
                r = mid - 1
            else:
                l = mid + 1
        return res
