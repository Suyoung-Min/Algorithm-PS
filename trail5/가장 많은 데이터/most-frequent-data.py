n = int(input())
words = [input() for _ in range(n)]

words2idx = {}

for word in words:
    if word not in words2idx:
        words2idx[word] = 1
    else:
        words2idx[word] += 1

print(max(words2idx.values()))