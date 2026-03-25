n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

grid_pos = [(y,x) for y in range(n) for x in range(n)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def generate_combinations(N, R): # 0~N-1 범위 중 R 개를 순서 없이
    result = []
    
    def backtrack(current, start):
        
        if len(current) == R:
            result.append(current[:])
            return
        
        for i in range(start, N):
            current.append(i)
            
            backtrack(current, i+1)
            
            current.pop()
            
    backtrack([], 0)
    
    return result

pos_combinations = generate_combinations(n**2, k)

ans = 0

from collections import deque

for pos_comb in pos_combinations:
    
    
    q = deque([])
    visited = [[0]*n for _ in range(n)]
    
    visit_city_num = 0
    
    for pidx in pos_comb: #pos_comb [1,2,3,4]
        y, x = grid_pos[pidx]
        
        q.append((y, x))
        visited[y][x] = 1
        visit_city_num += 1
        
    while q:
        y, x = q.popleft()
        
        for dy, dx in dirs: # 현재 도시에서 근처 도시 탐색
            ty = y + dy
            tx = x + dx
            
            if ty < 0 or ty >= n or tx < 0 or tx >= n: continue
            
            if visited[ty][tx]: continue
            
            height_diff = abs(grid[y][x] - grid[ty][tx])
            
            if u <= height_diff and height_diff <= d: # 도시 높이 차이가 범위 내
                q.append((ty, tx))
                visited[ty][tx] = 1 # 방문
                visit_city_num += 1
                
    ans = max(ans, visit_city_num)
        
print(ans)