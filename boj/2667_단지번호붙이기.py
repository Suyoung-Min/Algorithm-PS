import heapq
from collections import deque

N = int(input())

graph = [[] for _ in range(N)]
visit = [[False]*N for _ in range(N)]
area = []
d = [(-1,0),(0,-1),(0,1),(1,0)]

for i in range(N):
    graph[i] = list(input())
    graph[i] = list(map(int,graph[i]))


def bfs(y,x):
    q = deque()
    q.append((y,x))

    ret = 1

    while q:
        y,x = q.popleft()

        for dy,dx in d:
            ty = y+dy
            tx = x+dx

            if ty < 0 or ty >= N or tx < 0 or tx >= N:
                continue

            if graph[ty][tx] == 1 and visit[ty][tx] == False:
                visit[ty][tx] = True
                q.append((ty,tx))
                ret += 1

    return ret
    
building_num = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visit[i][j] == False:
            visit[i][j] = True
            heapq.heappush(area,bfs(i,j))
            building_num += 1

print(building_num)
while area:
    print(heapq.heappop(area))
