class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct_nums = set(nums)  # Set to store distinct integers
        
        for num in nums:
            reversed_num = int(str(num)[::-1])  # Reverse the digits of the number
            distinct_nums.add(reversed_num)  # Add the reversed number to the set
        
        return len(distinct_nums)  # Return the count of distinct integers
