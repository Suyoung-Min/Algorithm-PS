n, m = map(int, input().split())

A = list(map(int, input().split()))

dp = [0] * (m+1)
dp[0] = 1

for a in A:
    for s in range(m, a-1, -1):
        dp[s] = max(dp[s], dp[s-a])
        
print('Yes' if dp[m] else 'No')