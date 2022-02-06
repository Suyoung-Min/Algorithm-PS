from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

g = [list(input()) for _ in range(n)]

answer_a,answer_b = 0,0

visit = [[0]*n for _ in range(n)]
d = [(-1,0),(0,-1),(0,1),(1,0)]

def bfs(t,y,x):
    q = deque([(y,x)])
    visit[y][x] = True

    while q:
        y,x = q.popleft()


        for dy,dx in d:
            ty,tx = y+dy, x+dx

            if ty < 0 or ty >= n or tx < 0 or tx >= n: continue

            if not visit[ty][tx] and g[ty][tx] == t:
                visit[ty][tx] = True
                q.append((ty,tx)) 

for y in range(n):
    for x in range(n):
        if not visit[y][x]:
            answer_a += 1
            bfs(g[y][x],y,x)

for y in range(n):
    for x in range(n):
        if g[y][x] == 'G': g[y][x] = 'R'


visit = [[0]*n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if not visit[y][x]:
            answer_b += 1
            bfs(g[y][x],y,x)

print(answer_a,answer_b)
