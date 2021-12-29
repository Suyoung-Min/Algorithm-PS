import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())

g = ['' for i in range(r)]
visit = [[False]*c for i in range(r)]
d = [(-1,0),(0,-1),(0,1),(1,0)]

def checkWater(y,x):
    flag = False
    for dy,dx in d:
        ty=y+dy
        tx=x+dx

        if ty<0 or ty>=r or tx<0 or tx>=c: continue

        if g[ty][tx] == '*':
            flag = True
            break

    return flag

for i in range(r):
    g[i] = list(input().strip('\n'))


q = deque()
for i in range(r):
    for j in range(c):
        if g[i][j] == 'S':
            q.append(('S',i,j,0))
            visit[i][j] = True
            break

for i in range(r):
    for j in range(c):
        if g[i][j] == '*':
            q.append(('W',i,j,0))


ans = 'KAKTUS'
flag = False
while q:
    type,y,x,time = q.popleft()

    if type == 'S':
        for dy,dx in d:
            ty=y+dy
            tx=x+dx

            if ty<0 or ty>=r or tx<0 or tx>=c: continue
            if visit[ty][tx] == True: continue

            if g[ty][tx] == 'D':
                ans = time+1
                flag = True
                break

            if g[ty][tx] == '*' or g[ty][tx] == 'X' : continue
            if checkWater(ty,tx): continue

            visit[ty][tx] = True
            q.append(('S',ty,tx,time+1))
    else:
        for dy,dx in d:
            ty=y+dy
            tx=x+dx

            if ty<0 or ty>=r or tx<0 or tx>=c: continue
            
            if g[ty][tx] == '.':
                g[ty][tx] = '*'
                q.append(('W',ty,tx,0))

    if flag:
        break

print(ans)
