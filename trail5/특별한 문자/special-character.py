str = input()

# Please write your code here.

from collections import defaultdict

count = defaultdict(int)

for char in str: count[char] += 1

only_1 = set()

for k, v in count.items():
    if v == 1: only_1.add(k)

ans = None

for char in str:
    if char in only_1:
        ans = char
        break

print(ans)