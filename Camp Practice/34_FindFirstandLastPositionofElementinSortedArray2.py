class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        m = -1
        while l <= r:
            mid = l + (r-l)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                r = mid - 1
                m = mid

        l, r = 0, len(nums)-1
        n = -1
        while l <= r:
            mid = l + (r-l)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
                n = mid

        return [m, n]
