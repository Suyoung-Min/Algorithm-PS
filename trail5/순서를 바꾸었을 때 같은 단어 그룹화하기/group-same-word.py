n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

from collections import defaultdict

count = defaultdict(int)

for word in words:
    word = ''.join(sorted(word))
    count[word] += 1

print(max([v for v in count.values()]))