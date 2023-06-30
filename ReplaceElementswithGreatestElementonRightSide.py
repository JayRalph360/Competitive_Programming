class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = arr[n - 1]  # Initialize the maximum value to the last element
        arr[n - 1] = -1  # Replace the last element with -1
        
        for i in range(n - 2, -1, -1):
            temp = arr[i]  # Store the current element
            arr[i] = max_right  # Replace the current element with the maximum value so far
            max_right = max(max_right, temp)  # Update the maximum value if necessary
        
        return arr
