class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        common_count = {}
        C = [0] * n

        # Store the indices of elements in B
        for i in range(n):
            common_count[B[i]] = i + 1

        # Calculate the prefix common array C
        for i in range(n):
            count = 0
            for j in range(i + 1):
                if common_count[A[j]] <= i + 1:
                    count += 1
            C[i] = count

        return C
