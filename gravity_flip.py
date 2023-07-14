n = int(input())
columns = list(map(int, input().split()))
 
columns.sort()
 
for height in columns:
    print(height, end=' ')
