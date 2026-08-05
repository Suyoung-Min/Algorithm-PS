n, m = map(int, input().split())

jewels = [tuple(map(int, input().split())) for _ in range(n)] # (w, v)

dp = [-1] * (m+1)
dp[0] = 0

for w, v in jewels:
    for i in range(m, w-1, -1):
        if i - w >= 0:
            dp[i] = max(dp[i], dp[i-w] + v)
            
            
print(max(dp))