n=int(input())
map=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        if map[i][j]==0: continue
        if i+map[i][j]<=n-1: dp[i+map[i][j]][j]+=dp[i][j]
        if j+map[i][j]<=n-1: dp[i][j+map[i][j]]+=dp[i][j]
print(dp[n-1][n-1])
