from collections import OrderedDict

n = int(input())
words = []
occurrences = OrderedDict()

# Read input words and count occurrences
for _ in range(n):
    word = input().strip()
    if word not in occurrences:
        words.append(word)
    occurrences[word] = occurrences.get(word, 0) + 1

# Output the number of distinct words
print(len(occurrences))

# Output the number of occurrences for each distinct word in input order
print(' '.join(str(occurrences[word]) for word in words))
