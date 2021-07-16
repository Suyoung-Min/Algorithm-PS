n = int(input())

dp = [None, None]
dp[0] = [0]*(n+1)
dp[1] = [0]*(n+1)
dp[1][1]=1

for i in range(2,n+1):
    dp[0][i] = dp[0][i-1]+dp[1][i-1]
    dp[1][i] = dp[0][i-1]

print(dp[0][n] + dp[1][n])
