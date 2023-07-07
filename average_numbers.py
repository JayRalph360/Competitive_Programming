n = int(input())
sequence = list(map(int, input().split()))
 
indices = []
total_sum = sum(sequence)
for i in range(n):
    if (total_sum - sequence[i]) == (sequence[i] * (n - 1)):
        indices.append(i + 1)
 
num_indices = len(indices)
print(num_indices)
if num_indices > 0:
    print(' '.join(map(str, indices)))
