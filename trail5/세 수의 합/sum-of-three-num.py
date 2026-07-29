# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

from collections import defaultdict

count = defaultdict(int)
ans = 0

for x in arr:
    count[x] += 1

for i in range(n):
    count[arr[i]] -= 1
    for j in range(i):
        ans += count.get(k-arr[i]-arr[j], 0)

print(ans)