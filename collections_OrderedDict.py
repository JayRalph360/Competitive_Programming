from collections import OrderedDict

# Step 1
N = int(input())

# Step 2
items = OrderedDict()

# Step 3
for _ in range(N):
    line = input().split()
    item = ' '.join(line[:-1])
    price = int(line[-1])
    if item in items:
        items[item] += price
    else:
        items[item] = price

# Step 4
for item, net_price in items.items():
    print(item, net_price)
