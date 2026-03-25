n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

start_pos = [[int(x)-1  for x in input().split()] for _ in range(k)]

# Please write your code here.

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
stones_pos = []

ans = 0

for y in range(n):
    for x in range(n):
        if grid[y][x]: # 돌이면
            stones_pos.append((y,x))
            
def generate_combinations(stone_len, r): # stone 개수 중 r 개 조합 뽑기
    result = []
    
    def backtrack(current, start):
        
        # 종료 조건
        
        if len(current) == r:
            result.append(current[:])
            return
        
        
        for i in range(start, stone_len):
            current.append(i)
            
            backtrack(current, i+1)
            
            current.pop()
            
    backtrack([], 0)
    return result

stone_combs = generate_combinations(len(stones_pos), m)

from collections import deque


    
for stone_comb in stone_combs:

    
    # visited 초기화
    for y in range(n):
        for x in range(n):
            visited[y][x] = 0
    
    tmp_area = 0
    q = deque([])

    for sy, sx in start_pos: # 시작점을 큐에 넣기
        visited[sy][sx] = 1
        tmp_area += 1
        q.append((sy,sx))
        
            
    for sidx in stone_comb: # 해당 돌 조합 임시 삭제
        sy,sx = stones_pos[sidx]
        
        grid[sy][sx] = 0 
        
    
    while q:
        y,x = q.popleft()
        
        for dy, dx in dirs:
            ty = y + dy
            tx = x + dx
            
            if ty < 0 or ty >= n or tx < 0 or tx >= n: continue
            
            if not visited[ty][tx] and not grid[ty][tx]: # 방문하지 않았고, 돌이 아닐 때
                visited[ty][tx] = 1
                tmp_area += 1
                q.append((ty,tx))
    
    ans = max(ans ,tmp_area)
        
    for sidx in stone_comb: # 해당 돌 조합 삭제 복구
        sy,sx = stones_pos[sidx]
        
        grid[sy][sx] = 1
    
print(ans)