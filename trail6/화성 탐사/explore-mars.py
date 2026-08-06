n = int(input())

parent = []

grid = [list(map(int, input().split())) for _ in range(n)]

points = []

for y in range(n):
    for x in range(n):
        if grid[y][x] == 1 or grid[y][x] == 2:
            points.append((y,x))
            
fort_num = len(points)

parent = [i for i in range(len(points))] # 0 ~ fort_num-1 부모 자기자신으로 초기화

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def same(a, b):
    return find(a) == find(b)

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    parent[ max(root_a, root_b) ] = min(root_a, root_b)

# bfs 로 dist 계산 후 edges 에 저장하기

edges = []

from collections import deque

D = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 상 우 하 좌

for s in range(fort_num-1): # 0 ~ fort_num-2
    for e in range(s+1, fort_num):
        visited = [[0] * n for _ in range(n)]
        
        sy, sx = points[s]
        ey, ex = points[e]
        
        q = deque([(sy, sx, 0)])
        visited[sy][sx] = 1
        dist = 0
        
        while q:
            cy, cx, cur_d = q.popleft()
        
            if cy == ey and cx == ex:
                dist = cur_d
                break
            
            # 도달 불가 기지 찾기 위해 일단 다른 기지들도 밟고 경로 찾기
            
            for dy, dx in D:
                ny = cy + dy
                nx = cx + dx
                
                # 맵 안에 있고, 방문하지 않았고, 지나갈 수 있으면
                if (0 <= ny < n and 0 <= nx < n) and not visited[ny][nx] and grid[ny][nx] != -1:
                    visited[ny][nx] = 1
                    q.append((ny, nx, cur_d + 1))
                    
        if dist == 0: # 도달 불가능하면
            print(-1)
            exit()
        
        edges.append((dist, s, e)) 
        # 포인트 번호로 저장
        # s < e

edges.sort()

edges_num = 0
min_dist = 0
for dist, s, e in edges:
    
    if same(s, e): continue
    
    union(s, e)
    
    edges_num += 1
    min_dist += dist
    
    if edges_num == fort_num-1:
        print(min_dist)
        break