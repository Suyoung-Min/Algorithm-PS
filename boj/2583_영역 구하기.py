from collections import deque

m,n,k = map(int,input().split())
graph = [ [0]*n for _ in range(m) ]
visit = [ [False]*n for _ in range(m) ]
for i in range(k):
    a_x,a_y,b_x,b_y = map(int,input().split())
    for y in range(a_y,b_y):
        for x in range(a_x,b_x):
            graph[y][x] = 1
d = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(y,x):
    if graph[y][x] == 1 or visit[y][x] == True:
        return 0

    q = deque([(y,x)])
    square=0
    while q:
        pos = q.popleft()

        if graph[pos[0]][pos[1]] == 1 or visit[pos[0]][pos[1]] == True:
            continue
        
        square+=1
        visit[pos[0]][pos[1]] = True

        for dy,dx in d:
            if 0<=pos[0]+dy and pos[0]+dy < m and 0<=pos[1]+dx and pos[1]+dx < n:
                q.append((pos[0]+dy,pos[1]+dx))

    return square

arr=[]
for i in range(m):
    for j in range(n):
        tmp = bfs(i,j)
        if tmp != 0:
            arr.append(tmp)
arr.sort()
print(len(arr))
print(*arr)
