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
#############################################################
import sys
sys.setrecursionlimit(3000000)

def dfs(y, x, cnt):
    c = graph[y][x]
    graph[y][x] = 1
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == c:
            cnt = dfs(Y, X, cnt+1)
    return cnt

N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
w = b = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            w += dfs(i, j, 1)**2
        elif graph[i][j] == 'B':
            b += dfs(i, j, 1)**2
print(w, b)
##############################################################
from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    c = graph[y][x]
    graph[y][x] = 1
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == c:
                q.append((Y, X))
                graph[Y][X] = 1
    return cnt

N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
w = b = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            w += bfs(i, j)**2
        elif graph[i][j] == 'B':
            b += bfs(i, j)**2
print(w, b)
