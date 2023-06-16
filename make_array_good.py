sequence = [1]
while sequence[-1] < 10**18:
	sequence.append(sequence[-1]*2)

sequence.pop()

for x in range(int(input())):
	y = int(input())
	a = list(map(int, input().split()))

	print(y)
	for i in range(y):
		print(i+1, min([j for j in sequence if a[i] <= j]) - a[i])
