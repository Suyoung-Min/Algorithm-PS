'''
풀이시간: 2시간
'''
from collections import deque

n, r, c, direct = map(int, input().split())
r -= 1
c -= 1
# 답변 출력할 때 ( +1, +1 )

if direct == 1: direct = 0
elif direct == 4: direct = 1

d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상 우 하 좌

d1 = {0:0, 1:-1, 2:1, 3:-2}
d2 = {0:3, 1:2, 2:1, 3:0} # 우선순위 - 좌 하 우 상

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)] # 실제 방문 배열
pos_visit = [[0] * n for _ in range(n)] # 방문 가능한 바다 배열
visit_2 = [[0] * n for _ in range(n)] # Phase 2 의 visit

# 방문 가능 바다 판별

deq = deque([(r, c)])
pos_visit[r][c] = 1

while deq:
    y, x = deq.popleft()
    
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        
        if (0 <= ny < n and 0 <= nx < n) and not grid[ny][nx] and not pos_visit[ny][nx]:
            # 맵 안이고, 바다고, 아직 방문처리 안했으면
            pos_visit[ny][nx] = 1
            deq.append((ny, nx))
            
# 이후 pos_visit은 Read만 한다

ans_arr = [(r, c)] # 방문한 위치 좌표 배열
visited[r][c] = 1
visit_area = 1 # 현재까지 방문한 바다 수
max_visit = sum(sum(row) for row in pos_visit) # 최대 방문가능한 바다 수
y, x = r, c

while True:

    if visit_area == max_visit: # 방문가능 바다들 다 돌았으면
        break
    
    # 상하좌우 방문 가능 바다
    around_sea = False
    
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
    
        if  0 <= ny < n and 0 <= nx < n and not grid[ny][nx] and not visited[ny][nx]: # 접근가능한 방문가능 바다가 있을 때
            around_sea = True
            break
        
    if around_sea: # Phase 1 
        for i in range(4): # 0, 1, 2, 3
            nd = (direct + d1[i])%4 # 그대로, 좌회전, 우회전, 180도회전
            
            ny = y + d[nd][0]
            nx = x + d[nd][1]
            
            if (0 <= ny < n and 0 <= nx < n) and not grid[ny][nx] and not visited[ny][nx]:
                y, x = ny, nx
                visited[y][x] = 1
                direct = nd
                
                visit_area += 1
                ans_arr.append((y, x))
                break

        
    else: # Phase 2
        
        tarr = [] # 방문 가능한 좌표 저장
        
        # Phase 2 visit 초기화
        for ty in range(n): 
            for tx in range(n): visit_2[ty][tx] = 0
        
        deq = deque([(y, x, direct, 0)]) # y, x, 어디에서 왔는지 방향
        visit_2[y][x] = 1
        min_dist = float('inf')
        
        while deq:
            ty, tx, cur_direct, cur_dist = deq.popleft()
            
            if min_dist < cur_dist: continue
            
            if not visited[ty][tx]: # 아직 실제로 방문안한 바다면
                if cur_dist <= min_dist:
                    min_dist = cur_dist
                    tarr.append((cur_dist, ty, tx, cur_direct))
                    continue
            
            # 좌 하 우 상 순으로 
            for i in range(4):
                ny = ty + d[d2[i]][0]
                nx = tx + d[d2[i]][1]
                
                if ny < 0 or ny >= n or nx < 0 or nx >= n: continue
                # 바다고, 아직 방문안했고, 방문 가능하면
                if not grid[ny][nx] and not visit_2[ny][nx] and pos_visit[ny][nx]:
                    visit_2[ny][nx] = 1
                    deq.append((ny, nx, d2[i], cur_dist+1))
        
        # tarr 에 최소 dist 값들이 있다. dist, y, x, direct
        tarr.sort(key=lambda x:(x[0], x[1], x[2])) # dist, 행, 열 기준 정렬
        
        dist, y, x, direct = tarr[0]
        ans_arr.append((y, x))
        visited[y][x] = 1
        visit_area += 1
        
for ay, ax in ans_arr:
    print(ay+1, ax+1)