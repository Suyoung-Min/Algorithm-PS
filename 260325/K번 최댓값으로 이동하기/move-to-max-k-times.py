n, k = map(int ,input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())
r -= 1
c -= 1

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

from collections import deque

def move(y, x):
    
    
    visited = [[0] * n for _ in range(n)]
    
    visited[y][x] = 1
    q = deque([(y,x)])
    
    ry, rx = y, x # 리턴할 변수
    
    start_value = grid[y][x]
    
    tmp_max = 0
    
    while q:
        y, x = q.popleft()
        
        for dy, dx in dirs:
            ty = y + dy
            tx = x + dx
            
            if ty < 0 or ty >= n or tx < 0 or tx >= n: continue
            
            if visited[ty][tx]: continue
            
            if grid[ty][tx] >= start_value: continue
            
            visited[ty][tx] = 1
            
            if grid[ty][tx] > tmp_max:
                ry, rx = ty, tx
                tmp_max = grid[ty][tx]
                q.append((ty,tx))
            elif grid[ty][tx] == tmp_max: # 행이 작은 순, 열이 작은순
                
                if ty < ry: # 행이 작으면 갱신
                    ry, rx = ty, tx
                elif ty == ry and tx < rx: # 행이 같으면 열이 작은 순
                    ry, rx = ty, tx
                
                q.append((ty,tx))
            elif grid[ty][tx] < tmp_max:
                q.append((ty,tx))
            
    return ry, rx

for _ in range(k):
    r, c = move(r, c)

print(r+1, c+1)