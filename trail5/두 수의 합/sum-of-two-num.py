from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)
ans = 0

for elem in arr:
    ans += count.get(k - elem, 0)
    count[elem] += 1

print(ans)