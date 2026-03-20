n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bomb():
    """폭탄을 한 번 검사해서 M개 이상인 걸 0으로 바꾸고, 
    실제로 터뜨린 게 있다면 True를 반환해."""
    any_exploded = False
    for x in range(n):
        last_y = 0
        si = -1 
        for y in range(n-1, -1, -1):
            if grid[y][x] == 0: 
                last_y = y + 1
                break
            
            if si == -1:
                si = y
            elif grid[y][x] != grid[si][x]:
                # 숫자가 달라졌을 때 이전 뭉텅이 검사
                if si - y >= m:
                    for i in range(y + 1, si + 1):
                        grid[i][x] = 0
                    any_exploded = True
                si = y

        # 루프가 끝난 후 맨 위쪽 뭉텅이 처리 (0이 아닌 경우에만)
        if si != -1 and (si - last_y + 1 >= m):
            # si 위치의 숫자가 0이면 이미 터진 곳이므로 무시
            if grid[si][x] != 0:
                for i in range(last_y, si + 1):
                    grid[i][x] = 0
                any_exploded = True
                
    return any_exploded

def gravity_fall():
    for x in range(n):
        ng = [0] * n
        next_row = n - 1
        for y in range(n-1, -1, -1):
            if grid[y][x] != 0:
                ng[next_row] = grid[y][x]
                next_row -= 1
        for y in range(n):
            grid[y][x] = ng[y]

def rotate_cw():
    # 시계 방향 90도 회전
    ng = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            ng[y][x] = grid[n-x-1][y]
    
    # 값을 다시 복사
    for y in range(n):
        for x in range(n):
            grid[y][x] = ng[y][x]

# --- 메인 시뮬레이션 로직 ---
for _ in range(k):
    # 1. 터질 폭탄이 없을 때까지 '폭발 -> 중력' 반복 (핵심!)
    while True:
        if not bomb():
            break
        gravity_fall()
    
    # 2. 상자 회전
    rotate_cw()
    
    # 3. 회전 후 중력 작용
    gravity_fall()

# 4. K번 반복이 끝난 후 마지막으로 한 번 더 "안 터질 때까지" 폭발
while True:
    if not bomb():
        break
    gravity_fall()

# 최종 결과 계산
bombs_num = sum(1 for y in range(n) for x in range(n) if grid[y][x] != 0)
print(bombs_num)