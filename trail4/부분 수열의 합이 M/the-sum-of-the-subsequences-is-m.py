n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
INF = float('inf')

dp = [INF] * (m + 1)

dp[0] = 0

for a in A:
    for s in range(m, a-1, -1): # m -> a
        dp[s] = min(dp[s], dp[s - a] + 1)
        
print(dp[m] if dp[m] != INF else -1)