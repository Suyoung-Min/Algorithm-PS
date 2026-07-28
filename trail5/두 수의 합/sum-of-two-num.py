from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)
ans = 0

for elem in arr:

    target = k - elem

    if target in count:
        ans += count[target]
        
    count[elem] += 1

print(ans)