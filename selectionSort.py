#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        return min_idx
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_idx = self.select(arr, i)
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
