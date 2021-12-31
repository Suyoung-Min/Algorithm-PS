import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())

g = [[None] for _ in range(r)]

for i in range(r):
    g[i] = list(input().rstrip())

d = [(-1,0),(0,-1),(0,1),(1,0)]

def bfs(y,x):

    q = deque()
    visit = [[False]*c for _ in range(r)]
    visit[y][x] = True
    q.append((y,x,0))

    dist = 0

    while q:
        y,x,l = q.popleft()
        dist = l

        for dy,dx in d:
            ty = y+dy
            tx = x+dx

            if ty < 0 or ty >= r or tx < 0 or tx >= c: continue

            if g[ty][tx] == 'L' and visit[ty][tx] == False:
                visit[ty][tx] = True
                q.append((ty,tx,l+1))

    return dist

ans = 0
for i in range(r):
    for j in range(c):
        if g[i][j] == 'L':
            ans = max(ans,bfs(i,j))

print(ans)
## 브루트포스 + BFS
