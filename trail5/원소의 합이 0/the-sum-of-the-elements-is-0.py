n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.
from collections import defaultdict

count = defaultdict(int)

ans = 0

for a in A:
    for b in B:
        count[a+b] += 1

for c in C:
    for d in D:
        ans += count.get(-(c+d), 0)

print(ans)