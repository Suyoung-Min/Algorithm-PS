n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

is_water = [[0] * m for _ in range(n)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

from collections import deque

nq = deque([(0, 0)]) # 녹이는 과정의 큐
water_q = deque([(0,0)]) # 겉의 물의 큐
is_water[0][0] = 1

# 겉에 물만 q2 에 넣기
while water_q:
    y, x = water_q.popleft()
    
    for dy, dx in dirs:
        ty = y + dy
        tx = x + dx
        
        if ty < 0 or ty >= n or tx < 0 or tx >= m: continue
        
        if not is_water[ty][tx] and not grid[ty][tx]: # 방문 안했고, 물이면
            is_water[ty][tx] = 1
            water_q.append((ty,tx))
            nq.append((ty, tx))
            
t = 0

total_ice = sum(sum(row) for row in grid)
last_garea = 0

while True:
    
    cq = nq # cq: 현재 시간에 쓸 큐 , nq: 다음 시간에 쓸 큐
    nq = deque([])
    
    if total_ice == 0:
        break
    t += 1
    # 물 탐색 
    # 1. 빙하가 녹아서 물이 되면 nq 에 넣기 + 같혀 있던 물이 해방되면 cq에 넣기
    # 2. 한번 녹인 빙하는 is_water 로 관리
    tmp_garea = 0
    while cq: # cq 에 있는 건 무조건 빙하를 녹일 수 있는 물
        y, x = cq.popleft()
        
        # 1. 근처 빙하 녹이기
        
        for dy, dx in dirs:
            ty = y + dy
            tx = x + dx
            
            if ty < 0 or ty >= n or tx < 0 or tx >= m: continue
            
            if is_water[ty][tx]: continue # 이미 빙하를 녹인 물이면 -> nq 에 넣을 필요 없음
            
            if grid[ty][tx]: # 빙하면
                is_water[ty][tx] = 1
                grid[ty][tx] = 0 # 녹이기
                nq.append((ty,tx)) # 녹여서 물됐으니 nq 에 넣기
                tmp_garea += 1 # 현재 턴에서 녹인 빙하 크기 추가
            else: # 물인데 아직 방문표시 안된 물-> 갇혀있던 물이면 바로 cq 에 넣어서 빙하 녹이게
                is_water[ty][tx] = 1
                cq.append((ty,tx)) 
                
    last_garea = tmp_garea
    total_ice -= tmp_garea
            
print(t, last_garea)