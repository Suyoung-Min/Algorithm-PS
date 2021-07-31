import sys
sys.setrecursionlimit(3000000)

N,M = map(int,input().split())
graph = [ input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]

I_y=0
I_x=0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            I_y = i
            I_x = j
            break

def dfs(y,x):
    if y < 0 or y > N-1 or x < 0 or x > M -1:
        return 0

    if visited[y][x] or graph[y][x] == 'X':
        return 0
    
    visited[y][x] = True

    flag = 0
    if graph[y][x] == 'P':
        flag = 1
    
    return dfs(y-1,x)+dfs(y+1,x)+dfs(y,x-1)+dfs(y,x+1)+flag
    
ans = dfs(I_y,I_x)
if ans == 0:
    print('TT')
else:
    print(ans)
