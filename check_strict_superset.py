# Step 1
A = set(map(int, input().split()))

# Step 2
n = int(input())

# Step 3
is_superset = True
for _ in range(n):
    # Read the elements of set B
    B = set(map(int, input().split()))

    # Check if A is a strict superset of B
    if not A.issuperset(B):
        is_superset = False
        break

# Step 4
print(is_superset)
