t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    max_val = float('-inf')
    max_idx = -1
    min_val = float('inf')
    min_idx = -1
 
    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i+1
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i+1
 
    if min_idx == max_idx:
        print(min_idx, min_idx)
    else:
        print(min_idx, max_idx)
