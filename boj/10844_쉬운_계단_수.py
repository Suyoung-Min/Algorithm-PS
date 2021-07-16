n = int(input())
dp = [ None, None]
dp[1] = [1]*11
dp[1][0]=0
dp[1][10]=0
dp[0] = [0]*11
for i in range(n-1):
    for j in range(10):
        dp[i%2][j] = (dp[(i+1)%2][j-1]+ dp[(i+1)%2][j+1])%1000000000

print(sum(dp[n%2])%1000000000)
