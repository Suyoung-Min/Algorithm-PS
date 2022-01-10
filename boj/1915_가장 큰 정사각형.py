n,m = map(int,input().split())
g = [list(map(int,input().rstrip())) for _ in range(n)]
dp = g.copy()

for i in range(1,n):
    for j in range(1,m):
        if dp[i][j] == 1:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1

m = max(map(max,dp))
print(m*m)
