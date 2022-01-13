from collections import deque

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]
d = [(-1,0),(0,-1),(0,1),(1,0)]

ans = int(1e9)

def solved(y,x):
    global ans
    visit =[[False]*n for _ in range(n)]

    q = deque([(y,x)])
    island = deque([(y,x)])
    bridge = deque()
    g[y][x] = 2

    while q:
        y,x = q.popleft()

        for dy,dx in d:
            ty = y+dy
            tx = x+dx

            if ty < 0 or ty >= n or tx < 0 or tx >= n: continue

            if g[ty][tx] == 1:
                g[ty][tx] = 2
                q.append((ty,tx))
                island.append((ty,tx))

    while island:
        y,x = island.popleft()

        for dy,dx in d:
            ty = y+dy
            tx = x+dx

            if ty < 0 or ty >= n or tx < 0 or tx >= n: continue

            if g[ty][tx] == 0 and not visit[ty][tx]:
                visit[ty][tx] = True
                bridge.append((ty,tx,1))

    flag = False
    while bridge:
        y,x,blen = bridge.popleft()

        for dy,dx in d:
            ty = y+dy
            tx = x+dx

            if ty < 0 or ty >= n or tx < 0 or tx >= n: continue
            
            if g[ty][tx] == 0 and not visit[ty][tx]:
                visit[ty][tx] = True
                bridge.append((ty,tx,blen+1))

            if g[ty][tx] == 1:
                if blen < ans:
                    ans = blen
                flag = True
                break
        if flag:
            break

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            solved(i,j)

print(ans)
