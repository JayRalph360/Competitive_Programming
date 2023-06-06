from collections import defaultdict

# Step 1
n, m = map(int, input().split())

# Step 2
word_positions = defaultdict(list)

# Step 3
for i in range(n):
    word = input()
    word_positions[word].append(i + 1)  # Add 1 to adjust to 1-based indexing

# Step 4
for _ in range(m):
    word = input()

    # Step 5
    positions = word_positions[word]

    # Step 6
    if positions:
        print(*positions)
    else:
        print(-1)
