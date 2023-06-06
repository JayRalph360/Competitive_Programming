class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Current index
        j = 0  # Index where the next non-val element should be placed
        
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        
        return j
