class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        # Calculate the sum of the first k elements to initialize the maximum sum
        max_sum = sum(nums[:k])
        
        # Slide the window over the array and keep track of the maximum sum
        current_sum = max_sum
        for i in range(k, n):
            current_sum += nums[i] - nums[i - k]  # Add the next element and remove the first element in the window
            max_sum = max(max_sum, current_sum)

        # Calculate and return the maximum average with 10^-5 precision
        return round(max_sum / k, 5)
