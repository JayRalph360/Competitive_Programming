n = int(input())
arr = list(map(int, input().split()))

negative = []
positive = []
zero = []

for num in arr:
    if num < 0:
        negative.append(num)
    elif num > 0:
        positive.append(num)
    else:
        zero.append(num)

if len(positive) == 0:
    positive.append(negative.pop())
    positive.append(negative.pop())

print(len(negative), *negative)
print(len(positive), *positive)
print(len(zero), *zero)
