n, m = map(int, input().split())

coin = list(map(int, input().split()))

INF = float('inf')

dp = [INF]*(m+1)

dp[0] = 0

for i in range(1, m+1):
    for c in range(n):
        if i - coin[c] >= 0:
            dp[i] = min(dp[i], dp[i-coin[c]]+1)
            
print(dp[m] if dp[m] != INF else -1)