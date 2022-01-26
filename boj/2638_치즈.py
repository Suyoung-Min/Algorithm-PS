from collections import deque

n,m = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(n)]
d = [(-1,0),(0,-1),(0,1),(1,0)]

g[0][0],g[0][m-1],g[n-1][0],g[n-1][m-1] = -1,-1,-1,-1
q = deque([(0,0),(0,m-1),(n-1,0),(n-1,m-1)])
cheese = deque()
while q:
    y,x = q.popleft()

    for dy,dx in d:
        ty = y+dy
        tx = x+dx

        if ty < 0 or ty >= n or tx < 0 or tx >= m: continue

        if g[ty][tx] == 0:
            q.append((ty,tx))
            g[ty][tx] = -1

for y in range(1,n-1):
    for x in range(1,m-1):
        if g[y][x] == 1: 
            cheese.append((y,x))
            g[y][x] = 0
            for dy,dx in d:
                if g[y+dy][x+dx] == -1:
                    g[y][x] += 1
            
            if g[y][x] == 0: g[y][x] = 1

def air_bfs(y,x):
    q = deque([(y,x)])
    
    while q:
        y,x = q.popleft()

        for dy,dx in d:
            ty = y+dy
            tx = x+dx

            if ty < 0 or ty >= n or tx < 0 or tx >= m: continue

            if g[ty][tx] == 0:
                g[ty][tx] = -1
                q.append((ty,tx))


time = 0
while cheese:
    
    tmp = deque()
    while cheese:
        y,x = cheese.popleft()

        if g[y][x] >= 2:
            g[y][x] = -1
            air_bfs(y,x)
        else:
            tmp.append((y,x))
    
    for i in range(len(tmp)):
        y,x = tmp[i]

        g[y][x] = 0
        for dy,dx in d:
            if g[y+dy][x+dx] == -1:
                g[y][x] += 1

        if g[y][x] == 0: g[y][x] = 1

    cheese = tmp
    time+=1

print(time)
