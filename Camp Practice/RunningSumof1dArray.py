class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.prefix_sum = nums
        for i in range(len(nums)-1):
            self.prefix_sum[i+1] += self.prefix_sum[i]

        return self.prefix_sum
