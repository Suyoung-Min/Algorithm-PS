n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

start_pos = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

from collections import deque

visited = [[0] * n for _ in range(n)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0

def bfs(pos):
    global ans
    
    sy, sx = pos
    sy -= 1
    sx -= 1
    
    q = deque([])
    
    if visited[sy][sx]: return # 시작점 설정, 모든 시작점의 위치는 벽이 아님
    
    visited[sy][sx] = 1
    q.append((sy, sx))
    ans += 1
    
    while q:
        y, x = q.popleft()
        
        for dy,dx in dirs:
            ty = y + dy
            tx = x + dx
            
            if ty < 0 or ty >= n or tx < 0 or tx >= n: continue
            
            if not visited[ty][tx] and not a[ty][tx]: # 방문하지 않았고, 벽이 아니면
                visited[ty][tx] = 1
                q.append((ty, tx))
                ans += 1
                
        
for spos in start_pos:
    bfs(spos)
print(ans)