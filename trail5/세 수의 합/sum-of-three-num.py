# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

from collections import defaultdict

count = defaultdict(int)
ans = 0

for i in range(n-1, 0, -1):
    for j in range(i):
        ans += count.get(k-arr[i]-arr[j], 0)
    count[arr[i]]+=1

print(ans)