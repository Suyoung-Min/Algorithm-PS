n, m = map(int, input().split())

grid2 = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

from collections import deque

q2 = deque([])

for y in range(n):
    for x in range(m):
        if not grid2[y][x]:
            q2.append((y,x)) # 얼음 넣기
            
t = 0
last_garea = 0
while True:
    
    # print(f't == {t}')
    # for line in grid2:
    #     print(*line)
    # print("#"*20)
    
    q1 = q2
    q2 = deque([])
    grid1 = [row[:] for row in grid2]
    
    garea = sum(sum(row) for row in grid1)
    
    if garea == 0: # 빙하가 다 녹으면
        break
    t += 1
    # 물 탐색 
    # 1. 빙하를 못녹이는 물이면 q2 에 넣기
    # 2. 빙하가 녹아서 물이 되면 q2 에 넣기
    # 3. grid1 기반으로 판단 후 grid2 에 갱신
    # 4. 한번 녹인 빙하는 visited 로 관리 -> grid1, grid2 를 쓰기 때문에 필요
    tmp_garea = 0
    while q1:
        y, x = q1.popleft()
        
        around_flag = True # 빙하에 둘러쌓여 있나
        
        # 1
        for dy, dx in dirs:
            ty = y + dy
            tx = x + dx
            
            if ty < 0 or ty >= n or tx < 0 or tx >= m: continue
            
            if grid1[ty][tx] == 0: # 다른 물과 하나라도 연결되어 있으면
                around_flag = False
                break
            
        if around_flag: # 빙하에 둘러쌓여 있으면 -> 물못녹임
            q2.append((y,x))
            continue
        
        # 2. 근처 빙하 녹이기
        
        for dy, dx in dirs:
            ty = y + dy
            tx = x + dx
            
            if ty < 0 or ty >= n or tx < 0 or tx >= m: continue
            
            if not visited[ty][tx] and grid1[ty][tx]: # 근처 빙하가 있고 아직 안녹였으면
                visited[ty][tx] = 1
                grid2[ty][tx] = 0 # 녹이기
                q2.append((ty,tx)) # 녹여서 물됐으니 q2 에 넣기
                tmp_garea += 1 # 현재 턴에서 녹인 빙하 크기 추가
                
    last_garea = tmp_garea
            
print(t, last_garea)