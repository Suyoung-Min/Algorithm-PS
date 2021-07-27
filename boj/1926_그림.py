import sys
sys.setrecursionlimit(3000000) # 파이썬 재귀 사용할 때 추가할 것

n,m = map(int,input().split())

graph = [[] for _ in range(n)]
visited = [[False]*m for _ in range(n)]
painting_num=0
max_painting_area=0

for i in range(n):
    graph[i]=list(map(int,input().split()))

def dfs(y,x):
    if y<0 or y>=n or x<0 or x>=m:
        return 0
    if visited[y][x]:
        return 0
    
    visited[y][x]=True

    if graph[y][x] == 0:
        return 0

    return dfs(y-1,x)+dfs(y+1,x)+dfs(y,x-1)+dfs(y,x+1)+1

for i in range(n):
    for j in range(m):
        if (not visited[i][j]) and graph[i][j] == 1:
            painting_num+=1
        max_painting_area = max([max_painting_area, dfs(i,j) ])

print(painting_num)
print(max_painting_area)
