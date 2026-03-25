n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

q = deque([])

visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
q.append((0,0))

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = False

while q:
    y, x = q.popleft()
    
    if y == n-1 and x == m-1:
        ans = True
        break
    
    for dy, dx in dirs:
        ty = y + dy
        tx = x + dx
        
        if ty < 0 or ty >= n or tx < 0 or tx >= m: continue
        
        if not visited[ty][tx] and a[ty][tx] == 1:
            visited[ty][tx] = 1
            q.append((ty, tx))
            
print(int(ans))

# 3 5
# 1 1 0 1 0
# 1 1 1 1 1
# 0 0 1 0 1