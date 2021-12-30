import sys
inpurt = sys.stdin.readline

n,m = map(int,input().split())

g = [[0]*(m+1) for _ in range(n+1)]
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    g[i] = list(map(int,input().split()))
    g[i].insert(0,0)


for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + g[i][j]

k = int(input())

for t in range(k):
    i,j,x,y = map(int,input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
