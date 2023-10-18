class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def score(a, b):
            return (a <= b) and max(nums[a]-score(a+1,b), nums[b]-score(a,b-1))

        return len(nums) % 2 == 0 or score(0, len(nums)-1) >= 0
