t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    possible = True

    a.sort()

    for i in range(1, n):
        if abs(a[i] - a[i-1]) > 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")
