def solve():
    from collections import deque

    n, q = map(int, input().split())

    grid = [[0] * n for _ in range(n)]


    cells_input = [list(map(int, input().split())) for _ in range(q)]

    D = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def _pg(grid):
        print('#' * 10)
        for y in range(n - 1, -1, -1):
            for x in range(n):
                print(grid[y][x], end=' ')
            print()

    # 실험 실시
    for t in range(1, q + 1):
        
        # 1. 세포를 배양 용기에 투하

        r1, c1, r2, c2 = cells_input[t - 1]

        for y in range(c1, c2):
            for x in range(r1, r2):
                grid[y][x] = t
                
        # 2. 기존 무리 나눠졌는지 판정 by BFS
        # and 나눠진 무리 있다면 삭제

        visit = [[False] * n for _ in range(n)]
        cells_state = {}
        for y in range(n):
            for x in range(n):
                # 아직 방문안한 세포이면
                tgt = grid[y][x]
                if not visit[y][x] and tgt:
                    if tgt not in cells_state:
                        cells_state[tgt] = [1, 1, [y, x, y, x]]
                    else:
                        cell = cells_state[tgt]
                        cell[0] += 1 # 컴포넌트 개수 증가
                        cell[2][0] = min(cell[2][0], y)
                        cell[2][1] = min(cell[2][1], x)
                        cell[2][2] = max(cell[2][2], y)
                        cell[2][3] = max(cell[2][3], x)


                    cell = cells_state[tgt]
                    visit[y][x] = True
                    deq = deque([(y, x)])

                    while deq:
                        cy, cx = deq.popleft()

                        for d in range(4):
                            ny = cy + D[d][0]
                            nx = cx + D[d][1]

                            if not (0 <= ny < n and 0 <= nx < n): continue
                            if not visit[ny][nx] and grid[ny][nx] == tgt:
                                visit[ny][nx] = True

                                # cy, cx, ey, ex
                                cell[1] += 1 # 영역 증가
                                cell[2][0] = min(cell[2][0], ny)
                                cell[2][1] = min(cell[2][1], nx)
                                cell[2][2] = max(cell[2][2], ny)
                                cell[2][3] = max(cell[2][3], nx)
                                deq.append((ny, nx))

        delete_cell = []
        for tgt in cells_state:
            cell = cells_state[tgt]
            cy, cx, ey, ex = cell[2]
            # 세포 무리가 2부분 이상으로 나뉘었다면
            if cell[0] >= 2:
                for y in range(cy, ey + 1):
                    for x in range(cx, ex + 1):
                        if grid[y][x] == tgt: grid[y][x] = 0
                # grid 에서 지운 후, 삭제
                delete_cell.append(tgt)

        for tgt in delete_cell: del cells_state[tgt]

        # 3. 배양 용기 이동
        # 큰 무리부터, 먼저 들어온 것부터
        # (크기, tgt)

        move_cells = []
        for tgt in cells_state:
            cell = cells_state[tgt]
            move_cells.append((cell[1], tgt))

        # 큰 무리부터, 먼저 들어온 것부터 -> 크기도 저장해놔야 함.
        move_cells.sort(key= lambda x:(-x[0], x[1]))

        new_grid = [[0] * n for _ in range(n)]
        # (x, y) 중 가능한 가장 작은 위치로
        for _, tgt in move_cells:
            
            flag = True
            cell = cells_state[tgt]
            cy, cx, ey, ex = cell[2]
            h = ey - cy + 1
            w = ex - cx + 1
            ty, tx = 0, 0

            # 현재 tgt 가 새 배양기에 설치가능한지
            for sx in range(n - w + 1):
                for sy in range(n - h + 1):

                    flag = True
                    for x in range(w):
                        for y in range(h):
                            # tgt 세포가 새 위치에 겹치면 -> 설치불가하면
                            if grid[cy + y][cx + x] == tgt and new_grid[sy + y][sx + x]:
                                flag = False
                                break
                        # 설치불가하면 다음 좌표로
                        if not flag: break
                    
                    # 설치가능하면 탈출
                    if flag: break
                    
                if flag:
                    # 설치가능하면 설치가능위치 저장
                    ty, tx = sy, sx
                    break

            # 설치가능하면
            if flag:
                for y in range(h):
                    for x in range(w):
                        if grid[cy + y][cx + x] == tgt:
                            new_grid[ty + y][tx + x] = tgt

        grid = new_grid

        # 배양 용기 이동 완료
        # 실험 결과 기록

        # 1. cells_state 에 남아있는 세포 정보 기준
        # 2. grid bfs 하면서 세포끼리 접한 모든 쌍 확인 -> 조합
        # nC2

        # tgt 기준 순서 정해서 순회 -> (big, small) 로 저장
        couple_set = set()

        for y in range(n):
            for x in range(n):
                tgt = grid[y][x]
                # 빈칸이 아니면
                if tgt != 0:
                    #인접한 tgt 들 확인

                    for d in range(4):
                        ny = y + D[d][0]
                        nx = x + D[d][1]

                        if not(0 <= ny < n and 0 <= nx < n): continue

                        ntgt = grid[ny][nx]

                        # 빈칸 아니고 tgt 랑 다르면
                        if ntgt != 0 and ntgt != tgt:
                            small = min(tgt, ntgt)
                            big = max(tgt, ntgt)
                            couple_set.add((small, big))

        # couple_set 에 있는 정보 확인해서 실험결과값 출력

        expr_result = 0
        for a, b in couple_set:
            expr_result += cells_state[a][1] * cells_state[b][1]

        print(expr_result)



solve()
