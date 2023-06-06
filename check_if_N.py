class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums_set = set()
        
        for num in arr:
            if 2 * num in nums_set or (num % 2 == 0 and num // 2 in nums_set):
                return True
            nums_set.add(num)
        
        return False
