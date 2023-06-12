class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        numCount = {}

        for num in nums:
            if num in numCount:
                count += numCount[num]
            numCount[num] = numCount.get(num, 0) + 1

        return count
