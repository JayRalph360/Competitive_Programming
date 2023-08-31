lass Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total, prefixsum, n = 0, 0, len(nums)
        dic = {}
        dic[0] = 1

        for i in nums:
            prefixsum += i
            if prefixsum-k in dic:
                total += dic[prefixsum-k]
            dic[prefixsum] = dic.get(prefixsum, 0) + 1
        
        return total
