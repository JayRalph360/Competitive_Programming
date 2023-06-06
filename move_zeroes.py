class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0  # Current index
        j = 0  # Index where the next non-zero element should be placed
        
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        
        while j < len(nums):
            nums[j] = 0
            j += 1
