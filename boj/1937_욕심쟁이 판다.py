import sys
sys.setrecursionlimit(1000000)

# dfs + dp 알고리즘 -> 가지치기 ***

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

d = [(-1,0),(0,-1),(0,1),(1,0)]
def dfs(y,x):
    if dp[y][x] == 0:
        dp[y][x] = 1
    else:
        return dp[y][x]

    for dy,dx in d:
        ty = y+dy
        tx = x+dx

        if ty < 0 or ty >= n or tx < 0 or tx >= n: continue

        if g[y][x] < g[ty][tx]:
            dp[ty][tx] = dfs(ty,tx)
            dp[y][x] = max(dp[y][x],dp[ty][tx]+1)

    return dp[y][x]

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            dp[i][j] = dfs(i,j)

print(max(map(max,dp)))
