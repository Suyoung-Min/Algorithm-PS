import sys
n,m=map(int,input().split())

graph = [list(input()) for _ in range(m)]
visit = [[0]*n for i in range(m)]


def dfs(y,x,t):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0

    if visit[y][x] == 1 or graph[y][x] != t:
        return 0

    visit[y][x] = 1
    return dfs(y+1,x,t)+dfs(y-1,x,t)+dfs(y,x+1,t)+dfs(y,x-1,t)+1

b=0
w=0
for i in range(n):
    for j in range(m):
        b+=dfs(j,i,'B')**2

for i in range(n):
    for j in range(m):
        w+=dfs(j,i,'W')**2

print(w,b)
