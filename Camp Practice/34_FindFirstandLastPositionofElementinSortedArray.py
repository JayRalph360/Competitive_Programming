l, r = 0, len(nums)-1
        m = n = -1

        while l <= r:
            mid = l+(r-l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                m = mid

        l, r = 0, len(nums)-1
        while l <= r:
            mid = l+(r-l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                l = mid + 1
                n = mid

        return [m, n]
