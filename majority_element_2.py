class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize the potential majority elements
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        # Step 2: Find potential majority elements
        for num in nums:
            # Check if num matches the candidates
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            # Check if we need to replace the candidates
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            # Decrement the counts of the candidates
            else:
                count1 -= 1
                count2 -= 1

        # Step 3: Count the occurrences of the potential majority elements
        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Step 4: Check if the potential majority elements occur more than ⌊ n/3 ⌋ times
        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)

        return result
