n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.
from collections import defaultdict

count = defaultdict(int)

ans = 0

for i in range(n):
    for j in range(n):
        count[A[i] + B[j]] += 1

for i in range(n):
    for j in range(n):
        ans += count[-(C[i] + D[j])]

print(ans)