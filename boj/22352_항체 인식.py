import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

d = [(-1,0),(0,-1),(0,1),(1,0)]

#g1 = [list(input().strip().split()) for _ in range(n)]
#g2 = [list(input().strip().split()) for _ in range(n)]

g1 = [list(input().split()) for _ in range(n)]
g2 = [list(input().split()) for _ in range(n)]

def solve():
    for i in range(n):
        for j in range(m):
            if g1[i][j] != g2[i][j]:
                bfs(i,j)
                return check_ans()
    return 'YES'

def bfs(sy,sx):
    visit = [[False] * m for _ in range(n)]
    q = deque([(sy,sx)])

    visit[sy][sx] = True
    target = g1[sy][sx]
    num = g2[sy][sx]

    while q:
        y,x = q.popleft()
        g1[y][x] = num
        for dy,dx in d:
            ty = y+dy
            tx = x+dx

            if ty < 0 or ty >= n or tx < 0 or tx >= m: continue

            if not visit[ty][tx] and g1[ty][tx] == target:
                visit[ty][tx] = True
                q.append((ty,tx))

def check_ans():
    for i in range(n):
        for j in range(m):
            if g1[i][j] != g2[i][j]:
                return 'NO'
    return 'YES'

print(solve())
