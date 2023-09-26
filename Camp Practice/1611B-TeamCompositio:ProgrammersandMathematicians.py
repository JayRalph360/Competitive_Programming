t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    l, r = 0, (a+b)//4
    while l <= r:
        mid = l+(r-l)//2
        if (mid*4) <= (a+b) and ((mid-a <= 0) and (mid-b <= 0)):
            l = mid + 1
        else:
            r = mid - 1
    print(r)
