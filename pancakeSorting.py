class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flips = []

        for i in range(n, 1, -1):
            max_val = max(arr[:i])
            if max_val == arr[i - 1]:
                continue

            max_idx = arr.index(max_val, 0, i)
            arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
            flips.append(max_idx + 1)
            arr[:i] = arr[:i][::-1]
            flips.append(i)

        return flips
