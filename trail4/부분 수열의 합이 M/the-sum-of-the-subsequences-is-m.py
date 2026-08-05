n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
INF = float('inf')

dp = [INF] * (m + 1)

dp[0] = 0
        
for i in range(len(A)):
    for x in range(m, A[i]-1, -1):
        dp[x] = min(dp[x], dp[x - A[i]] + 1)
        
print(dp[m] if dp[m] != INF else -1)