from collections import deque

D = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상 우 하 좌
TURN = (0, -1, 1, 2)                    # 직진, 좌회전, 우회전, 후진
BFS_ORDER = (3, 2, 1, 0)                # 좌 하 우 상

n, r, c, direct = map(int, input().split())
r -= 1
c -= 1

# 입력 방향(1 상 / 2 하 / 3 좌 / 4 우)을 D의 인덱스(상우하좌)로 변환
# 2(하)와 3(좌)은 인덱스와 그대로 일치하므로 1과 4만 손본다
if direct == 1:
    direct = 0
elif direct == 4:
    direct = 1

grid = [list(map(int, input().split())) for _ in range(n)]

# 시작점에서 도달 가능한 바다의 총 개수 (종료 조건용)
reachable = [[0] * n for _ in range(n)]
reachable[r][c] = 1
max_visit = 1
reach_q = deque([(r, c)])
while reach_q:
    y, x = reach_q.popleft()
    for dy, dx in D:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and not grid[ny][nx] and not reachable[ny][nx]:
            reachable[ny][nx] = 1
            max_visit += 1
            reach_q.append((ny, nx))

visited = [[0] * n for _ in range(n)]
visited[r][c] = 1
visit_area = 1
ans_arr = [(r, c)]
y, x = r, c

while visit_area < max_visit:
    
    # Phase 1
    # 네방향 두 번 돌지 말고 한번에 -> moved 플래그 사용
    
    moved = False
    
    for turn in TURN:
        nd = (direct + turn)%4
        ny, nx = y + D[nd][0], x + D[nd][1]
        
        # 맵 안에 있고, 방문하지 않은 바다이면
        if (0 <= ny < n and 0 <= nx < n) and not grid[ny][nx] and not visited[ny][nx]:
            y, x, direct = ny, nx, nd
            visited[y][x] = 1
            ans_arr.append((y, x))
            visit_area += 1
            moved = True
            break
        
    if moved: continue # Phase 1 에서 움직였으면 처음으로
    
    # Phase 2
    # bfs 로 다음 이동 바다 탐색하기
    # 방문하지 않은 바다
    # BFS_ORDER = (3, 2, 1, 0)                # 좌 하 우 상
    seen = [[0] * n for _ in range(n)]
    seen[y][x] = 1
    q = deque([(0, y, x, direct)]) # 거리, y, x, 이전 방향
    min_dist = float('inf')
    candidates = []
    
    while q:
        dist, cy, cx, cd = q.popleft()
        
        if dist > min_dist: break
        
        if not visited[cy][cx]:
            min_dist = dist
            candidates.append((dist, cy, cx, cd))
            continue
        
        for nd in BFS_ORDER:
            ny, nx = cy + D[nd][0], cx + D[nd][1]
            
            if (0 <= ny < n and 0 <= nx < n) and not grid[ny][nx] and not seen[ny][nx]:
                seen[ny][nx] = 1
                q.append((dist+1, ny, nx, nd))
    
            
    _, y, x, direct = min(candidates)
    visited[y][x] = 1
    ans_arr.append((y,x))
    visit_area += 1

for ay, ax in ans_arr:
    print(ay + 1, ax + 1)