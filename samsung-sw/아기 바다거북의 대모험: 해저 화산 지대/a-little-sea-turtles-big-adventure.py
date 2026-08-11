def main():

    def pg(grid):
        print('#'*10)
        for row in grid:
            print(' '.join(map(str, row)))

    N, M, K = map(int, input().split())
    # 격자 크기, 바다거북 수, 해저 화산 수

    grid = [list(map(int, input().split())) for _ in range(N)]
    # 산호초 1, 화석 2, 바다거북 100 + id, 화산은 굳이?

    turtles = [tuple(map(int, input().split())) for _ in range(M)]
    # 해당 거북이가 도착 혹은 죽었으면 False 로 대체 -> t_ans 답 혹은 -1 로

    # id -> 100 + i
    for id in range(M):
        y, x = turtles[id]
        grid[y][x] = 100 + id


    t_ans = [-1] * M

    volcano = [list(map(int, input().split())) + [0] for _ in range(K)]
    # y, x, 분출 임계치 P, 현재 마그마 압력

    D = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 우 하 좌 상

    from collections import deque

    turn = 0
    while turn < 100:
        turn += 1

        # 1단계. 바다거북 이동
        # 바다거북 한마리당 최단거리 탐색 및 존재한다면 해당 경로 첫번째 칸으로 이동
        # bfs 돌릴 때, 원소에 초기 이동 방향 넣기
        for id in range(M):
            turtle = turtles[id]
            if not turtle: continue
            sy, sx = turtle

            q = deque([])

            visited = [[0]*N for _ in range(N)]
            visited[sy][sx] = 1

            # 거북이 이동시키기 위한 초기 이동 좌표 덱에 저장
            # 최단 거리 여러 개 존재가능하기 때문에 거리저장 해야겠다.
            for d in range(4): 
                y = sy + D[d][0]
                x = sx + D[d][1]

                if y < 0 or y >= N or x < 0 or x >= N: continue

                if not grid[y][x]: # 이동가능하면
                    q.append((y, x, 1, d)) # 좌표, 거리, 및 초기 방향

            min_dist = float('inf')
            init_d = 5

            while q:
                y, x, dist, d = q.popleft()

                # 최단 거리 이상이면 가지치기
                if dist > min_dist: continue
                
                if y == N-1 and x == N-1: # 파라다이스 도착가능하면
                    if dist < min_dist:
                        min_dist = dist
                        init_d = d
                    elif dist == min_dist:
                        init_d = min(init_d, d)

                if visited[y][x]: continue
                visited[y][x] = 1

                for nd in range(4):
                    ny = y + D[nd][0]
                    nx = x + D[nd][1]
                    
                    # 맵 안이고, 이동가능하다면
                    if (0 <= ny < N and 0 <= nx < N) and not grid[ny][nx]:
                        q.append((ny, nx, dist+1, d))

            if min_dist != float('inf'): # 최단거리 존재한다면
                y = sy + D[init_d][0]
                x = sx + D[init_d][1]

                grid[sy][sx] = 0
                if y == N-1 and x == N-1: # 파라다이스 도착이라면 삭제
                    t_ans[id] = turn
                    turtles[id] = False
                else:
                    grid[y][x] = 100 + id
                    turtles[id] = (y, x)

        # 2단계: 화산 압력 증가

        # 터질 화산 큐
        vq = deque([])
        # 터진 화산 큐
        fired = set()

        for vid in range(K):
            volcano[vid][3] += 10

            if volcano[vid][3] >= volcano[vid][2]: # 현재 마그마 압력이 분출 임계치 이상이면 q 에 넣기
                vq.append(vid)
                fired.add(vid)

        thermo = [[0]*N for _ in range(N)]


        # 3단계: 화산 분출 및 연쇄 반응

        while vq:
            tid = vq.popleft()

            y, x, P, _ = volcano[tid]
            
            # 열기 전파
            tq = deque([])
            thermo[y][x] += P

            for d in range(4):
                ny, nx = y, x
                pp = P

                while True:
                    ny += D[d][0]
                    nx += D[d][1]
                    pp //= 2
                    
                    # 중단조건
                    # 1. 맵 밖이면
                    # 2. 산호초를 만나면
                    # 3. 열기가 0 이 되면
                    if not (0 <= ny < N and 0 <= nx < N): break
                    if grid[ny][nx] == 1: break
                    if pp == 0: break

                    thermo[ny][nx] += pp
                    
            # 열기 전파 완료
            # 연쇄 화산 탐색
            # 화산 마그마 압력은 마지막에 thermo 를 더한다

            for vid in range(K):
                vy, vx, vP, vm = volcano[vid]

                # 아직 폭발안했고, 마그마 압력과 외부 온도가 임계점 넘었으면
                if vid not in fired and vm + thermo[vy][vx] >= vP:
                    fired.add(vid)
                    vq.append(vid)

        # 연쇄 반응 끝남
        # 바다거북 위기 (화석화)

        for id in range(M):
            turtle = turtles[id]
            if not turtle: continue

            ty, tx = turtle

            # 온도 20 이상이면 화석으로 변환
            if thermo[ty][tx] >= 20:
                grid[ty][tx] = 2
                turtles[id] = False

        # 터진 화산 압력 0 으로 초기화
        for vid in range(K):
            if vid in fired:
                volcano[vid][3] = 0

    for ans in t_ans:
        print(ans)

main()