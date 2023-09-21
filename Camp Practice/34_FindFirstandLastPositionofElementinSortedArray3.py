class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(nums, target, start, end):
            l, r = 0, len(nums)-1
            m = -1
            while l <= r:
                mid = l + (r-l)//2
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    m = mid
                    if start:
                        r = mid - 1
                    if end:
                        l = mid + 1
            return m

        left = binarySearch(nums, target, 1, 0)
        right = binarySearch(nums, target, 0, 1)

        return [left, right]
