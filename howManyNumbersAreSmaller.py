class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        result = []
        for num in nums:
            smaller_count = sum(count[n] for n in count if n < num)
            result.append(smaller_count)
        
        return result
