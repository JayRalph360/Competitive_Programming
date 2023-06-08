from collections import Counter

# Step 1
X = int(input())
shoe_sizes = list(map(int, input().split()))
N = int(input())

# Step 2
shoe_counts = Counter(shoe_sizes)

# Step 3
total_earned = 0

# Step 4
for _ in range(N):
    size, price = map(int, input().split())
    if shoe_counts[size] > 0:
        shoe_counts[size] -= 1
        total_earned += price

# Step 5
print(total_earned)
