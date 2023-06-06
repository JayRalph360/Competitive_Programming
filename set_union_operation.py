# Step 1
n_english = int(input())

# Step 2
english_subscribers = set(map(int, input().split()))

# Step 3
n_french = int(input())

# Step 4
french_subscribers = set(map(int, input().split()))

# Step 6
subscribed_students = english_subscribers.union(french_subscribers)

# Step 7
print(len(subscribed_students))
