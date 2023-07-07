class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            if sorted_nums[i] == target:
                result.append(i)

        return result
